from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.match_object import MatchObject
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.departure_window import DepartureWindow





T = TypeVar("T", bound="Match")



@_attrs_define
class Match:
    """ 
        Attributes:
            booking_url (str): Opens the booking flow on es-go.de. Booking happens there, not through the API.
            departure_window (DepartureWindow):
            destination_area (str): Destination of the trip, city level. Example: 80331 München.
            free_capacity_kg (float): Free payload in kilograms before your load. Example: 9000.
            free_capacity_ldm (float): Free loading meters on this trip before your load. Example: 6.2.
            instant_bookable (bool): The carrier offers a fixed price for this trip.
            match_score (float): How well the trip fits, 0 to 100. Example: 87.5.
            object_ (MatchObject):
            origin_area (str): Origin of the trip, city level. Example: 47057 Duisburg.
            route_id (str): ID of the offered trip.
            co2_saved_kg_estimate (float | None | Unset): Rough estimate of CO2 saved in kilograms; null where no estimate
                exists. Example: 1420.3.
            detour_km (float | None | Unset): Extra kilometers for the carrier. Example: 14.2.
            instant_price_eur (float | None | Unset): The carrier's standing fixed-price offer in EUR, if any. Example: 690.
            price_estimate_eur (float | None | Unset): Non-binding price estimate in EUR. Not an offer; null where no
                estimate exists. Example: 640.
     """

    booking_url: str
    departure_window: DepartureWindow
    destination_area: str
    free_capacity_kg: float
    free_capacity_ldm: float
    instant_bookable: bool
    match_score: float
    object_: MatchObject
    origin_area: str
    route_id: str
    co2_saved_kg_estimate: float | None | Unset = UNSET
    detour_km: float | None | Unset = UNSET
    instant_price_eur: float | None | Unset = UNSET
    price_estimate_eur: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.departure_window import DepartureWindow # noqa: PLC0415
        booking_url = self.booking_url

        departure_window = self.departure_window.to_dict()

        destination_area = self.destination_area

        free_capacity_kg = self.free_capacity_kg

        free_capacity_ldm = self.free_capacity_ldm

        instant_bookable = self.instant_bookable

        match_score = self.match_score

        object_ = self.object_.value

        origin_area = self.origin_area

        route_id = self.route_id

        co2_saved_kg_estimate: float | None | Unset
        if isinstance(self.co2_saved_kg_estimate, Unset):
            co2_saved_kg_estimate = UNSET
        else:
            co2_saved_kg_estimate = self.co2_saved_kg_estimate

        detour_km: float | None | Unset
        if isinstance(self.detour_km, Unset):
            detour_km = UNSET
        else:
            detour_km = self.detour_km

        instant_price_eur: float | None | Unset
        if isinstance(self.instant_price_eur, Unset):
            instant_price_eur = UNSET
        else:
            instant_price_eur = self.instant_price_eur

        price_estimate_eur: float | None | Unset
        if isinstance(self.price_estimate_eur, Unset):
            price_estimate_eur = UNSET
        else:
            price_estimate_eur = self.price_estimate_eur


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "booking_url": booking_url,
            "departure_window": departure_window,
            "destination_area": destination_area,
            "free_capacity_kg": free_capacity_kg,
            "free_capacity_ldm": free_capacity_ldm,
            "instant_bookable": instant_bookable,
            "match_score": match_score,
            "object": object_,
            "origin_area": origin_area,
            "route_id": route_id,
        })
        if co2_saved_kg_estimate is not UNSET:
            field_dict["co2_saved_kg_estimate"] = co2_saved_kg_estimate
        if detour_km is not UNSET:
            field_dict["detour_km"] = detour_km
        if instant_price_eur is not UNSET:
            field_dict["instant_price_eur"] = instant_price_eur
        if price_estimate_eur is not UNSET:
            field_dict["price_estimate_eur"] = price_estimate_eur

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.departure_window import DepartureWindow # noqa: PLC0415
        d = dict(src_dict)
        booking_url = d.pop("booking_url")

        departure_window = DepartureWindow.from_dict(d.pop("departure_window"))




        destination_area = d.pop("destination_area")

        free_capacity_kg = d.pop("free_capacity_kg")

        free_capacity_ldm = d.pop("free_capacity_ldm")

        instant_bookable = d.pop("instant_bookable")

        match_score = d.pop("match_score")

        object_ = MatchObject(d.pop("object"))




        origin_area = d.pop("origin_area")

        route_id = d.pop("route_id")

        def _parse_co2_saved_kg_estimate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        co2_saved_kg_estimate = _parse_co2_saved_kg_estimate(d.pop("co2_saved_kg_estimate", UNSET))


        def _parse_detour_km(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        detour_km = _parse_detour_km(d.pop("detour_km", UNSET))


        def _parse_instant_price_eur(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        instant_price_eur = _parse_instant_price_eur(d.pop("instant_price_eur", UNSET))


        def _parse_price_estimate_eur(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_estimate_eur = _parse_price_estimate_eur(d.pop("price_estimate_eur", UNSET))


        match = cls(
            booking_url=booking_url,
            departure_window=departure_window,
            destination_area=destination_area,
            free_capacity_kg=free_capacity_kg,
            free_capacity_ldm=free_capacity_ldm,
            instant_bookable=instant_bookable,
            match_score=match_score,
            object_=object_,
            origin_area=origin_area,
            route_id=route_id,
            co2_saved_kg_estimate=co2_saved_kg_estimate,
            detour_km=detour_km,
            instant_price_eur=instant_price_eur,
            price_estimate_eur=price_estimate_eur,
        )

        return match

