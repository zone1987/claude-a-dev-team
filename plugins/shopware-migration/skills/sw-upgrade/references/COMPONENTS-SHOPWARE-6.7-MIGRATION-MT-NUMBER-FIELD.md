# mt-number-field

> Number input with step, min/max, digits control, and increase/decrease buttons.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| update:modelValue | — | |
| change | — | |
| input-change | — | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-number-field
    v-model="country.position"
    name="sw-field--country-position"
    number-type="int"
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelPosition')"
    :placeholder="placeholder(country, 'position', $tc('sw-settings-country.detail.placeholderPosition'))"
/>
{% endblock %}

{% block sw_settings_country_general_content_field_iso %}

<mt-text-field
    v-model="country.iso"
    name="sw-field--country-iso"
```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-number-field
    v-model="country.customerTax.amount"
    name="sw-field--country-customerTax-amount"
    class="sw-settings-country-general__input-amount customer-tax-amount"
    :min="0"
    :label="$tc('sw-settings-country.detail.taxFreeFrom')"
    :help-text="$tc('sw-settings-country.detail.taxFreeFromHelpText')"
    :disabled="!acl.can('country.editor') || undefined"
>
    <template #suffix>
        <sw-entity-single-select
            v-model:value="country.customerTax.currencyId"
            name="sw-field--country-customerTax-currencyId"
            class="sw-settings-country-general__customer-select-currency sw-settings-country-general__select"
            entity="currency"
```

### Example 3
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
    <mt-number-field
        v-model="item.amount"
        class="sw-settings-country-currency-dependent-modal__input"
        :min="0"
        :disabled="(!item.enabled || !acl.can('country.editor')) || undefined"
        @update:model-value="reCalculatorInherited(item)"
    />
</template>
{% endblock %}

{% block sw_settings_country_currency_dependent_grid_column_is_base_currency %}
<template #column-enabled="{ item }">
    <sw-radio-field
        :value="checkBox"
        :name="radioButtonName"
```

### Example 4
Source: `sw-settings-country/component/sw-country-state-detail/sw-country-state-detail.html.twig`
```twig
    <mt-number-field
        v-model="countryState.position"
        name="sw-field--countryState-position"
        :disabled="!acl.can('country.editor') || undefined"
        :tooltip-text="$tc('sw-country-state-detail.tooltipPosition')"
        number-type="int"
        :label="$tc('sw-country-state-detail.labelPosition')"
    />
    {% endblock %}
</sw-container>

{% block sw_country_state_detail_modal_footer %}
<template #modal-footer>
    {% block sw_country_state_detail_modal_footer_cancel %}
    <mt-button
```

### Example 5
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
        <mt-number-field
            v-model="item.ranking"
            number-type="int"
            size="small"
        />
        {% endblock %}
    </template>
</template>
{% endblock %}

{% block sw_settings_search_searchable_content_general_searchable %}
<template #column-searchable="{ item, isInlineEdit }">
    <template v-if="isInlineEdit">
        {% block sw_settings_search_searchable_content_general_searchable_editor %}
        <mt-checkbox
```
