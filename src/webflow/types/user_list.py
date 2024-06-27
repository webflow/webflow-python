# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .user import User


class UserList(pydantic_v1.BaseModel):
    """
    The list users results
    """

    count: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Number of users returned
    """

    limit: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    The limit specified in the request
    """

    offset: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    The offset specified for pagination
    """

    total: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Total number of users in the collection
    """

    users: typing.Optional[typing.List[User]] = pydantic_v1.Field(default=None)
    """
    List of Users for a Site
    """

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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
