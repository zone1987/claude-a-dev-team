# sw-settings-currency-country-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currencyCountryRounding | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| result-label-property | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| edit-cancel | — | |
| save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCancel` | |
| `onSave` | |
| `shouldDisableCountry` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `countryCriteria` | |
| `countryRepository` | |
| `assignedCountriesCriteria` | |
| `currencyCountryRoundingCountryIdError` | |

## Examples

### Example 1
Source: `sw-settings-currency/page/sw-settings-currency-detail/sw-settings-currency-detail.html.twig`
```twig
                <sw-settings-currency-country-modal
                    v-if="currentCurrencyCountry"
                    :currency-country-rounding="currentCurrencyCountry"
                    @save="onSaveCurrencyCountry"
                    @edit-cancel="onCancelEditCountry"
                />
                {% endblock %}
                {% endblock %}

                {% block sw_settings_currency_detail_custom_field_sets %}
                <mt-card
                    v-if="showCustomFields"
                    position-identifier="sw-settings-currency-detail-custom-field-sets"
                    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                    :is-loading="isLoading"
```
