# Shopware Commercial – unlocking plan features

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/shopware-commercial

## Contents

- [Overview](#overview)
- [Installation](#installation)
- [Features by plan](#features-by-plan)
- [AI Copilot – details (all plans)](#ai-copilot-details-all-plans)
- [CLI commands (self-hosted)](#cli-commands-self-hosted)
- [Frequently asked questions](#frequently-asked-questions)

## Overview

The **Shopware Commercial Extension** unlocks all features of the booked plan
(Rise, Evolve or Beyond). It automatically syncs the active plan and provides
all available functions – without separate updates per feature.

---

## Installation

### Cloud users
- Pre-installed and automatically active – no action required.

### Self-hosted
1. Open **Erweiterungen** (Extensions) **> Store**
2. Search for "Shopware Commercial"
3. Click **Hinzufügen** (Add)
4. Then: **Erweiterungen > Meine Erweiterungen** (My extensions) **> Aktivieren** (Activate)

---

## Features by plan

### Shopware Rise (basis)

| Category | Feature | Description |
|---|---|---|
| **AI Copilot** | Content creation | AI-generated product descriptions |
| **AI Copilot** | Classification | Automatic product categorisation |
| **AI Copilot** | Translations | AI-assisted translations |
| **Workflow** | Rule Builder | Rule-based automations |
| **Workflow** | Flow Builder | Event-based workflows |
| **Content** | Custom Products | Configurable products with options |
| **Content** | Social Shopping | Facebook, Instagram, Google Shopping |
| **Content** | Immersive Elements | 3D/VR product presentations |

### Shopware Evolve (+ compared with Rise)

| Category | Feature | Description |
|---|---|---|
| **Search** | Advanced Search 2.0 | OpenSearch-based high-performance search |
| **Content** | CMS extensions | Quick View, scroll nav, block visibility |
| **Access** | Dynamic Access | Rule-based visibility for products/categories |
| **B2B** | Quick Order | Fast ordering for business customers |
| **B2B** | Approval processes | Order approvals |
| **B2B** | Angebote (Quotes) | Quote creation and management |
| **Publishing** | Shopware Publisher | Draft management for Erlebniswelten (Shopping Experiences) |
| **Sales** | Sales Agent | Field-sales frontend app |

### Shopware Beyond (+ compared with Evolve)

| Category | Feature | Description |
|---|---|---|
| **Inventory** | Multi-Inventory | Multiple warehouses, stock routing |
| **Subscription** | Subscriptions | Recurring orders |
| **Pricing** | Customer-specific prices | Individual prices per customer (API-based) |
| **Sales** | Digital Sales Rooms | Live shopping events with video |

---

## AI Copilot – details (all plans)

The AI Copilot is integrated into the administration and supports:

- **Generating product descriptions**: in the product form → "Beschreibung generieren" (Generate description)
- **SEO texts**: suggest meta descriptions and SEO titles
- **Translations**: translate existing texts into other languages
- **Classification**: assign products to categories automatically

---

## CLI commands (self-hosted)

The Commercial Extension adds additional console commands:

```bash
# Check the licence status
php bin/console commercial:license:status

# Reload the features
php bin/console commercial:feature:refresh

# Rebuild the index for Advanced Search
php bin/console es:admin:index
```

---

## Frequently asked questions

**Q: What happens if I downgrade my plan?**
A: Features of the higher plan are deactivated immediately. Data is retained but is no
longer accessible until a plan upgrade.

**Q: Do I have to reinstall Commercial after a Shopware update?**
A: No. The extension updates itself automatically together with Shopware updates.

**Q: Where do I see which plan I have active?**
A: Shopware Account (account.shopware.com) > Shop details > Active plan
