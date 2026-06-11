# sw-product-stream-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productStreamId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `loadProductTypes` | |
| `createProductStream` | |
| `loadEntityData` | |
| `loadFilters` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `onDuplicate` | |
| `onSave` | |
| `showErrorNotification` | |
| `saveProductStream` | |
| `syncProductStreamFilters` | |
| `onCancel` | |
| `openModalPreview` | |
| `closeModalPreview` | |
| `getProductCustomFields` | |
| `getCustomFieldLabel` | |
| `mapCustomFieldType` | |
| `updateFilterTree` | |
| `getNoPermissionsTooltip` | |
| `normalizeFilterCollection` | |
| `hasProductStatesFilter` | |
| `isDeprecatedProductStatesField` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `productStreamRepository` | |
| `productStreamFiltersRepository` | |
| `customFieldSetRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `isSystemLanguage` | |
| `nameRequired` | |
| `productStreamNameError` | |
| `showCustomFields` | |
| `productStreamIndexingEnabled` | |
| `showProductStatesFilterWarning` | |

## Examples

### Basic Usage
```twig
<sw-product-stream-detail>
    <!-- content -->
</sw-product-stream-detail>
```
