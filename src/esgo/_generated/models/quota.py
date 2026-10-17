from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="Quota")



@_attrs_define
class Quota:
    """ 
        Attributes:
            limit (int): Calls per rolling 24 hours. Example: 200.
            name (str): Operation the quota applies to. Example: matches_search.
            remaining (int): Calls left in the current window. Example: 198.
     """

    limit: int
    name: str
    remaining: int





    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        name = self.name

        remaining = self.remaining


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "limit": limit,
            "name": name,
            "remaining": remaining,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        name = d.pop("name")

        remaining = d.pop("remaining")

        quota = cls(
            limit=limit,
            name=name,
            remaining=remaining,
        )

        return quota

