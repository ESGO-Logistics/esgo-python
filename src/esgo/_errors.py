"""Exceptions raised by the ESGO SDK.

Every API error carries the fields of the ESGO error envelope
``{"error": {"type", "code", "message", "param"}}`` plus the HTTP status,
the request id and, for 429, the ``Retry-After`` value in seconds.
"""

from __future__ import annotations

from typing import Any

import httpx


class EsgoError(Exception):
    """Base class for all errors raised by this package."""


class APIConnectionError(EsgoError):
    """The API could not be reached (network error, timeout)."""


class APIError(EsgoError):
    """The API answered with an error status."""

    def __init__(
        self,
        message: str,
        *,
        status: int,
        type: str | None = None,
        code: str | None = None,
        param: str | None = None,
        request_id: str | None = None,
        retry_after: int | None = None,
        body: Any = None,
    ) -> None:
        super().__init__(f"[{status}] {code or 'error'}: {message}")
        self.message = message
        self.status = status
        self.type = type
        self.code = code
        self.param = param
        self.request_id = request_id
        self.retry_after = retry_after
        self.body = body


class InvalidRequestError(APIError):
    """400 or 422: the request was malformed or a field is invalid (see ``param``)."""


class AuthenticationError(APIError):
    """401: the API key is missing, unknown, revoked or expired."""


class PermissionDeniedError(APIError):
    """403: the key lacks a scope, the account is disabled or has no subscription."""


class NotFoundError(APIError):
    """404: the resource does not exist or does not belong to you."""


class RateLimitError(APIError):
    """429: rate limit or daily quota exceeded; wait ``retry_after`` seconds."""


class ServiceUnavailableError(APIError):
    """503: the API is switched off or temporarily unavailable."""


class InternalServerError(APIError):
    """5xx: an error on the ESGO side."""


_BY_STATUS: dict[int, type[APIError]] = {
    400: InvalidRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    422: InvalidRequestError,
    429: RateLimitError,
    503: ServiceUnavailableError,
}


def error_from_response(response: httpx.Response) -> APIError:
    try:
        body = response.json()
    except ValueError:
        body = None
    envelope = body.get("error") if isinstance(body, dict) else None
    if not isinstance(envelope, dict):
        envelope = {}

    retry_after = response.headers.get("Retry-After")
    cls = _BY_STATUS.get(response.status_code)
    if cls is None:
        cls = InternalServerError if response.status_code >= 500 else APIError
    return cls(
        envelope.get("message") or response.reason_phrase or "Unexpected response",
        status=response.status_code,
        type=envelope.get("type"),
        code=envelope.get("code"),
        param=envelope.get("param"),
        request_id=response.headers.get("X-Request-Id"),
        retry_after=int(retry_after) if retry_after and retry_after.isdigit() else None,
        body=body,
    )
