# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....types.sku_property_list import SkuPropertyList
from .product_sku_create_product_field_data_ec_product_type import ProductSkuCreateProductFieldDataEcProductType
from .product_sku_create_product_field_data_tax_category import ProductSkuCreateProductFieldDataTaxCategory

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProductSkuCreateProductFieldData(pydantic.BaseModel):
    name: str = pydantic.Field(description="Name of the Product")
    slug: str = pydantic.Field(description="URL structure of the Product in your site.")
    description: typing.Optional[str] = pydantic.Field(default=None, description="A description of your product")
    shippable: typing.Optional[bool] = pydantic.Field(
        default=None, description="Boolean determining if the Product is shippable"
    )
    sku_properties: typing.Optional[typing.List[SkuPropertyList]] = pydantic.Field(
        alias="sku-properties", default=None, description="Variant types to include in SKUs"
    )
    categories: typing.Optional[typing.List[typing.Any]] = pydantic.Field(
        default=None, description="The categories your product belongs to."
    )
    tax_category: typing.Optional[ProductSkuCreateProductFieldDataTaxCategory] = pydantic.Field(
        alias="tax-category", default=None, description="Product tax class"
    )
    ec_product_type: typing.Optional[ProductSkuCreateProductFieldDataEcProductType] = pydantic.Field(
        alias="ec-product-type",
        default=None,
        description='<a href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product types.</a> Enums reflect the following values in order: Physical, Digital, Service, Advanced"',
    )
    additional_properties: typing.Optional[typing.Any] = pydantic.Field(alias="additionalProperties", default=None)

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
