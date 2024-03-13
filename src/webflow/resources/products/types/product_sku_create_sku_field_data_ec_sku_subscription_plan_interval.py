# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ProductSkuCreateSkuFieldDataEcSkuSubscriptionPlanInterval(str, enum.Enum):
    """
    Interval of subscription renewal
    """

    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProductSkuCreateSkuFieldDataEcSkuSubscriptionPlanInterval.DAY:
            return day()
        if self is ProductSkuCreateSkuFieldDataEcSkuSubscriptionPlanInterval.WEEK:
            return week()
        if self is ProductSkuCreateSkuFieldDataEcSkuSubscriptionPlanInterval.MONTH:
            return month()
        if self is ProductSkuCreateSkuFieldDataEcSkuSubscriptionPlanInterval.YEAR:
            return year()
