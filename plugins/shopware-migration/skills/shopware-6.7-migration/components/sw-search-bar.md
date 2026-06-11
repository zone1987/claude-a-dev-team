# sw-search-bar

> Global search bar component with auto-complete and module filtering.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| initialSearchType | `any` | `''` | no |  |
| typeSearchAlwaysInContainer | `any` | `false` | no |  |
| placeholder | `any` | `''` | no |  |
| initialSearch | `any` | `''` | no |  |
| entitySearchColor | `any` | `''` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| search-input | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| search | — | |
| active-item-index-select | — | |
| keyup-enter | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `registerListener` | |
| `onMouseOver` | |
| `registerActiveItemIndexSelectHandler` | |
| `unregisterActiveItemIndexSelectHandler` | |
| `registerKeyupEnterHandler` | |
| `unregisterKeyupEnterHandler` | |
| `getLabelSearchType` | |
| `setFocus` | |
| `closeOnClickOutside` | |
| `clearSearchTerm` | |
| `onFocusInput` | |
| `onBlur` | |
| `showSearchBar` | |
| `hideSearchBar` | |
| `showSearchFieldOnLargerViewports` | |
| `onSearchTermChange` | |
| `showTypeContainer` | |
| `filterTypeSelectResults` | |
| `onClickType` | |
| `setSearchType` | |
| `toggleOffCanvas` | |
| `resetSearchType` | |
| `doListSearch` | |
| `doListSearchWithContainer` | |
| `doGlobalSearch` | |
| `loadResults` | |
| `loadTypeSearchResults` | |
| `loadTypeSearchResultsByService` | |
| `setActiveResultPosition` | |
| `emitActiveResultPosition` | |
| `navigateUpResults` | |
| `navigateDownResults` | |
| `checkScrollPosition` | |
| `onKeyUpEnter` | |
| `getSearchTypeProperty` | |
| `getEntityIconName` | |
| `getEntityIconColor` | |
| `getEntityIcon` | |
| `isResultEmpty` | |
| `onMouseEnterSearchType` | |
| `onOpenModuleFiltersDropDown` | |
| `loadSalesChannelType` | |
| `getModuleEntities` | |
| `getDefaultMatchSearchableModules` | |
| `getSalesChannelTypesBySearchTerm` | |
| `toggleSearchPreferencesModal` | |
| `loadSearchTrends` | |
| `getFrequentlyUsedModules` | |
| `getRecentlySearch` | |
| `getInfoModuleFrequentlyUsed` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `searchBarFieldClasses` | |
| `placeholderSearchInput` | |
| `salesChannelRepository` | |
| `salesChannelTypeRepository` | |
| `salesChannelCriteria` | |
| `canCreateSalesChannels` | |
| `moduleRegistry` | |
| `searchableModules` | |
| `criteriaCollection` | |
| `currentUser` | |
| `showSearchTipForEsSearch` | |
| `adminEsEnable` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
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
    {% block sw_settings_country_list_smart_bar_header_title %}
    <h2>
        {% block sw_settings_country_list_smart_bar_header_title_text %}
        {{ $tc('sw-settings.index.title') }}
```

### Example 2
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
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
    {% block sw_settings_logging_list_smart_bar_header_title %}
    <h2>
        {% block sw_settings_logging_list_smart_bar_header_title_text %}
        {{ $tc('sw-settings.index.title') }}
```

### Example 3
Source: `sw-settings-salutation/page/sw-settings-salutation-list/sw-settings-salutation-list.html.twig`
```twig
    <sw-search-bar
        initial-search-type="salutation"
        :placeholder="$tc('sw-settings-salutation.general.placeholderSearchBar')"
        :initial-search="term"
        @search="onSearch"
    />
</template>
{% endblock %}

{% block sw_settings_salutation_list_smart_bar_header %}
<template #smart-bar-header>
    {% block sw_settings_salutation_list_smart_bar_header_title %}
    <h2>
        {% block sw_settings_salutation_list_smart_bar_header_title_text %}
        {{ $tc('sw-settings.index.title') }}
```

### Example 4
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-search-bar />
```

### Example 5
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
<sw-search-bar />
```
