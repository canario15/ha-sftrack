"""SafeTrack integration for Home Assistant."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers import device_registry as dr
from homeassistant.const import Platform

from .api import SafeTrackApi
from .const import CONF_API_KEY, DOMAIN
from .coordinator import SafeTrackDataUpdateCoordinator
from .services import async_setup_services


PLATFORMS = [
    Platform.DEVICE_TRACKER,
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up SafeTrack from a config entry."""
    session = async_get_clientsession(hass)
    api = SafeTrackApi(entry.data[CONF_API_KEY], session)

    devices = await api.get_devices()
    imeis = [device.imei for device in devices]

    device_registry = dr.async_get(hass)

    for device in devices:
        
        device_registry.async_get_or_create(
            config_entry_id=entry.entry_id,
            identifiers={(DOMAIN, device.imei)},
            manufacturer="SafeTrack",
            name=device.name,
            model=device.device_type,
        )

    coordinator = SafeTrackDataUpdateCoordinator(hass, entry, imeis)

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "devices": devices,
        "coordinator": coordinator,
    }

    await async_setup_services(hass)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload SafeTrack config entry."""
    hass.data[DOMAIN].pop(entry.entry_id)

    return True