"""The ESGO client. Resources hang off it as attributes (``client.me``)."""

from __future__ import annotations

import os
from typing import Any

import httpx

from ._errors import APIConnectionError, EsgoError, error_from_response
from ._version import __version__

DEFAULT_BASE_URL = "https://api.es-go.de"
DEFAULT_TIMEOUT = 30.0


class Client:
    """Client for the ESGO API.

    >>> client = esgo.Client(api_key="esgo_live_...")
    >>> client.me.retrieve()

    The key falls back to the ``ESGO_API_KEY`` environment variable.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        http_client: httpx.Client | None = None,
    ) -> None:
        api_key = api_key or os.environ.get("ESGO_API_KEY")
        if not api_key:
            raise EsgoError(
                "No API key provided. Pass api_key=..., set esgo.api_key "
                "or the ESGO_API_KEY environment variable."
            )
        self.api_key = api_key
        self.base_url = (base_url or DEFAULT_BASE_URL).rstrip("/")
        self._http = http_client or httpx.Client(timeout=timeout)
        self._headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "User-Agent": f"esgo-python/{__version__}",
        }
        self.me = Me(self)

    def _request(self, method: str, path: str, *, json: Any = None) -> Any:
        try:
            response = self._http.request(
                method, self.base_url + path, json=json, headers=self._headers
            )
        except httpx.HTTPError as exc:
            raise APIConnectionError(f"Could not reach {self.base_url}: {exc}") from exc
        if response.is_success:
            return response.json()
        raise error_from_response(response)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


class Me:
    """The API key in use and its quotas (``GET /v1/me``)."""

    def __init__(self, client: Client) -> None:
        self._client = client

    def retrieve(self) -> dict[str, Any]:
        return self._client._request("GET", "/v1/me")
