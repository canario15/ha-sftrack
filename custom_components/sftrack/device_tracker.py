"""Device tracker platform for SafeTrack."""

from __future__ import annotations

from homeassistant.components.device_tracker import TrackerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN
from .coordinator import SafeTrackDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up SafeTrack device tracker entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    devices = data["devices"]
    coordinator = data["coordinator"]

    async_add_entities(
        SafeTrackDeviceTracker(coordinator, device.imei, device.name)
        for device in devices
    )


class SafeTrackDeviceTracker(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    TrackerEntity,
):
    """SafeTrack device tracker entity."""

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the tracker entity."""
        super().__init__(coordinator)
        self._imei = imei
        self._attr_unique_id = f"{imei}_tracker"
        self._attr_name = name

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def latitude(self) -> float | None:
        """Return latitude."""
        track = self.coordinator.data.get(self._imei)
        return track.latitude if track else None

    @property
    def longitude(self) -> float | None:
        """Return longitude."""
        track = self.coordinator.data.get(self._imei)
        return track.longitude if track else None