# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .product_field_data import ProductFieldData


class Product(pydantic_v1.BaseModel):
    """
    The Product object
    """

    id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Unique identifier for the Product
    """

    cms_locale_id: typing.Optional[str] = pydantic_v1.Field(alias="cmsLocaleId", default=None)
    """
    Identifier for the locale of the CMS item
    """

    last_published: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="lastPublished", default=None)
    """
    The date the Product was last published
    """

    last_updated: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="lastUpdated", default=None)
    """
    The date the Product was last updated
    """

    created_on: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="createdOn", default=None)
    """
    The date the Product was created
    """

    is_archived: typing.Optional[bool] = pydantic_v1.Field(alias="isArchived", default=None)
    """
    Boolean determining if the Product is set to archived
    """

    is_draft: typing.Optional[bool] = pydantic_v1.Field(alias="isDraft", default=None)
    """
    Boolean determining if the Product is set to draft
    """

    field_data: typing.Optional[ProductFieldData] = pydantic_v1.Field(alias="fieldData", default=None)

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
