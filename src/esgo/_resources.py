"""Resources of the ESGO API: client.me, client.matches, client.open_requests.

Hand-written layer over the generated models in ``_generated``. ``OPERATIONS``
is the single place that maps an operationId of the spec to its HTTP method,
path, models and SDK method; tests/test_operations.py checks it against
openapi.json, so a new endpoint in the spec fails the tests until it is added
here.
"""

from __future__ import annotations

import datetime
import enum
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

import attrs

from ._generated.models import (
    MatchList,
    MatchSearchRequest,
    MatchSearchResult,
    Me as MeModel,
    OpenRequest,
    OpenRequestCreate,
)

if TYPE_CHECKING:
    from ._client import Client


@dataclass(frozen=True)
class Operation:
    method: str
    path: str
    request: type | None
    response: type
    sdk_method: str


OPERATIONS: dict[str, Operation] = {
    "me_retrieve": Operation("GET", "/v1/me", None, MeModel, "me.retrieve"),
    "matches_search": Operation(
        "POST", "/v1/matches/search", MatchSearchRequest, MatchSearchResult, "matches.search"
    ),
    "open_requests_create": Operation(
        "POST", "/v1/open-requests", OpenRequestCreate, OpenRequest, "open_requests.create"
    ),
    "open_requests_list_matches": Operation(
        "GET", "/v1/open-requests/{request_id}/matches", None, MatchList,
        "open_requests.list_matches",
    ),
}


def _jsonable(value: Any) -> Any:
    """datetime/date/Enum/model in params -> JSON values; dicts and lists recursively."""
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    if isinstance(value, enum.Enum):
        return value.value
    if attrs.has(type(value)) and hasattr(value, "to_dict"):
        return value.to_dict()
    if isinstance(value, dict):
        return {k: _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    return value


def _check_params(model: type, params: dict[str, Any], where: str) -> None:
    """Fail like a normal Python call on unknown or missing keyword arguments.

    Values are validated by the API (422 with ``param``), which stays the
    single source of truth for the rules.
    """
    fields = {f.name: f for f in attrs.fields(model) if f.name != "additional_properties"}
    unknown = sorted(set(params) - set(fields))
    if unknown:
        raise TypeError(f"{where}() got unexpected keyword argument(s): {', '.join(unknown)}")
    missing = sorted(n for n, f in fields.items() if f.default is attrs.NOTHING and n not in params)
    if missing:
        raise TypeError(f"{where}() missing required keyword argument(s): {', '.join(missing)}")


class _Resource:
    def __init__(self, client: Client) -> None:
        self._client = client

    def _call(self, operation_id: str, params: dict[str, Any] | None = None, **path: str) -> Any:
        op = OPERATIONS[operation_id]
        body = None
        if op.request is not None:
            _check_params(op.request, params or {}, op.sdk_method)
            body = _jsonable(params or {})
        url = op.path.format(**{k: quote(str(v), safe="") for k, v in path.items()})
        data = self._client._request(op.method, url, json=body)
        return op.response.from_dict(data)


class Me(_Resource):
    """The API key in use and its daily quotas."""

    def retrieve(self) -> MeModel:
        """``GET /v1/me``."""
        return self._call("me_retrieve")


class Matches(_Resource):
    """Search for trips with free capacity that fit a shipment."""

    def search(self, **params: Any) -> MatchSearchResult:
        """``POST /v1/matches/search``.

        Required: ``origin``, ``destination``, ``weight_kg``. Optional:
        ``loading_meters``, ``loading_requirement``, ``service_ids``.
        Counts against the daily quota ``matches_search``.
        """
        return self._call("matches_search", params)


class OpenRequests(_Resource):
    """Publish open transport requests and read their matches."""

    def create(self, **params: Any) -> OpenRequest:
        """``POST /v1/open-requests``.

        Required: ``origin``, ``destination``, ``weight_kg``,
        ``loading_meters``, ``cargo_type``, ``time_windows`` (list of
        ``{"start": datetime, "end": datetime}``). Optional:
        ``cargo_description``, ``loading_requirement``, ``target_price_eur``,
        ``service_ids``. Counts against the daily quota
        ``open_requests_create``.
        """
        return self._call("open_requests_create", params)

    def list_matches(self, request_id: str) -> MatchList:
        """``GET /v1/open-requests/{request_id}/matches``."""
        return self._call("open_requests_list_matches", request_id=request_id)
