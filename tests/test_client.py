"""Tests without a real server: httpx.MockTransport answers like the ESGO API."""

import httpx
import pytest

import esgo

ME = {
    "object": "me",
    "account_role": "buyer",
    "key": {
        "id": "k1",
        "name": "TMS",
        "prefix": "esgo_live_ab",
        "scopes": ["matches:read"],
        "created_at": "2026-10-17T10:00:00Z",
        "expires_at": None,
    },
    "quotas": [{"name": "matches_search", "limit": 200, "remaining": 199}],
}


def _error(status, type_, code, message, param=None, headers=None):
    return httpx.Response(
        status,
        headers={"X-Request-Id": "req_123", **(headers or {})},
        json={"error": {"type": type_, "code": code, "message": message, "param": param}},
    )


def _client(handler, api_key="esgo_live_test"):
    seen = []

    def wrapped(request):
        seen.append(request)
        return handler(request)

    http = httpx.Client(transport=httpx.MockTransport(wrapped))
    return esgo.Client(api_key=api_key, http_client=http), seen


@pytest.fixture(autouse=True)
def reset_globals(monkeypatch):
    monkeypatch.delenv("ESGO_API_KEY", raising=False)
    monkeypatch.setattr(esgo, "api_key", None)
    monkeypatch.setattr(esgo, "base_url", esgo.DEFAULT_BASE_URL)
    monkeypatch.setattr(esgo, "_default_client", None)


def test_client_style_sends_key_and_returns_body():
    client, seen = _client(lambda r: httpx.Response(200, json=ME))
    assert client.me.retrieve() == ME
    request = seen[0]
    assert request.method == "GET"
    assert str(request.url) == "https://api.es-go.de/v1/me"
    assert request.headers["Authorization"] == "Bearer esgo_live_test"
    assert request.headers["User-Agent"] == f"esgo-python/{esgo.__version__}"


def test_global_style_uses_module_key(monkeypatch):
    client, seen = _client(lambda r: httpx.Response(200, json=ME), api_key="esgo_live_global")
    monkeypatch.setattr(esgo, "api_key", "esgo_live_global")
    monkeypatch.setattr(esgo, "_default_client", client)
    assert esgo.me.retrieve()["account_role"] == "buyer"
    assert seen[0].headers["Authorization"] == "Bearer esgo_live_global"


def test_global_style_rebuilds_client_when_key_changes(monkeypatch):
    monkeypatch.setattr(esgo, "api_key", "esgo_live_one")
    first = esgo._get_default_client()
    monkeypatch.setattr(esgo, "api_key", "esgo_live_two")
    second = esgo._get_default_client()
    assert first is not second
    assert second.api_key == "esgo_live_two"


def test_key_from_environment(monkeypatch):
    monkeypatch.setenv("ESGO_API_KEY", "esgo_live_env")
    assert esgo.Client().api_key == "esgo_live_env"


def test_missing_key_is_a_clear_error():
    with pytest.raises(esgo.EsgoError, match="No API key"):
        esgo.Client()
    with pytest.raises(esgo.EsgoError, match="No API key"):
        esgo.me.retrieve()


@pytest.mark.parametrize(
    "response, cls, code",
    [
        (_error(401, "authentication_error", "invalid_api_key", "Unknown key"),
         esgo.AuthenticationError, "invalid_api_key"),
        (_error(403, "permission_error", "insufficient_scope", "Missing scope"),
         esgo.PermissionDeniedError, "insufficient_scope"),
        (_error(404, "invalid_request_error", "resource_missing", "Not found", "request_id"),
         esgo.NotFoundError, "resource_missing"),
        (_error(422, "invalid_request_error", "invalid_parameter", "Bad", "time_windows.0.end"),
         esgo.InvalidRequestError, "invalid_parameter"),
        (_error(503, "api_error", "api_disabled", "Switched off"),
         esgo.ServiceUnavailableError, "api_disabled"),
        (_error(500, "api_error", "internal_error", "Boom"),
         esgo.InternalServerError, "internal_error"),
    ],
)
def test_error_envelope_becomes_typed_exception(response, cls, code):
    client, _ = _client(lambda r: response)
    with pytest.raises(cls) as info:
        client.me.retrieve()
    assert info.value.code == code
    assert info.value.status == response.status_code
    assert info.value.request_id == "req_123"
    assert isinstance(info.value, esgo.APIError)


def test_rate_limit_carries_retry_after():
    response = _error(429, "rate_limit_error", "daily_quota_exceeded", "Quota",
                      headers={"Retry-After": "3600"})
    client, _ = _client(lambda r: response)
    with pytest.raises(esgo.RateLimitError) as info:
        client.me.retrieve()
    assert info.value.retry_after == 3600


def test_non_json_error_still_raises():
    client, _ = _client(lambda r: httpx.Response(502, text="Bad Gateway"))
    with pytest.raises(esgo.InternalServerError) as info:
        client.me.retrieve()
    assert info.value.code is None


def test_network_error_becomes_connection_error():
    def boom(request):
        raise httpx.ConnectError("refused", request=request)

    client, _ = _client(boom)
    with pytest.raises(esgo.APIConnectionError):
        client.me.retrieve()
