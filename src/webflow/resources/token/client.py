# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...errors.forbidden_error import ForbiddenError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.authorization import Authorization
from ...types.authorized_user import AuthorizedUser

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TokenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def authorized_by(self, *, request_options: typing.Optional[RequestOptions] = None) -> AuthorizedUser:
        """
        Information about the Authorized User <br><br> Required Scope | `authorized_user:read`

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.token.authorized_by()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "token/authorized_by"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AuthorizedUser, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def introspect(self, *, request_options: typing.Optional[RequestOptions] = None) -> Authorization:
        """
        Information about the authorization token </br></br> Access to this endpoint requires a bearer token from a Data Client App.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.token.introspect()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "token/introspect"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Authorization, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTokenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def authorized_by(self, *, request_options: typing.Optional[RequestOptions] = None) -> AuthorizedUser:
        """
        Information about the Authorized User <br><br> Required Scope | `authorized_user:read`

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.token.authorized_by()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "token/authorized_by"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AuthorizedUser, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def introspect(self, *, request_options: typing.Optional[RequestOptions] = None) -> Authorization:
        """
        Information about the authorization token </br></br> Access to this endpoint requires a bearer token from a Data Client App.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.token.introspect()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "token/introspect"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Authorization, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
