# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .site_activity_log_item_resource_operation import SiteActivityLogItemResourceOperation
from .site_activity_log_item_user import SiteActivityLogItemUser


class SiteActivityLogItem(pydantic_v1.BaseModel):
    id: typing.Optional[str] = None
    created_on: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="createdOn", default=None)
    last_updated: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="lastUpdated", default=None)
    event: typing.Optional[str] = None
    resource_operation: typing.Optional[SiteActivityLogItemResourceOperation] = pydantic_v1.Field(
        alias="resourceOperation", default=None
    )
    user: typing.Optional[SiteActivityLogItemUser] = None
    resource_id: typing.Optional[str] = pydantic_v1.Field(alias="resourceId", default=None)
    resource_name: typing.Optional[str] = pydantic_v1.Field(alias="resourceName", default=None)
    new_value: typing.Optional[str] = pydantic_v1.Field(alias="newValue", default=None)
    previous_value: typing.Optional[str] = pydantic_v1.Field(alias="previousValue", default=None)
    payload: typing.Optional[typing.Dict[str, typing.Any]] = None

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
