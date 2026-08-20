# Shopware Advanced Search 2.0 – Complete documentation

## Contents

- [Overview](#overview)
- [Configuring search behaviour](#configuring-search-behaviour)
- [Searchable content](#searchable-content)
- [Search result display](#search-result-display)
- [Boostings](#boostings)
- [Actions (search term redirects)](#actions-search-term-redirects)
- [Synonyme (Synonyms)](#synonyme-synonyms)
- [AI Copilot integration (Rise+)](#ai-copilot-integration-rise)
- [Storefront integration](#storefront-integration)

## Overview

**Advanced Search 2.0** is the professional search solution of Shopware 6, based on OpenSearch infrastructure.

**Availability:** Evolve plan and higher
**Minimum version:** Shopware 6.5.6.0
**Prerequisites:**
- OpenSearch infrastructure
- Shopware Commercial extension
- Evolve plan or higher

**Path in the admin:** Einstellungen (Settings) → Allgemein (General) → Suche (Search)

---

## Configuring search behaviour

### Suchmodus (Search mode)

| Mode | Behaviour |
|---|---|
| AND-Suche (AND search) | Results must contain ALL search terms |
| OR-Suche (OR search) | Results must contain at least ONE term |

### Mindestsuchwortlänge (Minimum search term length)

Configurable per Verkaufskanal (sales channel) – searches with fewer characters are ignored.

### Special characters in product numbers

Special characters can be preserved via the YAML configuration:

```yaml
# config/packages/shopware.yaml
shopware:
  search:
    preserved_chars: ['-', '_', '.']
```

---

## Searchable content

You can define which fields appear in search results:

### Produkte (Products)
- Name, description, product number
- EAN, manufacturer number
- Custom fields

### Kategorien (Categories)
- Name, description
- Category tags

### Hersteller (Manufacturers)
- Name

### Ranking / weighting

Every search field is given a score. Higher values = higher visibility in search results.

**Example:**
- Product name: 1000 points
- Product number: 500 points
- Description: 100 points

---

## Search result display

Separate configuration for:

| Area | Setting |
|---|---|
| Schnellsuche (Quick search, dropdown) | Max. number of results |
| Volltextsuche (Full-text search, result page) | Max. number of results |

---

## Boostings

Boostings increase the visibility of specific products in search results.

**Creation:**
1. Einstellungen → Suche → Boostings → Neues Boosting (New boosting)
2. Define name and Priorität (Priority)
3. Product selection via Dynamische Produktgruppe (Dynamic product group) or custom rule
4. Gültigkeitszeitraum (Validity period, optional for seasonal relevance)
5. Zuweisung (Assignment) to Verkaufskanäle (Sales channels)

**Use cases:**
- Highlight seasonal products temporarily
- Prioritise new collections
- Favour high-margin products

---

## Actions (search term redirects)

Actions redirect customers from specific search terms to defined targets.

**Configuration:**
1. Einstellungen → Suche → Actions → Neue Action (New action)
2. Define search term(s)
3. Set the target: Produkt, Kategorie or URL

**Use cases:**
- Route brand names to a category
- Catch typos and forward correctly
- Show seasonal promotion pages for certain searches

---

## Synonyme (Synonyms)

Synonyms make sure that related terms return the same results.

### Equivalence synonyms
All terms are fully interchangeable:
- "Sofa" ↔ "Couch" ↔ "Sessel"

### Explicit mapping
Specific terms are mapped to broader categories:
- "iPhone" → "Smartphone", "Handy", "Mobiltelefon"
- A search for "iPhone" shows all smartphones, but not the other way round

---

## AI Copilot integration (Rise+)

With the AI Copilot (Rise plan), the search is extended by AI functions:

### Context-based search
- Customers describe their product in natural language
- The AI interprets customer intent taking the shop context into account
- Max. 100 characters of input
- In the storefront: icon next to the search field with example suggestions

### Image-based search
- Customers upload an image
- The system finds visually similar products in the assortment

---

## Storefront integration

Advanced Search activates itself automatically for all configured Verkaufskanäle. No further storefront adjustments are needed.

---

*Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/advancedsearch-2-0 (as of: 2026-06)*
