import pytest

from webflow import authorize_url, get_access_token
from webflow.client import Webflow, AsyncWebflow

# Get started with writing tests with pytest at https://docs.pytest.org
@pytest.mark.skip(reason="Unimplemented")
def test_client() -> None:
    client = Webflow(access_token="")
    client = AsyncWebflow(access_token="")
    client.collections.create()
