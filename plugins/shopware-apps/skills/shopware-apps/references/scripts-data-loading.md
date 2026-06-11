---
title: Data Loading Scripts
impact: MEDIUM
impactDescription: Data loading scripts add custom data to storefront pages
tags: scripts, data-loading, repository, store, page-extension
---

## Data Loading Scripts

Data loading scripts add custom data to storefront pages. Place them in `Resources/scripts/{hook-name}/` where the hook name matches a storefront page event (e.g., `product-page-loaded`).

### Repository Service (DAL Access)

```twig
{% set criteria = {
    'ids': ['uuid1', 'uuid2']
} %}
{% set products = services.repository.search('product', criteria) %}
```

### Store Service (Storefront-Optimized)

The store service is optimized for storefront use — it auto-resolves SEO URLs, calculates prices, and doesn't require permissions:

```twig
{% set criteria = {
    'filter': [
        { 'type': 'equals', 'field': 'active', 'value': true }
    ],
    'associations': {
        'manufacturer': {}
    }
} %}
{% set products = services.store.search('product', criteria) %}
```

### Adding Data to Page

```twig
{# Add entity or collection #}
{% do page.addExtension('swagMyProducts', products) %}

{# Add mixed data (arrays, scalars) #}
{% do page.addArrayExtension('swagMyData', {
    'totalCount': products|length,
    'showBanner': true
}) %}
```

### Accessing in Storefront Templates

```twig
{# In Resources/views/storefront/... templates #}
{% set myProducts = page.getExtension('swagMyProducts') %}
{% set myData = page.getExtension('swagMyData') %}

{% for product in myProducts %}
    <p>{{ product.name }}</p>
{% endfor %}

{% if myData.showBanner %}
    <div>Banner content ({{ myData.totalCount }} items)</div>
{% endif %}
```

### Search Criteria Format

```twig
{% set criteria = {
    'ids': ['uuid'],
    'limit': 10,
    'page': 1,
    'filter': [
        { 'type': 'equals', 'field': 'active', 'value': true },
        { 'type': 'range', 'field': 'stock', 'parameters': { 'gte': 1 } },
        { 'type': 'contains', 'field': 'name', 'value': 'search term' }
    ],
    'sort': [
        { 'field': 'name', 'order': 'ASC' }
    ],
    'associations': {
        'manufacturer': {},
        'categories': { 'limit': 5 }
    }
} %}
```

### Important Notes

- Use **vendor-prefixed** extension names (e.g., `swagMyData`) to avoid conflicts
- The `store` service is preferred for storefront — it handles pricing and SEO automatically
- The `repository` service gives raw DAL access but requires appropriate permissions
