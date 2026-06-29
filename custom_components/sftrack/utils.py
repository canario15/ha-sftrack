"""Utility functions for the SafeTrack integration."""

from __future__ import annotations

from datetime import UTC, datetime


def unix_to_datetime(value: int | None) -> datetime | None:
    """Convert a Unix timestamp to UTC datetime."""
    if not value:
        return None

    return datetime.fromtimestamp(value, tz=UTC)


def empty_to_none(value: str | None) -> str | None:
    """Convert empty strings to None."""
    if not value:
        return None

    return value

def meters_to_kilometers(value: int | float | None) -> float | None:
    """Convert meters to kilometers."""
    if value is None:
        return None

    return round(value / 1000, 2)