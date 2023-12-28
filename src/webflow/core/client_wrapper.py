# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(self, *, access_token: typing.Union[str, typing.Callable[[], str]], base_url: str):
        self._access_token = access_token
        self._base_url = base_url

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "webflow",
            "X-Fern-SDK-Version": "0.1.0b1",
        }
        headers["Authorization"] = f"Bearer {self._get_access_token()}"
        return headers

    def _get_access_token(self) -> str:
        if isinstance(self._access_token, str):
            return self._access_token
        else:
            return self._access_token()

    def get_base_url(self) -> str:
        return self._base_url


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self, *, access_token: typing.Union[str, typing.Callable[[], str]], base_url: str, httpx_client: httpx.Client
    ):
        super().__init__(access_token=access_token, base_url=base_url)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        access_token: typing.Union[str, typing.Callable[[], str]],
        base_url: str,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(access_token=access_token, base_url=base_url)
        self.httpx_client = httpx_client
