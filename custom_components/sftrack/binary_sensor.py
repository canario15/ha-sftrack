"""Binary sensor platform for SafeTrack."""

from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import SafeTrackDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up SafeTrack binary sensors."""
    data = hass.data[DOMAIN][entry.entry_id]

    coordinator = data["coordinator"]
    devices = data["devices"]

    entities = []

    for device in devices:
        entities.append(
            SafeTrackAccBinarySensor(
                coordinator,
                device.imei,
                device.name,
            )
        )

        entities.append(
            SafeTrackExternalPowerBinarySensor(
                coordinator,
                device.imei,
                device.name,
            )
        )

    async_add_entities(entities)


class SafeTrackAccBinarySensor(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    BinarySensorEntity,
):
    """SafeTrack ACC binary sensor."""

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator)

        self._imei = imei
        self._attr_unique_id = f"{imei}_acc"
        self._attr_name = f"{name} ACC"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def is_on(self) -> bool | None:
        """Return true if ACC is on."""
        track = self.coordinator.data.get(self._imei)
        return track.acc_status if track else None
    
    


class SafeTrackExternalPowerBinarySensor(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    BinarySensorEntity,
):
    """SafeTrack external power binary sensor."""

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator)

        self._imei = imei
        self._attr_unique_id = f"{imei}_external_power"
        self._attr_name = f"{name} External Power"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def is_on(self) -> bool | None:
        """Return true if external power is connected."""
        track = self.coordinator.data.get(self._imei)
        return track.external_power if track else None