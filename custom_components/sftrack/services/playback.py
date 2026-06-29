"""Playback service for SafeTrack."""

from __future__ import annotations

from datetime import datetime

import voluptuous as vol

from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse
from homeassistant.helpers import config_validation as cv

from ..const import DOMAIN


SERVICE_GET_PLAYBACK = "get_playback"

ATTR_IMEI = "imei"
ATTR_START = "start"
ATTR_END = "end"


GET_PLAYBACK_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_IMEI): cv.string,
        vol.Required(ATTR_START): cv.datetime,
        vol.Required(ATTR_END): cv.datetime,
    }
)


async def async_setup_playback_service(hass: HomeAssistant) -> None:
    """Set up playback service."""

    async def handle_get_playback(call: ServiceCall) -> dict:
        """Handle get playback service call."""
        imei: str = call.data[ATTR_IMEI]
        start: datetime = call.data[ATTR_START]
        end: datetime = call.data[ATTR_END]

        entries = hass.data[DOMAIN].values()
        first_entry_data = next(iter(entries))

        api = first_entry_data["api"]

        points = await api.get_playback(imei, start, end)

        return {
            "points": [
                {
                    "latitude": point.latitude,
                    "longitude": point.longitude,
                    "timestamp": point.timestamp.isoformat(),
                    "speed": point.speed,
                    "course": point.course,
                }
                for point in points
            ]
        }

    hass.services.async_register(
        DOMAIN,
        SERVICE_GET_PLAYBACK,
        handle_get_playback,
        schema=GET_PLAYBACK_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )