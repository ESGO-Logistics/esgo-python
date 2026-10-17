"""Official Python SDK for the ESGO API.

Two ways to call it, like the ``stripe`` and ``openai`` packages:

    import esgo

    esgo.api_key = "esgo_live_..."
    esgo.matches.search(origin="47057 Duisburg", destination="80331 München", weight_kg=12000)

    client = esgo.Client(api_key="esgo_live_...")
    client.matches.search(origin="47057 Duisburg", destination="80331 München", weight_kg=12000)

Responses are typed objects from ``esgo.models`` (``result.data[0].route_id``).
"""

from __future__ import annotations

from typing import Any

from ._client import DEFAULT_BASE_URL, Client
from ._errors import (
    APIConnectionError,
    APIError,
    AuthenticationError,
    EsgoError,
    InternalServerError,
    InvalidRequestError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    ServiceUnavailableError,
)
from ._generated import models
from ._version import __version__

__all__ = [
    "Client",
    "api_key",
    "base_url",
    "me",
    "matches",
    "open_requests",
    "models",
    "EsgoError",
    "APIConnectionError",
    "APIError",
    "InvalidRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "RateLimitError",
    "ServiceUnavailableError",
    "InternalServerError",
    "__version__",
]

# Module-level configuration for the global style.
api_key: str | None = None
base_url: str = DEFAULT_BASE_URL

_default_client: Client | None = None


def _get_default_client() -> Client:
    """Client behind ``esgo.me`` etc., rebuilt when api_key or base_url change."""
    global _default_client
    if (
        _default_client is None
        or (api_key and _default_client.api_key != api_key)
        or _default_client.base_url != base_url.rstrip("/")
    ):
        _default_client = Client(api_key=api_key, base_url=base_url)
    return _default_client


class _GlobalResource:
    def __init__(self, name: str) -> None:
        self._name = name

    def __getattr__(self, attr: str) -> Any:
        return getattr(getattr(_get_default_client(), self._name), attr)

    def __repr__(self) -> str:
        return f"<esgo.{self._name}>"


me = _GlobalResource("me")
matches = _GlobalResource("matches")
open_requests = _GlobalResource("open_requests")
