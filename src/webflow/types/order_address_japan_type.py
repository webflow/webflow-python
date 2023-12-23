# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderAddressJapanType(str, enum.Enum):
    """
    Japan-only address format
    """

    KANA = "kana"
    KANJI = "kanji"

    def visit(self, kana: typing.Callable[[], T_Result], kanji: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrderAddressJapanType.KANA:
            return kana()
        if self is OrderAddressJapanType.KANJI:
            return kanji()