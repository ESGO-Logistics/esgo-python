from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.me_object import MeObject
from typing import cast

if TYPE_CHECKING:
  from ..models.api_key_info import ApiKeyInfo
  from ..models.quota import Quota





T = TypeVar("T", bound="Me")



@_attrs_define
class Me:
    """ 
        Attributes:
            account_role (str): Role of the ESGO account the key belongs to. Example: buyer.
            key (ApiKeyInfo):
            object_ (MeObject):
            quotas (list[Quota]):
     """

    account_role: str
    key: ApiKeyInfo
    object_: MeObject
    quotas: list[Quota]





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_key_info import ApiKeyInfo # noqa: PLC0415
        from ..models.quota import Quota # noqa: PLC0415
        account_role = self.account_role

        key = self.key.to_dict()

        object_ = self.object_.value

        quotas = []
        for quotas_item_data in self.quotas:
            quotas_item = quotas_item_data.to_dict()
            quotas.append(quotas_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "account_role": account_role,
            "key": key,
            "object": object_,
            "quotas": quotas,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_info import ApiKeyInfo # noqa: PLC0415
        from ..models.quota import Quota # noqa: PLC0415
        d = dict(src_dict)
        account_role = d.pop("account_role")

        key = ApiKeyInfo.from_dict(d.pop("key"))




        object_ = MeObject(d.pop("object"))




        quotas = []
        _quotas = d.pop("quotas")
        for quotas_item_data in (_quotas):
            quotas_item = Quota.from_dict(quotas_item_data)



            quotas.append(quotas_item)


        me = cls(
            account_role=account_role,
            key=key,
            object_=object_,
            quotas=quotas,
        )

        return me

