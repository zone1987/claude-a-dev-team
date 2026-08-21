# Shopware 6 – editions & feature overview (complete)

## Contents

- [Edition hierarchy](#edition-hierarchy)
- [Community Edition (CE) – core functions](#community-edition-ce-core-functions)
- [Rise plan – additional features](#rise-plan-additional-features)
- [Evolve plan – additional features](#evolve-plan-additional-features)
- [Beyond plan – additional features](#beyond-plan-additional-features)
- [Support comparison](#support-comparison)
- [Shopware Commercial Extension – installation](#shopware-commercial-extension-installation)
- [Further skills](#further-skills)

## Edition hierarchy

Shopware 6 is available in four cumulative editions:

```
Community Edition (CE/Core)
  └── Rise (enthält alles aus CE)
        └── Evolve (enthält alles aus Rise)
              └── Beyond (enthält alles aus Evolve)
```

The **Shopware Commercial** extension unlocks plan-dependent additional functions. On Cloud installations it is pre-installed; on self-hosted it has to be installed manually via **Erweiterungen** (Extensions) **> Store**.

---

## Community Edition (CE) – core functions

### Content management & design
- **Erlebniswelten (Shopping Experiences)**: drag-and-drop editor for shop pages, landing pages, category and product pages
  - 5 layout types: shop pages, landing pages, category pages, product pages, bundle pages
  - Blocks: text, images, sliders, galleries, commerce, video, forms, HTML
  - Viewport preview for responsive design
  - Data mapping for dynamic content on category/product pages
- Device-optimised design with customisable templates

### Workflow & automation
- **Roles & permissions**: user management with individual permission levels
  - Permission hierarchy: view → edit → create → delete → all
  - Special permissions: basic settings, updates, extensions, event log, cache, import/export
  - API access keys for integrations
- **Rule Builder**: condition-based rules for shipping costs and other functions (basis)
- **Flow Builder**: event-based automation of business processes without code (basis)
  - 100+ triggers (orders, customers, payments, notifications)
  - Actions: sending emails, document creation, status assignment, customer group change, tag management

### Customer experience & marketing
- Customer groups
- Aktionen (Promotions) & promotions
- SEO optimisation
- Product search
- Cross-selling
- Product reviews
- Tag management

### Inventory & order management
- Physical and digital products
- Dynamische Produktgruppen (Dynamic product groups)
- Payment gateway integration
- Shipping provider integration
- Category management

### B2B (basis)
- Gross/net price display by customer group with configurable tax rates

### Internationalisation
- Unlimited Verkaufskanäle (Sales channels) (storefronts, comparison portals, social shopping)
- Multi-currency and tax management
- Multi-language support

### Further features
- Import/export tools
- Migration from other eCommerce platforms
- Extensibility via the Shopware Store

---

## Rise plan – additional features

Contains all CE features plus:

| Feature | Description |
|---|---|
| **Flow Builder – sharing flows** | Export/import of flows between instances (from 6.4.19.0) |
| **Custom Products** | Configurable/personalisable products with individual options |
| **Premium Themes** | Professional design templates for storefronts |
| **Retouren-Management (Returns management)** | Returns handling directly in the admin panel |
| **Rule Builder – Vorschau (Preview)** | Real-time testing of rules against real orders (TRUE/FALSE) |
| **Social Commerce** | Integration with social media sales channels |
| **Shopware AI Copilot** | AI assistant for content, product descriptions, search |
| **3D viewer block for Erlebniswelten** | 3D product visualisation in Shopping Experiences |
| **Immersive Elements** | 5 different 3D elements for Erlebniswelten (from 16/05/2024) |
| **Scene Editor (beta)** | Create visual 3D scenes and generate product images |
| **Rule Builder – sharing rules** | Download/import of rules as JSON (from 6.7.1.0) |

---

## Evolve plan – additional features

Contains all Rise features plus:

| Feature | Description |
|---|---|
| **Advanced Search 2.0** | OpenSearch-based advanced search with boostings, actions, synonyms |
| **B2B Components** | B2B functionality: Angebote (Quotes), Mitarbeiter (Employees), Genehmigungen (Approvals), Budgets |
| **CMS extensions** | Extended CMS functions |
| **CMS rules** | Rule-based visibility of CMS content |
| **Dynamic Access** | Access control and permission management |
| **Publisher** | Content publishing tools |
| **Flow Builder – webhook actions** | Call external URLs via GET/POST/PUT/PATCH/DELETE |
| **Sales Agent** | Field sales representative app for B2B customer management |

---

## Beyond plan – additional features

Contains all Evolve features plus:

| Feature | Description |
|---|---|
| **Digital Sales Rooms** | Interactive live video shopping events |
| **Customer-specific prices** | Individual prices per customer via API (ERP integration) |
| **Multi-Inventory** | Stock management across multiple locations |
| **Abonnements (Subscriptions)** | Recurring orders with configurable intervals |
| **Flow Builder – time-delayed actions** | Scheduled execution of flow actions (hours/days/weeks) |

---

## Support comparison

| Service | Rise | Evolve | Beyond |
|---|---|---|---|
| **Availability** | 09:00–17:00* | 07:00–19:00* | 24/7 |
| **Response time** | 8 hours | 4 hours | 1 hour |
| **Written support** | ✓ | ✓ | ✓ |
| **Telephone support (callback)** | — | ✓ | ✓ |
| **Hotline** | — | ✓ | ✓ |
| **Developer support** | — | — | ✓ |
| **Personal onboarding** | — | — | ✓ |
| **Account Manager** | — | — | ✓ |
| **Community forum** | ✓ | ✓ | ✓ |
| **Free initial installation** | ✓ | ✓ | ✓ |
| **Updates & patches** | ✓ | ✓ | ✓ |

*Exceptions: public holidays in NRW, 24/12 from 12:00, 31/12 from 12:00, 3 internal events per year (2026: 15/01, 14/04, 08/10)

---

## Shopware Commercial Extension – installation

- **Cloud**: automatically pre-installed
- **Self-hosted**: Erweiterungen > Store → search for "Shopware Commercial" and install

The extension activates features automatically according to the booked plan.

---

## Further skills

- `sw-merchant-commercial` – overview of all Commercial features
- `sw-merchant-commercial-ai-copilot` – AI Copilot functions
- `sw-merchant-commercial-subscriptions` – Abonnements (Subscriptions)
- `sw-merchant-commercial-advanced-search` – Advanced Search 2.0
- `sw-merchant-commercial-b2b` – B2B Components
- `sw-merchant-commercial-returns` – Retouren-Management (Returns management)
- `sw-merchant-commercial-flow-builder` – Flow Builder (Commercial)
- `sw-merchant-commercial-rule-builder` – Rule Builder (Commercial)
- `sw-merchant-commercial-multi-inventory` – Multi-Inventory
- `sw-merchant-commercial-sales-agent` – Sales Agent
- `sw-merchant-commercial-digital-sales-rooms` – Digital Sales Rooms
- `sw-merchant-commercial-custom-pricing` – customer-specific prices
- `sw-merchant-commercial-spatial` – Spatial Commerce

---

*Source: https://docs.shopware.com/de/shopware-6-de/features (as of: 2026-06)*
