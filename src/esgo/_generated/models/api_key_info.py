from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="ApiKeyInfo")



@_attrs_define
class ApiKeyInfo:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (str):
            name (str): Label given by ESGO. Example: TMS production.
            prefix (str): Visible start of the key. Example: esgo_live_Ab3dE9.
            scopes (list[str]): Granted scopes. Example: ['matches:read'].
            expires_at (datetime.datetime | None | Unset):
     """

    created_at: datetime.datetime
    id: str
    name: str
    prefix: str
    scopes: list[str]
    expires_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        prefix = self.prefix

        scopes = self.scopes



        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "created_at": created_at,
            "id": id,
            "name": name,
            "prefix": prefix,
            "scopes": scopes,
        })
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = d.pop("id")

        name = d.pop("name")

        prefix = d.pop("prefix")

        scopes = cast(list[str], d.pop("scopes"))


        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))


        api_key_info = cls(
            created_at=created_at,
            id=id,
            name=name,
            prefix=prefix,
            scopes=scopes,
            expires_at=expires_at,
        )

        return api_key_info

