# sw-order-saveable-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | yes |  |
| type | `any` | `'text'` | yes |  |
| placeholder | `any` | `null` | no |  |
| editable | `any` | `true` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| value-change | — | |
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onClick` | |
| `onSaveButtonClicked` | |
| `onCancelButtonClicked` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `component` | |
| `valuePropName` | |
| `computedAttrs` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
<sw-order-saveable-field
    v-tooltip="{
        showDelay: 300,
        message: shippingCostsDetail,
        disabled: taxStatus === 'tax-free'
    }"
    type="number"
    editable
    :value="cartDelivery.shippingCosts.totalPrice"
    @value-change="onShippingChargeEdited"
    @update:value="onShippingChargeUpdated"
>
    {{ currencyFilter(cartDelivery.shippingCosts.totalPrice, currency.isoCode, currency.totalRounding.decimals) }}
</sw-order-saveable-field>
```

### Example 2
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-saveable-field
    v-tooltip="{
        showDelay: 300,
        message: shippingCostsDetail,
        disabled: taxStatus === 'tax-free'
    }"
    type="number"
    editable
    :value="cartDelivery.shippingCosts.totalPrice"
    @value-change="onShippingChargeEdited"
    @update:value="onShippingChargeUpdated"
>
    {{ currencyFilter(cartDelivery.shippingCosts.totalPrice, currency.isoCode) }}
</sw-order-saveable-field>
```

### Example 3
Source: `sw-order/view/sw-order-detail-general/sw-order-detail-general.html.twig`
```twig
<sw-order-saveable-field
    ref="editShippingCosts"
    v-tooltip="{
        showDelay: 300,
        message: shippingCostsDetail,
        disabled: taxStatus === 'tax-free'
    }"
    type="number"
    :editable="acl.can('order.editor')"
    :step="1"
    :min="0"
    :value="delivery.shippingCosts.totalPrice"
    @value-change="onShippingChargeEdited"
    @update:value="onShippingChargeUpdated"
>
```
