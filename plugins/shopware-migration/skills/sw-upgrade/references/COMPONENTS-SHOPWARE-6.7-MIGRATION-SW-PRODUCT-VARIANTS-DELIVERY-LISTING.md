# sw-product-variants-delivery-listing

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-item | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateListingMode` | |
| `updateVariantMode` | |
| `updateMainVariant` | |
| `isActiveGroupInListing` | |
| `onChangeGroupListing` | |
| `isActiveListingMode` | |
| `isDisabledListingMode` | |
| `isSelected` | |
| `onSearchTermChange` | |
| `onSelectCollapsed` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `listingModeOptions` | |
| `listingMode` | |
| `mainVariantModeOptions` | |
| `mainVariant` | |
| `variantCriteria` | |
| `context` | |
| `selectedGroupsSorted` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-delivery/sw-product-modal-delivery.html.twig`
```twig
    <sw-product-variants-delivery-listing
        v-if="activeTab == 'listing'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_product_modal_delivery_footer %}
<template #modal-footer>
    {% block sw_product_modal_delivery_footer_button_cancel %}
    <mt-button
        size="small"
        variant="secondary"
```
