<!-- distilled from shopware/storefront v6.7.13.1 — layout/structured-data/, plugin/google-analytics/ -->

# Shopware Storefront — structured data and tracking

Two things that read the same page data for different consumers: JSON-LD for search engines, and
analytics events for a tag manager. Both are extension points that need no controller change.

## Contents

- [JSON-LD is built in Twig](#json-ld-is-built-in-twig)
- [The six schemas](#the-six-schemas)
- [Where each one is included](#where-each-one-is-included)
- [How the data is assembled](#how-the-data-is-assembled)
- [Extending or replacing a schema](#extending-or-replacing-a-schema)
- [Testing structured data](#testing-structured-data)
- [Reading page data from JavaScript](#reading-page-data-from-javascript)
- [The analytics event system](#the-analytics-event-system)
- [Building a tag manager plugin](#building-a-tag-manager-plugin)

## JSON-LD is built in Twig

There is **no PHP structured-data service**. Every schema is assembled in a Twig template under
`storefront/layout/structured-data/`, serialised with `json_encode(jsonLdFlags)` and printed inside
a `<script type="application/ld+json">` tag.

That single fact decides how you extend it: **override the block, not a PHP class.** There is no
event to subscribe to and no service to decorate.

`jsonLdFlags` is one of the eight global Twig variables and carries
`JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP`.
`JSON_HEX_TAG` and `JSON_HEX_AMP` are the security-relevant ones: they stop a product name
containing `</script>` from breaking out of the tag. Always reuse the flags rather than calling
`json_encode` bare.

## The six schemas

| Template | schema.org type | Data source |
|---|---|---|
| `json-ld-website.html.twig` | `WebSite` | sales channel domain, shop name, search action URL |
| `json-ld-organization.html.twig` | `Organization` | `config('core.basicInformation')`, `theme_config('sw-logo-desktop')` |
| `json-ld-webpage.html.twig` | `WebPage` | `page.metaInformation` |
| `json-ld-breadcrumb.html.twig` | `BreadcrumbList` | the `breadcrumb` variable passed in via `with` |
| `json-ld-product.html.twig` | `Product` (plus `Offer`, `AggregateRating`, `VideoObject`) | `page.product` |
| `json-ld-item-list.html.twig` | `ItemList` | the `searchResult` variable passed in via `with` |

Each has two blocks: an outer one that builds the data (`layout_structured_data_<name>`) and an
inner one that prints the script tag (`..._script`). The product template names its blocks
`page_product_detail_json_ld` and `page_product_detail_json_ld_script`.

## Where each one is included

All inclusion happens from a `meta.html.twig`, inside the document head.

| Page | Template | Includes |
|---|---|---|
| every page | `layout/meta.html.twig` | `website`, `organization`, `webpage`, `breadcrumb` |
| product detail | `page/product-detail/meta.html.twig` | `webpage`, `breadcrumb`, `product` |
| category / CMS | `page/content/meta.html.twig` | `webpage`, `breadcrumb`, `item-list` |
| search | `page/search/meta.html.twig` | `webpage`, `breadcrumb`, `item-list` |

The page-level `meta.html.twig` files extend `layout/meta.html.twig`, so a page that needs
different structured data overrides the block rather than adding a second include.

`breadcrumb` and `searchResult` are **passed in with `with {...}`** — they are not global. A
partial that expects them must be included the same way, or the values will be missing.

## How the data is assembled

The pattern throughout is build-a-hash, then merge conditionally:

```twig
{% set orgData = { '@context': 'https://schema.org', '@type': 'Organization', name: shopName } %}
{% if logoUrl %}
    {% set orgData = orgData|merge({ logo: { '@type': 'ImageObject', url: logoUrl } }) %}
{% endif %}
```

Two details worth knowing before extending:

- **Availability is derived, not stored.** `json-ld-product` maps stock, `minPurchase`,
  `isCloseout`, `releaseDate`, `deliveryTime` and `restockTime` onto the schema.org availability
  values, deliberately mirroring the logic in `delivery-information.html.twig`. Change one and the
  two disagree.
- **Media is split by type.** Images become `image` URLs; entries whose `mediaType.name` is
  `VIDEO` become `VideoObject` entries, and a video without a resolvable `thumbnailUrl` is skipped
  entirely, because Google rejects it.
- **Paginated listings describe only their own page.** `ItemList` lists the products of the current
  page number, which is the documented approach for paginated content.

## Extending or replacing a schema

Mirror the path in your theme or plugin and override the block:

```twig
{% sw_extends '@Storefront/storefront/layout/structured-data/json-ld-product.html.twig' %}

{% block page_product_detail_json_ld_script %}
    {% set productData = productData|merge({
        sku: page.product.productNumber,
        gtin13: page.product.ean
    }) %}
    {{ parent() }}
{% endblock %}
```

**Override the `_script` block, not the outer one**, when you want to add fields: the outer block
is where the data is built, so overriding it means rebuilding everything. The inner block runs after
the hash exists and before it is printed, which is exactly the seam you want.

To remove a schema entirely, override its block with an empty body in the including template.

## Testing structured data

- **In the page** — `curl -s <url> | grep -A40 'application/ld+json'`, or read the script tags in
  the browser's element inspector.
- **Validate the syntax** — [validator.schema.org](https://validator.schema.org) accepts a pasted
  snippet or a URL.
- **Validate for Google** — the [Rich Results Test](https://search.google.com/test/rich-results)
  reports which rich result types the markup qualifies for, which is stricter than schema validity.
- **In a test** — a Playwright test can assert on the parsed JSON:
  `JSON.parse(await page.locator('script[type="application/ld+json"]').first().textContent())`.
- **After a change**, check the product page in all three of its states — in stock, out of stock,
  pre-order — since availability is derived from several fields at once.

## Reading page data from JavaScript

Tracking code needs the same data the JSON-LD carries, but on the client. Three sources exist:

- **`data-product-information`** on every product card
  (`component/product/card/box-standard.html.twig`) carries
  `{id, name, brand, price, sku}` as JSON. This is the intended hook for listing-level tracking.
- **The JSON-LD script tags themselves** can be parsed from the DOM — the most complete product data
  available client-side, and it stays correct when the markup changes.
- **The storefront events** below, which carry their payload in `event.detail`.

## The analytics event system

`src/plugin/google-analytics/` is the reference implementation of e-commerce tracking, and the
structure is reusable: a plugin that owns the consent handling, plus one small class per event.

```
GoogleAnalyticsPlugin              registered without a selector — it is global
  ├─ checks cookie consent         'google-analytics-enabled' via CookieStorageHelper
  ├─ listens for COOKIE_CONFIGURATION_UPDATE to enable or disable at runtime
  └─ instantiates its events, each an AnalyticsEvent subclass
       supports(controllerName, actionName, activeRoute)   should this event run on this page?
       getPluginName()                                     which storefront plugin it listens to
       getEvents()                                         { storefrontEventName: handler }
       execute(event)                                      read event.detail, push the payload
```

`EventAwareAnalyticsEvent` subscribes to another plugin's emitter events; a plain `AnalyticsEvent`
fires on page load. The 18 shipped events cover the full funnel: `view-item`, `view-item-list`,
`view-search-results`, `search-ajax`, `add-to-cart`, `add-to-cart-by-number`,
`remove-from-cart`, `view-cart`, `begin-checkout`, `begin-checkout-on-cart`,
`checkout-progress`, `add-shipping-info`, `add-payment-info`, `purchase`, `login`, `sign-up`,
`add-to-wishlist`, `remove-from-wishlist`.

## Building a tag manager plugin

Follow the same shape rather than inventing one:

1. **One global plugin**, registered without a selector, that injects the container script.
2. **Gate it on consent.** Register your cookie in the cookie configuration so it appears in the
   consent dialogue, read it with `CookieStorageHelper`, and subscribe to
   `COOKIE_CONFIGURATION_UPDATE` so a consent change takes effect without a reload. Loading a tag
   manager before consent is the usual compliance failure.
3. **Subscribe to the existing storefront events** rather than adding attributes to templates —
   `JS-SELECTOR-MAP.md` lists all 111 with their publishing file. The cart, wishlist and form
   plugins already publish what a funnel needs, and events survive template overrides that
   attributes do not.
4. **Take product data from `data-product-information` or the JSON-LD**, so listing and detail
   tracking report the same numbers as the page.
5. **Push to `window.dataLayer`** in the handler. Keep the payload construction in the event class,
   exactly as the analytics events do, so each tracked action stays one readable file.
6. **Re-initialise after AJAX.** Cart and listing updates replace markup and `PluginManager` runs
   again; a global plugin must not assume it saw every element on first load.
