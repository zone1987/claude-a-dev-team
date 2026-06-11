# sw-settings-shipping-price-matrices

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onAddNewPriceGroup` | |
| `onDeletePriceMatrix` | |
| `onDuplicatePriceMatrix` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `shippingMethod` | |
| `shippingPriceGroups` | |
| `usedRules` | |
| `unrestrictedPriceMatrixExists` | |
| `newPriceMatrixExists` | |
| `ruleRepository` | |
| `ruleFilter` | |
| `shippingPriceRepository` | |
| `isLoaded` | |

## Examples

### Example 1
Source: `sw-settings-shipping/page/sw-settings-shipping-detail/sw-settings-shipping-detail.html.twig`
```twig
            <sw-settings-shipping-price-matrices
                v-if="!isLoading"
                ref="priceMatrices"
                :disabled="!acl.can('shipping.editor') || undefined"
            />
            {% endblock %}
            <sw-skeleton v-else />

            {% block sw_settings_shipping_detail_custom_field_sets %}
            <mt-card
                v-if="showCustomFields"
                position-identifier="sw-settings-shipping-detail-custom-fields"
                :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                :is-loading="isLoading"
            >
```
