from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_request_object import OpenRequestObject
from typing import cast
import datetime






T = TypeVar("T", bound="OpenRequest")



@_attrs_define
class OpenRequest:
    """ 
        Attributes:
            created_at (datetime.datetime):
            dashboard_url (str): The request in the ESGO dashboard.
            expires_at (datetime.datetime): End of the latest time window.
            id (str):
            matches_found (int): Matching trips found right away. Example: 2.
            object_ (OpenRequestObject):
            status (str): Status of the request. Example: active.
     """

    created_at: datetime.datetime
    dashboard_url: str
    expires_at: datetime.datetime
    id: str
    matches_found: int
    object_: OpenRequestObject
    status: str





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        dashboard_url = self.dashboard_url

        expires_at = self.expires_at.isoformat()

        id = self.id

        matches_found = self.matches_found

        object_ = self.object_.value

        status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "created_at": created_at,
            "dashboard_url": dashboard_url,
            "expires_at": expires_at,
            "id": id,
            "matches_found": matches_found,
            "object": object_,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        dashboard_url = d.pop("dashboard_url")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))




        id = d.pop("id")

        matches_found = d.pop("matches_found")

        object_ = OpenRequestObject(d.pop("object"))




        status = d.pop("status")

        open_request = cls(
            created_at=created_at,
            dashboard_url=dashboard_url,
            expires_at=expires_at,
            id=id,
            matches_found=matches_found,
            object_=object_,
            status=status,
        )

        return open_request

