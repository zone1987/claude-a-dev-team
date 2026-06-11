# sw-container

> Flexible layout container with configurable columns and gap.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| columns | `any` | `''` | no |  |
| rows | `any` | `''` | no |  |
| gap | `any` | `''` | no |  |
| justify | `any` | `'stretch'` | no | Valid: `start`, `end`, `center`, `stretch`, `left`, `right` |
| align | `any` | `'stretch'` | no | Valid: `start`, `end`, `center`, `stretch` |
| breakpoints | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `registerResizeListener` | |
| `updateCssGrid` | |
| `buildCssGrid` | |
| `cssGridDefaults` | |
| `buildCssGridProps` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<sw-container class="sw-settings-country-address-handling__options-container">

    <mt-switch
        :model-value="country.forceStateInRegistration"
        class="sw-settings-country-address-handling__option-items"
        bordered
        :disabled="!acl.can('country.editor') || undefined"
        :label="$tc('sw-settings-country.detail.labelForceStateInRegistration')"
        @update:model-value="updateCountry('forceStateInRegistration', $event)"
    />

    <mt-switch
        :model-value="country.postalCodeRequired"
        class="sw-settings-country-address-handling__option-items"
        bordered
```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<sw-container class="sw-settings-country-address-handling__options-container">
    <div class="sw-settings-country-address-handling__address-markup">
        <sw-multi-snippet-drag-and-drop
            v-for="(snippet, index) in addressFormat"
            :key="index"
            v-droppable="{ data: { snippet, index }, dragGroup: 'sw-multi-snippet' }"
            v-draggable="{ ...dragConf, data: { snippet, index }}"
            :value="snippet"
            :line-position="index"
            :get-label-property="getLabelProperty"
            :total-lines="addressFormat.length"
            @update:value="change"
            @drop-end="onDropEnd"
            @position-move="moveToNewPosition"
            @add-new-line="addNewLineAt"
```

### Example 3
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<sw-container
    columns="repeat(auto-fit, minmax(250px, 1fr))"
    gap="0px 30px"
>

    <!-- eslint-disable sw-deprecation-rules/no-twigjs-blocks, vue/attributes-order -->
    {% block sw_settings_country_general_content_field_name %}

    <mt-text-field
        v-model="country.name"
        name="sw-field--country-name"
        required
        :disabled="!acl.can('country.editor') || undefined"
        :label="$tc('sw-settings-country.detail.labelName')"
        :placeholder="placeholder(country, 'name', $tc('sw-settings-country.detail.placeholderName'))"
```

### Example 4
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<sw-container class="sw-settings-country-general__options-container">

    {% block sw_settings_country_general_content_field_active %}

    <mt-switch
        v-model="country.active"
        name="sw-field--country-active"
        class="sw-settings-country-general__option-items"
        bordered
        :disabled="!acl.can('country.editor') || undefined"
        :label="$tc('sw-settings-country.detail.labelActive')"
    />
    {% endblock %}

    {% block sw_settings_country_general_content_field_shipping_available %}
```

### Example 5
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
<sw-container
    columns="1fr 32px minmax(100px, 200px)"
    gap="0 10px"
>

    {% block sw_attribute_list_toolbar_searchfield %}
    <sw-simple-search-field
        v-model:value="term"
        size="small"
        variant="form"
        @search-term-change="onSearchCountryState"
    />
    {% endblock %}

    {% block sw_settings_country_state_list_toolbar_delete %}
```
