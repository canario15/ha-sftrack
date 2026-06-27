"""Parsers for SafeTrack API responses."""

from __future__ import annotations

from .models import Device
from .utils import empty_to_none, unix_to_datetime


def parse_device(data: dict) -> Device:
    """Parse a SafeTrack device response into a Device model."""
    return Device(
        imei=data["imei"],
        name=data.get("devicename") or data.get("name"),
        device_type=empty_to_none(data.get("devicetype")),
        plate_number=empty_to_none(data.get("platenumber")),
        simcard=empty_to_none(data.get("simcard")),
        iccid=empty_to_none(data.get("iccid")),
        customer_account=empty_to_none(data.get("customeraccount")),
        online_time=unix_to_datetime(data.get("onlinetime")),
        activated_time=unix_to_datetime(data.get("activatedtime")),
        user_due_time=unix_to_datetime(data.get("userduetime")),
        platform_due_time=unix_to_datetime(data.get("platformduetime")),
    )