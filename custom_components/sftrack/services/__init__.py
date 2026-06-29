"""Services for SafeTrack."""

from __future__ import annotations

from homeassistant.core import HomeAssistant

from .playback import async_setup_playback_service
from .alarms import async_setup_alarm_services

async def async_setup_services(hass: HomeAssistant) -> None:
    """Set up SafeTrack services."""
    await async_setup_playback_service(hass)
    await async_setup_alarm_services(hass)
