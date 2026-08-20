# sw-product-modal-delivery

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| configuration-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveDeliveryConfiguration` | |
| `cancelDeliveryConfiguration` | |
| `handleExpandedListing` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-variants/sw-product-detail-variants.html.twig`
```twig
    <sw-product-modal-delivery
        v-if="activeModal === 'deliveryModal'"
        :product="productEntity"
        :selected-groups="configSettingGroups"
        @configuration-close="onConfigurationClosed"
        @modal-close="activeModal = ''"
    />
    {% endblock %}

    {% block sw_product_properties_add_properties_modal %}
    <sw-product-add-properties-modal
        v-if="showAddPropertiesModal"
        :new-properties="newProperties"
        @modal-cancel="onCancelAddPropertiesModal"
        @modal-save="onSaveAddPropertiesModal"
```
