from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_request_create_loading_requirement import OpenRequestCreateLoadingRequirement
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.time_window import TimeWindow





T = TypeVar("T", bound="OpenRequestCreate")



@_attrs_define
class OpenRequestCreate:
    """ 
        Attributes:
            cargo_type (str): Kind of cargo. Example: Paletten.
            destination (str): Destination, ideally postcode and city. Example: 80331 München.
            loading_meters (float): Loading meters needed (max 13.6). Example: 4.8.
            origin (str): Origin, ideally postcode and city. Example: 47057 Duisburg.
            time_windows (list[TimeWindow]): Pickup time windows; at least one.
            weight_kg (float): Cargo weight in kilograms. Example: 12000.
            cargo_description (str | Unset): Free text for the carrier. Default: ''. Example: 12 EUR pallets, stackable.
            loading_requirement (OpenRequestCreateLoadingRequirement | Unset): How the cargo has to be loaded. "any" never
                filters; "seite" (side) and "oben" (top) exclude box bodies; "heck" means rear loading. Default:
                OpenRequestCreateLoadingRequirement.ANY. Example: any.
            service_ids (list[int] | Unset): Required additional services (ESGO service IDs). Example: [].
            target_price_eur (float | None | Unset): Optional target price in EUR shown to carriers as orientation. Example:
                650.
     """

    cargo_type: str
    destination: str
    loading_meters: float
    origin: str
    time_windows: list[TimeWindow]
    weight_kg: float
    cargo_description: str | Unset = ''
    loading_requirement: OpenRequestCreateLoadingRequirement | Unset = OpenRequestCreateLoadingRequirement.ANY
    service_ids: list[int] | Unset = UNSET
    target_price_eur: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.time_window import TimeWindow # noqa: PLC0415
        cargo_type = self.cargo_type

        destination = self.destination

        loading_meters = self.loading_meters

        origin = self.origin

        time_windows = []
        for time_windows_item_data in self.time_windows:
            time_windows_item = time_windows_item_data.to_dict()
            time_windows.append(time_windows_item)



        weight_kg = self.weight_kg

        cargo_description = self.cargo_description

        loading_requirement: str | Unset = UNSET
        if not isinstance(self.loading_requirement, Unset):
            loading_requirement = self.loading_requirement.value


        service_ids: list[int] | Unset = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids



        target_price_eur: float | None | Unset
        if isinstance(self.target_price_eur, Unset):
            target_price_eur = UNSET
        else:
            target_price_eur = self.target_price_eur


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cargo_type": cargo_type,
            "destination": destination,
            "loading_meters": loading_meters,
            "origin": origin,
            "time_windows": time_windows,
            "weight_kg": weight_kg,
        })
        if cargo_description is not UNSET:
            field_dict["cargo_description"] = cargo_description
        if loading_requirement is not UNSET:
            field_dict["loading_requirement"] = loading_requirement
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if target_price_eur is not UNSET:
            field_dict["target_price_eur"] = target_price_eur

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_window import TimeWindow # noqa: PLC0415
        d = dict(src_dict)
        cargo_type = d.pop("cargo_type")

        destination = d.pop("destination")

        loading_meters = d.pop("loading_meters")

        origin = d.pop("origin")

        time_windows = []
        _time_windows = d.pop("time_windows")
        for time_windows_item_data in (_time_windows):
            time_windows_item = TimeWindow.from_dict(time_windows_item_data)



            time_windows.append(time_windows_item)


        weight_kg = d.pop("weight_kg")

        cargo_description = d.pop("cargo_description", UNSET)

        _loading_requirement = d.pop("loading_requirement", UNSET)
        loading_requirement: OpenRequestCreateLoadingRequirement | Unset
        if isinstance(_loading_requirement,  Unset):
            loading_requirement = UNSET
        else:
            loading_requirement = OpenRequestCreateLoadingRequirement(_loading_requirement)




        service_ids = cast(list[int], d.pop("service_ids", UNSET))


        def _parse_target_price_eur(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        target_price_eur = _parse_target_price_eur(d.pop("target_price_eur", UNSET))


        open_request_create = cls(
            cargo_type=cargo_type,
            destination=destination,
            loading_meters=loading_meters,
            origin=origin,
            time_windows=time_windows,
            weight_kg=weight_kg,
            cargo_description=cargo_description,
            loading_requirement=loading_requirement,
            service_ids=service_ids,
            target_price_eur=target_price_eur,
        )

        return open_request_create

