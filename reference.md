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

Create a site. This endpoint requires an Enterprise workspace.

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

Delete a site. This endpoint requires an Enterprise workspace.

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

Update a site. This endpoint requires an Enterprise workspace.

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

Get static content from a static page. This includes text nodes, image nodes and component instances.
To retrieve the contents of components in the page use the [get component content](/data/reference/pages-and-components/components/get-content) endpoint.

<Note>If you do not provide a Locale ID in your request, the response will return any content that can be localized from the Primary locale.</Note>

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

Get the property default values of a component definition.

<Note>If you do not provide a Locale ID in your request, the response will return any properties that can be localized from the Primary locale.</Note>

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

Update the property default values of a component definition in a specificed locale.

Before making updates:
1. Use the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint to identify available properties

<Note>The request requires a secondary locale ID. If a locale is missing, the request will not be processed and will result in an error.</Note>

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

List of scripts registered to a Site. 

In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered 
to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
`custom_code` endpoints. 
Additionally, Scripts can be remotely hosted, or registered as inline snippets.

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>    

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

Add a script to a Site's Custom Code registry.

In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered 
to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
`custom_code` endpoints. 
Additionally, Scripts can be remotely hosted, or registered as inline snippets.  

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>    

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

Add a script to a Site's Custom Code registry. Inline scripts can be between 1 and 2000 characters.

In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered 
to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
`custom_code` endpoints. 

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>    

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

List assets for a given site

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

Create a new asset entry. 


This endpoint generates a response with the following information: `uploadUrl` and `uploadDetails`. 
You can use these two properties to [upload the file to Amazon s3 by making a POST](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html)
request to the `uploadUrl` with the `uploadDetails` object as your header information in the request.

 
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

Get an Asset

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

Update an Asset

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
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a User by ID 

  Required scope | `users:write`

