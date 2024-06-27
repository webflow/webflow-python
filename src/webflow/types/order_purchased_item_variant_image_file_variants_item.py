# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class OrderPurchasedItemVariantImageFileVariantsItem(pydantic_v1.BaseModel):
    url: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The hosted location for the Variant's image
    """

    original_file_name: typing.Optional[str] = pydantic_v1.Field(alias="originalFileName", default=None)
    size: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    The image size in bytes
    """

    width: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The image width in pixels
    """

    height: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The image height in pixels
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
