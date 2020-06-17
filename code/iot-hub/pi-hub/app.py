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
from dotenv import load_dotenv
from mappings import value_conversion, value_types, devices

load_dotenv()
ID_SCOPE = os.getenv('ID_SCOPE')
IOT_CENTRAL_KEY = os.getenv('IOT_CENTRAL_KEY')

def compute_derived_symmetricKey(device_id):
    """Creates a key for the device from the IoT Central master key and the device ID
    """
    return base64.b64encode(hmac.new(base64.b64decode(IOT_CENTRAL_KEY), msg=device_id.encode("utf8"), digestmod=hashlib.sha256).digest())

async def register_device(device_id, device_key):
    """Uses the Azure IoT Device Provisioning service to provision a device using the given key.
    This returns details on the device registration, including the IoT Hub used by IoT Central.
    The IoT Hub is then used to connect.
    """
    provisioning_device_client = ProvisioningDeviceClient.create_from_symmetric_key(
        provisioning_host='global.azure-devices-provisioning.net',
        registration_id=device_id,
        id_scope=ID_SCOPE,
        symmetric_key=device_key)

    return await provisioning_device_client.register()

async def get_or_create_device_client(device_id, device_clients):
    """Looks to see if there already is a device client connected to IoT Central for the given device.
    If so, it is returned. If not a new one is created and cached.
    """
    print("Looking for connection to IoT Central for", device_id)

    if device_id in device_clients:
        print("Connection to IoT Central for", device_id, "found!")
        return device_clients[device_id]

    print("No connection to IoT Central for", device_id, "found, creating new connection...")

    device_key = compute_derived_symmetricKey(device_id).decode("ascii")

    results = await asyncio.gather(register_device(device_id, device_key))
    registration_result = results[0]

    conn_str='HostName=' + registration_result.registration_state.assigned_hub + \
                ';DeviceId=' + device_id + \
                ';SharedAccessKey=' + device_key

    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    device_clients[device_id] = device_client

    print("Connection to IoT Central for", device_id, "created!")

    return device_client

def build_telemetry(value_type, value):
    """Converts the telemetry using the value type key from the device into a JSON
    object that IoT Central can use
    """
    return json.dumps({ value_types[value_type] : value_conversion[value_type](value) })

async def message_worker(queue, device_clients):
    """This asynchronously processes the messages sent from the micro:bit.
    The messages are decoded into their device ID and data. The device ID is used to 
    get a device client for that device. The data is converted to JSON.
    The data is then sent to IoT Central using the device client.
    """
    last_values = {}
    while True:
        try:
            item = await queue.get()
            print("Processing telemetry:", item)

            data = item.split(":")

            device_id = data[0]

            # Make sure the device ID is one we can map
            if device_id not in devices:
                continue

            device_id = devices[device_id]

            value_type = data[1]
            value = data[2]

            value_key = device_id + ":" + value_type
            if value_key in last_values:
                last_value = last_values[value_key]
                if last_value[0] == value and (time.time() - last_value[1]) < 60:
                    continue

            device = await get_or_create_device_client(device_id, device_clients)
            telemetry = build_telemetry(value_type, value)

            print("Sending telemetry for device", device_id, ":", telemetry, "...")

            await device.send_message(telemetry)

            print("Telemetry for device", device_id, "sent")

            last_values[value_key] = (value, time.time())

        except Exception as error:
            print(error)

async def main():
    """The main method.
    First this gets the connected micro:bits path, then it connects a serial reader to pull lines of data.
    Every time a line of data is received, it is queued up to be processed to send to IoT Central.
    """
    print("Detecting micro:bit...")
    microbit_path = "/dev/" + next(x for x in os.listdir("/dev") if x.startswith("ttyACM"))
    ser = serial.Serial(microbit_path, 115200, timeout=0.1)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
    print("Connected to micro:bit at", microbit_path)
    print("Waiting for telemetry...")

    queue = asyncio.Queue()
    device_clients = {}

    async def main_loop():
        while True:
            try:
                all_data = sio.readline().strip()
                if all_data != "":
                    lines = all_data.split("\n")

                    for line in lines:
                        print("Received telemetry:", line)
                        await queue.put(line)
            except:
                pass

            await asyncio.sleep(0.5)

    listeners = asyncio.gather(message_worker(queue, device_clients))

    await main_loop()

    listeners.cancel()

if __name__ == '__main__':
    asyncio.run(main())