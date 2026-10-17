from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.error_body_type import ErrorBodyType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ErrorBody")



@_attrs_define
class ErrorBody:
    """ 
        Attributes:
            code (str): Machine-readable error code. Example: invalid_parameter.
            message (str): Human-readable explanation.
            type_ (ErrorBodyType): Error category.
            param (None | str | Unset): Request field the error refers to, if any. Example: weight_kg.
     """

    code: str
    message: str
    type_: ErrorBodyType
    param: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        type_ = self.type_.value

        param: None | str | Unset
        if isinstance(self.param, Unset):
            param = UNSET
        else:
            param = self.param


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code": code,
            "message": message,
            "type": type_,
        })
        if param is not UNSET:
            field_dict["param"] = param

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        type_ = ErrorBodyType(d.pop("type"))




        def _parse_param(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        param = _parse_param(d.pop("param", UNSET))


        error_body = cls(
            code=code,
            message=message,
            type_=type_,
            param=param,
        )

        return error_body

