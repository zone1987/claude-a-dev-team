# Shopware 6 — Admin-Komponente überschreiben

`Shopware.Component.override(name, config)` erweitert eine bestehende Komponente; mehrere Overrides stapeln sich.

```js
import template from './sw-product-detail-override.html.twig';
Shopware.Component.override('sw-product-detail', {
    template,
    methods: {
        onSave() { this.$super('onSave'); /* zusätzliches Verhalten */ },
    },
});
```
```twig
{% block sw_product_detail_content %}
    {% parent %}
    <ff-extra-panel :product="product"/>
{% endblock %}
```

`this.$super('methode', ...args)` ruft die Original-Methode. Im Template `{% parent %}` für den Originalinhalt,
Block-Namen aus der Core-Komponente. Eigene neue Komponente stattdessen: `sw-admin-component`.
