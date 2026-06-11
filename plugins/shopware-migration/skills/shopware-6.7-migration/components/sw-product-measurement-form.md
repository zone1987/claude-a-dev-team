# sw-product-measurement-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `onUpdateLengthUnit` | |
| `convertWidth` | |
| `convertHeight` | |
| `convertLength` | |
| `onUpdateWeightUnit` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `lengthUnit` | |
| `weightUnit` | |
| `productWidthError` | |
| `productHeightError` | |
| `productLengthError` | |
| `productWeightError` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-specifications/sw-product-detail-specifications.html.twig`
```twig
    <sw-product-measurement-form
        :allow-edit="acl.can('product.editor')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_product_detail_specifications_measures_packaging %}
<mt-card
    v-if="showProductCard('selling_packaging') && !isDigitalProduct"
    class="sw-product-detail-specification__selling-packaging"
    position-identifier="sw-product-detail-specifications-measures-packaging"
    :title="$tc('sw-product.specifications.cardTitleSellingPackaging')"
>
    {% block sw_product_detail_specifications_measures_packaging_content %}
```
