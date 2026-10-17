from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.match_search_request_loading_requirement import MatchSearchRequestLoadingRequirement
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MatchSearchRequest")



@_attrs_define
class MatchSearchRequest:
    """ 
        Attributes:
            destination (str): Destination, ideally postcode and city. Example: 80331 München.
            origin (str): Origin, ideally postcode and city. Example: 47057 Duisburg.
            weight_kg (float): Cargo weight in kilograms. Example: 12000.
            loading_meters (float | None | Unset): Loading meters needed (max 13.6). Example: 4.8.
            loading_requirement (MatchSearchRequestLoadingRequirement | Unset): How the cargo has to be loaded. "any" never
                filters; "seite" (side) and "oben" (top) exclude box bodies; "heck" means rear loading. Default:
                MatchSearchRequestLoadingRequirement.ANY. Example: any.
            service_ids (list[int] | Unset): Required additional services (ESGO service IDs). Example: [].
     """

    destination: str
    origin: str
    weight_kg: float
    loading_meters: float | None | Unset = UNSET
    loading_requirement: MatchSearchRequestLoadingRequirement | Unset = MatchSearchRequestLoadingRequirement.ANY
    service_ids: list[int] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        destination = self.destination

        origin = self.origin

        weight_kg = self.weight_kg

        loading_meters: float | None | Unset
        if isinstance(self.loading_meters, Unset):
            loading_meters = UNSET
        else:
            loading_meters = self.loading_meters

        loading_requirement: str | Unset = UNSET
        if not isinstance(self.loading_requirement, Unset):
            loading_requirement = self.loading_requirement.value


        service_ids: list[int] | Unset = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "destination": destination,
            "origin": origin,
            "weight_kg": weight_kg,
        })
        if loading_meters is not UNSET:
            field_dict["loading_meters"] = loading_meters
        if loading_requirement is not UNSET:
            field_dict["loading_requirement"] = loading_requirement
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination = d.pop("destination")

        origin = d.pop("origin")

        weight_kg = d.pop("weight_kg")

        def _parse_loading_meters(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        loading_meters = _parse_loading_meters(d.pop("loading_meters", UNSET))


        _loading_requirement = d.pop("loading_requirement", UNSET)
        loading_requirement: MatchSearchRequestLoadingRequirement | Unset
        if isinstance(_loading_requirement,  Unset):
            loading_requirement = UNSET
        else:
            loading_requirement = MatchSearchRequestLoadingRequirement(_loading_requirement)




        service_ids = cast(list[int], d.pop("service_ids", UNSET))


        match_search_request = cls(
            destination=destination,
            origin=origin,
            weight_kg=weight_kg,
            loading_meters=loading_meters,
            loading_requirement=loading_requirement,
            service_ids=service_ids,
        )

        return match_search_request

