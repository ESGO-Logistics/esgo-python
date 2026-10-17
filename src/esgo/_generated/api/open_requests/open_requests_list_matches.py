from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.match_list import MatchList
from typing import cast



def _get_kwargs(
    request_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/open-requests/{request_id}/matches".format(request_id=quote(str(request_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MatchList:
    if response.status_code == 200:
        response_200 = MatchList.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    response_default = Error.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | MatchList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    request_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | MatchList]:
    """ List matches of an open request

     Trips ESGO has matched to one of your open requests, best first. Reading them does not mark them as
    seen in the dashboard.

    Args:
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MatchList]
     """


    kwargs = _get_kwargs(
        request_id=request_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    request_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | MatchList | None:
    """ List matches of an open request

     Trips ESGO has matched to one of your open requests, best first. Reading them does not mark them as
    seen in the dashboard.

    Args:
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MatchList
     """


    return sync_detailed(
        request_id=request_id,
client=client,

    ).parsed

async def asyncio_detailed(
    request_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | MatchList]:
    """ List matches of an open request

     Trips ESGO has matched to one of your open requests, best first. Reading them does not mark them as
    seen in the dashboard.

    Args:
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MatchList]
     """


    kwargs = _get_kwargs(
        request_id=request_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    request_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | MatchList | None:
    """ List matches of an open request

     Trips ESGO has matched to one of your open requests, best first. Reading them does not mark them as
    seen in the dashboard.

    Args:
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MatchList
     """


    return (await asyncio_detailed(
        request_id=request_id,
client=client,

    )).parsed
