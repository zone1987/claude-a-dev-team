# sw-customer-detail-order

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChange` | |
| `getOrderColumns` | |
| `refreshList` | |
| `navigateToCreateOrder` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `orderColumns` | |
| `orderRepository` | |
| `emptyTitle` | |
| `currencyFilter` | |
| `assetFilter` | |

## Examples

### Basic Usage
```twig
<sw-customer-detail-order
    customer="..."
>
    <!-- content -->
</sw-customer-detail-order>
```
