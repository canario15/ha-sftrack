"""Data coordinator for the SafeTrack integration."""

from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .api import SafeTrackApi
from .const import CONF_API_KEY, DOMAIN
from .models import Track

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=10)


class SafeTrackDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Track]]):
    """SafeTrack data update coordinator."""

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
        imeis: list[str],
    ) -> None:
        """Initialize the coordinator."""
        self.api = SafeTrackApi(
            entry.data[CONF_API_KEY],
            async_get_clientsession(hass),
        )
        self.imeis = imeis

        super().__init__(
            hass,
            logger=_LOGGER,
            name=DOMAIN,
            update_interval=SCAN_INTERVAL,
        )

    async def _async_update_data(self) -> dict[str, Track]:
        """Fetch latest data from SafeTrack."""
        tracks = await self.api.get_tracks(self.imeis)
        return {track.imei: track for track in tracks}