# sw-product-variants-delivery-media

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `onUploadsAdded` | |
| `successfulUpload` | |
| `removeMedia` | |
| `setMedia` | |
| `onChangeGroupListing` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `selectedGroupsSorted` | |
| `optionColumns` | |
| `activeOptions` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-delivery/sw-product-modal-delivery.html.twig`
```twig
    <sw-product-variants-delivery-media
        v-if="activeTab == 'media'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}

    {% block sw_product_modal_delivery_listing %}
    <sw-product-variants-delivery-listing
        v-if="activeTab == 'listing'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}
</div>
```
