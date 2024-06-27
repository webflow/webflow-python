# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .asset_variant import AssetVariant


class Asset(pydantic_v1.BaseModel):
    id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Unique identifier for this asset
    """

    original_file_name: typing.Optional[str] = pydantic_v1.Field(alias="originalFileName", default=None)
    """
    Original file name at the time of upload
    """

    display_name: typing.Optional[str] = pydantic_v1.Field(alias="displayName", default=None)
    """
    Display name of the asset
    """

    content_type: typing.Optional[str] = pydantic_v1.Field(alias="contentType", default=None)
    """
    File format type
    """

    size: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    size in bytes
    """

    site_id: typing.Optional[str] = pydantic_v1.Field(alias="siteId", default=None)
    """
    Unique identifier for the site that hosts this asset
    """

    created_on: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="createdOn", default=None)
    """
    Date the asset metadata was created
    """

    last_updated: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="lastUpdated", default=None)
    """
    Date the asset metadata was last updated
    """

    hosted_url: typing.Optional[str] = pydantic_v1.Field(alias="hostedUrl", default=None)
    """
    Link to the asset
    """

    variants: typing.Optional[typing.List[AssetVariant]] = None

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