<Note class="notice">The <code>email</code> and <code>password</code>
fields cannot be updated using this endpoint</Note>
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
from webflow.resources.users import UsersUpdateRequestData

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.users.update(
    site_id="580e63e98c9a982ac9b8b741",
    user_id="580e63e98c9a982ac9b8b741",
    data=UsersUpdateRequestData(
        name="Some One",
        accept_privacy=False,
        accept_communications=False,
    ),
    access_groups=["webflowers", "platinum", "free-tier"],
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

**data:** `typing.Optional[UsersUpdateRequestData]` 
    
</dd>
</dl>

<dl>
<dd>

**access_groups:** `typing.Optional[typing.Sequence[str]]` — An array of access group slugs. Access groups are assigned to the user as type `admin` and the user remains in the group until removed.

    
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

<details><summary><code>client.users.<a href="src/webflow/resources/users/client.py">invite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create and invite a user with an email address. 

The user will be sent and invite via email, which they will need to accept in order to join paid any paid access group. 

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
client.users.invite(
    site_id="580e63e98c9a982ac9b8b741",
    email="some.one@home.com",
    access_groups=["webflowers"],
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

**email:** `str` — Email address of user to send invite to
    
</dd>
</dl>

<dl>
<dd>

**access_groups:** `typing.Optional[typing.Sequence[str]]` — An array of access group slugs. Access groups are assigned to the user as type `admin` and the user remains in the group until removed.

    
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

## AccessGroups
<details><summary><code>client.access_groups.<a href="src/webflow/resources/access_groups/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of access groups for a site

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
client.access_groups.list(
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

**sort:** `typing.Optional[AccessGroupsListRequestSort]` 

Sort string to use when ordering access groups
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

## Products
<details><summary><code>client.products.<a href="src/webflow/resources/products/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all products for a site. 

Use `limit` and `offset` to page through all products with subsequent requests. All SKUs for each product
will also be fetched and returned. The `limit`, `offset` and `total` values represent Products only and do not include any SKUs.

Required scope | `ecommerce:read`
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
client.products.list(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/webflow/resources/products/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new product and SKU.

When you create a product, you will always create a SKU, since a Product Item must have, at minimum, a single SKU.

To create a Product with multiple SKUs - for example a T-shirt in sizes small, medium and large:
  - Create parameters in `sku-properties`, also known as [product options and variants.](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants).
  - A single `sku-property` would be `color`. Within the `color` property, list the various colors of T-shirts as an array of `enum` values: `royal-blue`, `crimson-red`, and `forrest-green`. 
  - Once, you've created a Product and its `sku-properties` with `enum` values, Webflow will create a **default SKU**, which will automatically be a combination of the first `sku-properties` you've created.
  - In our example, the default SKU will be a Royal Blue T-Shirt, because our first `enum` of our Color `sku-property` is Royal Blue. 
  - After you've created your product, you can create additional SKUs using the [Create SKU endpoint.](/data/reference/ecommerce/products/create-sku)

Upon creation, the default product type will be `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

Required scope | `ecommerce:write`
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
client.products.create(
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

**publish_status:** `typing.Optional[PublishStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**product:** `typing.Optional[Product]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[Sku]` 
    
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

<details><summary><code>client.products.<a href="src/webflow/resources/products/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single product by its ID. All of its SKUs will also be
retrieved.

Required scope | `ecommerce:read`
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
client.products.get(
    site_id="580e63e98c9a982ac9b8b741",
    product_id="580e63fc8c9a982ac9b8b745",
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

**product_id:** `str` — Unique identifier for a Product
    
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

<details><summary><code>client.products.<a href="src/webflow/resources/products/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing Product.

Updating an existing Product will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

Required scope | `ecommerce:write`
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
client.products.update(
    site_id="580e63e98c9a982ac9b8b741",
    product_id="580e63fc8c9a982ac9b8b745",
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

**product_id:** `str` — Unique identifier for a Product
    
</dd>
</dl>

<dl>
<dd>

**publish_status:** `typing.Optional[PublishStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**product:** `typing.Optional[Product]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[Sku]` 
    
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

<details><summary><code>client.products.<a href="src/webflow/resources/products/client.py">create_sku</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create additional SKUs to manage every [option and variant of your Product.](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants)

Creating SKUs through the API will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

Required scope | `ecommerce:write`
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
from webflow import Sku, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.products.create_sku(
    site_id="580e63e98c9a982ac9b8b741",
    product_id="580e63fc8c9a982ac9b8b745",
    skus=[Sku()],
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

**product_id:** `str` — Unique identifier for a Product
    
</dd>
</dl>

<dl>
<dd>

**skus:** `typing.Sequence[Sku]` — An array of the SKU data your are adding
    
</dd>
</dl>

<dl>
<dd>

**publish_status:** `typing.Optional[PublishStatus]` 
    
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

<details><summary><code>client.products.<a href="src/webflow/resources/products/client.py">update_sku</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specified SKU.

Updating an existing SKU will set the Product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

Required scope | `ecommerce:write`
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
from webflow import Sku, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.products.update_sku(
    site_id="580e63e98c9a982ac9b8b741",
    product_id="580e63fc8c9a982ac9b8b745",
    sku_id="5e8518516e147040726cc415",
    sku=Sku(),
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

**product_id:** `str` — Unique identifier for a Product
    
</dd>
</dl>

<dl>
<dd>

**sku_id:** `str` — Unique identifier for a SKU
    
</dd>
</dl>

<dl>
<dd>

**sku:** `Sku` 
    
</dd>
</dl>

<dl>
<dd>

**publish_status:** `typing.Optional[PublishStatus]` 
    
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

## Orders
<details><summary><code>client.orders.<a href="src/webflow/resources/orders/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all orders created for a given site.

Required scope | `ecommerce:read`
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
client.orders.list(
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

**status:** `typing.Optional[OrdersListRequestStatus]` — Filter the orders by status
    
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

<details><summary><code>client.orders.<a href="src/webflow/resources/orders/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single product by its ID. All of its SKUs will also be
retrieved.

Required scope | `ecommerce:read`
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
client.orders.get(
    site_id="580e63e98c9a982ac9b8b741",
    order_id="5e8518516e147040726cc415",
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

**order_id:** `str` — Unique identifier for an Order
    
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

<details><summary><code>client.orders.<a href="src/webflow/resources/orders/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API lets you update the fields, `comment`, `shippingProvider`,
and/or `shippingTracking` for a given order. All three fields can be
updated simultaneously or independently.

Required scope | `ecommerce:write`
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
client.orders.update(
    site_id="580e63e98c9a982ac9b8b741",
    order_id="5e8518516e147040726cc415",
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

**order_id:** `str` — Unique identifier for an Order
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — Arbitrary data for your records
    
</dd>
</dl>

<dl>
<dd>

**shipping_provider:** `typing.Optional[str]` — Company or method used to ship order
    
</dd>
</dl>

<dl>
<dd>

**shipping_tracking:** `typing.Optional[str]` — Tracking number for order shipment
    
</dd>
</dl>

<dl>
<dd>

**shipping_tracking_url:** `typing.Optional[str]` — URL to track order shipment
    
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

<details><summary><code>client.orders.<a href="src/webflow/resources/orders/client.py">update_fulfill</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an order's status to fulfilled

Required scope | `ecommerce:write`
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
client.orders.update_fulfill(
    site_id="580e63e98c9a982ac9b8b741",
    order_id="5e8518516e147040726cc415",
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

**order_id:** `str` — Unique identifier for an Order
    
</dd>
</dl>

<dl>
<dd>

**send_order_fulfilled_email:** `typing.Optional[bool]` — Whether or not the Order Fulfilled email should be sent
    
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

<details><summary><code>client.orders.<a href="src/webflow/resources/orders/client.py">update_unfulfill</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an order's status to unfulfilled

Required scope | `ecommerce:write`
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
client.orders.update_unfulfill(
    site_id="580e63e98c9a982ac9b8b741",
    order_id="5e8518516e147040726cc415",
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

**order_id:** `str` — Unique identifier for an Order
    
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

<details><summary><code>client.orders.<a href="src/webflow/resources/orders/client.py">refund</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API will reverse a Stripe charge and refund an order back to a
customer. It will also set the order's status to `refunded`.

Required scope | `ecommerce:write`
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
client.orders.refund(
    site_id="580e63e98c9a982ac9b8b741",
    order_id="5e8518516e147040726cc415",
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

**order_id:** `str` — Unique identifier for an Order
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[OrdersRefundRequestReason]` — The reason for the refund
    
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

## Inventory
<details><summary><code>client.inventory.<a href="src/webflow/resources/inventory/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the current inventory levels for a particular SKU item.

Required scope | `ecommerce:read`
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
client.inventory.list(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
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

**item_id:** `str` — Unique identifier for an Item
    
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

<details><summary><code>client.inventory.<a href="src/webflow/resources/inventory/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the current inventory levels for a particular SKU item. 

Updates may be given in one or two methods, absolutely or incrementally. 
- Absolute updates are done by setting `quantity` directly. 
- Incremental updates are by specifying the inventory delta in `updateQuantity` which is then added to the `quantity` stored on the server.

Required scope | `ecommerce:write`
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
client.inventory.update(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
    inventory_type="infinite",
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

**item_id:** `str` — Unique identifier for an Item
    
</dd>
</dl>

<dl>
<dd>

**inventory_type:** `InventoryUpdateRequestInventoryType` — infinite or finite
    
</dd>
</dl>

<dl>
<dd>

**update_quantity:** `typing.Optional[float]` — Adds this quantity to currently store quantity. Can be negative.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[float]` — Immediately sets quantity to this value.
    
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

## Ecommerce
<details><summary><code>client.ecommerce.<a href="src/webflow/resources/ecommerce/client.py">get_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve ecommerce settings for a site.

Required scope | `ecommerce:read`
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
client.ecommerce.get_settings(
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

## Collections Fields
<details><summary><code>client.collections.fields.<a href="src/webflow/resources/collections/resources/fields/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a custom field in a collection. 

Slugs must be all lowercase letters without spaces.
If you pass a string with uppercase letters and/or spaces to the "Slug" property, Webflow will
convert the slug to lowercase and replace spaces with "-."

Only some field types can be created through the API. 
This endpoint does not currently support bulk creation. 

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
client.collections.fields.create(
    collection_id="580e63fc8c9a982ac9b8b745",
    is_required=False,
    type="RichText",
    display_name="Post Body",
    help_text="Add the body of your post here",
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

**type:** `FieldCreateType` — Choose these appropriate field type for your collection data
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` — The name of a field
    
</dd>
</dl>

<dl>
<dd>

**is_required:** `typing.Optional[bool]` — define whether a field is required in a collection
    
</dd>
</dl>

<dl>
<dd>

**help_text:** `typing.Optional[str]` — Additional text to help anyone filling out this field
    
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

<details><summary><code>client.collections.fields.<a href="src/webflow/resources/collections/resources/fields/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a custom field in a collection. This endpoint does not currently support bulk deletion.

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
client.collections.fields.delete(
    collection_id="580e63fc8c9a982ac9b8b745",
    field_id="580e63fc8c9a982ac9b8b745",
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

**field_id:** `str` — Unique identifier for a Field in a collection
    
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

<details><summary><code>client.collections.fields.<a href="src/webflow/resources/collections/resources/fields/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a custom field in a collection.

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
client.collections.fields.update(
    collection_id="580e63fc8c9a982ac9b8b745",
    field_id="580e63fc8c9a982ac9b8b745",
    is_required=False,
    display_name="Post Body",
    help_text="Add the body of your post here",
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

**field_id:** `str` — Unique identifier for a Field in a collection
    
</dd>
</dl>

<dl>
<dd>

**is_required:** `typing.Optional[bool]` — Define whether a field is required in a collection
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The name of a field
    
</dd>
</dl>

<dl>
<dd>

**help_text:** `typing.Optional[str]` — Additional text to help anyone filling out this field
    
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

## Collections Items
<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">list_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all Items within a Collection.

Required scope | `CMS:read`
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
client.collections.items.list_items(
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

**cms_locale_id:** `typing.Optional[str]` — Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.
    
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

**name:** `typing.Optional[str]` — The name of the item(s)
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — The slug of the item
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ItemsListItemsRequestSortBy]` — Sort results by the provided value
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ItemsListItemsRequestSortOrder]` — Sorts the results by asc or desc
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">create_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Item(s) in a Collection.


To create items across multiple locales, please use [this endpoint.](/v2.0.0/data/reference/cms/collection-items/staged-items/create-items)

Required scope | `CMS:write`
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
    CollectionItemPostSingle,
    CollectionItemPostSingleFieldData,
    Webflow,
)
from webflow.resources.collections.resources.items import MultipleItems

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.create_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    request=MultipleItems(
        items=[
            CollectionItemPostSingle(
                is_archived=False,
                is_draft=False,
                field_data=CollectionItemPostSingleFieldData(
                    name="Senior Data Analyst",
                    slug="senior-data-analyst",
                ),
            ),
            CollectionItemPostSingle(
                is_archived=False,
                is_draft=False,
                field_data=CollectionItemPostSingleFieldData(
                    name="Product Manager",
                    slug="product-manager",
                ),
            ),
        ],
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

**collection_id:** `str` — Unique identifier for a Collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `ItemsCreateItemRequest` 
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">delete_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Items from a Collection.

**Note:** If the `cmsLocaleId` parameter is undefined or empty and the items are localized, items will be deleted only in the primary locale.

Required scope | `CMS:write`
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
client.collections.items.delete_items(
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

**items:** `typing.Optional[typing.Sequence[ItemsDeleteItemsRequestItemsItem]]` 
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">update_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a single item or multiple items (up to 100) in a Collection.

**Note:** If the `cmsLocaleId` parameter is undefined or empty and the items are localized, items will be updated only in the primary locale.

Required scope | `CMS:write`
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
    CollectionItemWithIdInput,
    CollectionItemWithIdInputFieldData,
    Webflow,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.update_items(
    collection_id="580e63fc8c9a982ac9b8b745",
    items=[
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5ea6",
            cms_locale_id="66f6e966c9e1dc700a857ca5",
            field_data=CollectionItemWithIdInputFieldData(
                name="Ne Paniquez Pas",
                slug="ne-paniquez-pas",
            ),
        ),
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5ea6",
            cms_locale_id="66f6e966c9e1dc700a857ca4",
            field_data=CollectionItemWithIdInputFieldData(
                name="No Entrar en Pánico",
                slug="no-entrar-en-panico",
            ),
        ),
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5eaa",
            cms_locale_id="66f6e966c9e1dc700a857ca5",
            field_data=CollectionItemWithIdInputFieldData(
                name="Au Revoir et Merci pour Tous les Poissons",
                slug="au-revoir-et-merci",
            ),
        ),
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5eaa",
            cms_locale_id="66f6e966c9e1dc700a857ca4",
            field_data=CollectionItemWithIdInputFieldData(
                name="Hasta Luego y Gracias por Todo el Pescado",
                slug="hasta-luego-y-gracias",
            ),
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

**collection_id:** `str` — Unique identifier for a Collection
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.Sequence[CollectionItemWithIdInput]]` 
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">list_items_live</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all live Items within a Collection.

Required scope | `CMS:read`
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
client.collections.items.list_items_live(
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

**cms_locale_id:** `typing.Optional[str]` — Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.
    
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

**name:** `typing.Optional[str]` — The name of the item(s)
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — The slug of the item
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ItemsListItemsLiveRequestSortBy]` — Sort results by the provided value
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ItemsListItemsLiveRequestSortOrder]` — Sorts the results by asc or desc
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">create_item_live</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create live Item(s) in a Collection. The Item(s) will be published to the live site.


To create items across multiple locales, [please use this endpoint.](/v2.0.0/data/reference/cms/collection-items/staged-items/create-items)


Required scope | `CMS:write`
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
from webflow import CollectionItem, CollectionItemFieldData, Webflow
from webflow.resources.collections.resources.items import MultipleLiveItems

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.create_item_live(
    collection_id="580e63fc8c9a982ac9b8b745",
    request=MultipleLiveItems(
        items=[
            CollectionItem(
                is_archived=False,
                is_draft=False,
                field_data=CollectionItemFieldData(
                    name="Senior Data Analyst",
                    slug="senior-data-analyst",
                ),
            ),
            CollectionItem(
                is_archived=False,
                is_draft=False,
                field_data=CollectionItemFieldData(
                    name="Product Manager",
                    slug="product-manager",
                ),
            ),
        ],
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

**collection_id:** `str` — Unique identifier for a Collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `ItemsCreateItemLiveRequest` 
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">delete_items_live</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an item or multiple items (up to 100 items) from the live site. Deleting published items will unpublish the items from the live site and set them to draft. 

**Note:** If the `cmsLocaleId` parameter is undefined or empty and the items are localized, items will be unpublished only in the primary locale.

Required scope | `CMS:write`
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
client.collections.items.delete_items_live(
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

**items:** `typing.Optional[typing.Sequence[ItemsDeleteItemsLiveRequestItemsItem]]` 
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">update_items_live</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a single live item or multiple live items (up to 100) in a Collection

**Note:** If the `cmsLocaleId` parameter is undefined or empty and the items are localized, items will be updated only in the primary locale. 

Required scope | `CMS:write`
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
    CollectionItemWithIdInput,
    CollectionItemWithIdInputFieldData,
    Webflow,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.update_items_live(
    collection_id="580e63fc8c9a982ac9b8b745",
    items=[
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5ea6",
            cms_locale_id="66f6e966c9e1dc700a857ca5",
            field_data=CollectionItemWithIdInputFieldData(
                name="Ne Paniquez Pas",
                slug="ne-paniquez-pas",
            ),
        ),
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5ea6",
            cms_locale_id="66f6e966c9e1dc700a857ca4",
            field_data=CollectionItemWithIdInputFieldData(
                name="No Entrar en Pánico",
                slug="no-entrar-en-panico",
            ),
        ),
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5eaa",
            cms_locale_id="66f6e966c9e1dc700a857ca5",
            field_data=CollectionItemWithIdInputFieldData(
                name="Au Revoir et Merci pour Tous les Poissons",
                slug="au-revoir-et-merci",
            ),
        ),
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5eaa",
            cms_locale_id="66f6e966c9e1dc700a857ca4",
            field_data=CollectionItemWithIdInputFieldData(
                name="Hasta Luego y Gracias por Todo el Pescado",
                slug="hasta-luego-y-gracias",
            ),
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

**collection_id:** `str` — Unique identifier for a Collection
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.Sequence[CollectionItemWithIdInput]]` 
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">create_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an item or multiple items in a CMS Collection across multiple corresponding locales.

**Notes:**
  - This endpoint can create up to 100 items in a request.
  - If the `cmsLocaleIds` parameter is undefined or empty and localization is enabled, items will only be created in the primary locale.

Required scope | `CMS:write`
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
from webflow.resources.collections.resources.items import SingleCmsItem

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.create_items(
    collection_id="580e63fc8c9a982ac9b8b745",
    cms_locale_ids=[
        "66f6e966c9e1dc700a857ca3",
        "66f6e966c9e1dc700a857ca4",
        "66f6e966c9e1dc700a857ca5",
    ],
    is_archived=False,
    is_draft=False,
    field_data=SingleCmsItem(
        name="Don’t Panic",
        slug="dont-panic",
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

**collection_id:** `str` — Unique identifier for a Collection
    
</dd>
</dl>

<dl>
<dd>

**field_data:** `CreateBulkCollectionItemRequestBodyFieldData` 
    
</dd>
</dl>

<dl>
<dd>

**cms_locale_ids:** `typing.Optional[typing.Sequence[str]]` — Array of identifiers for the locales where the item will be created
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` — Indicates whether the item is archived.
    
</dd>
</dl>

<dl>
<dd>

**is_draft:** `typing.Optional[bool]` — Indicates whether the item is in draft state.
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">get_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a selected Collection Item.

Required scope | `CMS:read`
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
client.collections.items.get_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
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

**item_id:** `str` — Unique identifier for an Item
    
</dd>
</dl>

<dl>
<dd>

**cms_locale_id:** `typing.Optional[str]` — Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">delete_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an Item from a Collection. This endpoint does not currently support bulk deletion.

Required scope | `CMS:write`
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
client.collections.items.delete_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
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

**item_id:** `str` — Unique identifier for an Item
    
</dd>
</dl>

<dl>
<dd>

**cms_locale_id:** `typing.Optional[str]` — Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">update_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a selected Item in a Collection.

Required scope | `CMS:write`
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
from webflow import CollectionItemPatchSingleFieldData, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.update_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
    is_archived=False,
    is_draft=False,
    field_data=CollectionItemPatchSingleFieldData(
        name="Pan Galactic Gargle Blaster Recipe",
        slug="pan-galactic-gargle-blaster",
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

**collection_id:** `str` — Unique identifier for a Collection
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — Unique identifier for an Item
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier for the Item
    
</dd>
</dl>

<dl>
<dd>

**cms_locale_id:** `typing.Optional[str]` — Identifier for the locale of the CMS item
    
</dd>
</dl>

<dl>
<dd>

**last_published:** `typing.Optional[str]` — The date the item was last published
    
</dd>
</dl>

<dl>
<dd>

**last_updated:** `typing.Optional[str]` — The date the item was last updated
    
</dd>
</dl>

<dl>
<dd>

**created_on:** `typing.Optional[str]` — The date the item was created
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` — Boolean determining if the Item is set to archived
    
</dd>
</dl>

<dl>
<dd>

**is_draft:** `typing.Optional[bool]` — Boolean determining if the Item is set to draft
    
</dd>
</dl>

<dl>
<dd>

**field_data:** `typing.Optional[CollectionItemPatchSingleFieldData]` 
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">get_item_live</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a selected Collection live Item.

Required scope | `CMS:read`
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
client.collections.items.get_item_live(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
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

**item_id:** `str` — Unique identifier for an Item
    
</dd>
</dl>

<dl>
<dd>

**cms_locale_id:** `typing.Optional[str]` — Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">delete_item_live</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a live item from the site. Removing a published item will unpublish the item from the live site and set it to draft. 

This endpoint does not currently support bulk deletion.

Required scope | `CMS:write`
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
client.collections.items.delete_item_live(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
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

**item_id:** `str` — Unique identifier for an Item
    
</dd>
</dl>

<dl>
<dd>

**cms_locale_id:** `typing.Optional[str]` — Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">update_item_live</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a selected live Item in a Collection. The updates for this Item will be published to the live site.

Required scope | `CMS:write`
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
from webflow import CollectionItemPatchSingleFieldData, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.update_item_live(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
    is_archived=False,
    is_draft=False,
    field_data=CollectionItemPatchSingleFieldData(
        name="Pan Galactic Gargle Blaster Recipe",
        slug="pan-galactic-gargle-blaster",
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

**collection_id:** `str` — Unique identifier for a Collection
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — Unique identifier for an Item
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier for the Item
    
</dd>
</dl>

<dl>
<dd>

**cms_locale_id:** `typing.Optional[str]` — Identifier for the locale of the CMS item
    
</dd>
</dl>

<dl>
<dd>

**last_published:** `typing.Optional[str]` — The date the item was last published
    
</dd>
</dl>

<dl>
<dd>

**last_updated:** `typing.Optional[str]` — The date the item was last updated
    
</dd>
</dl>

<dl>
<dd>

**created_on:** `typing.Optional[str]` — The date the item was created
    
</dd>
</dl>

<dl>
<dd>

**is_archived:** `typing.Optional[bool]` — Boolean determining if the Item is set to archived
    
</dd>
</dl>

<dl>
<dd>

**is_draft:** `typing.Optional[bool]` — Boolean determining if the Item is set to draft
    
</dd>
</dl>

<dl>
<dd>

**field_data:** `typing.Optional[CollectionItemPatchSingleFieldData]` 
    
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

<details><summary><code>client.collections.items.<a href="src/webflow/resources/collections/resources/items/client.py">publish_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish an item or multiple items.

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
client.collections.items.publish_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_ids=["itemIds"],
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

**item_ids:** `typing.Sequence[str]` 
    
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

## Pages Scripts
<details><summary><code>client.pages.scripts.<a href="src/webflow/resources/pages/resources/scripts/client.py">get_custom_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all registered scripts that have been applied to a specific Page. 

In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered 
to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
`custom_code` endpoints. 

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

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
client.pages.scripts.get_custom_code(
    page_id="63c720f9347c2139b248e552",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.scripts.<a href="src/webflow/resources/pages/resources/scripts/client.py">upsert_custom_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a registered script to a Page. 

In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered 
to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
`custom_code` endpoints.

A site can have a maximum of 800 registered scripts.

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

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
from webflow import ScriptApply, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.pages.scripts.upsert_custom_code(
    page_id="63c720f9347c2139b248e552",
    scripts=[
        ScriptApply(
            id="cms_slider",
            location="header",
            version="1.0.0",
            attributes={"my-attribute": "some-value"},
        ),
        ScriptApply(
            id="alert",
            location="header",
            version="0.0.1",
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

**scripts:** `typing.Optional[typing.Sequence[ScriptApply]]` — A list of scripts applied to a Site or a Page
    
</dd>
</dl>

<dl>
<dd>

**last_updated:** `typing.Optional[str]` — Date when the Site's scripts were last updated
    
</dd>
</dl>

<dl>
<dd>

**created_on:** `typing.Optional[str]` — Date when the Site's scripts were created
    
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

<details><summary><code>client.pages.scripts.<a href="src/webflow/resources/pages/resources/scripts/client.py">delete_custom_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the custom code block that an app has created for a page

In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered 
to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
`custom_code` endpoints. 

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

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
client.pages.scripts.delete_custom_code(
    page_id="63c720f9347c2139b248e552",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sites Redirects
<details><summary><code>client.sites.redirects.<a href="src/webflow/resources/sites/resources/redirects/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a list of all URL redirect rules configured for a specific site.

Use this endpoint to review, audit, or manage the redirection rules that control how traffic is rerouted on your site.


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
client.sites.redirects.list(
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

<details><summary><code>client.sites.redirects.<a href="src/webflow/resources/sites/resources/redirects/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new URL redirection rule to a site.

This endpoint allows you to define a source path (`fromUrl`) and its corresponding destination path (`toUrl`), which will dictate how traffic is rerouted on your site. This is useful for managing site changes, restructuring URLs, or handling outdated links.

Required scope: `sites:write`
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
client.sites.redirects.create(
    site_id="580e63e98c9a982ac9b8b741",
    id="42e1a2b7aa1a13f768a0042a",
    from_url="/mostly-harmless",
    to_url="/earth",
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

**id:** `typing.Optional[str]` — The ID of the specific redirect rule
    
</dd>
</dl>

<dl>
<dd>

**from_url:** `typing.Optional[str]` — The source URL path that will be redirected.
    
</dd>
</dl>

<dl>
<dd>

**to_url:** `typing.Optional[str]` — The target URL path where the user or client will be redirected.
    
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

<details><summary><code>client.sites.redirects.<a href="src/webflow/resources/sites/resources/redirects/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a URL redirection rule from a site.
This is useful for cleaning up outdated or unnecessary redirects, ensuring that your site's routing behavior remains efficient and up-to-date.
Required scope: `sites:write`
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
client.sites.redirects.delete(
    site_id="580e63e98c9a982ac9b8b741",
    redirect_id="66c4cb9a20cac35ed19500e6",
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

**redirect_id:** `str` — Unique identifier site rediect
    
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

<details><summary><code>client.sites.redirects.<a href="src/webflow/resources/sites/resources/redirects/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a URL redirection rule from a site.
Required scope: `sites:write`
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
client.sites.redirects.update(
    site_id="580e63e98c9a982ac9b8b741",
    redirect_id="66c4cb9a20cac35ed19500e6",
    id="42e1a2b7aa1a13f768a0042a",
    from_url="/mostly-harmless",
    to_url="/earth",
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

**redirect_id:** `str` — Unique identifier site rediect
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The ID of the specific redirect rule
    
</dd>
</dl>

<dl>
<dd>

**from_url:** `typing.Optional[str]` — The source URL path that will be redirected.
    
</dd>
</dl>

<dl>
<dd>

**to_url:** `typing.Optional[str]` — The target URL path where the user or client will be redirected.
    
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

## Sites Plans
<details><summary><code>client.sites.plans.<a href="src/webflow/resources/sites/resources/plans/client.py">get_site_plan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get site plan details for the specified Site.

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
client.sites.plans.get_site_plan(
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

## Sites ActivityLogs
<details><summary><code>client.sites.activity_logs.<a href="src/webflow/resources/sites/resources/activity_logs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve Activity Logs for a specific Site. Requires Site to be on an Enterprise plan. </br></br>  Required scope | `site_activity:read`
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
client.sites.activity_logs.list(
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

## Sites Scripts
<details><summary><code>client.sites.scripts.<a href="src/webflow/resources/sites/resources/scripts/client.py">get_custom_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all registered scripts that have been applied to a specific Site. 

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>    

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
client.sites.scripts.get_custom_code(
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

<details><summary><code>client.sites.scripts.<a href="src/webflow/resources/sites/resources/scripts/client.py">upsert_custom_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a registered script to a Site. 

In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered 
to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
`custom_code` endpoints. 

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>    

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
from webflow import ScriptApply, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.sites.scripts.upsert_custom_code(
    site_id="580e63e98c9a982ac9b8b741",
    scripts=[
        ScriptApply(
            id="cms_slider",
            location="header",
            version="1.0.0",
            attributes={"my-attribute": "some-value"},
        ),
        ScriptApply(
            id="alert",
            location="header",
            version="0.0.1",
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

**scripts:** `typing.Optional[typing.Sequence[ScriptApply]]` — A list of scripts applied to a Site or a Page
    
</dd>
</dl>

<dl>
<dd>

**last_updated:** `typing.Optional[str]` — Date when the Site's scripts were last updated
    
</dd>
</dl>

<dl>
<dd>

**created_on:** `typing.Optional[str]` — Date when the Site's scripts were created
    
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

<details><summary><code>client.sites.scripts.<a href="src/webflow/resources/sites/resources/scripts/client.py">delete_custom_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the custom code block that an app created for a Site

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>    

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
client.sites.scripts.delete_custom_code(
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

<details><summary><code>client.sites.scripts.<a href="src/webflow/resources/sites/resources/scripts/client.py">list_custom_code_blocks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all instances of Custom Code applied to a Site or Pages. 

<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>    

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
client.sites.scripts.list_custom_code_blocks(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

