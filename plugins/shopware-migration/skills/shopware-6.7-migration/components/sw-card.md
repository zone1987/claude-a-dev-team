# sw-card

> **Migration wrapper** — Delegates to `mt-card` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-card](mt-card.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| deprecated | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_country_list_content_card %}
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
```

### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_country_detail_content_language_info %}
    <sw-language-info
        :entity-description="placeholder(country, 'name', $tc('sw-settings-country.detail.textHeadline'))"
    />
    {% endblock %}

    {% block sw_settings_country_tabs_header %}
    <sw-tabs position-identifier="sw-settings-country-detail-header">
        {% block sw_setting_country_tabs_setting %}
        <sw-tabs-item
            v-bind="$props"
            class="sw-settings-country__setting-tab"
            :route="{ name: isNewCountry ? 'sw.settings.country.create.general' : 'sw.settings.country.detail.general' }"
        >
```

### Example 3
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_search_tabs_header %}
    <sw-tabs position-identifier="sw-settings-search-header">
        {% block sw_setting_search_tabs_general %}
        <sw-tabs-item
            v-bind="$props"
            class="sw-settings-search__general-tab"
            :route="{ name: 'sw.settings.search.index.general' }"
            @click="onTabChange"
        >
            {{ $tc('sw-settings-search.page.generalTab') }}
        </sw-tabs-item>
        {% endblock %}

        {% block sw_setting_search_tabs_live_search %}
```

### Example 4
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
<sw-card-filter
    ref="itemFilter"
    :placeholder="$tc('sw-settings-search.generalTab.textPlaceholderTermsFilter')"
    @sw-card-filter-term-change="onSearchTermChange"
/>
{% endblock %}

{% block sw_settings_search_excluded_search_terms_actions %}
<div class="sw-settings-search-excluded-search-terms-group-actions">
    {% block sw_settings_search_excluded_search_terms_add_button %}
    <mt-button
        class="sw-settings-search-excluded-search-terms__insert-button"
        ghost
        size="small"
        :disabled="!acl.can('product_search_config.creator')"
```

### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-card-view>
    <sw-skeleton v-if="isLoading" />

    <template v-else>
        {% block sw_settings_salutation_detail_content_language_info %}
        <sw-language-info :entity-description="entityDescription" />
        {% endblock %}

        {% block sw_settings_salutation_detail_content_card %}
        <mt-card
            position-identifier="sw-settings-salutation-detail-content"
            :is-loading="isLoading"
            :title="$tc('sw-settings-salutation.detail.cardTitle')"
        >

```
