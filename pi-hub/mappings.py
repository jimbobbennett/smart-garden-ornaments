"""Mappings between single character codes, and data types and device ids.
This is needed as micro:bits can only send 19 characters, so this saves message space.
"""

# Devices
#
# Maps the device codes to IoT Central device ids.
devices = {
    "1" : "device-1",
}

# Value types
#
# Maps the single character value type codes sent by the micro:bit into
# the telemetry property name to send
value_types = {
    "t" : "Temperature",
}
