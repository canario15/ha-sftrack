"""Client for the SafeTrack API."""

from __future__ import annotations
from datetime import datetime

import aiohttp

from .const import BASE_URL
from .models import Alarm, Device, PlaybackPoint, Track
from .parsers import parse_alarms, parse_device, parse_playback, parse_track


class SafeTrackApiError(Exception):
    """Base error for SafeTrack API."""


class SafeTrackAuthError(SafeTrackApiError):
    """Error raised when the API key is invalid."""


class SafeTrackApi:
    """Small client for the SafeTrack API."""

    def __init__(self, api_key: str, session: aiohttp.ClientSession) -> None:
        """Initialize the SafeTrack API client."""
        self._api_key = api_key
        self._session = session

    async def get_devices(self) -> list[Device]:
        """Return devices linked to the API key with detailed information."""
        url = f"{BASE_URL}/api/v1/device/list"

        async with self._session.get(url, params={"api_key": self._api_key}) as response:
            if response.status == 401:
                raise SafeTrackAuthError("Invalid API key")

            response.raise_for_status()
            data = await response.json()

        if isinstance(data, list):
            imeis = [item["imei"] for item in data]
            return await self._get_device_details(imeis)

        if isinstance(data, dict) and data.get("code") == 0:
            imeis = [item["imei"] for item in data.get("record", [])]
            return await self._get_device_details(imeis)

        raise SafeTrackApiError("Unexpected response from SafeTrack API")
    
    async def get_tracks(self, imeis: list[str]) -> list[Track]:
        """Return live tracking data for the given IMEIs."""
        url = f"{BASE_URL}/api/v1/track"

        async with self._session.get(
            url,
            params={
                "api_key": self._api_key,
                "imeis": ",".join(imeis),
            },
        ) as response:
            if response.status == 401:
                raise SafeTrackAuthError("Invalid API key")

            response.raise_for_status()
            data = await response.json()

        if isinstance(data, dict) and data.get("code") == 0:
            return [parse_track(item) for item in data.get("record", [])]

        raise SafeTrackApiError("Unexpected response from SafeTrack API")

    async def _get_device_details(self, imeis: list[str]) -> list[Device]:
        """Return detailed device information for the given IMEIs."""
        if not imeis:
            return []

        url = f"{BASE_URL}/api/v1/device/detail"

        async with self._session.get(
            url,
            params={
                "api_key": self._api_key,
                "imeis": ",".join(imeis),
            },
        ) as response:
            if response.status == 401:
                raise SafeTrackAuthError("Invalid API key")

            response.raise_for_status()
            data = await response.json()

        if isinstance(data, dict) and data.get("code") == 0:
            return [parse_device(item) for item in data.get("record", [])]

        raise SafeTrackApiError("Unexpected response from SafeTrack API")
    
    async def get_playback(
        self,
        imei: str,
        start: datetime,
        end: datetime,
    ) -> list[PlaybackPoint]:
        """Return playback points for a device."""
        url = f"{BASE_URL}/api/v1/playback"

        async with self._session.get(
            url,
            params={
                "api_key": self._api_key,
                "imei": imei,
                "begintime": int(start.timestamp()),
                "endtime": int(end.timestamp()),
            },
        ) as response:
            if response.status == 401:
                raise SafeTrackAuthError("Invalid API key")

            response.raise_for_status()
            data = await response.json()

        if isinstance(data, dict) and data.get("code") == 0:
            return parse_playback(data.get("record", ""))

        raise SafeTrackApiError("Unexpected response from SafeTrack API")
    
    async def get_alarms(
        self,
        imei: str,
        start: datetime,
        end: datetime,
    ) -> list[Alarm]:
        """Return alarm events for a device."""
        url = f"{BASE_URL}/api/v1/alarm/list"

        async with self._session.get(
            url,
            params={
                "api_key": self._api_key,
                "imei": imei,
                "begintime": int(start.timestamp()),
                "endtime": int(end.timestamp()),
            },
        ) as response:
            if response.status == 401:
                raise SafeTrackAuthError("Invalid API key")

            response.raise_for_status()
            data = await response.json()

        if isinstance(data, dict) and data.get("code") == 0:
            return parse_alarms(data.get("record", ""))

        raise SafeTrackApiError("Unexpected response from SafeTrack API")