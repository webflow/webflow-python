# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class StripeDetails(pydantic_v1.BaseModel):
    """
    An object with various Stripe IDs, useful for linking into the stripe dashboard.
    """

    subscription_id: typing.Optional[str] = pydantic_v1.Field(alias="subscriptionId", default=None)
    """
    Stripe-generated identifier for the Subscription
    """

    payment_method: typing.Optional[str] = pydantic_v1.Field(alias="paymentMethod", default=None)
    """
    Stripe-generated identifier for the PaymentMethod used
    """

    payment_intent_id: typing.Optional[str] = pydantic_v1.Field(alias="paymentIntentId", default=None)
    """
    Stripe-generated identifier for the PaymentIntent, or null
    """

    customer_id: typing.Optional[str] = pydantic_v1.Field(alias="customerId", default=None)
    """
    Stripe-generated customer identifier, or null
    """

    charge_id: typing.Optional[str] = pydantic_v1.Field(alias="chargeId", default=None)
    """
    Stripe-generated charge identifier, or null
    """

    dispute_id: typing.Optional[str] = pydantic_v1.Field(alias="disputeId", default=None)
    """
    Stripe-generated dispute identifier, or null
    """

    refund_id: typing.Optional[str] = pydantic_v1.Field(alias="refundId", default=None)
    """
    Stripe-generated refund identifier, or null
    """

    refund_reason: typing.Optional[str] = pydantic_v1.Field(alias="refundReason", default=None)
    """
    Stripe-generated refund reason, or null
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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
