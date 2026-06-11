# sw-product-variants-configurator-restrictions

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
| `getOptionsForGroupId` | |
| `getRestrictionsWithNaming` | |
| `filterEmptyValues` | |
| `addEmptyRestrictionCombination` | |
| `addEmptyRestriction` | |
| `cancelAddRestriction` | |
| `saveAddRestriction` | |
| `editRestrictionCombination` | |
| `deleteRestrictionCombination` | |
| `deleteRestriction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `restrictionColumns` | |
| `actualRestrictionValueLength` | |
| `filteredRestrictions` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
    <sw-product-variants-configurator-restrictions
        v-if="activeTab == 'restrictions'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_product_modal_variant_generation_footer %}
<template #modal-footer>
    {% block sw_product_modal_variant_generation_footer_cancel %}
    <mt-button
        size="small"
        variant="secondary"
```
