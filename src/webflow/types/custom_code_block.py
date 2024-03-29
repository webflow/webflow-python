# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .custom_code_block_type import CustomCodeBlockType
from .scripts import Scripts

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CustomCodeBlock(pydantic.BaseModel):
    """
    A specific instance of Custom Code applied to a Site or Page
    """

    site_id: typing.Optional[str] = pydantic.Field(
        alias="siteId", default=None, description="The Site id where the custom code was applied"
    )
    page_id: typing.Optional[str] = pydantic.Field(
        alias="pageId", default=None, description="The Page id (if applied at Page-level)"
    )
    type: typing.Optional[CustomCodeBlockType] = pydantic.Field(
        default=None, description="Whether the Custom Code script is applied at the Site-level or Page-level"
    )
    scripts: typing.Optional[Scripts] = None
    created_on: typing.Optional[dt.datetime] = pydantic.Field(
        alias="createdOn", default=None, description="The date the Block was created"
    )
    last_updated: typing.Optional[dt.datetime] = pydantic.Field(
        alias="lastUpdated", default=None, description="The date the Block was most recently updated"
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
