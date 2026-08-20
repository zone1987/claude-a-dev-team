# sw-customer-detail-base

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| customerEditMode | `any` | `false` | yes |  |
| isLoading | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |

## Examples

### Basic Usage
```twig
<sw-customer-detail-base
    customer="..."
    customerEditMode="..."
>
    <!-- content -->
</sw-customer-detail-base>
```
