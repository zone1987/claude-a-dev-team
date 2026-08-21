# Search in the administration

**Source**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/suche-administration  
**AND/OR search from**: Shopware 6.4.19.0

## Overview

The Shopware 6 administration contains a **central search bar** at the top,
which searches all activated entities.

---

## Access & operation

- **Position**: top bar of the administration, centred
- **Open via keyboard shortcut**: `Strg/Cmd + F`
- **Open the module filter**: type `#` → dropdown for module selection

---

## Module filtering

A **dropdown in the search bar** lets you narrow the search down to certain areas:

| Module shortcut | Searched area |
|---|---|
| `#produkte` | Product catalogue |
| `#bestellungen` | Bestellungen (Orders) |
| `#kunden` | Customer master data |
| `#kategorien` | Category tree |
| `#medien` | Media management |
| `#hersteller` | Manufacturer list |

---

## Personalising the search settings

Under **Profil** (Profile) **> Sucheinstellungen** (Search settings), every user can configure
individually which entities should appear in the search:

- **Alle auswählen** (Select all): activate all entities
- **Alle abwählen** (Deselect all): deactivate all entities
- **Standard wiederherstellen** (Restore default): reset to the Shopware default

---

## Practical use cases

| Scenario | Procedure |
|---|---|
| Customer calls with an invoice number | Enter the invoice number in the search → open the order directly |
| Search for a product by a name fragment | Enter a partial term → hits are shown from all active modules |
| Search for a product by EAN/GTIN | Enter the EAN/GTIN (the setting must be activated) |

---

## Advanced AND/OR search (from 6.4.19.0)

For more complex queries, the AND/OR search function can be activated.

### Prerequisites
- OpenSearch configured as the search engine
- Environment variable in `.env`:
  ```
  SHOPWARE_ES_INDEXING_ENABLED=1
  ```
- Rebuild the search index:
  ```bash
  php bin/console es:admin:index
  ```

### Usage
- **AND**: all search terms must occur
- **OR**: at least one search term must occur
- Combination via search operators in the input

> **Note**: this function requires server configuration and is not available in the standard setup
> without Elasticsearch/OpenSearch.

---

## Relationship with Advanced Search

The standard admin search is to be distinguished from the **Advanced Search Extension**
for the storefront. The admin search concerns the backend only.

→ For storefront search: `../../../sw-merchant-extensions/references/deep/advanced-search.md`
