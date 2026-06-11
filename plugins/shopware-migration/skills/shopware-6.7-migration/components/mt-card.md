# mt-card

> Card container for grouping related content with optional title, subtitle, hero, and toolbar.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `string` | — | no | |
| subtitle | `string` | — | no | |
| isLoading | `boolean` | — | no | |
| large | `boolean` | — | no | |
| inheritance | `boolean` | — | no | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| title | — | |
| subtitle | — | |
| avatar | — | |
| grid | — | |
| footer | — | |
| default | — | |
| toolbar | — | |
| tabs | — | |
| headerRight | — | |
| before-card | — | |
| context-actions | — | |
| after-card | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:inheritance | value: boolean | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<mt-card
    v-if="isLoading || country"
    position-identifier="sw-settings-country-list"
>
    {% block sw_settings_country_list_grid %}
    <template #grid>
        {% block sw_settings_country_list_grid_inner %}
        <sw-entity-listing
            ref="swSettingsCountryGrid"
            class="sw-settings-country-list-grid"
            :data-source="country"
            :columns="getCountryColumns()"
            :repository="countryRepository"
            :full-page="false"
            detail-route="sw.settings.country.detail"
```

### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<mt-card
    v-if="showCustomFields"
    position-identifier="sw-settings-country-detail-custom-field-sets"
    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
    :is-loading="isLoading"
>
    <sw-custom-field-set-renderer
        :entity="country"
        :disabled="!acl.can('country.editor')"
        :sets="customFieldSets"
    />
</mt-card>
```

### Example 3
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<mt-card
    position-identifier="sw-settings-country-address-handling-options"
    :title="$tc('sw-settings-country.detail.titleOptions')"
    :is-loading="isLoading"
>
    <sw-container class="sw-settings-country-address-handling__options-container">

        <mt-switch
            :model-value="country.forceStateInRegistration"
            class="sw-settings-country-address-handling__option-items"
            bordered
            :disabled="!acl.can('country.editor') || undefined"
            :label="$tc('sw-settings-country.detail.labelForceStateInRegistration')"
            @update:model-value="updateCountry('forceStateInRegistration', $event)"
        />
```

### Example 4
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<mt-card
    position-identifier="sw-settings-country-address-handling-formatting"
    :title="$tc('sw-settings-country.detail.titleFormatting')"
    :is-loading="isLoading"
>
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
```

### Example 5
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-card
    position-identifier="sw-settings-country-detail-general"
    :title="$tc('sw-settings-country.detail.titleCard')"
    :is-loading="isLoading"
>
    <sw-container
        columns="repeat(auto-fit, minmax(250px, 1fr))"
        gap="0px 30px"
    >

        <!-- eslint-disable sw-deprecation-rules/no-twigjs-blocks, vue/attributes-order -->
        {% block sw_settings_country_general_content_field_name %}

        <mt-text-field
            v-model="country.name"
```
