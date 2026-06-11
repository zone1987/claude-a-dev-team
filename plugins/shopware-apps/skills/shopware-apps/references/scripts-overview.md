---
title: App Scripts Overview
impact: MEDIUM
impactDescription: App scripts extend Shopware behavior without an external app server
tags: scripts, twig, hooks, app-scripts, sandbox
---

## App Scripts Overview

App scripts are Twig-based scripts that run inside Shopware's sandboxed environment. They allow apps to extend cart behavior, load data, create custom endpoints, and define rule conditions — all without requiring an external app server.

### Directory Structure

Scripts are placed in `Resources/scripts/{hook-name}/`:

```
Resources/
└── scripts/
    ├── cart/                       (cart manipulation)
    │   └── my-cart-script.twig
    ├── product-page-loaded/        (storefront data loading)
    │   └── load-extra-data.twig
    ├── api-my-endpoint/            (Admin API endpoint)
    │   └── my-endpoint-script.twig
    ├── store-api-my-endpoint/      (Store API endpoint)
    │   └── my-endpoint-script.twig
    ├── storefront-my-page/         (Storefront endpoint)
    │   └── my-page-script.twig
    ├── rule-conditions/            (rule builder conditions)
    │   └── my-condition.twig
    └── include/                    (shared macros)
        └── helpers.twig
```

### Twig Syntax Extensions

App scripts support extended Twig syntax beyond standard Twig:

```twig
{# Strict equality #}
{% if value === 'exact' %}{% endif %}
{% if value !== 'other' %}{% endif %}

{# foreach with break #}
{% foreach items as item %}
    {% if item.found %}
        {% break %}
    {% endif %}
{% endforeach %}

{# Type checking #}
{% if value is string %}{% endif %}
{% if value is number %}{% endif %}

{# Type casting #}
{% set num = intval(value) %}
{% set str = strval(value) %}
{% set bool = boolval(value) %}
{% set float = floatval(value) %}

{# Logical operators #}
{% if condA && condB %}{% endif %}

{# Return from macros #}
{% macro calculate(x) %}
    {% return x * 2 %}
{% endmacro %}
```

### Available Services

Access via the `services` variable:

| Service | Purpose |
|---------|---------|
| `services.repository` | DAL repository access (search, ids, aggregate) |
| `services.store` | Storefront-optimized data loading |
| `services.config` | App/system configuration access |
| `services.cart` | Cart manipulation (only in cart hook) |
| `services.cart.price` | Price object creation |
| `services.response` | Response creation (JSON, HTML, redirect) |

### IDE Support

```twig
{# @var services \Shopware\Core\Framework\Script\ServiceStubs #}
```

### Translation

```twig
{{ 'my-app.snippet-key'|trans }}
{{ 'my-app.greeting'|trans({'%name%': customer.firstName}) }}
```

### Shared Macros

Place shared code in `Resources/scripts/include/`:

```twig
{# Resources/scripts/include/helpers.twig #}
{% macro calculateDiscount(price, percent) %}
    {% return price * (percent / 100) %}
{% endmacro %}
```

Usage in scripts:

```twig
{% import "include/helpers.twig" as helpers %}
{% set discount = helpers.calculateDiscount(100, 10) %}
```
