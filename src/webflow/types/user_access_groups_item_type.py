# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UserAccessGroupsItemType(str, enum.Enum):
    """
    The type of access group based on how it was assigned to the user.

    - `admin` - Assigned to the user via API or in the designer
    - `ecommerce` - Assigned to the user via an ecommerce purchase
    """

    ADMIN = "admin"
    ECOMMERCE = "ecommerce"

    def visit(self, admin: typing.Callable[[], T_Result], ecommerce: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserAccessGroupsItemType.ADMIN:
            return admin()
        if self is UserAccessGroupsItemType.ECOMMERCE:
            return ecommerce()
