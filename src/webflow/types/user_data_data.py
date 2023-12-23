# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class UserDataData(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(description="The name of the user")
    email: typing.Optional[str] = pydantic.Field(description="The email address of the user")
    accept_privacy: typing.Optional[bool] = pydantic.Field(
        alias="accept-privacy", description="Boolean indicating if the user has accepted the privacy policy"
    )
    accept_communications: typing.Optional[bool] = pydantic.Field(
        alias="accept-communications",
        description="Boolean indicating if the user has accepted to receive communications",
    )
    additional_properties: typing.Optional[str] = pydantic.Field(
        alias="additionalProperties", description="Custom user attributes"
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