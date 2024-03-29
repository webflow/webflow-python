# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AssetVariant(pydantic.BaseModel):
    hosted_url: typing.Optional[str] = pydantic.Field(alias="hostedUrl", default=None)
    original_file_name: typing.Optional[str] = pydantic.Field(alias="originalFileName", default=None)
    display_name: typing.Optional[str] = pydantic.Field(alias="displayName", default=None)
    format: typing.Optional[str] = None
    width: typing.Optional[int] = pydantic.Field(default=None, description="Width in pixels")
    height: typing.Optional[int] = pydantic.Field(default=None, description="Height in pixels")
    quality: typing.Optional[int] = pydantic.Field(
        default=None, description="Value between 0 and 100 representing the image quality"
    )
    error: typing.Optional[str] = pydantic.Field(default=None, description="Any associated validation errors")

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
