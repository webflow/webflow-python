# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .form_field_value_type import FormFieldValueType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class FormFieldValue(pydantic.BaseModel):
    display_name: typing.Optional[str] = pydantic.Field(
        alias="displayName", description="The field name displayed on the site"
    )
    type: typing.Optional[FormFieldValueType] = pydantic.Field(description="The field type")
    placeholder: typing.Optional[str] = pydantic.Field(description="The placeholder text for the field")
    user_visible: typing.Optional[bool] = pydantic.Field(
        alias="userVisible", description="Whether the field is visible to the user"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}