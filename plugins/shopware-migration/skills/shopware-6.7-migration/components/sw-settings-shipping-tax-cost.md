# sw-settings-shipping-tax-cost

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `getTaxLabel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `shippingMethod` | |
| `currencies` | |
| `defaultCurrency` | |
| `usedRules` | |
| `unrestrictedPriceMatrixExists` | |
| `newPriceMatrixExists` | |
| `shippingMethodTaxTypeError` | |
| `shippingMethodTaxIdError` | |
| `shippingCostTaxOptions` | |
| `taxCriteria` | |
| `taxType` | |

## Examples

### Example 1
Source: `sw-settings-shipping/page/sw-settings-shipping-detail/sw-settings-shipping-detail.html.twig`
```twig
<sw-settings-shipping-tax-cost
    v-if="!isLoading"
    :disabled="!acl.can('shipping.editor') || undefined"
/>
{% endblock %}
<sw-skeleton v-else />

{% block sw_settings_shipping_detail_price_matrices %}
<sw-settings-shipping-price-matrices
    v-if="!isLoading"
    ref="priceMatrices"
    :disabled="!acl.can('shipping.editor') || undefined"
/>
{% endblock %}
<sw-skeleton v-else />
```
