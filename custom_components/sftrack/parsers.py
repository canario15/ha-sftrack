"""Parsers for SafeTrack API responses."""

from __future__ import annotations

from .models import Device, PlaybackPoint, Track
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

def parse_track(data: dict) -> Track:
    """Parse a SafeTrack track response into a Track model."""
    return Track(
        imei=data["imei"],
        latitude=data["latitude"],
        longitude=data["longitude"],
        speed=data.get("speed"),
        course=data.get("course"),
        battery=data.get("battery"),
        acc_status=bool(data.get("accstatus")) if data.get("accstatus") != -1 else None,
        external_power=bool(data.get("oilpowerstatus")) if data.get("oilpowerstatus") != -1 else None,
        charge_status=data.get("chargestatus"),
        oil_power_status=data.get("oilpowerstatus"),
        data_status=data.get("datastatus"),
        door_status=data.get("doorstatus"),
        defense_status=data.get("defencestatus"),
        mileage=data.get("mileage"),
        today_mileage=data.get("todaymileage"),
        odometer=data.get("odometer"),
        gps_time=unix_to_datetime(data.get("gpstime")),
        server_time=unix_to_datetime(data.get("servertime")),
        system_time=unix_to_datetime(data.get("systemtime")),
        heart_time=unix_to_datetime(data.get("hearttime")),
    )

def parse_playback(record: str) -> list[PlaybackPoint]:
    """Parse SafeTrack playback response into playback points."""
    if not record:
        return []

    points = []

    for raw_point in record.split(";"):
        if not raw_point:
            continue

        longitude, latitude, timestamp, speed, course = raw_point.split(",")

        points.append(
            PlaybackPoint(
                longitude=float(longitude),
                latitude=float(latitude),
                timestamp=unix_to_datetime(int(timestamp)),
                speed=int(speed),
                course=int(course),
            )
        )

    return points