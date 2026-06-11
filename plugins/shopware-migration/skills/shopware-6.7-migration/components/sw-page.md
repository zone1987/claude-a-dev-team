# sw-page

> Base page layout component with smart bar, header, content area, and sidebar.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| showSmartBar | `any` | `true` | no |  |
| showSearchBar | `any` | `true` | no |  |
| headerBorderColor | `any` | `''` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| search-bar | — | |
| smart-bar-back | — | |
| smart-bar-header | — | |
| language-switch | — | |
| smart-bar-actions | — | |
| side-content | — | |
| content | — | |
| sidebar | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `updatedComponent` | |
| `beforeDestroyComponent` | |
| `readScreenWidth` | |
| `setSidebarOffset` | |
| `removeSidebarOffset` | |
| `setScrollbarOffset` | |
| `initPage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `routerBack` | |
| `pageColor` | |
| `hasSideContentSlot` | |
| `hasSidebarSlot` | |
| `showHeadArea` | |
| `pageClasses` | |
| `pageContainerClasses` | |
| `pageContentClasses` | |
| `pageOffset` | |
| `headerStyles` | |
| `topBarActionStyles` | |
| `smartBarContentStyle` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-page class="sw-settings-country-list">

    {% block sw_settings_country_list_search_bar %}
    <template #search-bar>
        <sw-search-bar
            initial-search-type="country"
            :placeholder="$tc('sw-settings-country.general.placeholderSearchBar')"
            :initial-search="term"
            @search="onSearch"
        />
    </template>
    {% endblock %}

    {% block sw_settings_country_list_smart_bar_header %}
    <template #smart-bar-header>
```

### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-page class="sw-settings-country-detail">

    {% block sw_settings_country_detail_header %}
    <template #smart-bar-header>
        <h2>{{ placeholder(country, 'name', $tc('sw-settings-country.detail.textHeadline')) }}</h2>
    </template>
    {% endblock %}

    {% block sw_settings_country_detail_actions %}
    <template #smart-bar-actions>
        {% block sw_settings_country_detail_actions_abort %}
        <mt-button
            v-tooltip.bottom="{
                message: 'ESC',
                appearance: 'light'
```

### Example 3
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
<sw-page class="sw-settings-logging-list">

    {% block sw_settings_logging_list_search_bar %}
    <template #search-bar>
        <sw-search-bar
            initial-search-type="Logs"
            :placeholder="$tc('sw-settings-logging.general.placeholderSearchBar')"
            :initial-search="term"
            @search="onSearch"
        />
    </template>
    {% endblock %}

    {% block sw_settings_logging_list_smart_bar_header %}
    <template #smart-bar-header>
```

### Example 4
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-page class="sw-settings-search">
    {% block sw_settings_search_smart_bar_header %}
    <template #smart-bar-header>
        <h2>
            {% block sw_settings_search_smart_bar_header_title_text %}
            {{ $tc('sw-settings.index.title') }}
            <mt-icon
                name="regular-chevron-right-xs"
                size="12px"
            />
            {{ $tc('sw-settings-search.general.mainMenuItemGeneral') }}
            {% endblock %}
        </h2>
    </template>
    {% endblock %}
```

### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-page class="sw-settings-salutation-detail">

    {% block sw_settings_salutation_detail_search_bar %}
    <template #search-bar></template>
    {% endblock %}

    {% block sw_settings_salutation_detail_smart_bar_header %}
    <template #smart-bar-header>
        {% block sw_settings_salutation_detail_smart_bar_header_title %}
        <h2>
            {% block sw_settings_salutation_detail_smart_bar_header_title_text %}
            {{ placeholder(salutation, 'salutationKey', $tc('sw-settings-salutation.detail.placeholderNewSalutation')) }}
            {% endblock %}
        </h2>
        {% endblock %}
```
