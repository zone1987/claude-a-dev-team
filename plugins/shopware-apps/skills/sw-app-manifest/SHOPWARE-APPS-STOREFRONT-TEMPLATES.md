---
title: Storefront Templates
impact: MEDIUM
impactDescription: Apps can customize the storefront via Twig templates, JS, and SCSS
tags: storefront, templates, twig, javascript, scss, views
---

## Storefront Templates

Apps modify the storefront through Twig templates, JavaScript, and SCSS placed in the app's `Resources` directory.

### Directory Structure

```
Resources/
├── views/
│   └── storefront/
│       └── page/
│           └── product-detail/
│               └── index.html.twig
├── app/
│   └── storefront/
│       └── src/
│           ├── scss/
│           │   └── base.scss
│           └── main.js
└── public/
    └── ... (fonts, images, etc.)
```

### Template Override Example

```twig
{# Resources/views/storefront/page/product-detail/index.html.twig #}
{% sw_extends '@Storefront/storefront/page/product-detail/index.html.twig' %}

{% block page_product_detail_content %}
    {{ parent() }}
    <div class="my-app-extra-content">
        <p>Additional content from my app</p>
    </div>
{% endblock %}
```

### Custom Assets (since 6.4.8.0)

Place static files in `Resources/public/`. They are accessible through Shopware's asset system.

### Template Load Priority (since 6.4.12.0)

Control template loading order via manifest.xml:

```xml
<storefront>
    <template-load-priority>100</template-load-priority>
</storefront>
```

- Default: `0`
- Positive: loads earlier (higher priority)
- Negative: loads later (lower priority)
