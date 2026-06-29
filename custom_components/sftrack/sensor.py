"""Sensor platform for SafeTrack."""

from __future__ import annotations
from token import PERCENT

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfSpeed
from homeassistant.const import UnitOfTemperature
from homeassistant.const import UnitOfLength
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import SafeTrackDataUpdateCoordinator

DEGREE = "°"
PERCENT = "%"

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up SafeTrack sensors."""
    data = hass.data[DOMAIN][entry.entry_id]

    coordinator = data["coordinator"]
    devices = data["devices"]

    entities = []

    for device in devices:
        entities.append(
            SafeTrackSpeedSensor(
                coordinator,
                device.imei,
                device.name,
            )
        )

        entities.append(
            SafeTrackCourseSensor(
                coordinator,
                device.imei,
                device.name,
            )
        )

        entities.append(
            SafeTrackBatterySensor(
                coordinator,
                device.imei,
                device.name,
            )
        )

        entities.append(
            SafeTrackOdometerSensor(
                coordinator,
                device.imei,
                device.name,
            )
        )  

        entities.append(
            SafeTrackTodayMileageSensor(
                coordinator,
                device.imei,
                device.name,
            )
        )

        entities.append(
            SafeTrackFuelSensor(
                coordinator,
                device.imei,
                device.name,
            )
        )

        entities.append(
            SafeTrackTemperatureSensor(
                coordinator,
                device.imei,
                device.name,
            )
        )

    async_add_entities(entities)


class SafeTrackSpeedSensor(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    SensorEntity,
):
    """SafeTrack speed sensor."""

    _attr_native_unit_of_measurement = UnitOfSpeed.KILOMETERS_PER_HOUR

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)

        self._imei = imei

        self._attr_unique_id = f"{imei}_speed"
        self._attr_name = f"{name} Speed"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def native_value(self):
        """Return current speed."""
        track = self.coordinator.data.get(self._imei)
        return track.speed if track else None

class SafeTrackCourseSensor(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    SensorEntity,
):
    """SafeTrack course sensor."""

    _attr_native_unit_of_measurement = DEGREE

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)

        self._imei = imei

        self._attr_unique_id = f"{imei}_course"
        self._attr_name = f"{name} Course"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def native_value(self):
        """Return current course."""
        track = self.coordinator.data.get(self._imei)
        return track.course if track else None

class SafeTrackBatterySensor(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    SensorEntity,
):
    """SafeTrack battery sensor."""

    _attr_native_unit_of_measurement = PERCENT

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)

        self._imei = imei

        self._attr_unique_id = f"{imei}_battery"
        self._attr_name = f"{name} Battery"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def native_value(self):
        """Return current battery level."""
        track = self.coordinator.data.get(self._imei)
        return track.battery if track else None
    
class SafeTrackOdometerSensor(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    SensorEntity,
):
    """SafeTrack odometer sensor."""

    _attr_native_unit_of_measurement = UnitOfLength.KILOMETERS

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)

        self._imei = imei

        self._attr_unique_id = f"{imei}_odometer"
        self._attr_name = f"{name} Odometer"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def native_value(self):
        """Return current odometer reading."""
        track = self.coordinator.data.get(self._imei)
        return track.odometer if track else None

class SafeTrackTodayMileageSensor(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    SensorEntity,
):
    """SafeTrack today's mileage sensor."""

    _attr_native_unit_of_measurement = UnitOfLength.KILOMETERS

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)

        self._imei = imei

        self._attr_unique_id = f"{imei}_today_mileage"
        self._attr_name = f"{name} Today Mileage"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def native_value(self):
        """Return current today's mileage."""
        track = self.coordinator.data.get(self._imei)
        return track.today_mileage if track else None

class SafeTrackFuelSensor(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    SensorEntity,
):
    """SafeTrack fuel sensor."""

    _attr_native_unit_of_measurement = PERCENT

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)

        self._imei = imei

        self._attr_unique_id = f"{imei}_fuel"
        self._attr_name = f"{name} Fuel"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def native_value(self):
        """Return current fuel level."""
        track = self.coordinator.data.get(self._imei)
        return track.fuel if track else None

class SafeTrackTemperatureSensor(
    CoordinatorEntity[SafeTrackDataUpdateCoordinator],
    SensorEntity,
):
    """SafeTrack temperature sensor."""

    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    def __init__(
        self,
        coordinator: SafeTrackDataUpdateCoordinator,
        imei: str,
        name: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)

        self._imei = imei

        self._attr_unique_id = f"{imei}_temperature"
        self._attr_name = f"{name} Temperature"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._imei)},
        )

    @property
    def native_value(self):
        """Return current temperature."""
        track = self.coordinator.data.get(self._imei)
        return track.temperature if track else None
