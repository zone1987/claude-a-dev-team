# Shopware CMS / Shopping Experiences — concept

Complete concept documentation: `CONTENT-CMS-DETAIL.md`

## Quick overview

### Hierarchical structure

```
Page → Section(s) → Block(s) → Slot(s) → Element
```

- **Page** — wrapper, type: `page`, `landingpage`, `product_list`, `product_detail`
- **Section** — horizontal container; type: `fullwidth` or `sidebar`
- **Block** — row with slots; categorised by `text`, `image`, `commerce` etc.
- **Slot** — named container for exactly one element
- **Element** — primitives such as `text`, `image`, `product-listing`, `buy-box` etc.

### Content hydration (resolving)

1. Load the CMS layout (incl. sections, blocks, slots)
2. Build the resolver context (SalesChannelContext + associated entity, e.g. category)
3. Override the entity's slot configuration (category-specific adjustments)
4. Collect → Optimize → Fetch → Enrich (2-phase resolver)
5. Fire `CmsPageLoadedEvent` → collect cache tags

### Headless capability

The CMS is **channel-independent** — the storefront renders HTML, a headless frontend consumes JSON via API.
The same layouts for all presentation channels.

### Cookie consent management (from 6.7.3.0)

- 4 categories: Required, Comfort, Marketing, Statistical
- Hash mechanism: re-consent on configuration change (per language)
- Store API: `GET /store-api/cookie/groups`

Technical implementation: `shopware-cms` (dev plugin)
