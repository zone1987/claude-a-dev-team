# sw-order-delivery-metadata

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| delivery | `any` | — | yes |  |
| order | `any` | — | yes |  |
| title | `any` | `null` | no |  |
| isLoading | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `renderFormattingAddress` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currencyFilter` | |
| `dateFilter` | |

## Examples

### Basic Usage
```twig
<sw-order-delivery-metadata
    delivery="..."
    order="..."
>
    <!-- content -->
</sw-order-delivery-metadata>
```
