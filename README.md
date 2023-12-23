# Webflow Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

The Webflow Python Library provides convenient access to the Webflow API from 
applications written in Python. The library includes type definitions for all 
request and response fields, and offers both synchronous and asynchronous clients powered by httpx.

## Documentation

API reference documentation is available [here](https://developers.webflow.com/reference/designer-api-reference).

## Installation

Add this dependency to your project's build file:

```bash
pip install webflow
# or
poetry add webflow
```

## Usage
Simply import `Webflow` and start making calls to our API. 

```python
from webflow.client import Webflow

client = Webflow(
  client_id="YOUR_CLIENT_ID",
  client_secret="YOUR_CLIENT_SECRET",
  code="YOUR_AUTHORIZATION_CODE"
)
site = client.sites.get("site-id")
```

## Async Client
The SDK also exports an async client so that you can make non-blocking
calls to our API. 

```python
from webflow.client import AsyncWebflow

client = AsyncWebflow(
  client_id="YOUR_CLIENT_ID",
  client_secret="YOUR_CLIENT_SECRET", 
  code="YOUR_AUTHORIZATION_CODE"
)

async def main() -> None:
    site = await client.sites.get("site-id")
    print("Received site", site)

asyncio.run(main())
```

## OAuth

To implement OAuth, you'll need a registred Webflow App.

### Step 1: Authorize URL 

The first step in OAuth is to generate an authorization url. Use this URL 
to fetch your authorization code. See the [docs](https://docs.developers.webflow.com/v1.0.0/docs/oauth#user-authorization)
for more details. 

```python
from webflow.oauth import authorize_url
from webflow import OauthScope

url = webflow.authorize_url({
  client_id = "[CLIENT ID]",
  scope = OauthScope.ReadUsers, # or [OauthScope.ReadUsers, OauthScope.WriteUsers]
  state = "1234567890", # optional
  redirect_uri = "https://my.server.com/oauth/callback", # optional
});

print(url)
```

### Step 2: Instantiate the client
Pass in your `client_id`, `client_secret`, `authorization_code` when instantiating 
the client. Our SDK handles generating an access token and passing that to every endpoint. 

```python
from webflow.client import Webflow

client = Webflow(
  client_id="YOUR_CLIENT_ID",
  client_secret="YOUR_CLIENT_SECRET",
  code="YOUR_AUTHORIZATION_CODE",
  redirect_uri = "https://my.server.com/oauth/callback", # optional
)
```

If you want to generate an access token yourself, simply import the 
`get_access_token` function. 

```python
from webflow.oauth import get_access_token

access_token = get_access_token(
  client_id="YOUR_CLIENT_ID", 
  client_secret="YOUR_CLIENT_SECRET", 
  code="YOUR_AUTHORIZATION_CODE"
  )
```

## Webflow Module
All of the models are nested within the Webflow module. Let Intellisense 
guide you! 

![Alt text](assets/module.png)

## Exception Handling
All errors thrown by the SDK will be sublcasses of [`ApiError`](./src/webflow/core/api_error.py).

```python
import webflow

try:
  client.sites.get(...)
except webflow.core.ApiError as e: # Handle all errors
  print(e.status_code)
  print(e.body)
except webflow.BadRequestError as e: # Handle specific error
  print(e.status_code)
  print(e.body)
```

## Advanced

### Timeouts
By default requests time out after 60 seconds. You can configure this with a 
timeout option, which accepts a float.

```python
from webflow.client import Webflow

client = Webflow(
    # 20 seconds
    timeout=20.0,
)
```

### Custom HTTP client
You can override the httpx client to customize it for your use case. Some common usecases 
include support for proxies and transports.

```python
import httpx

from webflow.client import Webflow

client = Webflow(
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Beta Status

This SDK is in beta, and there may be breaking changes between versions without a major 
version update. Therefore, we recommend pinning the package version to a specific version. 
This way, you can install the same version each time without breaking changes.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. 
Additions made directly to this library would have to be moved over to our generation code, 
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
 a proof of concept, but know that we will not be able to merge it as-is. We suggest opening 
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
