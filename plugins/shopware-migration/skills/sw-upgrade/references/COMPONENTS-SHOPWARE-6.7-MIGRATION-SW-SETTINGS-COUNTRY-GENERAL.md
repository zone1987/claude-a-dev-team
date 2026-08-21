# sw-settings-country-general

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| country | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| userConfig | `any` | — | yes |  |
| userConfigValues | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCurrencies` | |
| `openCustomerTaxModal` | |
| `openCompanyTaxModal` | |
| `onToggleCurrencyModal` | |
| `changeBaseItem` | |
| `createDataModal` | |
| `clearMenuOptions` | |
| `addCheckedHamburgerMenu` | |
| `addDisabledBaseCurrencyCheckBox` | |
| `sortCurrencyCheckBox` | |
| `pushDataFromUserConfig` | |
| `calculateInheritedPrice` | |
| `getPriceByCurrency` | |
| `getCurrencyById` | |
| `saveCountryCurrencyDependent` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `countryRepository` | |
| `currencyRepository` | |
| `countryNameError` | |

## Examples

### Basic Usage
```twig
<sw-settings-country-general
    country="..."
    isLoading="..."
    userConfig="..."
>
    <!-- content -->
</sw-settings-country-general>
```
