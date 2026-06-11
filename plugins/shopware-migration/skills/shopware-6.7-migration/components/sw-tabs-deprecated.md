# sw-tabs-deprecated

> **Deprecated in 6.7** — Use `mt-tabs` instead. Will be removed in 6.8.
> See [mt-tabs](mt-tabs.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-tabs>` | `<mt-tabs>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| positionIdentifier | `any` | `null` | yes |  |
| isVertical | `any` | `false` | no |  |
| small | `any` | `true` | no |  |
| alignRight | `any` | `false` | no |  |
| defaultItem | `any` | `''` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | active: active | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| new-item-active | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `registerOnNewItemActiveHandler` | |
| `registerNewTabItem` | |
| `unregisterNewTabItem` | |
| `onNewItemActiveHandler` | |
| `onTabBarResize` | |
| `recalculateSlider` | |
| `updateActiveItem` | |
| `scrollTo` | |
| `checkIfNeedScroll` | |
| `setActiveItem` | |
| `scrollToItem` | |
| `addScrollbarOffset` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `tabClasses` | |
| `arrowClassesLeft` | |
| `arrowClassesRight` | |
| `sliderLength` | |
| `activeTabHasErrors` | |
| `activeTabHasWarnings` | |
| `sliderClasses` | |
| `sliderMovement` | |
| `sliderStyle` | |
| `tabContentStyle` | |
| `tabExtensions` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-tabs position-identifier="sw-settings-country-detail-header">
    {% block sw_setting_country_tabs_setting %}
    <sw-tabs-item
        v-bind="$props"
        class="sw-settings-country__setting-tab"
        :route="{ name: isNewCountry ? 'sw.settings.country.create.general' : 'sw.settings.country.detail.general' }"
    >
        {{ $tc('sw-settings-country.page.generalTab') }}
    </sw-tabs-item>
    {% endblock %}

    {% block sw_setting_country_tabs_state %}
    <sw-tabs-item
        v-bind="$props"
        class="sw-settings-country__state-tab"
```

### Example 2
Source: `sw-settings-logging/component/sw-settings-logging-mail-sent-info/sw-settings-logging-mail-sent-info.html.twig`
```twig
<sw-tabs-item
    class="sw-settings-logging-mail-sent-info__tab-item"
    :active="activeTab === 'html'"
    @click="activeTab = 'html'"
>
    {{ $tc('sw-settings-logging.mailInfo.tabHTML') }}
</sw-tabs-item>

<sw-tabs-item
    class="sw-settings-logging-mail-sent-info__tab-item"
    :active="activeTab === 'plain'"
    @click="activeTab = 'plain'"
>
    {{ $tc('sw-settings-logging.mailInfo.tabPlain') }}
</sw-tabs-item>
```

### Example 3
Source: `sw-settings-logging/component/sw-settings-logging-entry-info/sw-settings-logging-entry-info.html.twig`
```twig
<sw-tabs position-identifier="sw-settings-logging-entry-info">

    {% block sw_settings_logging_entry_info_tab_items %}
    <sw-tabs-item
        :active="activeTab === 'raw'"
        @click="activeTab = 'raw'"
    >
        {{ $tc('sw-settings-logging.entryInfo.tabRaw') }}
    </sw-tabs-item>
    {% endblock %}

    <template #content>
        {% block sw_settings_logging_entry_info_content %}
        {% block sw_settings_logging_entry_info_raw_content %}
        <mt-textarea
```

### Example 4
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
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
    <sw-tabs-item
        v-bind="$props"
```

### Example 5
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
<sw-tabs
    :default-item="defaultTab"
    position-identifier="sw-settings-search-searchable-content"
>
    <template #default="{ active }">
        {% block sw_settings_search_searchable_content_general_tab_title %}
        <sw-tabs-item
            v-bind="$props"
            class="sw-settings-search__searchable-content-tab-title"
            :name="tabNames.generalTab"
            :active-tab="active"
            @click="onChangeTab(tabNames.generalTab)"
        >
            {{ $tc('sw-settings-search.generalTab.labelGeneralTab') }}
        </sw-tabs-item>
```
