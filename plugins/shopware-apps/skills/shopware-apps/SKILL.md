---
name: shopware-apps
description: Comprehensive guide for developing Shopware 6 Apps, covering manifest configuration, webhooks, authentication, app scripts, storefront/admin customization, payments, custom data, flow actions, gateways, and in-app purchases.
license: MIT
metadata:
  author: A Dev Team
  version: "1.0.0"
  organization: A Dev Team
  date: March 2026
  abstract: Complete reference for Shopware 6 App development including manifest XML structure, app server setup (JS/PHP SDKs), webhooks, authentication, app scripts (Twig), storefront templates/themes, Admin SDK integration, custom entities/fields, payment handlers, shipping methods, tax providers, flow actions/triggers, rule conditions, checkout/context gateways, and in-app purchases.
---

# Shopware App Development

## When to Apply

- Creating a new Shopware 6 App (manifest.xml, app server, scripts)
- Configuring manifest.xml (meta, setup, permissions, webhooks, admin, cookies, etc.)
- Setting up app server authentication (registration, HMAC, JWT)
- Building an app server with JS SDK (Hono, Node.js) or PHP SDK (Symfony)
- Writing app scripts (cart manipulation, data loading, custom endpoints, rule conditions)
- Adding storefront templates, themes, or cookie consent from an app
- Integrating with the Administration via Meteor Admin SDK (modules, action buttons, CMS elements)
- Defining custom fields, custom entities, or custom CMS blocks
- Implementing payment handlers (sync, async, prepared, refund, recurring)
- Adding shipping method or tax provider integrations
- Creating flow actions or flow triggers
- Adding custom rule conditions via app scripts
- Working with checkout gateways, context gateways, or in-app purchase gateways
- Implementing in-app purchases for Shopware apps

## Rule Categories by Priority

| Priority | Category | Prefix | Description |
|----------|----------|--------|-------------|
| CRITICAL | Manifest XML | `manifest-` | Manifest structure, meta section, permissions |
| HIGH | Configuration | `config-` | App configuration (config.xml) field types |
| HIGH | Webhooks | `webhook-` | Webhook events, HMAC verification |
| HIGH | Authentication | `auth-` | App registration, request signing, JWT tokens |
| HIGH | App Lifecycle | `lifecycle-` | Install, update, activate, deactivate, delete events |
| HIGH | JavaScript SDK | `sdk-js-` | JS SDK setup, HTTP client, Hono integration |
| HIGH | PHP SDK | `sdk-php-` | PHP SDK setup, HTTP client, Symfony integration |
| HIGH | App Server Setup | `sdk-php-public-htaccess` | `.htaccess` im `public/`-Verzeichnis (Apache-Pflicht) |
| MEDIUM | App Scripts | `scripts-` | Cart manipulation, data loading, custom endpoints |
| MEDIUM | Storefront | `storefront-` | Templates, themes, cookies |
| MEDIUM | Administration | `admin-` | Admin SDK, action buttons, modules, CMS elements, snippets |
| MEDIUM | Custom Data | `custom-` | Custom fields, custom entities, custom CMS blocks |
| MEDIUM | Payment | `payment-` | Sync/async/prepared payment, refund, recurring |
| LOW-MEDIUM | Shipping | `shipping-` | Shipping method integration |
| LOW-MEDIUM | Tax | `tax-` | Tax provider integration |
| LOW-MEDIUM | Flow Builder | `flow-` | Flow actions and triggers |
| LOW | Rule Builder | `rule-` | Custom rule conditions |
| LOW | Gateways | `gateway-` | Checkout, context, and IAP gateways |
| LOW | In-App Purchases | `iap-` | In-app purchase flow |

## How to Use

Read relevant reference files from the `references/` directory based on the task at hand. Files are prefixed by category for easy discovery.

- **`references/`** — Best practices, patterns, and rules organized by topic
- **`examples/`** — Complete, working code examples (XML, Twig, TS, PHP, JS)
- **`schemas/`** — XSD schema files for XML validation (manifest, config, entities, flow, CMS)

Start with `references/_sections.md` for an overview of all available references.

## Searching the Shopware Documentation

When you need up-to-date information from the Shopware developer docs, use the Algolia search API:

**Step 1 — Search:** POST to the Algolia endpoint, replacing `"query"` value with your search term:

```bash
curl -s -X POST \
  "https://j1y01x9hgm-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(5.19.0)%3B%20Lite%20(5.19.0)%3B%20Browser%3B%20docsearch%20(3.9.0)%3B%20docsearch-react%20(3.9.0)%3B%20docsearch.js%20(3.9.0)&x-algolia-api-key=711e1cadf66a3957aaf183a58aad12a7&x-algolia-application-id=J1Y01X9HGM" \
  -H "Content-Type: application/json" \
  -d '{
    "requests": [{
      "query": "YOUR_SEARCH_TERM",
      "indexName": "beta-developer-shopware",
      "attributesToRetrieve": ["hierarchy.lvl0","hierarchy.lvl1","hierarchy.lvl2","hierarchy.lvl3","hierarchy.lvl4","hierarchy.lvl5","hierarchy.lvl6","content","type","url"],
      "attributesToSnippet": ["hierarchy.lvl1:10","hierarchy.lvl2:10","hierarchy.lvl3:10","hierarchy.lvl4:10","hierarchy.lvl5:10","hierarchy.lvl6:10","content:10"],
      "snippetEllipsisText": "…",
      "highlightPreTag": "<mark>",
      "highlightPostTag": "</mark>",
      "hitsPerPage": 30,
      "clickAnalytics": false,
      "filters": "version:main",
      "length": 30,
      "offset": 0
    }]
  }'
```

**Step 2 — Parse results:** The response contains `results[0].hits[]` sorted by relevance (best match first). Each hit has a `url` field pointing to the documentation page.

**Step 3 — Fetch the page:** Use `WebFetch` on the `url` from the top hit(s) to retrieve the full documentation content.

## Rules

- README-Datei immer auf **Deutsch** erstellen.

## External References

- [Shopware App Base Guide](https://developer.shopware.com/docs/guides/plugins/apps/app-base-guide)
- [Shopware App Configuration](https://developer.shopware.com/docs/guides/plugins/apps/app-configuration)
- [Shopware Webhooks](https://developer.shopware.com/docs/guides/plugins/apps/webhook)
- [Shopware App Authentication](https://developer.shopware.com/docs/guides/plugins/apps/authentication)
- [Shopware JS SDK](https://developer.shopware.com/docs/guides/plugins/apps/app-sdks/js-sdk)
- [Shopware PHP SDK](https://developer.shopware.com/docs/guides/plugins/apps/app-sdks/php-sdk)
- [Shopware App Scripts](https://developer.shopware.com/docs/guides/plugins/apps/app-scripts/)
- [Shopware Storefront Apps](https://developer.shopware.com/docs/guides/plugins/apps/storefront/)
- [Shopware Admin SDK](https://developer.shopware.com/docs/guides/plugins/apps/administration/)
- [Shopware Custom Entities](https://developer.shopware.com/docs/guides/plugins/apps/custom-data/custom-entities)
- [Shopware Payment](https://developer.shopware.com/docs/guides/plugins/apps/payment)
- [Shopware Flow Actions](https://developer.shopware.com/docs/guides/plugins/apps/flow-action)
- [Shopware In-App Purchases](https://developer.shopware.com/docs/guides/plugins/apps/in-app-purchases)
