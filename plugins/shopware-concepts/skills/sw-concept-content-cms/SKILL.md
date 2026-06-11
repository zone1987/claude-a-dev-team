---
name: sw-concept-content-cms
description: >
  Shopware Shopping Experiences (CMS): Struktur (Page/Section/Block/Slot/Element),
  Content-Hydration, Headless-CMS, Cookie Consent Management. Trigger: "Shopping Experiences",
  "CMS Konzept", "wie ist das CMS aufgebaut", "Page Builder Shopware", "CMS Seiten Struktur",
  "CMS Element Resolver", "wie wird CMS-Inhalt geladen", "headless CMS shopware",
  "shopware content", "Cookie Consent Shopware", "GDPR Cookie", "shopware cms blocks slots",
  "CmsElementResolverInterface", "wie funktioniert Content in Shopware".
---

# Shopware CMS / Shopping Experiences — Konzept

Vollständige Konzept-Doku: `references/deep/content-cms.md`

## Kurzüberblick

### Hierarchische Struktur

```
Page → Section(en) → Block(s) → Slot(s) → Element
```

- **Page** — Wrapper, Type: `page`, `landingpage`, `product_list`, `product_detail`
- **Section** — horizontaler Container; Typ: `fullwidth` oder `sidebar`
- **Block** — Zeile mit Slots; kategorisiert nach `text`, `image`, `commerce` etc.
- **Slot** — benannter Container für genau ein Element
- **Element** — Primitive wie `text`, `image`, `product-listing`, `buy-box` etc.

### Content-Hydration (Resolving)

1. CMS-Layout laden (inkl. Sections, Blocks, Slots)
2. Resolver-Kontext aufbauen (SalesChannelContext + assoziierte Entity, z.B. Category)
3. Slot-Konfiguration der Entity überschreiben (Category-spezifische Anpassungen)
4. Collect → Optimize → Fetch → Enrich (2-Phasen-Resolver)
5. `CmsPageLoadedEvent` feuern → Cache-Tags sammeln

### Headless-Fähigkeit

CMS ist **kanalunabhängig** — Storefront rendert HTML, Headless-Frontend konsumiert JSON via API.
Gleiche Layouts für alle Präsentationskanäle.

### Cookie Consent Management (ab 6.7.3.0)

- 4 Kategorien: Required, Comfort, Marketing, Statistical
- Hash-Mechanismus: Neueinwilligung bei Konfigurationsänderung (per Sprache)
- Store API: `GET /store-api/cookie/groups`

Technische Umsetzung: `shopware-cms` (Dev-Plugin)
