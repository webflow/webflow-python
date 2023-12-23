# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PublishStatus(str, enum.Enum):
    """
    Publish target
    """

    STAGING = "staging"
    LIVE = "live"

    def visit(self, staging: typing.Callable[[], T_Result], live: typing.Callable[[], T_Result]) -> T_Result:
        if self is PublishStatus.STAGING:
            return staging()
        if self is PublishStatus.LIVE:
            return live()