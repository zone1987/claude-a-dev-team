# sw-settings-price-rounding

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemRounding | `any` | — | no |  |
| totalRounding | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onChangeDecimals` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `itemIntervalDisabled` | |
| `totalIntervalDisabled` | |
| `showHeaderInfo` | |
| `showHeaderWarning` | |

## Examples

### Example 1
Source: `sw-settings-currency/page/sw-settings-currency-detail/sw-settings-currency-detail.html.twig`
```twig
    <sw-settings-price-rounding
        :item-rounding="currency.itemRounding"
        :total-rounding="currency.totalRounding"
    />
</mt-card>
{% endblock %}

{% block sw_settings_currency_detail_content_card_country_price_rounding %}
<mt-card
    position-identifier="sw-settings-currency-detail-country-price-rounding"
    :title="$tc('sw-settings-currency.detail.titleCountryRoundingCard')"
    :is-loading="currencyCountryLoading"
>
    <template
        v-if="currency.id && !currency.isNew()"
```

### Example 2
Source: `sw-settings-currency/component/sw-settings-currency-country-modal/sw-settings-currency-country-modal.html.twig`
```twig
<sw-settings-price-rounding
    :item-rounding="currencyCountryRounding.itemRounding"
    :total-rounding="currencyCountryRounding.totalRounding"
/>
{% endblock %}

{% block sw_settings_currency_country_modal_footer %}
<template #modal-footer>
    {% block sw_settings_currency_country_modal_footer_cancel %}
    <mt-button
        size="small"
        variant="secondary"
        @click="onCancel"
    >
        {{ $tc('global.default.cancel') }}
```
