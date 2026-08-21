# sw-product-packaging-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | — | yes |  |
| showSettingPackaging | `any` | — | yes |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `isLoading` | |
| `productPurchaseUnitError` | |
| `productReferenceUnitError` | |
| `productPackUnitError` | |
| `productPackUnitPluralError` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-specifications/sw-product-detail-specifications.html.twig`
```twig
    <sw-product-packaging-form
        :show-setting-packaging="showModeSetting"
        :allow-edit="acl.can('product.editor')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_product_detail_specifications_property %}
<sw-product-properties
    v-show="showProductCard('properties')"
/>
{% endblock %}

{% block sw_product_detail_specifications_essential_characteristics %}
```
