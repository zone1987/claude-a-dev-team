# sw-settings-currency-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currencyId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCurrencyCountryRoundings` | |
| `loadCustomFieldSets` | |
| `saveFinish` | |
| `onSave` | |
| `onCancel` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `onChangeCountrySearch` | |
| `onAddCountry` | |
| `onCancelEditCountry` | |
| `onClickEdit` | |
| `onSaveCurrencyCountry` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `currencyRepository` | |
| `currencyCountryRoundingRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `currencyNameError` | |
| `currencyIsoCodeError` | |
| `currencyShortNameError` | |
| `currencySymbolError` | |
| `currencyIsDefaultError` | |
| `currencyDecimalPrecisionError` | |
| `currencyFactorError` | |
| `currencyCountryColumns` | |
| `currencyCountryRoundingCriteria` | |
| `emptyStateText` | |
| `showCustomFields` | |

## Examples

### Basic Usage
```twig
<sw-settings-currency-detail>
    <!-- content -->
</sw-settings-currency-detail>
```
