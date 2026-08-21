# Shopware 6 — Overriding an admin component

`Shopware.Component.override(name, config)` extends an existing component; multiple overrides stack.

```js
import template from './sw-product-detail-override.html.twig';
Shopware.Component.override('sw-product-detail', {
    template,
    methods: {
        onSave() { this.$super('onSave'); /* additional behaviour */ },
    },
});
```
```twig
{% block sw_product_detail_content %}
    {% parent %}
    <ff-extra-panel :product="product"/>
{% endblock %}
```

`this.$super('method', ...args)` calls the original method. In the template use `{% parent %}` for the original content,
with block names taken from the core component. To create a new component of your own instead: `sw-admin-component`.
