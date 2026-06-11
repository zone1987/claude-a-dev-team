# sw-settings-country-currency-dependent-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currencyDependsValue | `any` | — | yes |  |
| countryId | `any` | — | yes |  |
| userConfig | `any` | — | yes |  |
| userConfigValues | `any` | — | yes |  |
| menuOptions | `any` | — | yes |  |
| taxFreeType | `any` | `''` | no |  |
| isLoading | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| modal-save | — | |
| base-item-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `saveModal` | |
| `changeCurrencyDependentRow` | |
| `addCurrencyDependentRow` | |
| `removeCurrencyDependentRow` | |
| `updateCheckBoxHamburgerMenu` | |
| `onChangeBaseCurrency` | |
| `calculateInheritedPrice` | |
| `reCalculatorInherited` | |
| `getPriceByCurrency` | |
| `createUserConfigValue` | |
| `createNewUserConfig` | |
| `updateExistedValue` | |
| `getCurrencyNameById` | |
| `getCurrencyById` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentUserId` | |
| `currencyTaxFreeDependentRepository` | |
| `radioButtonName` | |
| `countryCurrencyColumns` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<sw-settings-country-currency-dependent-modal
    v-if="showCurrencyModal"
    :currency-depends-value="currencyDependsValue"
    :country-id="countryId"
    :is-loading="isLoading"
    :menu-options="menuOptions"
    :user-config="userConfig"
    :user-config-values="userConfigValues"
    :tax-free-type="taxFreeType"
    @modal-close="onToggleCurrencyModal"
    @modal-save="saveCountryCurrencyDependent"
    @base-item-change="changeBaseItem"
/>
{% endblock %}

```
