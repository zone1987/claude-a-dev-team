# Shopware CMS / Shopping Experiences — complete concept documentation

Sources: `concepts/commerce/content/index.md`, `shopping-experiences-cms.md`, `cookie-consent-management.md`

---

## Contents

- [Content overview (index.md)](#content-overview-indexmd)
- [Shopping Experiences / CMS (shopping-experiences-cms.md)](#shopping-experiences-cms-shopping-experiences-cmsmd)
- [Cookie Consent Management (cookie-consent-management.md)](#cookie-consent-management-cookie-consent-managementmd)

## Content overview (index.md)

Shopware 6 has an integrated CMS system called **Shopping Experiences** based on layouts.
Tool: the **Page Builder** in the admin panel.

In addition: **cookie consent management** for GDPR compliance.

---

## Shopping Experiences / CMS (shopping-experiences-cms.md)

### Structure

Hierarchical structure: **Page → Section(s) → Block(s) → Slot(s) → Element**

#### Page

Wrapper with a `type`:
- `page` — standard CMS page (shop pages, category pages)
- `landingpage` — landing page layouts
- `product_list` — product listing/category layouts
- `product_detail` — product detail page layouts

#### Section

Horizontal container. `type`:
- `sidebar` — two-column layout (sidebar + content)
- `fullwidth` — single full-width column

#### Block

A unit that usually spans an entire row. Block categories:
`text`, `image`, `video`, `text-image`, `commerce`, `sidebar`, `form`, `html`, `favorite`, `app`

Each block contains zero or more slots. A slot has a name and is a container for exactly one element.

Example block JSON:
```json
{
    "type": "text-hero",
    "slots": [{
        "type": "text",
        "slot": "content",
        "config": {
            "content": { "source": "static", "value": "Hello World" }
        }
    }]
}
```

#### Slot

Named container for exactly one element.
- `source: "static"` — static value
- `source: "mapped"` — resolved dynamically at runtime (e.g. `category.description`)

#### Elements (primitives)

Built-in element types:
`text`, `html`, `form`, `image`, `image-slider`, `video`, `youtube-video`, `vimeo-video`,
`product-listing`, `product-box`, `product-slider`, `product-name`, `manufacturer-logo`,
`buy-box`, `cross-selling`, `product-description-reviews`, `category-navigation`

Register your own element types via `CmsElementResolverInterface`.

### Hydration of dynamic content

While the CMS structure is static, the content can be dynamic and context-aware.
Example: the same layout for several category pages — product listing, header image, description
are loaded depending on the category configuration.

**Resolving process** (orchestrator: `SalesChannelCmsPageLoader::load()`):

1. Dispatch `CmsPageLoaderCriteriaEvent` (criteria adjustable)
2. Load the CMS layout (sections, blocks, slots, background media)
3. Sort by `position`
4. Build the resolver context (request + SalesChannelContext + optional entity)
5. Override the entity's slot configuration (e.g. category-specific adjustments)
6. Resolve slot data via `CmsSlotsDataResolver`:
   - **Collect**: each element resolver's `collect()` creates a `CriteriaCollection`
   - **Optimize**: merge simple ID criteria, separate complex searches (min. DB queries)
   - **Fetch**: execute the optimised criteria against the DAL
   - **Enrich**: `enrich()` fills the slot with the fetched data
7. Dispatch `CmsPageLoadedEvent` (post-processing possible)
8. Collect cache tags (product IDs etc. for HTTP cache invalidation)
9. Return the complete page data

### Extensibility

**Custom element resolver** via `CmsElementResolverInterface`:
- `getType()` — element type identifier
- `collect()` — build the CriteriaCollection
- `enrich()` — fill the slot with data

**Event-based extensions** (from 6.6.7):
- `CmsSlotsDataResolveExtension`
- `CmsSlotsDataCollectExtension`
- `CmsSlotsDataEnrichExtension`

### Headless capability / separation of content and presentation

The CMS is **channel-independent**:
- Browser: Shopware storefront → HTML
- SPA / headless frontend: API → interpret JSON
- Native app: show only the relevant blocks
- Smart speaker: read out only `voice`-type elements

**Important for headless**: the admin preview only shows how the storefront renders it — with strongly
diverging headless frontends the preview is only of limited representativeness.

---

## Cookie Consent Management (cookie-consent-management.md)

### Overview

A GDPR-supporting cookie consent system. Available from 6.7.3.0 for the Store API endpoint and the
hash mechanism.

### System components

1. **Cookie provider service** — collects all cookie definitions (core, plugins, apps)
2. **Store API endpoint** (`GET /store-api/cookie/groups`) — exposes the cookie configuration + hash
3. **Storefront component** — manages the consent UI and user preferences
4. **Configuration hash** — tracks changes for re-consent

### Cookie flow

```
User → Storefront → StoreAPI → CookieProvider
                             ↓ Cookie groups + hash
Storefront compares the stored hash (per language)
→ Hash changed: show the consent banner
→ Hash identical: apply the stored preferences
User makes a choice → store the preferences + hash (with the language ID)
```

### Cookie categories (GDPR-compliant)

| Category | Snippet key | Examples |
|---|---|---|
| Technically required | `cookie.groupRequired` | Session, cart, security token |
| Comfort features | `cookie.groupComfortFeatures` | YouTube, social media, chat |
| Marketing | `cookie.groupMarketing` | Facebook Pixel, Google Ads, affiliate |
| Statistics/tracking | `cookie.groupStatistical` | Google Analytics, Hotjar, A/B testing |

Technically required cookies **cannot** be deactivated.

### Hash mechanism

- The hash is calculated from all cookie configurations (name, description, expiry)
- Stored as the cookie `cookie-config-hash`: `{"<language-id>": "<hash>"}` 
- On a visit: compare the current hash against the stored hash for the current language
- Difference → remove all non-essential cookies → re-consent

**The hash changes on**: new cookies (plugins/apps), modified/removed cookies, changed cookie groups

**Why a language ID in the hash?** — For multi-language shops on the same domain (different domains
are already separated by the browser's cookie scoping).

### Cookie lifetime tracking

| Cookie | Purpose | Lifetime |
|---|---|---|
| `cookie-preference` | Stored consent decisions | 30 days |
| `cookie-config-hash` | Configuration change tracking per language | 30 days |

**Protected cookies** (never removed): `session-*`, `timezone`

### Store API endpoint (from 6.7.3.0)

`GET /store-api/cookie/groups`

Delivers: cookie groups, configuration, hash, language ID.
Enables headless implementations, custom frontends and third-party integrations.

### Extensibility

- **Plugins**: event listener for adding your own cookies
- **Apps**: define cookies in `manifest.xml`
- **JavaScript**: events for consent changes (`reacting-to-cookie-consent-changes`)

### GDPR features

- Opt-in by default (no pre-filled checkboxes)
- Granular control (accept/reject individual categories)
- Re-consent on configuration changes
- Clear cookie descriptions
- Easy revocation (preferences changeable at any time)
- Configuration change tracking via a hash
