---
title: Custom API Endpoint Scripts
impact: MEDIUM
impactDescription: Custom endpoints create new API routes without an external server
tags: scripts, endpoints, api, store-api, storefront, custom-routes
---

## Custom API Endpoint Scripts

Apps can create custom API endpoints using scripts in three scopes:

| Scope | Directory | URL | Methods |
|-------|-----------|-----|---------|
| Admin API | `api-{name}/` | `/api/script/{name}` | POST |
| Store API | `store-api-{name}/` | `/store-api/script/{name}` | POST, GET |
| Storefront | `storefront-{name}/` | `/storefront/script/{name}` | POST, GET |

### Admin API Endpoint

```twig
{# Resources/scripts/api-custom-action/custom-action.twig #}
{% set products = services.repository.search('product', {
    'limit': 10,
    'filter': [{ 'type': 'equals', 'field': 'active', 'value': true }]
}) %}

{% set response = services.response.json({
    'products': products|map(p => { 'id': p.id, 'name': p.name })
}) %}

{% do hook.setResponse(response) %}
```

### Store API Endpoint (Interface Hook)

```twig
{# Resources/scripts/store-api-custom-products/custom-products.twig #}
{% block response %}
    {% set products = services.store.search('product', {
        'limit': hook.query.limit|default(10),
        'filter': [{ 'type': 'equals', 'field': 'active', 'value': true }]
    }) %}

    {% set response = services.response.json(products) %}
    {% do hook.setResponse(response) %}
{% endblock %}

{% block cache_key %}
    {{ hook.query.limit|default(10) }}
{% endblock %}
```

### Storefront Endpoint (HTML Response)

```twig
{# Resources/scripts/storefront-my-page/my-page.twig #}
{% block response %}
    {% set products = services.store.search('product', { 'limit': 5 }) %}
    {% set response = services.response.render('@MyApp/storefront/page/my-page.html.twig', {
        'products': products
    }) %}
    {% do hook.setResponse(response) %}
{% endblock %}
```

### Storefront Endpoint (Redirect)

```twig
{% set response = services.response.redirect('https://example.com', 302) %}
{% do hook.setResponse(response) %}
```

### Response Types

| Method | Purpose |
|--------|---------|
| `services.response.json(data)` | JSON response |
| `services.response.render(template, vars)` | Rendered Twig template |
| `services.response.redirect(url, code)` | HTTP redirect |

### Header Manipulation (since 6.6.10.4)

```twig
{% do hook.setHeader('X-Custom-Header', 'value') %}
{% set existing = hook.getHeader('Content-Type') %}
```

### Query Parameters

```twig
{% set page = hook.query.page|default(1) %}
{% set limit = hook.query.limit|default(10) %}
```

### Script Propagation

```twig
{# Prevent other scripts from executing for this hook #}
{% do hook.stopPropagation() %}
```

### Action Button Endpoint

```twig
{# Resources/scripts/api-action-button/action-button.twig #}
{% set ids = hook.request.ids %}

{% set response = services.response.json({
    'actionType': 'notification',
    'payload': {
        'status': 'success',
        'message': 'Processed ' ~ ids|length ~ ' items.'
    }
}) %}

{% do hook.setResponse(response) %}
```
