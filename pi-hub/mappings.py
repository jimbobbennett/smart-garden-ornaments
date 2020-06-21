"""Mappings between single character codes and data types, conversion functions and device ids.
This is needed as micro:bits can only send 19 characters, so this saves message space.
"""

# Value types
#
# Maps the single character value type codes sent by the micro:bit into
# the telemetry property name to send
value_types = {
    "t" : "Temperature",
}

# Value conversions
#
# Maps the single character value type codes sent by the micro:bit into
# conversion functions to make the data the correct type
value_conversion = {
    "t" : float,
}

# Devices
#
# Maps the device codes to IoT Central device ids.
devices = {
    "1" : "device-1",
}
