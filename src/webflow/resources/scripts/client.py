# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.custom_code_response import CustomCodeResponse
from ...types.registered_script_list import RegisteredScriptList

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ScriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RegisteredScriptList:
        """
        List of scripts registered to a Site. </br></br> In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate `custom_code` endpoints. Additionally, Scripts can be remotely hosted, or registered as inline snippets. </br></br> Required scope | `custom_code:read`

        Parameters:
            - site_id: str. Unique identifier for a Site

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.scripts.list(
            site_id="site_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"sites/{jsonable_encoder(site_id)}/registered_scripts"
            ),
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
            return pydantic.parse_obj_as(RegisteredScriptList, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def register_hosted(
        self,
        site_id: str,
        *,
        hosted_location: str,
        integrity_hash: str,
        can_copy: typing.Optional[bool] = OMIT,
        version: str,
        display_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomCodeResponse:
        """
        Add a script to a Site's Custom Code registry. </br></br> In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate `custom_code` endpoints. Additionally, Scripts can be remotely hosted, or registered as inline snippets. </br></br> Required scope | `custom_code:write`

        Parameters:
            - site_id: str. Unique identifier for a Site

            - hosted_location: str. URI for an externally hosted script location

            - integrity_hash: str. Sub-Resource Integrity Hash

            - can_copy: typing.Optional[bool]. Define whether the script can be copied on site duplication and transfer

            - version: str. A Semantic Version (SemVer) string, denoting the version of the script

            - display_name: str. User-facing name for the script

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.scripts.register_hosted(
            site_id="site_id",
            hosted_location="hostedLocation",
            integrity_hash="integrityHash",
            version="version",
            display_name="displayName",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "hostedLocation": hosted_location,
            "integrityHash": integrity_hash,
            "version": version,
            "displayName": display_name,
        }
        if can_copy is not OMIT:
            _request["canCopy"] = can_copy
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"sites/{jsonable_encoder(site_id)}/registered_scripts/hosted",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic.parse_obj_as(CustomCodeResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def register_inline(
        self,
        site_id: str,
        *,
        source_code: str,
        integrity_hash: typing.Optional[str] = OMIT,
        can_copy: typing.Optional[bool] = OMIT,
        version: str,
        display_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomCodeResponse:
        """
        Add a script to a Site's Custom Code registry. Inline scripts can be between 1 and 2000 characters. </br></br> In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate `custom_code` endpoints. </br></br> Required scope | `custom_code:write`

        Parameters:
            - site_id: str. Unique identifier for a Site

            - source_code: str. The code to be added to the site (to be hosted by Webflow).

            - integrity_hash: typing.Optional[str]. Sub-Resource Integrity Hash. Only required for externally hosted scripts (passed via hostedLocation)

            - can_copy: typing.Optional[bool]. Define whether the script can be copied on site duplication and transfer

            - version: str. A Semantic Version (SemVer) string, denoting the version of the script

            - display_name: str. User-facing name for the script

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.scripts.register_inline(
            site_id="site_id",
            source_code="alert('hello world');",
            version="0.0.1",
            display_name="Alert",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "sourceCode": source_code,
            "version": version,
            "displayName": display_name,
        }
        if integrity_hash is not OMIT:
            _request["integrityHash"] = integrity_hash
        if can_copy is not OMIT:
            _request["canCopy"] = can_copy
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"sites/{jsonable_encoder(site_id)}/registered_scripts/inline",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic.parse_obj_as(CustomCodeResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncScriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisteredScriptList:
        """
        List of scripts registered to a Site. </br></br> In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate `custom_code` endpoints. Additionally, Scripts can be remotely hosted, or registered as inline snippets. </br></br> Required scope | `custom_code:read`

        Parameters:
            - site_id: str. Unique identifier for a Site

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.scripts.list(
            site_id="site_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"sites/{jsonable_encoder(site_id)}/registered_scripts"
            ),
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
            return pydantic.parse_obj_as(RegisteredScriptList, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def register_hosted(
        self,
        site_id: str,
        *,
        hosted_location: str,
        integrity_hash: str,
        can_copy: typing.Optional[bool] = OMIT,
        version: str,
        display_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomCodeResponse:
        """
        Add a script to a Site's Custom Code registry. </br></br> In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate `custom_code` endpoints. Additionally, Scripts can be remotely hosted, or registered as inline snippets. </br></br> Required scope | `custom_code:write`

        Parameters:
            - site_id: str. Unique identifier for a Site

            - hosted_location: str. URI for an externally hosted script location

            - integrity_hash: str. Sub-Resource Integrity Hash

            - can_copy: typing.Optional[bool]. Define whether the script can be copied on site duplication and transfer

            - version: str. A Semantic Version (SemVer) string, denoting the version of the script

            - display_name: str. User-facing name for the script

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.scripts.register_hosted(
            site_id="site_id",
            hosted_location="hostedLocation",
            integrity_hash="integrityHash",
            version="version",
            display_name="displayName",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "hostedLocation": hosted_location,
            "integrityHash": integrity_hash,
            "version": version,
            "displayName": display_name,
        }
        if can_copy is not OMIT:
            _request["canCopy"] = can_copy
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"sites/{jsonable_encoder(site_id)}/registered_scripts/hosted",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic.parse_obj_as(CustomCodeResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def register_inline(
        self,
        site_id: str,
        *,
        source_code: str,
        integrity_hash: typing.Optional[str] = OMIT,
        can_copy: typing.Optional[bool] = OMIT,
        version: str,
        display_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomCodeResponse:
        """
        Add a script to a Site's Custom Code registry. Inline scripts can be between 1 and 2000 characters. </br></br> In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate `custom_code` endpoints. </br></br> Required scope | `custom_code:write`

        Parameters:
            - site_id: str. Unique identifier for a Site

            - source_code: str. The code to be added to the site (to be hosted by Webflow).

            - integrity_hash: typing.Optional[str]. Sub-Resource Integrity Hash. Only required for externally hosted scripts (passed via hostedLocation)

            - can_copy: typing.Optional[bool]. Define whether the script can be copied on site duplication and transfer

            - version: str. A Semantic Version (SemVer) string, denoting the version of the script

            - display_name: str. User-facing name for the script

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.scripts.register_inline(
            site_id="site_id",
            source_code="alert('hello world');",
            version="0.0.1",
            display_name="Alert",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "sourceCode": source_code,
            "version": version,
            "displayName": display_name,
        }
        if integrity_hash is not OMIT:
            _request["integrityHash"] = integrity_hash
        if can_copy is not OMIT:
            _request["canCopy"] = can_copy
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"sites/{jsonable_encoder(site_id)}/registered_scripts/inline",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic.parse_obj_as(CustomCodeResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
