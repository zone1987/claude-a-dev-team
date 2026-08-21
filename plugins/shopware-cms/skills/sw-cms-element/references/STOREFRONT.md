# Shopware 6 — CMS element (storefront)

The element is rendered in the storefront through a Twig template, path
`src/Resources/views/storefront/element/cms-element-ff-teaser.html.twig`.

```twig
{% block element_ff_teaser %}
<div class="cms-element-ff-teaser">
    {% set product = element.data.product %}
    {% if product %}
        <a href="{{ seoUrl('frontend.detail.page', { productId: product.id }) }}">{{ product.translated.name }}</a>
    {% endif %}
</div>
{% endblock %}
```

`element.data` = the DataResolver's result (`sw-cms-data-resolver`), `element.config` = the configuration. The template
is found automatically by the element name. Styling via storefront SCSS (`shopware-storefront`).
