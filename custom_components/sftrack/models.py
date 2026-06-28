"""Models for the SafeTrack integration."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Device:
    """SafeTrack device."""

    imei: str
    name: str
    device_type: str | None = None
    plate_number: str | None = None
    simcard: str | None = None
    iccid: str | None = None
    customer_account: str | None = None
    online_time: datetime | None = None
    activated_time: datetime | None = None
    user_due_time: datetime | None = None
    platform_due_time: datetime | None = None

@dataclass(frozen=True)
class Track:
    """SafeTrack live tracking data."""

    imei: str
    latitude: float
    longitude: float
    speed: int | None = None
    course: int | None = None
    battery: int | None = None
    acc_status: int | None = None
    charge_status: int | None = None
    oil_power_status: int | None = None
    data_status: int | None = None
    door_status: int | None = None
    defense_status: int | None = None
    mileage: int | None = None
    today_mileage: int | None = None
    odometer: int | None = None
    gps_time: datetime | None = None
    server_time: datetime | None = None
    system_time: datetime | None = None
    heart_time: datetime | None = None