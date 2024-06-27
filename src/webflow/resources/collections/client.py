# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.collection import Collection
from ...types.collection_list import CollectionList
from .resources.fields.client import AsyncFieldsClient, FieldsClient
from .resources.items.client import AsyncItemsClient, ItemsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CollectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.fields = FieldsClient(client_wrapper=self._client_wrapper)
        self.items = ItemsClient(client_wrapper=self._client_wrapper)

    def list(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> CollectionList:
        """
        List of all Collections within a Site. </br></br> Required scope | `cms:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionList
            Request was successful

        Examples
        --------
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.list(
            site_id="site_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/collections", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CollectionList, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        site_id: str,
        *,
        display_name: str,
        singular_name: str,
        slug: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collection:
        """
        Create a Collection for a site. </br></br> Required scope | `cms:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        display_name : str
            Name of the collection. Each collection name must be distinct.

        singular_name : str
            Singular name of each item.

        slug : typing.Optional[str]
            Part of a URL that identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Request was successful

        Examples
        --------
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.create(
            site_id="site_id",
            display_name="Blog Posts",
            singular_name="Blog Post",
            slug="posts",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/collections",
            method="POST",
            json={"displayName": display_name, "singularName": singular_name, "slug": slug},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Collection, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Collection:
        """
        Get the full details of a collection from its ID. </br></br> Required scope | `cms:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Request was successful

        Examples
        --------
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.get(
            collection_id="collection_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"collections/{jsonable_encoder(collection_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Collection, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_collection(self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a collection using its ID. </br></br> Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.delete_collection(
            collection_id="collection_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"collections/{jsonable_encoder(collection_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, collection_id: str, field_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a custom field in a collection. This endpoint does not currently support bulk deletion. </br></br> Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        field_id : str
            Unique identifier for a Field in a collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.delete(
            collection_id="collection_id",
            field_id="field_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"collections/{jsonable_encoder(collection_id)}/fields/{jsonable_encoder(field_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCollectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.fields = AsyncFieldsClient(client_wrapper=self._client_wrapper)
        self.items = AsyncItemsClient(client_wrapper=self._client_wrapper)

    async def list(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> CollectionList:
        """
        List of all Collections within a Site. </br></br> Required scope | `cms:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionList
            Request was successful

        Examples
        --------
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.list(
            site_id="site_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/collections", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CollectionList, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        site_id: str,
        *,
        display_name: str,
        singular_name: str,
        slug: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collection:
        """
        Create a Collection for a site. </br></br> Required scope | `cms:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        display_name : str
            Name of the collection. Each collection name must be distinct.

        singular_name : str
            Singular name of each item.

        slug : typing.Optional[str]
            Part of a URL that identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Request was successful

        Examples
        --------
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.create(
            site_id="site_id",
            display_name="Blog Posts",
            singular_name="Blog Post",
            slug="posts",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/collections",
            method="POST",
            json={"displayName": display_name, "singularName": singular_name, "slug": slug},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Collection, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Collection:
        """
        Get the full details of a collection from its ID. </br></br> Required scope | `cms:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Request was successful

        Examples
        --------
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.get(
            collection_id="collection_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"collections/{jsonable_encoder(collection_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Collection, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a collection using its ID. </br></br> Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.delete_collection(
            collection_id="collection_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"collections/{jsonable_encoder(collection_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, collection_id: str, field_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a custom field in a collection. This endpoint does not currently support bulk deletion. </br></br> Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        field_id : str
            Unique identifier for a Field in a collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.delete(
            collection_id="collection_id",
            field_id="field_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"collections/{jsonable_encoder(collection_id)}/fields/{jsonable_encoder(field_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 429:
                raise TooManyRequestsError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
