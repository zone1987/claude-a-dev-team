# sw-settings-tax-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `onSave` | |
| `onCancel` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `changeName` | |
| `reloadDefaultTaxRate` | |
| `onChangeDefaultTaxRate` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `taxRepository` | |
| `taxNameError` | |
| `taxTaxRateError` | |
| `isNewTax` | |
| `allowSave` | |
| `tooltipSave` | |
| `isShopwareDefaultTax` | |
| `label` | |
| `showCustomFields` | |
| `isDefaultTaxRate` | |

## Examples

### Basic Usage
```twig
<sw-settings-tax-detail>
    <!-- content -->
</sw-settings-tax-detail>
```
