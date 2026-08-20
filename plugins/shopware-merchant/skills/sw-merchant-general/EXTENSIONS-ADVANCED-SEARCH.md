# Advanced Search – high-performance search for the storefront

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/advanced-search  
**Plan**: Shopware Evolve (or higher)  
**Technology**: Elasticsearch (up to SW 6.4) / OpenSearch (from SW 6.5.6.0)

## Contents

- [Overview](#overview)
- [Versions & compatibility](#versions--compatibility)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration areas](#configuration-areas)
- [Index management](#index-management)
- [Difference from the standard search](#difference-from-the-standard-search)

## Overview

**Advanced Search** offers simple configuration options and, thanks to its
Elasticsearch/OpenSearch foundation, **high performance** even with large product catalogues.
From Shopware 6.5 onwards, the successor **Advanced Search 2.0** must be used.

---

## Versions & compatibility

| Shopware version | Advanced Search version | Search engine |
|---|---|---|
| up to 6.4.20.2 | Advanced Search 1.x | Elasticsearch |
| 6.5.x | Advanced Search 2.0 | OpenSearch (from 6.5.6.0) |
| 6.6+ | Advanced Search 2.0+ | OpenSearch |

---

## Prerequisites

- An **Elasticsearch instance** (for 1.x) or an **OpenSearch instance** (for 2.0) is mandatory
- Set the environment variable:
  ```
  SHOPWARE_ES_INDEXING_ENABLED=1
  ```
- Create the index:
  ```bash
  php bin/console es:index
  php bin/console messenger:consume
  # Optional:
  php bin/console es:create:alias
  ```

---

## Installation

1. **Erweiterungen** (Extensions) **> Meine Erweiterungen** (My extensions) in the admin
2. Log in on the Shopware Account tab (licence verification)
3. Download and install Advanced Search
4. Activate it
5. Rebuild the index (see above)

---

## Configuration areas

### 1. Durchsuchbare Informationen (Searchable information)

Define **which data fields** are indexed and with which priority:

| Entity | Fields (examples) |
|---|---|
| Produkte (Products) | name, description, EAN, product number, manufacturer, properties |
| Kategorien (Categories) | name, description, keywords |
| Hersteller (Manufacturers) | name, description |

Options per field:
- **Teilübereinstimmung** (Partial match): also find parts of the search term
- **Komposita** (Compound words): compound words (e.g. "Laufschuhe" finds "Lauf" + "Schuhe")
- **Priorität** (Priority): higher number = more important in the search order

### 2. Vorschau (Preview)

- **Test the search live** by sales channel and entity type
- Shows relevance scores of the hits
- Ideal for checking configuration changes before going live

### 3. Boostings

Targeted visibility adjustments for specific content:

| Type | Description |
|---|---|
| Product boostings | Defined via dynamic product groups |
| Category boostings | Via custom rules (Rule Builder) |
| Manufacturer boostings | Via custom rules |

### 4. Actions (search redirects)

**Automatically redirect** customers for certain search terms:
- To a URL (external or internal)
- To a specific product
- To a specific category

Example: a search for "Sale" → automatic redirect to the sale category

### 5. Synonyme (Synonyms)

Configure equivalent or defining synonyms:

| Type | Example |
|---|---|
| Equivalent | "Hose" ↔ "Jeans" ↔ "Chino" |
| Defining | "Smartphone" → "Handy, Mobiltelefon, Telefon" |

- Multiple languages are supported
- Considerably extends the search coverage

---

## Index management

| Command | Description |
|---|---|
| `php bin/console es:index` | Rebuild the index |
| `php bin/console es:create:alias` | Set the alias anew |
| `php bin/console es:admin:index` | Update the admin search index |
| `php bin/console messenger:consume` | Process the message queue |

> **Important**: for new products or price changes no manual rebuild is required
> when `SHOPWARE_ES_INDEXING_ENABLED=1` is set – this happens automatically.

---

## Difference from the standard search

| Feature | Standard search | Advanced Search |
|---|---|---|
| Technology | Database-based (MySQL) | Elasticsearch/OpenSearch |
| Performance with a large catalogue | Limited | Very high |
| Configurable fields | No | Yes |
| Synonyms | No | Yes |
| Boostings | No | Yes |
| Actions/redirects | No | Yes |
| Partial match | Limited | Complete |
