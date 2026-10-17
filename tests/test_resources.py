"""matches.search, open_requests.create, open_requests.list_matches against a mock API."""

import datetime
import json

import httpx
import pytest

import esgo

MATCH = {
    "object": "match",
    "route_id": "r_1",
    "origin_area": "Duisburg",
    "destination_area": "München",
    "departure_window": {"start": "2026-10-20T08:00:00", "end": "2026-10-20T12:00:00"},
    "free_capacity_kg": 8000.0,
    "free_capacity_ldm": 6.2,
    "instant_bookable": False,
    "match_score": 87.5,
    "booking_url": "https://es-go.de/booking_request/r_1",
    "detour_km": 12.0,
    "price_estimate_eur": 640.0,
}

OPEN_REQUEST = {
    "object": "open_request",
    "id": "or_1",
    "status": "open",
    "matches_found": 2,
    "created_at": "2026-10-17T10:00:00",
    "expires_at": "2026-10-21T18:00:00",
    "dashboard_url": "https://es-go.de/buyer/requests/or_1/matches",
}


def _client(handler):
    seen = []

    def wrapped(request):
        seen.append(request)
        return handler(request)

    http = httpx.Client(transport=httpx.MockTransport(wrapped))
    return esgo.Client(api_key="esgo_live_test", http_client=http), seen


def test_search_sends_params_and_returns_typed_result():
    result_body = {"object": "match_search", "distance_km": 612.4, "match_count": 1, "data": [MATCH]}
    client, seen = _client(lambda r: httpx.Response(200, json=result_body))

    result = client.matches.search(origin="47057 Duisburg", destination="80331 München",
                                   weight_kg=12000, loading_requirement="seite")

    request = seen[0]
    assert (request.method, request.url.path) == ("POST", "/v1/matches/search")
    assert json.loads(request.content) == {
        "origin": "47057 Duisburg", "destination": "80331 München",
        "weight_kg": 12000, "loading_requirement": "seite",
    }
    assert isinstance(result, esgo.models.MatchSearchResult)
    assert result.match_count == 1
    match = result.data[0]
    assert match.route_id == "r_1"
    assert match.departure_window.start == datetime.datetime(2026, 10, 20, 8, 0)
    assert match.price_estimate_eur == 640.0


def test_create_serializes_datetimes_and_returns_open_request():
    client, seen = _client(lambda r: httpx.Response(201, json=OPEN_REQUEST))
    start = datetime.datetime(2026, 10, 20, 8, 0)

    created = client.open_requests.create(
        origin="47057 Duisburg", destination="80331 München", weight_kg=12000,
        loading_meters=4.8, cargo_type="Paletten",
        time_windows=[{"start": start, "end": start + datetime.timedelta(hours=4)}],
    )

    body = json.loads(seen[0].content)
    assert body["time_windows"] == [{"start": "2026-10-20T08:00:00", "end": "2026-10-20T12:00:00"}]
    assert isinstance(created, esgo.models.OpenRequest)
    assert created.id == "or_1"
    assert created.expires_at == datetime.datetime(2026, 10, 21, 18, 0)


def test_list_matches_quotes_the_path_parameter():
    client, seen = _client(lambda r: httpx.Response(200, json={"object": "list", "data": [MATCH]}))
    matches = client.open_requests.list_matches("or/1")
    assert seen[0].url.raw_path == b"/v1/open-requests/or%2F1/matches"
    assert matches.data[0].route_id == "r_1"


def test_unknown_or_missing_arguments_fail_before_the_request():
    client, seen = _client(lambda r: httpx.Response(500))
    with pytest.raises(TypeError, match="unexpected keyword argument.*origni"):
        client.matches.search(origni="Duisburg", destination="München", weight_kg=1)
    with pytest.raises(TypeError, match="missing required keyword argument.*weight_kg"):
        client.matches.search(origin="Duisburg", destination="München")
    assert seen == []


def test_validation_error_names_the_field():
    response = httpx.Response(422, json={"error": {
        "type": "invalid_request_error", "code": "invalid_parameter",
        "message": "End must be after start.", "param": "time_windows.0.end"}})
    client, _ = _client(lambda r: response)
    with pytest.raises(esgo.InvalidRequestError) as info:
        client.open_requests.create(origin="A", destination="B", weight_kg=1, loading_meters=1,
                                    cargo_type="x", time_windows=[])
    assert info.value.param == "time_windows.0.end"
