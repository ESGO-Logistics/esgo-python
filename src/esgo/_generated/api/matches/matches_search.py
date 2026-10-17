from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.match_search_request import MatchSearchRequest
from ...models.match_search_result import MatchSearchResult
from typing import cast



def _get_kwargs(
    *,
    body: MatchSearchRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/matches/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MatchSearchResult:
    if response.status_code == 200:
        response_200 = MatchSearchResult.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    response_default = Error.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | MatchSearchResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MatchSearchRequest,

) -> Response[Error | MatchSearchResult]:
    """ Search matching capacity

     Finds trips whose route, time and free capacity fit your shipment. Prices are non-binding estimates;
    a fixed price is the standing offer of the carrier. Counts against the daily quota "matches_search".

    Args:
        body (MatchSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MatchSearchResult]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: MatchSearchRequest,

) -> Error | MatchSearchResult | None:
    """ Search matching capacity

     Finds trips whose route, time and free capacity fit your shipment. Prices are non-binding estimates;
    a fixed price is the standing offer of the carrier. Counts against the daily quota "matches_search".

    Args:
        body (MatchSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MatchSearchResult
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MatchSearchRequest,

) -> Response[Error | MatchSearchResult]:
    """ Search matching capacity

     Finds trips whose route, time and free capacity fit your shipment. Prices are non-binding estimates;
    a fixed price is the standing offer of the carrier. Counts against the daily quota "matches_search".

    Args:
        body (MatchSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MatchSearchResult]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MatchSearchRequest,

) -> Error | MatchSearchResult | None:
    """ Search matching capacity

     Finds trips whose route, time and free capacity fit your shipment. Prices are non-binding estimates;
    a fixed price is the standing offer of the carrier. Counts against the daily quota "matches_search".

    Args:
        body (MatchSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MatchSearchResult
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
