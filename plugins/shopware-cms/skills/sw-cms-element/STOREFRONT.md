# Shopware 6 — CMS-Element (Storefront)

Das Element wird im Storefront über ein Twig-Template gerendert, Pfad
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

`element.data` = Ergebnis des DataResolvers (`sw-cms-data-resolver`), `element.config` = Konfiguration. Template wird
über den Element-Namen automatisch gefunden. Styling über Storefront-SCSS (`shopware-storefront`).
