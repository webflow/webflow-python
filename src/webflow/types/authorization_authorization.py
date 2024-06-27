# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .authorization_authorization_authorized_to import AuthorizationAuthorizationAuthorizedTo


class AuthorizationAuthorization(pydantic_v1.BaseModel):
    """
    The Authorization object
    """

    id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The unique id of the Authorization instance
    """

    created_on: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="createdOn", default=None)
    """
    The date the Authorization was created
    """

    last_used: typing.Optional[dt.datetime] = pydantic_v1.Field(alias="lastUsed", default=None)
    """
    The date the Authorization was last used
    """

    grant_type: typing.Optional[str] = pydantic_v1.Field(alias="grantType", default=None)
    """
    The grant type of the Authorization
    """

    rate_limit: typing.Optional[int] = pydantic_v1.Field(alias="rateLimit", default=None)
    """
    The default rate limit for the Authorization (requests/min)
    """

    scope: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Comma separted list of OAuth scopes corresponding to the Authorization
    """

    authorized_to: typing.Optional[AuthorizationAuthorizationAuthorizedTo] = pydantic_v1.Field(
        alias="authorizedTo", default=None
    )

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
