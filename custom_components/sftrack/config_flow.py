"""Config flow for SafeTrack GPS."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import SafeTrackApi, SafeTrackApiError, SafeTrackAuthError
from .const import CONF_API_KEY, DOMAIN


class SafeTrackConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for SafeTrack GPS."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            api_key = user_input[CONF_API_KEY]

            session = async_get_clientsession(self.hass)
            client = SafeTrackApi(api_key, session)

            try:
                devices = await client.get_devices()
            except SafeTrackAuthError:
                errors["base"] = "invalid_auth"
            except SafeTrackApiError:
                errors["base"] = "cannot_connect"
            else:
                if not devices:
                    errors["base"] = "no_devices"
                else:
                    return self.async_create_entry(
                        title="SafeTrack",
                        data={CONF_API_KEY: api_key},
                    )

        data_schema = vol.Schema(
            {
                vol.Required(CONF_API_KEY): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )