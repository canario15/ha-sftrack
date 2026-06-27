"""Client for the SafeTrack API."""

from __future__ import annotations

import aiohttp

from .const import BASE_URL


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

    async def get_devices(self) -> list[dict]:
        """Return devices linked to the API key."""
        url = f"{BASE_URL}/api/v1/device/list"

        async with self._session.get(url, params={"api_key": self._api_key}) as response:
            if response.status == 401:
                raise SafeTrackAuthError("Invalid API key")

            response.raise_for_status()
            data = await response.json()

        if isinstance(data, list):
            return data

        if isinstance(data, dict) and data.get("code") == 0:
            return data.get("record", [])

        raise SafeTrackApiError("Unexpected response from SafeTrack API")