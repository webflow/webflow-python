
import typing
import httpx
import urllib.parse
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.jsonable_encoder import jsonable_encoder
from .environment import WebflowEnvironment
from .types import OauthScope

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


def authorize_url(
    *,
    client_id: str,
    state: typing.Optional[str] = OMIT,
    redirect_uri: typing.Optional[str] = OMIT,
    scope: typing.Optional[typing.Union[OauthScope, typing.List[OauthScope]]] = OMIT,
) -> str: 
    """
    Get the URL to authorize a user

    Parameters:
        - client_id: str. The OAuth client ID

        - state: typing.Optional[str]. The state.

        - redirect_uri: typing.Optional[str]. The redirect URI.

        - scope: typing.Optional[typing.Union[OauthScope, typing.List[OauthScope]]]. 
          OAuth Scopes.
    ---
    from webflow.oauth import authorize_url
    from webflow import OauthScope

    url = authorize_url(
        client_id = "<YOUR_CLIENT_ID>",
        redirect_uri = "https://my.server.com/oauth/callback",
        scopes =  [OauthScope.ReadSites, OauthScope.WriteItems", OauthScope.ReadUsers],
    )
    """
    params: typing.Dict[str, typing.Any] = {
        "client_id": client_id,
        "response_type": "code",
    }
    if state is not OMIT: 
        params["state"] = state
    if redirect_uri is not OMIT: 
        params["redirect_uri"] = redirect_uri
    if scope is not OMIT and isinstance(scope, str): 
        params["scope"] = scope.value
    elif scope is not OMIT: 
        params["scope"] = " ".join([s.value for s in scope])  # type: ignore
    return f"https://webflow.com/oauth/authorize?{urllib.parse.urlencode(params)}"


def get_access_token(
    *,
    client_id: str,
    client_secret: str,
    code: str,
    redirect_uri: typing.Optional[str] = OMIT,
) -> str: 
    """
    Get the URL to authorize a user

    Parameters:
        - client_id: str. The OAuth client ID

        - client_secret: str. The OAuth client secret

        - code: str. The OAuth code

        - redirect_uri: typing.Optional[str]. The redirect URI.
    ---
    from webflow.oauth import get_access_token

    token = get_access_token(
        client_id = "<YOUR_CLIENT_ID>",
        client_secret = "<YOUR_CLIENT_ID>",
        code= "<YOUR_CODE>"
        redirect_uri = "https://my.server.com/oauth/callback",
    )
    """
    request: typing.Dict[str, typing.Any] = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "grant_type": "authorization_code",
    }
    if redirect_uri is not OMIT: 
        request["redirect_uri"] = redirect_uri
    response = httpx.request(
        "POST",
        "https://api.webflow.com/oauth/access_token",
        json=jsonable_encoder(request),
        timeout=60,
    )
    if 200 <= response.status_code < 300:
        _response_json = response.json()
        return _response_json["access_token"]
    try:
        raise ApiError(status_code=response.status_code, body=response.json())
    except JSONDecodeError:
        raise ApiError(status_code=response.status_code, body=response.text)

