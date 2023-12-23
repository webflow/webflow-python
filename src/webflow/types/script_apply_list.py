# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .script_apply import ScriptApply

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ScriptApplyList(pydantic.BaseModel):
    scripts: typing.Optional[typing.List[ScriptApply]]
    last_updated: typing.Optional[str] = pydantic.Field(
        alias="lastUpdated", description="Date when the Site's scripts were last updated"
    )
    created_on: typing.Optional[str] = pydantic.Field(
        alias="createdOn", description="Date when the Site's scripts were created"
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