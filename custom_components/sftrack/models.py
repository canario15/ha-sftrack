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