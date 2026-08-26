# Shopware 6 — Storefront templates

Templates live in `src/Resources/views/storefront/...` and mirror the core paths. With `sw_extends` you inherit
the original and override only the block you need.

```twig
{% sw_extends '@Storefront/storefront/page/product-detail/index.html.twig' %}

{% block page_product_detail_buy_container %}
    {{ parent() }}
    <div class="ff-hint">{{ "ff.hint"|trans }}</div>
{% endblock %}
```

Use `{% sw_extends %}` instead of Twig's `extends` (multiple inheritance across plugins). `{{ parent() }}` keeps the core content.
Reuse the block names from the original. Header/footer via their respective blocks. Custom functions: `sw-twig-functions`.

To find **which** template and block to override, call the Skill tool with "sw-structure": it
carries every block with its nesting, the inheritance chains and the CSS class to block map.
