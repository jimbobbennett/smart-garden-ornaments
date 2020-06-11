import asyncio
import base64
import hmac
import hashlib
import io
import os
import json
import serial
import time
from azure.iot.device.aio import IoTHubDeviceClient, ProvisioningDeviceClient
from azure.iot.device import MethodResponse
from dotenv import load_dotenv
from mappings import value_conversion, value_types

load_dotenv()
id_scope = os.getenv('ID_SCOPE')
master_key = os.getenv('MASTER_KEY')

def compute_drived_symmetricKey(master_key, device_id):
    return base64.b64encode(hmac.new(base64.b64decode(master_key), msg=device_id.encode("utf8"), digestmod=hashlib.sha256).digest())

async def register_device(device_id, device_key):
    provisioning_device_client = ProvisioningDeviceClient.create_from_symmetric_key(
        provisioning_host='global.azure-devices-provisioning.net',
        registration_id=device_id,
        id_scope=id_scope,
        symmetric_key=device_key)

    return await provisioning_device_client.register()

async def get_device_client(device_id, device_clients):
    if device_id in device_clients:
        return device_clients[device_id]

    device_key = compute_drived_symmetricKey(master_key, device_id).decode("ascii")

    results = await asyncio.gather(register_device(device_id, device_key))
    registration_result = results[0]

    conn_str='HostName=' + registration_result.registration_state.assigned_hub + \
                ';DeviceId=' + device_id + \
                ';SharedAccessKey=' + device_key

    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    device_clients[device_id] = device_client
    return device_client    
    
def build_telemetry(value_type, value):
    return json.dumps({ value_types[value_type] : value_conversion[value_type](value) })

async def message_worker(queue, device_clients):
    last_values = {}
    while True:
        try:
            item = await queue.get()
            print(item)

            data = item.split(":")

            device_id = data[0]
            value_type = data[1]
            value = data[2]

            #print("Device:", device_id, "Value type:", value_type, "value", value)

            value_key = device_id + ":" + value_type
            if value_key in last_values:
                last_value = last_values[value_key]
                if last_value[0] == value and (time.time() - last_value[1]) < 60:
                    continue

            device = await get_device_client(device_id, device_clients)
            telemetry = build_telemetry(value_type, value)

            print("Sending item:", item)
            #print("Sending telemetry:", telemetry)

            await device.send_message(telemetry)

            last_values[value_key] = (value, time.time())

        except Exception as error:
            print(error)
        
async def main():
    microbit_path = "/dev/" + next(x for x in os.listdir("/dev") if x.startswith("ttyACM"))
    ser = serial.Serial(microbit_path, 115200, timeout=0.1)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

    queue = asyncio.Queue()
    device_clients = {}

    async def main_loop():
        while True:
            try:
                all_data = sio.readline().strip()
                if all_data != "":
                    lines = all_data.split("\n")

                    for line in lines:
                        await queue.put(line)
            except:
                pass

            await asyncio.sleep(0.5)
    
    listeners = asyncio.gather(message_worker(queue, device_clients))

    await main_loop()

    listeners.cancel()

if __name__ == '__main__':
    asyncio.run(main())