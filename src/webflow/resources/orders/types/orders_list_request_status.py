# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrdersListRequestStatus(str, enum.Enum):
    PENDING = "pending"
    REFUNDED = "refunded"
    DISPUTE_LOST = "dispute-lost"
    FULFILLED = "fulfilled"
    DISPUTED = "disputed"
    UNFULFILLED = "unfulfilled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        dispute_lost: typing.Callable[[], T_Result],
        fulfilled: typing.Callable[[], T_Result],
        disputed: typing.Callable[[], T_Result],
        unfulfilled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrdersListRequestStatus.PENDING:
            return pending()
        if self is OrdersListRequestStatus.REFUNDED:
            return refunded()
        if self is OrdersListRequestStatus.DISPUTE_LOST:
            return dispute_lost()
        if self is OrdersListRequestStatus.FULFILLED:
            return fulfilled()
        if self is OrdersListRequestStatus.DISPUTED:
            return disputed()
        if self is OrdersListRequestStatus.UNFULFILLED:
            return unfulfilled()