from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.open_request import OpenRequest
from ...models.open_request_create import OpenRequestCreate
from typing import cast



def _get_kwargs(
    *,
    body: OpenRequestCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/open-requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | OpenRequest:
    if response.status_code == 201:
        response_201 = OpenRequest.from_dict(response.json())



        return response_201

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



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | OpenRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenRequestCreate,

) -> Response[Error | OpenRequest]:
    """ Create an open transport request

     Posts a transport request that carriers on ESGO see. ESGO matches it against existing trips right
    away and against every new trip later. Counts against the daily quota "open_requests_create". Not
    retried automatically: a repeated call creates a second request.

    Args:
        body (OpenRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OpenRequest]
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
    body: OpenRequestCreate,

) -> Error | OpenRequest | None:
    """ Create an open transport request

     Posts a transport request that carriers on ESGO see. ESGO matches it against existing trips right
    away and against every new trip later. Counts against the daily quota "open_requests_create". Not
    retried automatically: a repeated call creates a second request.

    Args:
        body (OpenRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OpenRequest
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenRequestCreate,

) -> Response[Error | OpenRequest]:
    """ Create an open transport request

     Posts a transport request that carriers on ESGO see. ESGO matches it against existing trips right
    away and against every new trip later. Counts against the daily quota "open_requests_create". Not
    retried automatically: a repeated call creates a second request.

    Args:
        body (OpenRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OpenRequest]
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
    body: OpenRequestCreate,

) -> Error | OpenRequest | None:
    """ Create an open transport request

     Posts a transport request that carriers on ESGO see. ESGO matches it against existing trips right
    away and against every new trip later. Counts against the daily quota "open_requests_create". Not
    retried automatically: a repeated call creates a second request.

    Args:
        body (OpenRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OpenRequest
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
