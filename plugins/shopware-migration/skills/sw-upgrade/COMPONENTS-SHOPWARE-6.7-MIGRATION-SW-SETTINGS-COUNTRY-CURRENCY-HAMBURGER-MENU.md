# sw-settings-country-currency-hamburger-menu

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |
| options | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| currency-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onCheckCurrency` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
    <sw-settings-country-currency-hamburger-menu
        :options="menuOptions"
        @currency-change="changeCurrencyDependentRow"
    />
</template>
{% endblock %}

{% block  sw_settings_country_currency_dependent_modal_content_currency_name %}
<template #column-currencyId="{ item }">
    <div class="sw-settings-country-currency-dependent-modal__inheritance-wrapper">
        <!-- eslint-disable-next-line vuejs-accessibility/label-has-for -->
        <label>{{ getCurrencyNameById(item.currencyId) }}</label>
    </div>
</template>
{% endblock %}
```
