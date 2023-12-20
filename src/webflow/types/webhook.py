# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .trigger_type import TriggerType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Webhook(pydantic.BaseModel):
    id: typing.Optional[str] = pydantic.Field(description="Unique identifier for the Webhook registration")
    workspace_id: typing.Optional[str] = pydantic.Field(
        alias="workspaceId", description="Unique identifier for the Workspace the Webhook is registered in"
    )
    site_id: typing.Optional[str] = pydantic.Field(
        alias="siteId", description="Unique identifier for the Site the Webhook is registered in"
    )
    trigger_type: typing.Optional[TriggerType] = pydantic.Field(alias="triggerType")
    filter: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="Filter for selecting which events you want Webhooks to be sent for. Only supported for form_submission trigger types."
    )
    last_triggered: typing.Optional[dt.datetime] = pydantic.Field(
        alias="lastTriggered", description="Date the Webhook instance was last triggered"
    )
    created_on: typing.Optional[dt.datetime] = pydantic.Field(
        alias="createdOn", description="Date the Webhook registration was created"
    )
    url: typing.Optional[str] = pydantic.Field(description="URL to send the Webhook payload to")

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
