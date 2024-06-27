# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ItemsListItemsLiveRequestSortBy(str, enum.Enum):
    LAST_PUBLISHED = "lastPublished"
    NAME = "name"
    SLUG = "slug"

    def visit(
        self,
        last_published: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        slug: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ItemsListItemsLiveRequestSortBy.LAST_PUBLISHED:
            return last_published()
        if self is ItemsListItemsLiveRequestSortBy.NAME:
            return name()
        if self is ItemsListItemsLiveRequestSortBy.SLUG:
            return slug()
