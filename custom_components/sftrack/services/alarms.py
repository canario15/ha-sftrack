"""Alarm services for SafeTrack."""

from __future__ import annotations

from datetime import datetime

import voluptuous as vol

from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse
from homeassistant.helpers import config_validation as cv

from ..const import DOMAIN


SERVICE_GET_ALARMS = "get_alarms"

ATTR_IMEI = "imei"
ATTR_START = "start"
ATTR_END = "end"


GET_ALARMS_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_IMEI): cv.string,
        vol.Required(ATTR_START): cv.datetime,
        vol.Required(ATTR_END): cv.datetime,
    }
)


async def async_setup_alarm_services(hass: HomeAssistant) -> None:
    """Set up alarm services."""

    async def handle_get_alarms(call: ServiceCall) -> dict:
        """Handle get alarms service call."""
        imei: str = call.data[ATTR_IMEI]
        start: datetime = call.data[ATTR_START]
        end: datetime = call.data[ATTR_END]

        entries = hass.data[DOMAIN].values()
        first_entry_data = next(iter(entries))

        api = first_entry_data["api"]

        alarms = await api.get_alarms(imei, start, end)

        return {
            "alarms": [
                {
                    "alarm_type": alarm.alarm_type,
                    "alarm_name": alarm.alarm_name,
                    "latitude": alarm.latitude,
                    "longitude": alarm.longitude,
                    "gps_time": alarm.gps_time.isoformat(),
                    "system_time": alarm.system_time.isoformat(),
                    "speed": alarm.speed,
                    "course": alarm.course,
                    "geofence_id": alarm.geofence_id,
                }
                for alarm in alarms
            ]
        }

    hass.services.async_register(
        DOMAIN,
        SERVICE_GET_ALARMS,
        handle_get_alarms,
        schema=GET_ALARMS_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )