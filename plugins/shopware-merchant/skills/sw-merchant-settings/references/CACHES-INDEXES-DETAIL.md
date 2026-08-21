# Shopware 6 – Caches & Indizes (Caches & indexes) (complete reference)

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/caches-indizes

---

## Contents

- [Overview](#overview)
- [Configuration overview (dashboard)](#configuration-overview-dashboard)
- [Admin actions](#admin-actions)
- [Indexer overview](#indexer-overview)
- [Clearing the cache automatically](#clearing-the-cache-automatically)
- [Manual cache deletion (fallback)](#manual-cache-deletion-fallback)
- [Background knowledge](#background-knowledge)

## Overview

**Path:** Einstellungen (Settings) > System > Caches & Indizes  
**Self-hosted only** (not for SaaS environments)  
**Available from:** 6.2.0

---

## Configuration overview (dashboard)

The dashboard shows three main pieces of information:

| Information | Description |
|---|---|
| Umgebung (Environment) | Shows whether the shop runs in "Production" mode |
| HTTP-Cache | Status of the HTTP cache activation |
| Cache-Adapter | Which adapter is in use |

### Configuration via .env
```env
# Enable (1) or disable (0) the HTTP cache
SHOPWARE_HTTP_CACHE_ENABLED=1
```

---

## Admin actions

### Cache aktualisieren (Refresh cache)
Deletes cached data for recently changed content (e.g. theme or product adjustments).

### Cache löschen (Clear cache)
Removes the **entire cache** without warming it up afterwards.
```bash
php bin/console cache:clear
```

### Indizes aktualisieren (Update indexes)
Updates the category, product and SEO URL indexes:
```bash
php bin/console dal:refresh:index
```

---

## Indexer overview

| Indexer | Function |
|---|---|
| `category.indexer` | Category index with subcategories, tree, breadcrumb, SEO URLs |
| `customer.indexer` | Search index for customer records |
| `landing_page.indexer` | Index for landing pages with SEO URLs |
| `media.indexer` | Media files and folders with inheritance |
| `payment_method.indexer` | Payment method index |
| `product.indexer` | Comprehensive product index: inheritance, stock, variants, category assignments, prices, reviews, streams, SEO URLs |
| `product_stream.indexer` | Dynamische Produktgruppen (Dynamic product groups) |
| `promotion.indexer` | Rabatte & Aktionen (Discounts & promotions) with exclusions and usage |
| `rule.indexer` | Rule Builder rules and Bedingungen (Conditions) |
| `sales_channel.indexer` | Verkaufskanäle (Sales channels) |
| `flow.indexer` | Workflow flows |
| `newsletter_recipient.indexer` | Newsletter recipients |

### Selective index refresh
- Select an indexer from the dropdown
- Method: "Nur Auswahl aktualisieren" (Update selection only) or "Alle außer Auswahl" (All except selection)

---

## Clearing the cache automatically

Shopware 6 does **not** clear the cache automatically. Recommendation:

```bash
php bin/console cache:clear
php bin/console cache:warmup
```

**Best practice:** run this daily via cron job during low traffic (e.g. at night).

---

## Manual cache deletion (fallback)

If the CLI command fails:
```bash
rm -rf /path/to/shopware/var/cache/*
```

---

## Background knowledge

| Term | Meaning |
|---|---|
| **Cache** | Speeds up requests by means of stored data |
| **Index** | Lists of data in text format for fast search algorithms |
