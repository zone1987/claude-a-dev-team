# shopware-merchant

> Operator/usage knowledge for the administration (no code).

`shopware-merchant` is the **operator/usage knowledge** — how to **operate the shop in the administration**
(no code). It is distilled from the official end-user documentation (`docs.shopware.com`) and includes
**screenshots**.

All areas of the administration are covered: **Kataloge** (Catalogues — products, categories, manufacturers,
properties, dynamic product groups, reviews, media), **Bestellungen** (Orders — creating/editing, states, documents,
refunds), **Kunden** (Customers — accounts, addresses, groups, B2B), **Inhalte** (Content — Erlebniswelten/Shopping
Experiences, media, themes), **Marketing** (promotions, discount codes, newsletter, rule builder),
**Einstellungen** (Settings — shop, taxes, currencies/languages, shipping/payment methods, delivery times,
flow/rule builder, mail templates, import/export, users/permissions, caches/indexes), **Verkaufskanäle**
(Sales Channels), **Erweiterungen** (Extensions), **Cloud**, **migration**, the **Commercial features**,
**Services**, **Spatial Commerce**, **insider previews**, **tutorials/FAQ** and **update guides**.

Advisor: **`shopware-merchant-guide`** answers "how do I configure/do X in the admin". **When to use:** for
usage/configuration questions from an operator's point of view. The *technical* implementation of the same concepts
lives in the developer plugins.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official sources and embedded; each skill's depth sits in flat SCREAMING-CASE.md reference files next to its SKILL.md and is loaded progressively.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-merchant@claude-a-dev-team
```

## Skills (16)

| Skill | Description |
|---|---|
| `sw-merchant-catalog` | Operating the Shopware catalogue: products, variants, categories, properties, manufacturers, media, product streams, reviews. Use when the request is about the Shopware admin under **Kataloge** (Catalogues). |
| `sw-merchant-cloud` | Operating Shopware Cloud: SaaS setup, tenant administration, what differs from a self-hosted shop. Use when the request names Shopware Cloud or SaaS. |
| `sw-merchant-commercial` | Operating Shopware Commercial features: B2B suite, subscriptions, custom pricing, returns, multi-inventory, advanced search. Use when the request names a Shopware Commercial or Evolve feature. |
| `sw-merchant-content` | Operating Shopware content: Shopping Experiences, CMS blocks and elements, themes, media manager. Use when the request is about the Shopware admin under **Inhalte** (Content) or **Erlebniswelten** (Shopping Experiences). |
| `sw-merchant-customers` | Operating Shopware customers: accounts, addresses, customer groups, bulk edits, B2B customers, storefront account view. Use when the request is about the Shopware admin under **Kunden** (Customers). |
| `sw-merchant-general` | Shopware administration orientation: first steps, feature overview, extension management, comparison with Shopify. Use when the request asks what the Shopware admin offers or how to get started. |
| `sw-merchant-insider` | Shopware insider previews: bundles, the new scene editor, features not yet generally available. Use when the request names a Shopware insider preview or an unreleased feature. |
| `sw-merchant-marketing` | Operating Shopware marketing: promotions, discount codes, newsletter, the rule builder for marketing rules. Use when the request is about the Shopware admin under **Marketing** or **Aktionen** (Promotions). |
| `sw-merchant-migration` | Migrating to Shopware: the migration process, data mapping, going live. Use when the request is about migrating a shop to Shopware or the Migration Assistant. |
| `sw-merchant-orders` | Operating Shopware orders: order list, creating and editing orders, state machine transitions, documents, refunds. Use when the request is about the Shopware admin under **Bestellungen** (Orders). |
| `sw-merchant-sales` | Operating Shopware sales channels: creating channels, domains, product assignment, API access, comparison feeds. Use when the request names a Shopware **Verkaufskanal** (sales channel). |
| `sw-merchant-services` | Operating Shopware Services: AI copilot, image editor, 3D preview, Nexus, Intelligence Plus. Use when the request names a Shopware Service or Shopware Payments. |
| `sw-merchant-settings` | Operating Shopware settings: shop basics, taxes, currencies, payment and shipping methods, rule and flow builder, mail templates. Use when the request is about Shopware **Einstellungen** (Settings). |
| `sw-merchant-spatial` | Operating Shopware Spatial Commerce: 3D products, AR, the scene editor, immersive elements. Use when the request names Shopware Spatial, 3D products or AR. |
| `sw-merchant-tutorials` | Shopware how-to guides: worked examples, multilingual shops, EU regulations, troubleshooting recipes. Use when the request asks how to accomplish a concrete task in the Shopware admin. |
| `sw-merchant-update` | Updating a Shopware shop: running the update, version specifics, staging environments, pre-update checks. Use when the request is about updating or upgrading a Shopware shop. |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-merchant-guide` | Advisor for Shopware 6 operators/merchants: answers "how do I do X in the administration?" from the distilled merchant documentation (**Kataloge**/catalogues, **Bestellungen**/orders, **Kunden**/customers, **Inhalte**/content and **Erlebniswelten**/Shopping Experiences, **Marketing**, **Einstellungen**/settings, **Verkaufskanäle**/sales channels, **Erweiterungen**/extensions and more) |
