# Reference
## Token
<details><summary><code>client.token.<a href="src/webflow/resources/token/client.py">authorized_by</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Information about the Authorized User

Required Scope | `authorized_user:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.token.authorized_by()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.token.<a href="src/webflow/resources/token/client.py">introspect</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Information about the authorization token

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.token.introspect()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sites
<details><summary><code>client.sites.<a href="src/webflow/resources/sites/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a site. 

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope | `workspace:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.sites.create(
    workspace_id="580e63e98c9a982ac9b8b741",
    name="The Hitchhiker's Guide to the Galaxy",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `str` — Unique identifier for a Workspace
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the site
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `typing.Optional[str]` — The workspace or marketplace template to use
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `typing.Optional[str]` — MegaDodo Publications - Potential Book Ideas
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sites.<a href="src/webflow/resources/sites/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all sites the provided access token is able to access.

Required scope | `sites:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.sites.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sites.<a href="src/webflow/resources/sites/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a site.

Required scope | `sites:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.sites.get(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sites.<a href="src/webflow/resources/sites/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a site. 

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope | `sites:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.sites.delete(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sites.<a href="src/webflow/resources/sites/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a site. 

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope | `sites:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.sites.update(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the site
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `typing.Optional[str]` — The parent folder ID of the site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sites.<a href="src/webflow/resources/sites/client.py">get_custom_domain</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all custom domains related to site.

Required scope | `sites:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.sites.get_custom_domain(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sites.<a href="src/webflow/resources/sites/client.py">publish</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publishes a site to one or more more domains.

<Note title="Endpoint-specific rate limit">This endpoint has a limit of one successful publish queue per minute.</Note>

Required scope | `sites:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.sites.publish(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**custom_domains:** `typing.Optional[typing.Sequence[str]]` — Array of Custom Domain IDs to publish
    
</dd>
</dl>

<dl>
<dd>

**publish_to_webflow_subdomain:** `typing.Optional[bool]` — Choice of whether to publish to the default Webflow Subdomain
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Collections
<details><summary><code>client.collections.<a href="src/webflow/resources/collections/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all Collections within a Site.

Required scope | `cms:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.list(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/webflow/resources/collections/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Collection for a site.

Required scope | `cms:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.create(
    site_id="580e63e98c9a982ac9b8b741",
    display_name="Blog Posts",
    singular_name="Blog Post",
    slug="posts",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` — Name of the collection. Each collection name must be distinct.
    
</dd>
</dl>

<dl>
<dd>

**singular_name:** `str` — Singular name of each item.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — Part of a URL that identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/webflow/resources/collections/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the full details of a collection from its ID.

Required scope | `cms:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.get(
    collection_id="580e63fc8c9a982ac9b8b745",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — Unique identifier for a Collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/webflow/resources/collections/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a collection using its ID.

Required scope | `cms:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.delete(
    collection_id="580e63fc8c9a982ac9b8b745",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — Unique identifier for a Collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Pages
<details><summary><code>client.pages.<a href="src/webflow/resources/pages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all pages for a site.

Required scope | `pages:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.pages.list(
    site_id="580e63e98c9a982ac9b8b741",
    locale_id="65427cf400e02b306eaa04a0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `typing.Optional[str]` — Unique identifier for a specific locale. Applicable, when using localization.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum number of records to be returned (max limit: 100)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Offset used for pagination if the results have more than limit records
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/webflow/resources/pages/client.py">get_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get metadata information for a single page.

Required scope | `pages:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.pages.get_metadata(
    page_id="63c720f9347c2139b248e552",
    locale_id="65427cf400e02b306eaa04a0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — Unique identifier for a Page
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `typing.Optional[str]` — Unique identifier for a specific locale. Applicable, when using localization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/webflow/resources/pages/client.py">update_page_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Page-level metadata, including SEO and Open Graph fields.

Required scope | `pages:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from webflow import PageOpenGraph, PageSeo, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.pages.update_page_settings(
    page_id="63c720f9347c2139b248e552",
    locale_id="65427cf400e02b306eaa04a0",
    id="6596da6045e56dee495bcbba",
    site_id="6258612d1ee792848f805dcf",
    title="Guide to the Galaxy",
    slug="guide-to-the-galaxy",
    created_on=datetime.datetime.fromisoformat(
        "2024-03-11 10:42:00+00:00",
    ),
    last_updated=datetime.datetime.fromisoformat(
        "2024-03-11 10:42:42+00:00",
    ),
    archived=False,
    draft=False,
    can_branch=True,
    is_branch=False,
    seo=PageSeo(
        title="The Ultimate Hitchhiker's Guide to the Galaxy",
        description="Everything you need to know about the galaxy, from avoiding Vogon poetry to the importance of towels.",
    ),
    open_graph=PageOpenGraph(
        title="Explore the Cosmos with The Ultimate Guide",
        title_copied=False,
        description="Dive deep into the mysteries of the universe with your guide to everything galactic.",
        description_copied=False,
    ),
    page_locale_id="653fd9af6a07fc9cfd7a5e57",
    published_path="/en-us/guide-to-the-galaxy",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — Unique identifier for a Page
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Unique identifier for the Page
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `typing.Optional[str]` — Unique identifier for a specific locale. Applicable, when using localization.
    
</dd>
</dl>

<dl>
<dd>

**site_id:** `typing.Optional[str]` — Unique identifier for the Site
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title of the Page
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — slug of the Page (derived from title)
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Identifier of the parent folder
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` — Unique identifier for a linked Collection, value will be null if the Page is not part of a Collection.
    
</dd>
</dl>

<dl>
<dd>

**created_on:** `typing.Optional[dt.datetime]` — The date the Page was created
    
</dd>
</dl>

<dl>
<dd>

**last_updated:** `typing.Optional[dt.datetime]` — The date the Page was most recently updated
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Whether the Page has been archived
    
</dd>
</dl>

<dl>
<dd>

**draft:** `typing.Optional[bool]` — Whether the Page is a draft
    
</dd>
</dl>

<dl>
<dd>

**can_branch:** `typing.Optional[bool]` — Indicates whether the Page supports [Page Branching](https://university.webflow.com/lesson/page-branching)
    
</dd>
</dl>

<dl>
<dd>

**is_branch:** `typing.Optional[bool]` — Indicates whether the Page is a Branch of another Page [Page Branching](https://university.webflow.com/lesson/page-branching)
    
</dd>
</dl>

<dl>
<dd>

**is_members_only:** `typing.Optional[bool]` — Indicates whether the Page is restricted by [Memberships Controls](https://university.webflow.com/lesson/webflow-memberships-overview#how-to-manage-page-restrictions)
    
</dd>
</dl>

<dl>
<dd>

**seo:** `typing.Optional[PageSeo]` — SEO-related fields for the Page
    
</dd>
</dl>

<dl>
<dd>

**open_graph:** `typing.Optional[PageOpenGraph]` — Open Graph fields for the Page
    
</dd>
</dl>

<dl>
<dd>

**page_locale_id:** `typing.Optional[str]` — Unique ID of the page locale
    
</dd>
</dl>

<dl>
<dd>

**published_path:** `typing.Optional[str]` — Relative path of the published page URL
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/webflow/resources/pages/client.py">get_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get content from a static page. This includes text nodes, image nodes, and component instances with [property overrides](https://help.webflow.com/hc/en-us/articles/33961219350547-Component-properties#how-to-modify-property-values-on-component-instances).

To retrieve the static content of a component instance, use the [Get Component Content](/data/reference/pages-and-components/components/get-content) endpoint.

<Note>If you do not include a `localeId` in your request, the response will return any content that can be localized from the Primary locale.</Note>

Required scope | `pages:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.pages.get_content(
    page_id="63c720f9347c2139b248e552",
    locale_id="65427cf400e02b306eaa04a0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — Unique identifier for a Page
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `typing.Optional[str]` — Unique identifier for a specific locale. Applicable, when using localization.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum number of records to be returned (max limit: 100)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Offset used for pagination if the results have more than limit records
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/webflow/resources/pages/client.py">update_static_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint updates content on a static page in **secondary locales**. It supports updating up to 1000 nodes in a single request.

Before making updates:
1. Use the [get page content](/data/reference/pages-and-components/pages/get-content) endpoint to identify available content nodes and their types
2. If the page has component instances, retrieve the component's properties that you'll override using the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint

<Note>
  This endpoint is specifically for localized pages. Ensure that the specified `localeId` is a valid **secondary locale** for the site otherwise the request will fail.
</Note>

Required scope | `pages:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import (
    ComponentInstanceNodePropertyOverridesWrite,
    ComponentInstanceNodePropertyOverridesWritePropertyOverridesItem,
    TextNodeWrite,
    Webflow,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.pages.update_static_content(
    page_id="63c720f9347c2139b248e552",
    locale_id="localeId",
    nodes=[
        TextNodeWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad623",
            text="<h1>The Hitchhiker's Guide to the Galaxy</h1>",
        ),
        TextNodeWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad627",
            text="<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>",
        ),
        ComponentInstanceNodePropertyOverridesWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad629",
            property_overrides=[
                ComponentInstanceNodePropertyOverridesWritePropertyOverridesItem(
                    property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f0",
                    text="<div><h1>Time is an <em>illusion</em></h1></div>",
                ),
                ComponentInstanceNodePropertyOverridesWritePropertyOverridesItem(
                    property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f1",
                    text="Life, the Universe and Everything",
                ),
            ],
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — Unique identifier for a Page
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `str` — The locale identifier.
    
</dd>
</dl>

<dl>
<dd>

**nodes:** `typing.Sequence[PageDomWriteNodesItem]` — List of DOM Nodes with the new content that will be updated in each node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Components
<details><summary><code>client.components.<a href="src/webflow/resources/components/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all components for a site.

Required scope | `components:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.components.list(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum number of records to be returned (max limit: 100)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Offset used for pagination if the results have more than limit records
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.components.<a href="src/webflow/resources/components/client.py">get_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get static content from a component definition. This includes text nodes, image nodes and nested component instances.
To retrieve dynamic content set by component properties, use the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint.

<Note>If you do not provide a Locale ID in your request, the response will return any content that can be localized from the Primary locale.</Note>

Required scope | `components:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.components.get_content(
    site_id="580e63e98c9a982ac9b8b741",
    component_id="8505ba55-ef72-629e-f85c-33e4b703d48b",
    locale_id="65427cf400e02b306eaa04a0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**component_id:** `str` — Unique identifier for a Component
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `typing.Optional[str]` — Unique identifier for a specific locale. Applicable, when using localization.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum number of records to be returned (max limit: 100)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Offset used for pagination if the results have more than limit records
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.components.<a href="src/webflow/resources/components/client.py">update_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint updates content within a component defintion for **secondary locales**. It supports updating up to 1000 nodes in a single request.

Before making updates:
1. Use the [get component content](/data/reference/pages-and-components/components/get-content) endpoint to identify available content nodes and their types
2. If your component definition has a component instance nested within it, retrieve the nested component instance's properties that you'll override using the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint

<Note>
  This endpoint is specifically for localizing component definitions. Ensure that the specified `localeId` is a valid **secondary locale** for the site otherwise the request will fail.
</Note>

Required scope | `components:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import (
    ComponentInstanceNodePropertyOverridesWrite,
    ComponentInstanceNodePropertyOverridesWritePropertyOverridesItem,
    TextNodeWrite,
    Webflow,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.components.update_content(
    site_id="580e63e98c9a982ac9b8b741",
    component_id="8505ba55-ef72-629e-f85c-33e4b703d48b",
    locale_id="65427cf400e02b306eaa04a0",
    nodes=[
        TextNodeWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad623",
            text="<h1>The Hitchhiker's Guide to the Galaxy</h1>",
        ),
        TextNodeWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad627",
            text="<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>",
        ),
        ComponentInstanceNodePropertyOverridesWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad629",
            property_overrides=[
                ComponentInstanceNodePropertyOverridesWritePropertyOverridesItem(
                    property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f0",
                    text="<div><h1>Time is an <em>illusion</em></h1></div>",
                ),
                ComponentInstanceNodePropertyOverridesWritePropertyOverridesItem(
                    property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f1",
                    text="Life, the Universe and Everything",
                ),
            ],
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**component_id:** `str` — Unique identifier for a Component
    
</dd>
</dl>

<dl>
<dd>

**nodes:** `typing.Sequence[ComponentDomWriteNodesItem]` — List of DOM Nodes with the new content that will be updated in each node.
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `typing.Optional[str]` — Unique identifier for a specific locale. Applicable, when using localization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.components.<a href="src/webflow/resources/components/client.py">get_properties</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the default property values of a component definition.

<Note>If you do not include a `localeId` in your request, the response will return any properties that can be localized from the Primary locale.</Note>

Required scope | `components:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.components.get_properties(
    site_id="580e63e98c9a982ac9b8b741",
    component_id="8505ba55-ef72-629e-f85c-33e4b703d48b",
    locale_id="65427cf400e02b306eaa04a0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**component_id:** `str` — Unique identifier for a Component
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `typing.Optional[str]` — Unique identifier for a specific locale. Applicable, when using localization.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum number of records to be returned (max limit: 100)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Offset used for pagination if the results have more than limit records
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.components.<a href="src/webflow/resources/components/client.py">update_properties</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the default property values of a component definition in a specificed locale.

Before making updates, use the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint to identify properties that can be updated in a secondary locale.

<Note>The request requires a secondary locale ID. If a `localeId` is missing, the request will not be processed and will result in an error.</Note>

Required scope | `components:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow
from webflow.resources.components import ComponentPropertiesWritePropertiesItem

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.components.update_properties(
    site_id="580e63e98c9a982ac9b8b741",
    component_id="8505ba55-ef72-629e-f85c-33e4b703d48b",
    locale_id="65427cf400e02b306eaa04a0",
    properties=[
        ComponentPropertiesWritePropertiesItem(
            property_id="a245c12d-995b-55ee-5ec7-aa36a6cad623",
            text="The Hitchhiker’s Guide to the Galaxy",
        ),
        ComponentPropertiesWritePropertiesItem(
            property_id="a245c12d-995b-55ee-5ec7-aa36a6cad627",
            text="<div><h3>Dont Panic!</h3><p>Always know where your towel is.</p></div>",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**component_id:** `str` — Unique identifier for a Component
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Sequence[ComponentPropertiesWritePropertiesItem]` — A list of component properties to update within the specified secondary locale.
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `typing.Optional[str]` — Unique identifier for a specific locale. Applicable, when using localization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scripts
<details><summary><code>client.scripts.<a href="src/webflow/resources/scripts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of scripts that have been registered to a site. A site can have a maximum of 800 registered scripts.

<Note title="Script Registration">
  To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
</Note>

Required scope | `custom_code:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.scripts.list(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scripts.<a href="src/webflow/resources/scripts/client.py">register_hosted</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a hosted script to a site.

<Note title="Script Registration">
  To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
</Note>

Required scope | `custom_code:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.scripts.register_hosted(
    site_id="580e63e98c9a982ac9b8b741",
    hosted_location="hostedLocation",
    integrity_hash="integrityHash",
    version="version",
    display_name="displayName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**hosted_location:** `str` — URI for an externally hosted script location
    
</dd>
</dl>

<dl>
<dd>

**integrity_hash:** `str` — Sub-Resource Integrity Hash
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — A Semantic Version (SemVer) string, denoting the version of the script
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` — User-facing name for the script. Must be between 1 and 50 alphanumeric characters
    
</dd>
</dl>

<dl>
<dd>

**can_copy:** `typing.Optional[bool]` — Define whether the script can be copied on site duplication and transfer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scripts.<a href="src/webflow/resources/scripts/client.py">register_inline</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register an inline script to a site. Inline scripts are limited to 2000 characters.

<Note title="Script Registration">
  To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
</Note>

Required scope | `custom_code:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.scripts.register_inline(
    site_id="580e63e98c9a982ac9b8b741",
    source_code="alert('hello world');",
    version="0.0.1",
    display_name="Alert",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**source_code:** `str` — The code to be added to the site (to be hosted by Webflow).
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — A Semantic Version (SemVer) string, denoting the version of the script
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` — User-facing name for the script. Must be between 1 and 50 alphanumeric characters
    
</dd>
</dl>

<dl>
<dd>

**integrity_hash:** `typing.Optional[str]` — Sub-Resource Integrity Hash. Only required for externally hosted scripts (passed via hostedLocation)
    
</dd>
</dl>

<dl>
<dd>

**can_copy:** `typing.Optional[bool]` — Define whether the script can be copied on site duplication and transfer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Assets
<details><summary><code>client.assets.<a href="src/webflow/resources/assets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of assets uploaded to a site

Required scope | `assets:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.assets.list(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/webflow/resources/assets/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The first step in uploading an asset to a site. 


This endpoint generates a response with the following information: `uploadUrl` and `uploadDetails`.


Use these properties in the header of a [POST request to Amazson s3](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html) to complete the upload.


To learn more about how to upload assets to Webflow, see our [assets guide](/data/docs/working-with-assets).
  
 Required scope | `assets:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.assets.create(
    site_id="580e63e98c9a982ac9b8b741",
    file_name="file.png",
    file_hash="3c7d87c9575702bc3b1e991f4d3c638e",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — File name including file extension. File names must be less than 100 characters.
    
</dd>
</dl>

<dl>
<dd>

**file_hash:** `str` — MD5 hash of the file
    
</dd>
</dl>

<dl>
<dd>

**parent_folder:** `typing.Optional[str]` — ID of the Asset folder (optional)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/webflow/resources/assets/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about an asset

Required scope | `assets:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.assets.get(
    asset_id="580e63fc8c9a982ac9b8b745",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — Unique identifier for an Asset on a site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/webflow/resources/assets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an Asset

Required Scope: `assets: write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.assets.delete(
    asset_id="580e63fc8c9a982ac9b8b745",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — Unique identifier for an Asset on a site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/webflow/resources/assets/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update details of an Asset.

Required scope | `assets:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.assets.update(
    asset_id="580e63fc8c9a982ac9b8b745",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — Unique identifier for an Asset on a site
    
</dd>
</dl>

<dl>
<dd>

**locale_id:** `typing.Optional[str]` — Unique identifier for a specific locale. Applicable, when using localization.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — A human readable name for the asset
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/webflow/resources/assets/client.py">list_folders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Asset Folders within a given site

Required scope | `assets:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.assets.list_folders(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/webflow/resources/assets/client.py">create_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an Asset Folder within a given site

Required scope | `assets:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.assets.create_folder(
    site_id="580e63e98c9a982ac9b8b741",
    display_name="my asset folder",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` — A human readable name for the Asset Folder
    
</dd>
</dl>

<dl>
<dd>

**parent_folder:** `typing.Optional[str]` — An (optional) pointer to a parent Asset Folder (or null for root)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/webflow/resources/assets/client.py">get_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about a specific Asset Folder

Required scope | `assets:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.assets.get_folder(
    asset_folder_id="6390c49774a71f0e3c1a08ee",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_folder_id:** `str` — Unique identifier for an Asset Folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/webflow/resources/webhooks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all App-created Webhooks registered for a given site

Required scope | `sites:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.webhooks.list(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/webflow/resources/webhooks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Webhook.

Limit of 75 registrations per `triggerType`, per site.

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>
Required scope | `sites:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.webhooks.create(
    site_id_="580e63e98c9a982ac9b8b741",
    id="582266e0cd48de0f0e3c6d8b",
    trigger_type="form_submission",
    url="https://webhook.site/7f7f7f7f-7f7f-7f7f-7f7f-7f7f7f7f7f7f",
    workspace_id="4f4e46fd476ea8c507000001",
    site_id="562ac0395358780a1f5e6fbd",
    last_triggered=datetime.datetime.fromisoformat(
        "2023-02-08 23:59:28+00:00",
    ),
    created_on=datetime.datetime.fromisoformat(
        "2022-11-08 23:59:28+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id_:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier for the Webhook registration
    
</dd>
</dl>

<dl>
<dd>

**trigger_type:** `typing.Optional[TriggerType]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL to send the Webhook payload to
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — Unique identifier for the Workspace the Webhook is registered in
    
</dd>
</dl>

<dl>
<dd>

**site_id:** `typing.Optional[str]` — Unique identifier for the Site the Webhook is registered in
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[WebhookFilter]` — Only supported for the `form_submission` trigger type. Filter for the form you want Webhooks to be sent for.
    
</dd>
</dl>

<dl>
<dd>

**last_triggered:** `typing.Optional[dt.datetime]` — Date the Webhook instance was last triggered
    
</dd>
</dl>

<dl>
<dd>

**created_on:** `typing.Optional[dt.datetime]` — Date the Webhook registration was created
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/webflow/resources/webhooks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific Webhook instance

Required scope: `sites:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.webhooks.get(
    webhook_id="580e64008c9a982ac9b8b754",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — Unique identifier for a Webhook
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/webflow/resources/webhooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a Webhook

Required scope: `sites:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.webhooks.delete(
    webhook_id="580e64008c9a982ac9b8b754",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — Unique identifier for a Webhook
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Forms
<details><summary><code>client.forms.<a href="src/webflow/resources/forms/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List forms for a given site.

Required scope | `forms:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.forms.list(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum number of records to be returned (max limit: 100)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Offset used for pagination if the results have more than limit records
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forms.<a href="src/webflow/resources/forms/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a given form.

Required scope | `forms:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.forms.get(
    form_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**form_id:** `str` — Unique identifier for a Form
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forms.<a href="src/webflow/resources/forms/client.py">list_submissions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List form submissions for a given form

Required scope | `forms:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.forms.list_submissions(
    form_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**form_id:** `str` — Unique identifier for a Form
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Offset used for pagination if the results have more than limit records
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum number of records to be returned (max limit: 100)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forms.<a href="src/webflow/resources/forms/client.py">get_submission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a given form submissio.

Required scope | `forms:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.forms.get_submission(
    form_submission_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**form_submission_id:** `str` — Unique identifier for a Form Submission
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forms.<a href="src/webflow/resources/forms/client.py">update_submission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update hidden fields on a form submission

Required scope | `forms:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.forms.update_submission(
    form_submission_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**form_submission_id:** `str` — Unique identifier for a Form Submission
    
</dd>
</dl>

<dl>
<dd>

**form_submission_data:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — An existing **hidden field** defined on the form schema, and the corresponding value to set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/webflow/resources/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of users for a site

Required scope | `users:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.users.list(
    site_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Offset used for pagination if the results have more than limit records
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Maximum number of records to be returned (max limit: 100)
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[UsersListRequestSort]` 

Sort string to use when ordering users

Example(`CreatedOn`, `Email`, `Status`, `LastLogin`, `UpdatedOn`).

Can be prefixed with a `-` to reverse the sort (ex. `-CreatedOn`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/webflow/resources/users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a User by ID

Required scope | `users:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.users.get(
    site_id="580e63e98c9a982ac9b8b741",
    user_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique identifier for a User
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/webflow/resources/users/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a User by ID

Required scope | `users:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.users.delete(
    site_id="580e63e98c9a982ac9b8b741",
    user_id="580e63e98c9a982ac9b8b741",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — Unique identifier for a Site
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Unique identifier for a User
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/webflow/resources/users/client.py">update</a>(...)</code></summary>
