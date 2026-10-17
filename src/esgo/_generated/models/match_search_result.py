from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.match_search_result_object import MatchSearchResultObject
from typing import cast

if TYPE_CHECKING:
  from ..models.match import Match





T = TypeVar("T", bound="MatchSearchResult")



@_attrs_define
class MatchSearchResult:
    """ 
        Attributes:
            data (list[Match]):
            distance_km (float): Road distance of your route. Example: 612.4.
            match_count (int): Number of matching trips found (data may be shorter). Example: 3.
            object_ (MatchSearchResultObject):
     """

    data: list[Match]
    distance_km: float
    match_count: int
    object_: MatchSearchResultObject





    def to_dict(self) -> dict[str, Any]:
        from ..models.match import Match # noqa: PLC0415
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        distance_km = self.distance_km

        match_count = self.match_count

        object_ = self.object_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "distance_km": distance_km,
            "match_count": match_count,
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


        distance_km = d.pop("distance_km")

        match_count = d.pop("match_count")

        object_ = MatchSearchResultObject(d.pop("object"))




        match_search_result = cls(
            data=data,
            distance_km=distance_km,
            match_count=match_count,
            object_=object_,
        )

        return match_search_result

