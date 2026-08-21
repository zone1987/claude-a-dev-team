# sw-category-detail-products

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadProductStreamPreview` | |
| `onPaginateManualProductAssignment` | |
| `getParentProducts` | |
| `getItemName` | |
| `getManufacturer` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `category` | |
| `productStreamRepository` | |
| `productRepository` | |
| `productColumns` | |
| `manufacturerColumn` | |
| `nameColumn` | |
| `productCriteria` | |
| `productStreamCriteria` | |
| `productStreamInvalidError` | |
| `categoryProductStreamIdError` | |
| `categoryProductAssignmentTypeError` | |
| `productAssignmentTypes` | |
| `dynamicProductGroupHelpText` | |
| `assetFilter` | |

## Examples

### Basic Usage
```twig
<sw-category-detail-products
    isLoading="..."
>
    <!-- content -->
</sw-category-detail-products>
```
