from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.match_list_object import MatchListObject
from typing import cast

if TYPE_CHECKING:
  from ..models.match import Match





T = TypeVar("T", bound="MatchList")



@_attrs_define
class MatchList:
    """ 
        Attributes:
            data (list[Match]):
            object_ (MatchListObject):
     """

    data: list[Match]
    object_: MatchListObject





    def to_dict(self) -> dict[str, Any]:
        from ..models.match import Match # noqa: PLC0415
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        object_ = self.object_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "object": object_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match import Match # noqa: PLC0415
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = Match.from_dict(data_item_data)



            data.append(data_item)


        object_ = MatchListObject(d.pop("object"))




        match_list = cls(
            data=data,
            object_=object_,
        )

        return match_list

