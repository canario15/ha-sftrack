"""Constants for the SafeTrack GPS integration."""

DOMAIN = "sftrack"

CONF_API_KEY = "api_key"

BASE_URL = "https://dstracker.fly.dev"

ALARM_TYPE_NAMES = {
    1: "SOS Alarm",
    2: "Low Battery Alarm",
    3: "Power Disconnect Alarm",
    4: "Vibration Alarm",
    5: "Geofence Enter Alarm",
    6: "Geofence Exit Alarm",
    7: "Overspeed Alarm",
    8: "Vehicle Movement Alarm",
    9: "Engine On",
    10: "Engine Off",
    11: "Tire Temperature Alarm",
    12: "Tire Pressure Leak Alarm",
    13: "Low Tire Pressure Alarm",
    14: "High Tire Pressure Alarm",
    15: "GPS Blind Area Enter",
    16: "GPS Blind Area Exit",
    17: "OBD DTC Alarm",
    18: "Device Removal Alarm",
    19: "Power Off Alarm",
    20: "Collision Alarm",
    21: "Rollover Alarm",
    22: "Route Alarm",
    23: "Rapid Acceleration",
    24: "Rapid Deceleration",
    25: "Sharp Turn",
    26: "Door Open",
    27: "Door Closed",
}