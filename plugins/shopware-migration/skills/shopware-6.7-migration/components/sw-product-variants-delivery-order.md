# sw-product-variants-delivery-order

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `createOrderObjects` | |
| `getOptionsForGroup` | |
| `orderChanged` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-delivery/sw-product-modal-delivery.html.twig`
```twig
    <sw-product-variants-delivery-order
        v-if="activeTab == 'order'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}

    {% block sw_product_modal_delivery_media %}
    <sw-product-variants-delivery-media
        v-if="activeTab == 'media'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}

```
