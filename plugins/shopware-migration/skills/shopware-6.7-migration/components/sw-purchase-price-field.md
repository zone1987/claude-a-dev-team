# sw-purchase-price-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| price | `any` | — | yes |  |
| compact | `any` | `false` | no |  |
| taxRate | `any` | — | yes |  |
| error | `any` | `null` | no |  |
| label | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |
| currency | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `purchasePriceChanged` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `purchasePrice` | |

## Examples

### Basic Usage
```twig
<sw-purchase-price-field
    price="..."
    taxRate="..."
>
    <!-- content -->
</sw-purchase-price-field>
```
