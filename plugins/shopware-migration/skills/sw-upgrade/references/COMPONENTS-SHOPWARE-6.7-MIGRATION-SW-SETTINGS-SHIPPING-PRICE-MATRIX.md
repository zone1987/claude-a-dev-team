# sw-settings-shipping-price-matrix

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| priceGroup | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| duplicate-price-matrix | — | |
| delete-price-matrix | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onAddNewShippingPrice` | |
| `onSaveMainRule` | |
| `onSaveCustomShippingRule` | |
| `onCalculationChange` | |
| `onDeletePriceMatrix` | |
| `onConfirmDeleteShippingPrice` | |
| `onCloseDeleteModal` | |
| `onDeleteShippingPrice` | |
| `convertDefaultPriceToCurrencyPrice` | |
| `initCurrencyPrice` | |
| `getPrice` | |
| `setPrice` | |
| `getPriceOfCurrency` | |
| `convertPrice` | |
| `onQuantityEndChange` | |
| `updateShowAllPrices` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `shippingMethod` | |
| `currencies` | |
| `restrictedRuleIds` | |
| `unrestrictedPriceMatrixExists` | |
| `newPriceMatrixExists` | |
| `defaultCurrency` | |
| `ruleRepository` | |
| `shippingPriceRepository` | |
| `labelQuantityStart` | |
| `labelQuantityEnd` | |
| `numberFieldType` | |
| `confirmDeleteText` | |
| `currencyColumns` | |
| `showDataGrid` | |
| `disableDeleteButton` | |
| `ruleFilterCriteria` | |
| `shippingRuleFilterCriteria` | |
| `isRuleMatrix` | |
| `usedCalculationRules` | |
| `mainRulePlaceholder` | |
| `cardTitle` | |
| `prices` | |

## Examples

### Example 1
Source: `sw-settings-shipping/component/sw-settings-shipping-price-matrices/sw-settings-shipping-price-matrices.html.twig`
```twig
<sw-settings-shipping-price-matrix
    v-for="priceGroup in shippingPriceGroups"
    :key="priceGroup.ruleId"
    :price-group="priceGroup"
    :disabled="disabled || undefined"
    @duplicate-price-matrix="onDuplicatePriceMatrix"
    @delete-price-matrix="onDeletePriceMatrix"
/>
{% endblock %}

{% block sw_settings_shipping_detail_advanced_prices_actions %}
<div class="sw-settings-shipping-price-matrices__actions">
    {% block sw_settings_shipping_detail_advanced_prices_actions_add_button %}
    <mt-button
        v-tooltip="{
```
