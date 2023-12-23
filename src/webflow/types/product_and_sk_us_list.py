# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .pagination import Pagination
from .product_and_sk_us import ProductAndSkUs

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProductAndSkUsList(pydantic.BaseModel):
    """
    Results from product list
    """

    items: typing.Optional[typing.List[ProductAndSkUs]] = pydantic.Field(
        description="List of Item objects within the Collection. Contains product and skus keys for each Item"
    )
    pagination: typing.Optional[Pagination]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}