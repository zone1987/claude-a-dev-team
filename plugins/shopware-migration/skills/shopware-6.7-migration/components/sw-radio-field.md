# sw-radio-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| bordered | `any` | `false` | no |  |
| block | `any` | `false` | no |  |
| description | `any` | `null` | no |  |
| options | `any` | — | no |  |
| value | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| `custom-field-${option.value}` | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `currentIndex` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
        <sw-radio-field
            :value="checkBox"
            :name="radioButtonName"
            :options="[{ value: item.enabled }]"
            :disabled="!acl.can('country.editor') || undefined"
            @update:value="onChangeBaseCurrency(item)"
        />
    </template>
    {% endblock %}

    {% block sw_settings_country_currency_dependent_column_actions %}
    <template #actions="{ item }">

        {% block sw_settings_country_currency_dependent_grid_column_action_delete %}
        <sw-context-menu-item
```

### Example 2
Source: `sw-settings-search/component/sw-settings-search-search-behaviour/sw-settings-search-search-behaviour.html.twig`
```twig
<sw-radio-field
    v-model:value="searchBehaviourConfigs.andLogic"
    v-tooltip="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('product_search_config.editor'),
        showOnDisabledElements: true
    }"
    name="sw-field--searchBehaviourConfigs-andLogic"
    class="sw-settings-search__search-behaviour-condition"
    block
    :disabled="!acl.can('product_search_config.editor')"
    :options="conditionsOptions"
/>
{% endblock %}

```

### Example 3
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-modal/sw-settings-product-feature-sets-modal.html.twig`
```twig
    <sw-radio-field
        v-model:value="selectedFeatureType"
        :label="$tc('sw-settings-product-feature-sets.modal.labelTitlePageOne')"
        block
        class="sw-settings-product-feature-sets-modal__options"
        identification="fieldType"
        :options="settingOptions"
        @update:value="onChangeOption"
    />
</template>
{% endblock %}

{% block sw_settings_product_feature_sets_modal_custom_field_list %}
<template v-if="showCustomField">

```

### Example 4
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
    <sw-radio-field
        :disabled="disabled"
        :value="item.visibility"
        :name="'visibility' + item.id"
        :options="[{ value: 30 }]"
        @update:value="changeVisibilityValue($event, item)"
    />
</sw-grid-column>
{% endblock %}

{% block sw_settings_listing_visibility_detail_columns_search_only %}
<sw-grid-column
    :label="$tc('sw-product.visibility.columnSearchOnly')"
    flex="0.7fr"
    align="left"
```

### Example 5
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
            <sw-radio-field
                type="radio"
                :disabled="disabled"
                :value="item.visibility"
                :name="'visibility' + item.id"
                :options="[{ value: 10 }]"
                @update:value="changeVisibilityValue($event, item)"
            />
        </sw-grid-column>
        {% endblock %}
    </template>
    {% endblock %}

    {% block sw_settings_listing_visibility_detail_pagination %}
    <template #pagination>
```
