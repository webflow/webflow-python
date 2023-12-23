# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .authorization_authorization_authorized_to import AuthorizationAuthorizationAuthorizedTo

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AuthorizationAuthorization(pydantic.BaseModel):
    """
    The Authorization object
    """

    id: typing.Optional[str] = pydantic.Field(description="The unique id of the Authorization instance")
    created_on: typing.Optional[dt.datetime] = pydantic.Field(
        alias="createdOn", description="The date the Authorization was created"
    )
    last_used: typing.Optional[dt.datetime] = pydantic.Field(
        alias="lastUsed", description="The date the Authorization was last used"
    )
    grant_type: typing.Optional[str] = pydantic.Field(
        alias="grantType", description="The grant type of the Authorization"
    )
    rate_limit: typing.Optional[int] = pydantic.Field(
        alias="rateLimit", description="The default rate limit for the Authorization (requests/min)"
    )
    scope: typing.Optional[str] = pydantic.Field(
        description="Comma separted list of OAuth scopes corresponding to the Authorization"
    )
    authorized_to: typing.Optional[AuthorizationAuthorizationAuthorizedTo] = pydantic.Field(alias="authorizedTo")

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