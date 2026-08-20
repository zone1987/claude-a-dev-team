# Shopware product catalogue — complete concept documentation

Sources: `concepts/commerce/catalog/index.md`, `products.md`, `categories.md`, `sales-channels.md`

---

## Contents

- [Products (concepts/commerce/catalog/products.md)](#products-conceptscommercecatalogproductsmd)
- [Categories (concepts/commerce/catalog/categories.md)](#categories-conceptscommercecatalogcategoriesmd)
- [Sales Channels (concepts/commerce/catalog/sales-channels.md)](#sales-channels-conceptscommercecatalogsales-channelsmd)

## Products (concepts/commerce/catalog/products.md)

Products are sellable entities (physical and digital) in the shop.

### Product structure

- **Product details** — general information (title, ID, manufacturer, price, etc.)
- **Product properties** — property groups and options; in a table on the product detail page, listings, filtering
- **Categories** — hierarchical tree; a product can be in several categories
- **Packaging dimensions** — weight (kg), dimensions (mm); from 6.7.1.0 configurable display units

### Database structure (core ERD relations)

- `Product` 1:M `ProductCategory` M:1 `Category`
- `Product` 1:M `ProductOption` M:1 `PropertyGroupOption` M:1 `PropertyGroup`

### Product variants

- **Self-referencing entity** — parent-child relationship (`parent_id`)
- Variants inherit fields and associations from the parent (DAL inheritance mechanism)
- Categories without their own assignment → the parent product is used

### Properties vs. options — an important difference!

| | Properties | Options |
|---|---|---|
| **Meaning** | Facts about the product | Variant-defining characteristics |
| **Examples** | Product series, washing instructions, country of origin | Size, colour, container volume |
| **Variant-forming?** | No | **Yes** |
| **DB relation** | product → property_group_option | product → property_group_option |

Both use the same database relation, but only **options** constitute variants.

### Configurator

When a variant product is loaded via the Store API, Shopware delivers a **configurator object**
with all property groups and the corresponding variants. Storefront and composable frontends
use this object for the variant selection UI.

---

## Categories (concepts/commerce/catalog/categories.md)

Categories organise products, control storefront navigation and define SEO-relevant URLs.
The entire catalogue lives in **one category tree**; each sales channel chooses entry points.

### Category model

- `parentId`, `path`, `level` — for breadcrumbs, inheritance, efficient traversal
- **Flags**: `active`, `visible`, `hideInNavigation` — control rendering independently
- **Types**:
  - `page` — regular category (listing or landing page)
  - `folder` — structuring element; is not rendered as a page
  - `link` — redirect to an external URL or an internal link

### Entity associations

```
CATEGORY ←→ CATEGORY_TRANSLATION (translations)
CATEGORY → CMS_PAGE (layout reference, inheritable)
CATEGORY → PRODUCT_STREAM (dynamic product assignment)
CATEGORY ←→ PRODUCT (explicit product links via product_category)
SALES_CHANNEL → CATEGORY (navigation/footer/service entry points)
CATEGORY → SEO_URL (generated URLs per category + sales channel)
```

### Sales channel navigation

Every sales channel defines `navigation`, `footer`, `service` entry categories.
The storefront builds menus from the child categories of these entry points.

Store API endpoints:
- `GET /store-api/navigation/{activeId}/{rootId}` — hierarchical menus
- `GET /store-api/category/{navigationId}` — category details incl. CMS layout data

Navigation responses are cached. Cache adjustment via `NavigationRouteCacheKeyEvent` and `NavigationRouteCacheTagsEvent`.

### Product assignments

1. **Explicit assignment** — direct links in `product_category` (and `product_category_tree`)
2. **Dynamic Product Groups** — stored filters as a `product_stream` on the category (runtime evaluation)

Both assignment types are merged for category listings.
Listing criteria: `ProductListingRoute` → extensible via `ProductListingCriteriaEvent`.

### CMS layout integration

- Categories can reference a CMS layout (`cmsPageId`)
- **Inheritance**: if `cmsPageId` is missing → the parent layout is used
- Category-specific slot configuration is merged at runtime
- `folder` categories ignore layouts; `link` categories redirect immediately

### SEO fields

- `metaTitle`, `metaDescription`, `keywords`, `seoUrl`, `noIndex`, `noFollow`
- URL templates configurable under *Settings → SEO*
- Rebuild when categories change or via the SEO indexer

### Extensibility events

- `NavigationLoadedEvent` — navigation tree loaded; enrich/adjust
- `CategoryIndexerEvent` — synchronise denormalised data or external search indexes
- `ProductListingCriteriaEvent` — adjust listing filters, sorting, aggregations
- `SeoUrlUpdateEvent` — react to SEO URL regeneration

---

## Sales Channels (concepts/commerce/catalog/sales-channels.md)

Sales channels define how the catalogue is exposed to a concrete target audience.
One Shopware instance can serve multiple "stores" without duplicating data.

### What a sales channel controls

- **Channel type**: storefront, headless Store API, product feed, custom
- **Audience defaults**: language, currency, country, tax calculation mode, customer group, default payment/shipping
- **Navigation roots**: `navigation`, `footer`, `service` entry categories
- **Presentation**: home CMS page (`homeCmsPageId`) + theme configuration
- **Availability**: allowed domains, payment/shipping methods, languages, currencies, countries, product visibility

### Core model

```
SALES_CHANNEL → SALES_CHANNEL_DOMAIN (URLs + language + currency + snippet set)
SALES_CHANNEL → CATEGORY (navigation/footer/service roots)
SALES_CHANNEL → CMS_PAGE (home page)
SALES_CHANNEL ←→ PRODUCT (via product_visibility)
SALES_CHANNEL ←→ PAYMENT_METHOD / SHIPPING_METHOD / CURRENCY / LANGUAGE (mappings)
```

- `sales_channel`: defaults, navigation roots, home CMS page, access key, maintenance flags, hreflang
- `sales_channel_domain`: URL + language + currency + snippet set — matched via host/path

### Domains and localisation

Example configuration:
```
https://example.com/     → en-GB, GBP
https://de.example.com   → de-DE, EUR
https://example.es/      → es-ES, EUR
```

**Recommendation**: subdomains (e.g. `de.example.com`) instead of sub-paths (e.g. `example.com/de`),
because sub-paths on the same domain lead to cookie conflicts between channels.

`hreflangActive` and `hreflangDefaultDomainId` control hreflang links.

### Product visibility

Products need a `product_visibility` row per sales channel.
The visibility level determines: searchable and/or directly reachable.
`main_category` — SEO-friendly URL per product and sales channel.

### Context creation

Incoming requests → resolve the sales channel via access key or domain matching.
`SalesChannelContextService` builds the `SalesChannelContext` with:
- Defaults (language, currency, payment, shipping)
- Token, customer, rule-based prices, permissions

Relevant Store API routes:
- `GET /store-api/context` — read/switch the current context
- `GET /store-api/navigation/{activeId}/{rootId}`
- `GET /store-api/category/{navigationId}`

### Extension Points

- `SalesChannelContextCreatedEvent` — context built; enrich or persist the session
- `SalesChannelContextSwitchEvent` — on a change of currency, language, payment, shipping, address
- `SalesChannelContextRestoredEvent` — stored context token restored
