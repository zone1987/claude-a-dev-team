# Administration (sw-*) components

> **`size="default"` on every `mt-button` you write.** The component defaults to
> `size="small"` — 32 pixels against the 40 of every core control beside it. Examples below
> that are quoted from Shopware's own source keep the core's spelling; **a plugin's own
> template sets the size explicitly.**
> → `shopware-admin` → `sw-meteor` → `COMPONENTS.md`

49 components, each with its props, slots, events and examples exactly as the generator extracted them. One file per component cost 1044 unreachable references; grouped, every component stays one direct link from SKILL.md.

## Contents

- [`sw-tabs-deprecated`](#sw-tabs-deprecated)
- [`sw-tabs-item`](#sw-tabs-item)
- [`sw-tabs`](#sw-tabs)
- [`sw-tagged-field`](#sw-tagged-field)
- [`sw-tax-rule-card`](#sw-tax-rule-card)
- [`sw-text-editor-link-menu`](#sw-text-editor-link-menu)
- [`sw-text-editor-table-toolbar`](#sw-text-editor-table-toolbar)
- [`sw-text-editor-toolbar-button-link`](#sw-text-editor-toolbar-button-link)
- [`sw-text-editor-toolbar-button`](#sw-text-editor-toolbar-button)
- [`sw-text-editor-toolbar-table-button`](#sw-text-editor-toolbar-table-button)
- [`sw-text-editor-toolbar`](#sw-text-editor-toolbar)
- [`sw-text-editor`](#sw-text-editor)
- [`sw-text-field-deprecated`](#sw-text-field-deprecated)
- [`sw-text-field`](#sw-text-field)
- [`sw-text-preview`](#sw-text-preview)
- [`sw-textarea-field-deprecated`](#sw-textarea-field-deprecated)
- [`sw-textarea-field`](#sw-textarea-field)
- [`sw-time-ago`](#sw-time-ago)
- [`sw-tree-input-field`](#sw-tree-input-field)
- [`sw-tree-item`](#sw-tree-item)
- [`sw-tree`](#sw-tree)
- [`sw-upload-listener`](#sw-upload-listener)
- [`sw-upload-status`](#sw-upload-status)
- [`sw-url-field-deprecated`](#sw-url-field-deprecated)
- [`sw-url-field`](#sw-url-field)
- [`sw-usage-data-consent-banner`](#sw-usage-data-consent-banner)
- [`sw-user-card`](#sw-user-card)
- [`sw-user-sso-access-key-create-modal`](#sw-user-sso-access-key-create-modal)
- [`sw-user-sso-invitation-modal`](#sw-user-sso-invitation-modal)
- [`sw-user-sso-status-label`](#sw-user-sso-status-label)
- [`sw-users-permissions-additional-permissions`](#sw-users-permissions-additional-permissions)
- [`sw-users-permissions-configuration`](#sw-users-permissions-configuration)
- [`sw-users-permissions-detailed-additional-permissions`](#sw-users-permissions-detailed-additional-permissions)
- [`sw-users-permissions-detailed-permissions-grid`](#sw-users-permissions-detailed-permissions-grid)
- [`sw-users-permissions-permissions-grid`](#sw-users-permissions-permissions-grid)
- [`sw-users-permissions-role-detail`](#sw-users-permissions-role-detail)
- [`sw-users-permissions-role-listing`](#sw-users-permissions-role-listing)
- [`sw-users-permissions-role-view-detailed`](#sw-users-permissions-role-view-detailed)
- [`sw-users-permissions-role-view-general`](#sw-users-permissions-role-view-general)
- [`sw-users-permissions-user-create`](#sw-users-permissions-user-create)
- [`sw-users-permissions-user-detail`](#sw-users-permissions-user-detail)
- [`sw-users-permissions-user-listing`](#sw-users-permissions-user-listing)
- [`sw-users-permissions`](#sw-users-permissions)
- [`sw-verify-user-modal`](#sw-verify-user-modal)
- [`sw-version`](#sw-version)
- [`sw-vnode-renderer`](#sw-vnode-renderer)
- [`sw-wizard-dot-navigation`](#sw-wizard-dot-navigation)
- [`sw-wizard-page`](#sw-wizard-page)
- [`sw-wizard`](#sw-wizard)

## sw-tabs-deprecated

> **Deprecated in 6.7** — Use `mt-tabs` instead. Will be removed in 6.8.
> See mt-tabs for the replacement.

- [Props](#props)
- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-tabs>` | `<mt-tabs>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| positionIdentifier | `any` | `null` | yes |  |
| isVertical | `any` | `false` | no |  |
| small | `any` | `true` | no |  |
| alignRight | `any` | `false` | no |  |
| defaultItem | `any` | `''` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | active: active | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| new-item-active | — | |

### Methods

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

### Computed Properties

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

### Examples

#### Example 1
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

#### Example 2
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

#### Example 3
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

#### Example 4
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

#### Example 5
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

## sw-tabs-item

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| route | `null \| null` | `''` | no |  |
| active | `any` | `false` | no |  |
| activeTab | `any` | `''` | no |  |
| name | `any` | `''` | no |  |
| hasError | `any` | `false` | no |  |
| hasWarning | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| errorTooltip | `any` | — | no |  |
| warningTooltip | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUpdateComponent` | |
| `mountedComponent` | |
| `updateActiveState` | |
| `clickEvent` | |
| `checkIfActive` | |
| `checkIfRouteMatchesLink` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isNative` | |
| `tabsItemClasses` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-tabs-item
    v-bind="$props"
    class="sw-settings-country__setting-tab"
    :route="{ name: isNewCountry ? 'sw.settings.country.create.general' : 'sw.settings.country.detail.general' }"
>
    {{ $tc('sw-settings-country.page.generalTab') }}
</sw-tabs-item>
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-tabs-item
    v-bind="$props"
    class="sw-settings-country__state-tab"
    :route="{ name: isNewCountry ? 'sw.settings.country.create.state' : 'sw.settings.country.detail.state' }"
>
    {{ $tc('sw-settings-country.page.stateTab') }}
</sw-tabs-item>
```

#### Example 3
Source: `sw-settings-logging/component/sw-settings-logging-mail-sent-info/sw-settings-logging-mail-sent-info.html.twig`
```twig
<sw-tabs-item
    class="sw-settings-logging-mail-sent-info__tab-item"
    :active="activeTab === 'html'"
    @click="activeTab = 'html'"
>
    {{ $tc('sw-settings-logging.mailInfo.tabHTML') }}
</sw-tabs-item>
```

#### Example 4
Source: `sw-settings-logging/component/sw-settings-logging-mail-sent-info/sw-settings-logging-mail-sent-info.html.twig`
```twig
<sw-tabs-item
    class="sw-settings-logging-mail-sent-info__tab-item"
    :active="activeTab === 'plain'"
    @click="activeTab = 'plain'"
>
    {{ $tc('sw-settings-logging.mailInfo.tabPlain') }}
</sw-tabs-item>
```

#### Example 5
Source: `sw-settings-logging/component/sw-settings-logging-entry-info/sw-settings-logging-entry-info.html.twig`
```twig
<sw-tabs-item
    :active="activeTab === 'raw'"
    @click="activeTab = 'raw'"
>
    {{ $tc('sw-settings-logging.entryInfo.tabRaw') }}
</sw-tabs-item>
```

## sw-tabs

> **Migration wrapper** — Delegates to `mt-tabs` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-tabs for the new component.

- [Slots](#slots)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | — | |
| name | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |
| `mountedComponent` | |
| `setActiveItem` | |
| `onNewItemActive` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `useMeteorComponent` | |
| `itemsBackwardCompatible` | |

### Examples

#### Example 1
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

#### Example 2
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

#### Example 3
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

#### Example 4
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

#### Example 5
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

## sw-tagged-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| placeholder | `any` | — | no |  |
| addOnKey | `any` | — | no |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `dismissLastTag` | |
| `dismissTag` | |
| `performAddTag` | |
| `setFocus` | |
| `noTriggerKey` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasValues` | |
| `taggedFieldClasses` | |
| `taggedFieldInputClasses` | |

### Examples

#### Example 1
Source: `sw-cms/elements/form/config/sw-cms-el-config-form.html.twig`
```twig
                    <sw-tagged-field
                        v-model:value="element.config.mailReceiver.value"
                        :class="getLastMailClass"
                        name="mailReceiver"
                        placeholder="john@doe.com"
                        :disabled="isInherited"
                        @update:value="updateMailReceiver"
                    />
                </template>
            </sw-cms-inherit-wrapper>
        </sw-container>
        {% endblock %}
    </template>
</sw-tabs>
{% endblock %}
```

#### Example 2
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
    <sw-tagged-field
        ref="product-stream-value-multi-value-tagged-field"
        v-model:value="multiValue"
        size="medium"
    />
    {% endblock %}
</template>

<template v-else-if="filterType === 'since' || filterType === 'until'">
    {% block sw_product_stream_value_relative_time_operator %}
    <sw-arrow-field
        ref="product-stream-value-relative-time-arrow-field"
        :disabled="disabled"
    >
        <sw-single-select
```

## sw-tax-rule-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| tax | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `paginate` | |
| `onColumnSort` | |
| `onSearchTermChange` | |
| `onModalClose` | |
| `showRuleModal` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `hasTypeCellComponent` | |
| `getTypeCellComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `taxRuleRepository` | |
| `taxRulesEmpty` | |
| `taxRuleCardClasses` | |
| `taxRuleCriteria` | |
| `getColumns` | |
| `assetFilter` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-settings-tax/page/sw-settings-tax-detail/sw-settings-tax-detail.html.twig`
```twig
                <sw-tax-rule-card
                    v-if="tax.id"
                    :disabled="!taxId"
                    class="sw-settings-tax-detail__tax-rule-grid"
                    :tax="tax"
                    :is-loading="isLoading"
                />
                {% endblock %}

                {% block sw_settings_tax_detail_custom_field_sets %}
                <mt-card
                    v-if="showCustomFields"
                    position-identifier="sw-settings-tax-detail-custom-field-sets"
                    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                    :is-loading="isLoading"
```

## sw-text-editor-link-menu

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| buttonConfig | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `getCategoryCollection` | |
| `getEmptyCategoryCollection` | |
| `parseLink` | |
| `replaceCategorySelection` | |
| `removeCategorySelection` | |
| `prepareLink` | |
| `addProtocolToLink` | |
| `setLink` | |
| `removeLink` | |
| `onSelectFieldChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `seoUrlReplacePrefix` | |
| `entityFilter` | |
| `categoryRepository` | |
| `linkCategoryOptions` | |

### Examples

#### Basic Usage
```twig
<sw-text-editor-link-menu
    buttonConfig="..."
>
    <!-- content -->
</sw-text-editor-link-menu>
```

## sw-text-editor-table-toolbar

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selection | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| table-modify | — | |
| table-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onAddRow` | |
| `fillRowWithCells` | |
| `removeResizeHandle` | |
| `onAddColumn` | |
| `insertNewCellsForColumn` | |
| `onDeleteColumn` | |
| `setRangeAfterDelete` | |
| `onDeleteRow` | |
| `addResizeHandle` | |
| `deleteCells` | |
| `onDeleteTable` | |
| `getVariables` | |
| `getNode` | |
| `setSelectionRange` | |
| `keepSelection` | |

### Examples

#### Basic Usage
```twig
<sw-text-editor-table-toolbar>
    <!-- content -->
</sw-text-editor-table-toolbar>
```

## sw-text-editor-toolbar-button-link

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| editor | `any` | — | yes |  |
| button | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `openLinkModal` | |
| `parseLink` | |
| `parseButtonClass` | |
| `applyLink` | |
| `removeLink` | |
| `isLink` | |
| `prepareLink` | |
| `prepareClass` | |
| `prepareTarget` | |
| `addProtocolToLink` | |
| `getCategoryCollection` | |
| `getEmptyCategoryCollection` | |
| `replaceCategorySelection` | |
| `removeCategorySelection` | |
| `onSelectFieldChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `linkOptions` | |
| `buttonVariantList` | |
| `seoUrlReplacePrefix` | |
| `categoryRepository` | |
| `showOpenInNewTabToggle` | |
| `productEntityFilter` | |
| `entityFilter` | |

### Examples

#### Basic Usage
```twig
<sw-text-editor-toolbar-button-link
    editor="..."
    button="..."
>
    <!-- content -->
</sw-text-editor-toolbar-button-link>
```

## sw-text-editor-toolbar-button

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| buttonConfig | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| isInlineEdit | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| buttonSlot | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| button-click | — | |
| menu-toggle | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `buttonHandler` | |
| `childActive` | |
| `handleButtonClick` | |
| `onToggleMenu` | |
| `getDropdownClasses` | |
| `onChildMounted` | |
| `getTooltipConfig` | |
| `positionLinkMenu` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `tooltipAppearance` | |

### Examples

#### Basic Usage
```twig
<sw-text-editor-toolbar-button
    buttonConfig="..."
>
    <!-- content -->
</sw-text-editor-toolbar-button>
```

## sw-text-editor-toolbar-table-button

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| buttonConfig | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| mounted | — | |
| table-create | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `onMouseOverColumn` | |
| `setSelectedTableColsAndRows` | |
| `setSelectedCols` | |
| `setSelectedRows` | |
| `loopTableRows` | |
| `loopTableCols` | |
| `onMouseOut` | |
| `onLastRowMouseOut` | |
| `onLastColMouseOut` | |
| `emitTable` | |
| `createHtmlTable` | |

### Examples

#### Basic Usage
```twig
<sw-text-editor-toolbar-table-button
    buttonConfig="..."
>
    <!-- content -->
</sw-text-editor-toolbar-table-button>
```

## sw-text-editor-toolbar

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| parentIsActive | `any` | `false` | no |  |
| isInlineEdit | `any` | `false` | no |  |
| selection | `any` | `null` | no |  |
| buttonConfig | `any` | — | yes |  |
| isCodeEdit | `any` | `false` | no |  |
| isTableEdit | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| itemsSlot | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| created-el | — | |
| destroyed-el | — | |
| remove-link | — | |
| text-style-change | — | |
| table-edit | — | |
| on-set-link | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `isOverlayingLeft` | |
| `destroyedComponent` | |
| `onMouseUp` | |
| `setToolbarPosition` | |
| `setSelectionRange` | |
| `setButtonValues` | |
| `isDisabled` | |
| `handleToolbarClick` | |
| `onButtonClick` | |
| `closeExpandedMenu` | |
| `setActiveTags` | |
| `setButtonPositions` | |
| `handleTextStyleChangeLink` | |
| `keepSelection` | |
| `onToggleMenu` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |

### Examples

#### Basic Usage
```twig
<sw-text-editor-toolbar>
    <!-- content -->
</sw-text-editor-toolbar>
```

## sw-text-editor

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| isInlineEdit | `any` | `false` | no |  |
| verticalAlign | `any` | `''` | no |  |
| label | `any` | `''` | no |  |
| placeholder | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |
| allowInlineDataMapping | `any` | `false` | no |  |
| sanitizeInput | `any` | `false` | no |  |
| sanitizeFieldName | `any` | `null` | no |  |
| sanitizeInfoWarn | `any` | `false` | no |  |
| enableTransparentBackground | `any` | `false` | no |  |
| buttonConfig | `any` | — | no |  |
| error | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `destroyedComponent` | |
| `keyListener` | |
| `onSelectionChange` | |
| `getPath` | |
| `toggleCodeEditor` | |
| `handleInsertDataMapping` | |
| `resetForeColor` | |
| `onToolbarCreated` | |
| `onToolbarDestroyed` | |
| `onTextStyleChange` | |
| `expandSelectionToNearestEndBracket` | |
| `expandSelectionToNearestStartBracket` | |
| `setSelection` | |
| `containsStartBracket` | |
| `containsEndBracket` | |
| `isInsideInlineMapping` | |
| `handleInsertTable` | |
| `setTablesResizable` | |
| `setTableResizable` | |
| `setTableSelectorListeners` | |
| `setTableListeners` | |
| `onSetLink` | |
| `onRemoveLink` | |
| `onClick` | |
| `onFocus` | |
| `onEnter` | |
| `fixWrongNodes` | |
| `hasDirectMinorElements` | |
| `setFocus` | |
| `removeFocus` | |
| `onDocumentClick` | |
| `onInput` | |
| `onContentChange` | |
| `onCopy` | |
| `onPaste` | |
| `emitContent` | |
| `emitHtmlContent` | |
| `getContentValue` | |
| `emptyCheck` | |
| `setWordCount` | |
| `onTableEdit` | |
| `onTableModify` | |
| `onTableDelete` | |
| `showLabel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `contentClasses` | |
| `verticalAlignStyle` | |
| `availableDataMappings` | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
    <sw-text-editor
        v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
        :key="category.id + 'description'"
        v-model:value="category.description"
        class="sw-category-detail-base__description"
        type="textarea"
        :disabled="!acl.can('category.editor')"
        sanitize-input
        sanitize-field-name="category_translation.description"
        :label="$tc('sw-category.base.menu.descriptionLabel')"
        :placeholder="$tc('sw-category.base.menu.descriptionPlaceholder')"
    />
    <mt-text-editor
        v-else
        :key="category.id + 'description-meteor'"
```

#### Example 2
Source: `sw-cms/elements/text/config/sw-cms-el-config-text.html.twig`
```twig
                <sw-text-editor
                    v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
                    :key="isInherited"
                    :value="element.config.content.value"
                    :disabled="isInherited"
                    :allow-inline-data-mapping="true"
                    :sanitize-info-warn="true"
                    enable-transparent-background
                    @update:value="onInput"
                    @blur="onBlur"
                />

                <mt-text-editor
                    v-else
                    :key="isInherited + '-meteor'"
```

#### Example 3
Source: `sw-cms/elements/text/component/sw-cms-el-text.html.twig`
```twig
    <sw-text-editor
        v-else-if="!feature.isActive('METEOR_TEXT_EDITOR')"
        v-model:value="element.config.content.value"
        :disabled="disabled"
        :vertical-align="element.config.verticalAlign.value"
        :allow-inline-data-mapping="true"
        :is-inline-edit="true"
        sanitize-input
        sanitize-field-name="app_cms_block.template"
        enable-transparent-background
        @blur="onBlur"
        @update:value="onInput"
    />
    <mt-text-editor
        v-else
```

#### Example 4
Source: `sw-product/component/sw-product-basic-form/sw-product-basic-form.html.twig`
```twig
        <sw-text-editor
            v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
            :key="isInherited"
            :placeholder="placeholder(product, 'description', $tc('sw-product.basicForm.placeholderDescriptionLong'))"
            :error="productDescriptionError"
            :disabled="isInherited || !allowEdit"
            :value="currentValue"
            sanitize-input
            sanitize-field-name="product_translation.description"
            @update:value="updateCurrentValue"
        />
        <mt-text-editor
            v-else
            :key="'meteor-' + isInherited"
            :placeholder="placeholder(product, 'description', $tc('sw-product.basicForm.placeholderDescriptionLong'))"
```

#### Example 5
Source: `sw-manufacturer/page/sw-manufacturer-detail/sw-manufacturer-detail.html.twig`
```twig
    <sw-text-editor
        v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
        v-model:value="manufacturer.description"
        :label="$tc('sw-manufacturer.detail.labelDescription')"
        :placeholder="placeholder(manufacturer, 'description', $tc('sw-manufacturer.detail.placeholderDescription'))"
        name="description"
        sanitize-input
        sanitize-field-name="product_manufacturer_translation.description"
        :error="manufacturerDescriptionError"
        :disabled="!acl.can('product_manufacturer.editor') || undefined"
    />
    <mt-text-editor
        v-else
        v-model="manufacturer.description"
        :label="$tc('sw-manufacturer.detail.labelDescription')"
```

## sw-text-field-deprecated

> **Deprecated in 6.7** — Use `mt-text-field` instead. Will be removed in 6.8.
> See mt-text-field for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-text-field>` | `<mt-text-field>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| placeholder | `any` | `''` | no |  |
| copyable | `any` | `false` | no |  |
| copyableTooltip | `any` | `false` | no |  |
| idSuffix | `any` | — | no |  |
| ariaLabel | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| prefix | — | |
| suffix | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |
| `onInput` | |
| `restoreInheritance` | |
| `createInputId` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasPrefix` | |
| `hasSuffix` | |
| `filteredInputAttributes` | |

### Examples

#### Basic Usage
```twig
<sw-text-field-deprecated>
    <!-- content -->
</sw-text-field-deprecated>
```

## sw-text-field

> **Migration wrapper** — Delegates to `mt-text-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-text-field for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `any` | `null` | no |  |
| value | `any` | `null` | no |  |
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |
| `handleUpdateModelValue` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `compatValue` | |

### Examples

#### Basic Usage
```twig
<sw-text-field>
    <!-- content -->
</sw-text-field>
```

## sw-text-preview

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `any` | — | yes |  |
| maximumLength | `any` | — | yes |  |
| modalTitle | `any` | `''` | no |  |
| maximumNewLines | `any` | `0` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `openModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `shortenedText` | |
| `fullText` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-customer-comment/sw-order-customer-comment.html.twig`
```twig
    <sw-text-preview
        :text="customerComment"
        :modal-title="$tc('sw-order.detailCustomerComment.title')"
        :maximum-length="750"
        :maximum-new-lines="5"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```

## sw-textarea-field-deprecated

> **Deprecated in 6.7** — Will be removed in 6.8.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |
| placeholder | `any` | `null` | no |  |
| ariaLabel | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| change | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onInput` | |
| `onChange` | |

### Examples

#### Basic Usage
```twig
<sw-textarea-field-deprecated>
    <!-- content -->
</sw-textarea-field-deprecated>
```

## sw-textarea-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| placeholder | `any` | — | no |  |
| value | `any` | — | no |  |
| modelValue | `any` | — | no |  |
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| name | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `realValue` | |

### Examples

#### Basic Usage
```twig
<sw-textarea-field>
    <!-- content -->
</sw-textarea-field>
```

## sw-time-ago

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| date | `null \| null` | — | yes |  |
| dateTimeFormat | `any` | `{}` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `formatRelativeTime` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `dateObject` | |
| `dateFilter` | |
| `fullDatetime` | |
| `lessThanOneMinute` | |
| `lessThanOneHour` | |
| `lessThanOneMinuteFromNow` | |
| `lessThanOneHourFromNow` | |
| `isToday` | |

### Examples

#### Example 1
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
<sw-time-ago :date="item.createdAt" />
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-search-index/sw-settings-search-search-index.html.twig`
```twig
        {{ $tc('sw-settings-search.generalTab.textLastedBuild') }} <sw-time-ago
            :date="latestIndex.lastDate"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </template>
    <template v-else>
        {{ $tc('sw-settings-search.generalTab.textSearchNotIndexedYet') }}
    </template>
</span>
{% endblock %}
{% endblock %}

{% block sw_settings_search_search_index_rebuild_progress %}
<div
    v-if="progressBarValue"
```

#### Example 3
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
        <sw-time-ago
            v-if="extension.installedAt.date"
            :date="extension.installedAt.date"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </span>

    <span v-else-if="extension.storeLicense">
        {{ $tc('sw-extension-store.component.sw-extension-card-base.purchasedLabel') }}
        <sw-time-ago
            v-if="extension.storeLicense.creationDate"
            :date="extension.storeLicense.creationDate"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </span>
```

#### Example 4
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
        <sw-time-ago
            :date="item.createdAt"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </mt-link>
</template>
{% endblock %}

{% block sw_import_export_activity_listing_state %}
<template #column-state="{ item }">
    <sw-color-badge
        v-if="item.state === 'failed'"
        variant="error"
        rounded
    />
```

#### Example 5
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
        <sw-time-ago
            :date="logEntity.createdAt"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </dd>
</div>
{% endblock %}

{% block sw_import_export_activity_result_modal_info_log_user %}
<div class="sw-import-export-activity-result-modal__list-item sw-import-export-activity-result-modal__log-info-user">
    <dt>{{ $tc('sw-import-export.activity.result.logInfo.labelUser') }}</dt>

    <dd>{{ logEntity.username }}</dd>
</div>
{% endblock %}
```

## sw-tree-input-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentValue | `any` | — | no |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| new-item-create | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createNewItem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |

### Examples

#### Basic Usage
```twig
<sw-tree-input-field>
    <!-- content -->
</sw-tree-input-field>
```

## sw-tree-item

> Individual tree node within sw-tree.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| draggedItem | `any` | — | no |  |
| newElementId | `any` | — | no |  |
| translationContext | `any` | — | no |  |
| onChangeRoute | `any` | — | no |  |
| disableContextMenu | `any` | — | no |  |
| contextMenuTooltipText | `any` | — | no |  |
| activeParentIds | `any` | — | no |  |
| activeItemIds | `any` | — | no |  |
| sortable | `any` | — | no |  |
| markInactive | `any` | `false` | no |  |
| shouldFocus | `any` | `false` | no |  |
| shouldShowActiveState | `any` | `false` | no |  |
| activeFocusId | `any` | — | no |  |
| displayCheckbox | `any` | — | no |  |
| allowNewCategories | `any` | — | no |  |
| allowDeleteCategories | `any` | — | no |  |
| allowCreateWithoutPosition | `any` | — | no |  |
| allowDuplicate | `any` | — | no |  |
| getItemUrl | `any` | — | no |  |
| getIsHighlighted | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| grip | — | |
| content | — | |
| actions | item: item | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| check-item | — | |

### Methods

| Method | Description |
|--------|-------------|
| `updatedComponent` | |
| `mountedComponent` | |
| `beforeUnmountComponent` | |
| `handleKeyDown` | |
| `openTreeItem` | |
| `getTreeItemChildren` | |
| `dragStart` | |
| `dragEnd` | |
| `onMouseEnter` | |
| `startDrag` | |
| `endDrag` | |
| `moveDrag` | |
| `emitCheckedItem` | |
| `toggleItemCheck` | |
| `addSubElement` | |
| `addElement` | |
| `duplicateElement` | |
| `onDuplicate` | |
| `editElementName` | |
| `onFinishNameingElement` | |
| `onBlurTreeItemInput` | |
| `onCancelSubmit` | |
| `abortCreateElement` | |
| `deleteElement` | |
| `getName` | |
| `getActiveIconColor` | |
| `showItemUrl` | |
| `renderContentSlotNode` | |
| `renderActionsSlotNode` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `checked` | |
| `activeElementId` | |
| `isOpened` | |
| `isDragging` | |
| `styling` | |
| `dragConf` | |
| `parentScope` | |
| `toolTip` | |
| `isDisabled` | |
| `isHighlighted` | |
| `contentSlot` | |
| `actionsSlot` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-tree-item
    v-for="item in treeItems"
    :key="item.id"
    should-focus
    :display-checkbox="false"
    :item="item"
    :active="item.active"
    :sortable="sortable"
    :on-change-route="onChangeRoute"
    :active-parent-ids="selectedItemsPathIds"
    :active-item-ids="checkedItemIds"
    @check-item="checkItem"
>

    <template #actions="{ item }">
```

#### Example 2
Source: `sw-category/component/sw-landing-page-tree/sw-landing-page-tree.html.twig`
```twig
<sw-tree-item
    v-for="item in treeItems"
    :key="item.id"
    :item="item"
    :should-show-active-state="true"
    :allow-duplicate="true"
    :allow-new-categories="false || undefined"
    :allow-delete-categories="allowDelete || undefined"
    :active="item.active"
    :translation-context="translationContext"
    :on-change-route="onChangeRoute"
    :sortable="sortable || undefined"
    :dragged-item="draggedItem"
    :disable-context-menu="disableContextMenu"
    :display-checkbox="allowEdit || undefined"
```

#### Example 3
Source: `sw-category/component/sw-category-tree/sw-category-tree.html.twig`
```twig
        <sw-tree-item
            v-for="item in treeItems"
            :key="item.id"
            :item="item"
            :should-show-active-state="true"
            :allow-duplicate="false"
            :allow-new-categories="allowCreate || undefined"
            :allow-delete-categories="allowDelete || undefined"
            :active="item.active"
            :translation-context="translationContext"
            :on-change-route="onChangeRoute"
            :sortable="sortable"
            :dragged-item="draggedItem"
            :disable-context-menu="disableContextMenu"
            :display-checkbox="allowEdit || undefined"
```

#### Example 4
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
        <sw-tree-item
            v-for="(item, index) in treeItems"
            :key="item.id"
            :sortable="false"
            :item="item"
            disable-context-menu
            @check-item="filterOptionChecked"
        />
    </template>
</sw-tree>
{% endblock %}

{% block sw_product_variant_modal_option_list_toolbar_container_filter_buttons %}
<div class="sw-product-variant-modal__filter-buttons">
    {% block sw_product_variant_modal_option_list_toolbar_container_button_filter_reset %}
```

#### Example 5
Source: `sw-product/component/sw-product-variants/sw-product-variants-delivery/sw-product-variants-delivery-order/sw-product-variants-delivery-order.html.twig`
```twig
                <sw-tree-item
                    v-for="item in treeItems"
                    :key="item.id"
                    :item="item"
                    :disable-context-menu="true"
                    :sortable="true"
                />
            </template>
        </sw-tree>
        {% endblock %}

        {% block sw_product_variants_delivery_order_loader %}
        <sw-loader v-else />
        {% endblock %}
    </div>
```

## sw-tree

> Tree view component with drag & drop reordering.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | — | yes |  |
| rootParentId | `any` | — | no |  |
| parentProperty | `any` | — | no |  |
| afterIdProperty | `any` | — | no |  |
| childCountProperty | `any` | — | no |  |
| searchable | `any` | — | no |  |
| activeTreeItemId | `any` | — | no |  |
| routeParamsActiveElementId | `any` | — | no |  |
| translationContext | `any` | — | no |  |
| onChangeRoute | `any` | — | no |  |
| disableContextMenu | `any` | — | no |  |
| bindItemsToFolder | `any` | — | no |  |
| sortable | `any` | — | no |  |
| checkItemsInitial | `any` | — | no |  |
| allowDeleteCategories | `any` | — | no |  |
| allowCreateCategories | `any` | — | no |  |
| initiallyExpandedRoot | `any` | — | no |  |
| ariaLabel | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| search | — | |
| headline | — | |
| items | sortable: sortable | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| checked-elements-count | — | |
| get-tree-items | — | |
| search-tree-items | — | |
| drag-start | — | |
| drag-end | — | |
| delete-element | — | |
| editing-end | — | |
| batch-delete | — | |
| save-tree-items | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeUnmountedComponent` | |
| `handleFocusIn` | |
| `handleKeyDown` | |
| `getItems` | |
| `searchItems` | |
| `getTreeItems` | |
| `updateSorting` | |
| `startDrag` | |
| `endDrag` | |
| `moveDrag` | |
| `openTreeById` | |
| `findTreeByParentId` | |
| `findById` | |
| `onCreateNewItem` | |
| `addSubElement` | |
| `duplicateElement` | |
| `addElement` | |
| `getNewTreeItem` | |
| `deleteElement` | |
| `abortCreateElement` | |
| `onFinishNameingElement` | |
| `deleteSelectedElements` | |
| `checkItem` | |
| `saveItems` | |
| `onDeleteElements` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `activeElementId` | |
| `isSortable` | |
| `isSearched` | |
| `hasActionSlot` | |
| `hasNoItems` | |
| `selectedItemsPathIds` | |
| `checkedItemIds` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-tree
    :sortable="false"
    :items="searchResults"
    :searchable="false"
    :disable-context-menu="true"
    bind-items-to-folder
    :active-tree-item-id="activeFocusId"
    initially-expanded-root
    route-params-active-element-id="snippet"
>

    <template #headline>
        <span></span>
    </template>

```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
        <sw-tree-item
            v-for="item in treeItems"
            :key="item.id"
            should-focus
            :display-checkbox="false"
            :item="item"
            :active="item.active"
            :sortable="sortable"
            :on-change-route="onChangeRoute"
            :active-parent-ids="selectedItemsPathIds"
            :active-item-ids="checkedItemIds"
            @check-item="checkItem"
        >

            <template #actions="{ item }">
```

#### Example 3
Source: `sw-category/component/sw-landing-page-tree/sw-landing-page-tree.html.twig`
```twig
<sw-tree
    v-if="!isLoadingInitialData"
    ref="landingPageTree"
    class="sw-landing-page-tree__inner"
    :items="landingPages"
    :sortable="false || undefined"
    :searchable="false"
    :translation-context="translationContext"
    :on-change-route="changeLandingPage"
    :disable-context-menu="disableContextMenu"
    :allow-delete-categories="allowDelete || undefined"
    :allow-create-categories="false"
    :active-tree-item-id="landingPageId"
    @batch-delete="deleteCheckedItems"
    @delete-element="onDeleteLandingPage"
```

#### Example 4
Source: `sw-category/component/sw-landing-page-tree/sw-landing-page-tree.html.twig`
```twig
<sw-tree-item
    v-for="item in treeItems"
    :key="item.id"
    :item="item"
    :should-show-active-state="true"
    :allow-duplicate="true"
    :allow-new-categories="false || undefined"
    :allow-delete-categories="allowDelete || undefined"
    :active="item.active"
    :translation-context="translationContext"
    :on-change-route="onChangeRoute"
    :sortable="sortable || undefined"
    :dragged-item="draggedItem"
    :disable-context-menu="disableContextMenu"
    :display-checkbox="allowEdit || undefined"
```

#### Example 5
Source: `sw-category/component/sw-category-tree/sw-category-tree.html.twig`
```twig
<sw-tree
    v-if="!isLoadingInitialData"
    ref="categoryTree"
    class="sw-category-tree__inner"
    after-id-property="afterCategoryId"
    :items="categories"
    :sortable="sortable"
    :searchable="false"
    :active-tree-item-id="categoryId"
    :translation-context="translationContext"
    :on-change-route="changeCategory"
    :disable-context-menu="disableContextMenu"
    :allow-delete-categories="allowDelete || undefined"
    initially-expanded-root
    @batch-delete="deleteCheckedItems"
```

## sw-upload-listener

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| uploadTag | `any` | — | yes |  |
| autoUpload | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `convertStoreEventToVueEvent` | |
| `handleError` | |
| `updateSuccessNotification` | |
| `showErrorNotification` | |
| `syncEntitiesAndRunUploads` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |

### Examples

#### Example 1
Source: `sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig`
```twig
<sw-upload-listener
    :upload-tag="currentOption.id"
    auto-upload
    @media-upload-finish="successfulUpload"
/>
<sw-media-compact-upload-v2
    default-folder="product"
    :label="$tc('sw-property.detail.labelMediaUpload')"
    :source="currentOption.mediaId"
    :upload-tag="currentOption.id"
    :disabled="!allowEdit"
    @media-upload-remove-image="removeMedia"
    @selection-change="setMedia"
/>
{% endblock %}
```

#### Example 2
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
<sw-upload-listener
    :key="category.id + 'uploadListener'"
    :upload-tag="category.id"
    auto-upload
    @media-upload-finish="onSetMediaItem"
/>
<sw-media-upload-v2
    :key="category.id + 'upload'"
    :label="$tc('sw-category.base.menu.imageLabel')"
    variant="regular"
    :disabled="!acl.can('category.editor')"
    :source="mediaItem"
    :upload-tag="category.id"
    :allow-multi-select="false"
    :default-folder="category.getEntityName()"
```

#### Example 3
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="successfulUpload"
        />

        {% block sw_cms_section_config_background_image_position_field %}
        <mt-select
            v-model="section.backgroundMediaMode"
            :label="$tc('sw-cms.detail.label.backgroundMediaMode')"
            :disabled="!section.backgroundMediaId"
            :options="backgroundMediaModeOptions"
        />
        {% endblock %}
        {% endblock %}
```

#### Example 4
Source: `sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig`
```twig
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="successfulUpload"
        />

        {% block sw_cms_block_config_background_image_position_field %}
        <mt-select
            v-model="block.backgroundMediaMode"
            :label="$tc('sw-cms.detail.label.backgroundMediaMode')"
            :disabled="!block.backgroundMediaId"
            :options="backgroundModeOptions"
        />
        {% endblock %}
        {% endblock %}
```

#### Example 5
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="onVideoUpload"
        />
        {% endblock %}

        {% block sw_cms_element_video_config_media_modal %}
        <sw-media-modal-v2
            v-if="showMediaModal"
            variant="full"
            :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
            :entity-context="cmsPageState.entityName"
            :allow-multi-select="false"
            :initial-folder-id="cmsPageState.defaultMediaFolderId"
```

## sw-upload-status

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `registerListeners` | |
| `getUploadId` | |
| `findByTargetId` | |
| `onUploadEvent` | |
| `onUploadAdded` | |
| `onUploadFinished` | |
| `onUploadFailed` | |
| `onUploadProgress` | |
| `onUploadCancel` | |
| `updateSnackbar` | |
| `showErrorNotification` | |
| `getTransportErrorSnippet` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `snackbar` | |
| `uploadCount` | |
| `hasFailedUploads` | |
| `uploadProgress` | |
| `processedUploadCount` | |
| `uploadComplete` | |
| `snackbarMessage` | |
| `snackbarConfig` | |

### Examples

#### Basic Usage
```twig
<sw-upload-status>
    <!-- content -->
</sw-upload-status>
```

## sw-url-field-deprecated

> **Deprecated in 6.7** — Use `mt-url-field` instead. Will be removed in 6.8.
> See mt-url-field for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-url-field>` | `<mt-url-field>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| error | `any` | `null` | no |  |
| omitUrlHash | `any` | `false` | no |  |
| omitUrlSearch | `any` | `false` | no |  |
| addTrailingSlash | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onBlur` | |
| `checkInput` | |
| `handleEmptyUrl` | |
| `validateCurrentValue` | |
| `changeMode` | |
| `getURLInstance` | |
| `getSSLMode` | |
| `setInvalidUrlError` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `prefixClass` | |
| `urlPrefix` | |
| `url` | |
| `combinedError` | |
| `unicodeUriFilter` | |

### Examples

#### Basic Usage
```twig
<sw-url-field-deprecated>
    <!-- content -->
</sw-url-field-deprecated>
```

## sw-url-field

> **Migration wrapper** — Delegates to `mt-url-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-url-field for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| placeholder | `any` | — | no |  |
| value | `any` | — | no |  |
| modelValue | `any` | — | no |  |
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| name | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `realValue` | |

### Examples

#### Basic Usage
```twig
<sw-url-field>
    <!-- content -->
</sw-url-field>
```

## sw-usage-data-consent-banner

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| canBeHidden | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onReject` | |
| `onAccept` | |
| `onHide` | |
| `onClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isAccepted` | |
| `isHidden` | |
| `hasSufficientPrivileges` | |

### Examples

#### Example 1
Source: `sw-settings-usage-data/view/sw-settings-usage-data-general/sw-settings-usage-data-general.html.twig`
```twig
<sw-usage-data-consent-banner v-if="!feature.isActive('PRODUCT_ANALYTICS')" />
```

#### Example 2
Source: `sw-dashboard/page/sw-dashboard-index/sw-dashboard-index.html.twig`
```twig
<sw-usage-data-consent-banner
    v-if="!feature.isActive('PRODUCT_ANALYTICS')"
    can-be-hidden
/>

<sw-extension-component-section
    position-identifier="sw-dashboard__before-content"
    class="sw-dashboard__before-content"
/>

{% block sw_dashboard_index_content_info_grid %}
<div class="sw-dashboard-index__card-grid">
    {% block sw_dashboard_index_content_info_grid_inner %}

    {% block sw_dashboard_index_content_info__grid_inner_welcome_card %}
```

## sw-user-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| user | `any` | — | yes |  |
| title | `any` | `''` | yes |  |
| isLoading | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| metadata-additional | — | |
| actions | — | |
| summary | — | |
| data-additional | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasActionSlot` | |
| `hasAdditionalDataSlot` | |
| `hasSummarySlot` | |
| `moduleColor` | |
| `salutationFilter` | |

### Examples

#### Basic Usage
```twig
<sw-user-card
    user="..."
    title="..."
>
    <!-- content -->
</sw-user-card>
```

## sw-user-sso-access-key-create-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | yes |  |
| isOpen | `any` | — | yes |  |
| accessKey | `any` | — | yes |  |
| secretAccessKey | `any` | — | yes |  |
| mode | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| access-key-modal-create:cancel | — | |
| access-key-modal-create:save | — | |
| access-key-modal-create:generate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onSave` | |
| `onGenerateNewAccessKey` | |

### Examples

#### Example 1
Source: `sw-users-permissions/page/sw-sso-users-permission-user-detail/sw-sso-users-permission-user-detail.html.twig`
```twig
        <sw-user-sso-access-key-create-modal
            :is-loading="isLoading"
            :is-open="isCreateAccessKeyModalOpen"
            :access-key="newAccessKey"
            :secret-access-key="newSecretAccessKey"
            :mode="editMode"
            @access-key-modal-create:cancel="onAccessKeyCreateCancel"
            @access-key-modal-create:save="onSaveAccessKey"
            @access-key-modal-create:generate="onGenerateNewKey"
        />
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

## sw-user-sso-invitation-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| user-invited | — | |
| invitation-failed | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `componentCreated` | |
| `loadLanguages` | |
| `sendInvitation` | |
| `closeModal` | |
| `validateEmail` | |
| `validateLanguage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `invitationService` | |
| `languageRepository` | |
| `languageCriteria` | |
| `hasError` | |

### Examples

#### Example 1
Source: `sw-users-permissions/components/sw-users-permissions-user-listing/sw-users-permissions-user-listing.html.twig`
```twig
            <sw-user-sso-invitation-modal
                v-if="showInvitationModal"
                @modal-close="closeInvitationModal"
                @user-invited="onUserInvited"
                @invitation-failed="invitationFailed"
            />
            {% endblock %}
        {% endblock %}
        </sw-container>
    </div>

{% block sw_settings_user_list_content %}
    {% block sw_settings_user_list_content_grid %}
    <sw-data-grid
        :data-source="user"
```

## sw-user-sso-status-label

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| user | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `status` | |
| `statusText` | |
| `variant` | |

### Examples

#### Example 1
Source: `sw-users-permissions/components/sw-users-permissions-user-listing/sw-users-permissions-user-listing.html.twig`
```twig
<sw-user-sso-status-label :user="item" />
```

## sw-users-permissions-additional-permissions

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| role | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `isPrivilegeSelected` | |
| `onSelectPrivilege` | |
| `changeAllAppPermissionsForKey` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `additionalPermissions` | |
| `appPermissions` | |

### Examples

#### Example 1
Source: `sw-users-permissions/view/sw-users-permissions-role-view-general/sw-users-permissions-role-view-general.html.twig`
```twig
    <sw-users-permissions-additional-permissions
        :role="role"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```

## sw-users-permissions-configuration

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeLoading` | |

### Examples

#### Example 1
Source: `sw-users-permissions/page/sw-users-permissions/sw-users-permissions.html.twig`
```twig
            <sw-users-permissions-configuration
                ref="configuration"
                @loading-change="onChangeLoading"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

## sw-users-permissions-detailed-additional-permissions

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| role | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| detailedPrivileges | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setDetailedAdditionalPermissions` | |
| `isEntitySelected` | |
| `isEntityDisabled` | |
| `changePermissionForEntity` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `allGeneralSelectedPrivileges` | |

### Examples

#### Example 1
Source: `sw-users-permissions/view/sw-users-permissions-role-view-detailed/sw-users-permissions-role-view-detailed.html.twig`
```twig
    <sw-users-permissions-detailed-additional-permissions
        :role="role"
        :detailed-privileges="detailedPrivileges"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```

## sw-users-permissions-detailed-permissions-grid

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| role | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| detailedPrivileges | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `isEntitySelected` | |
| `isEntityDisabled` | |
| `changePermissionForEntity` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `allEntities` | |
| `allGeneralSelectedPrivileges` | |
| `permissionTypes` | |

### Examples

#### Example 1
Source: `sw-users-permissions/view/sw-users-permissions-role-view-detailed/sw-users-permissions-role-view-detailed.html.twig`
```twig
    <sw-users-permissions-detailed-permissions-grid
        :role="role"
        :detailed-privileges="detailedPrivileges"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />

    {% block sw_users_permissions_role_role_view_general_card_view_additional_permissions %}
    <sw-users-permissions-detailed-additional-permissions
        :role="role"
        :detailed-privileges="detailedPrivileges"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```

## sw-users-permissions-permissions-grid

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| role | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `changePermission` | |
| `addPermission` | |
| `addDependenciesForRole` | |
| `removePermission` | |
| `isPermissionSelected` | |
| `isPermissionDisabled` | |
| `changeAllPermissionsForKey` | |
| `allPermissionsForKeySelected` | |
| `getPermissionsForParent` | |
| `areAllChildrenRolesSelected` | |
| `areAllChildrenWithAllRolesSelected` | |
| `areSomeChildrenRolesSelected` | |
| `areSomeChildrenWithAllRolesSelected` | |
| `isParentRoleDisabled` | |
| `toggleAllChildrenWithRole` | |
| `toggleAllChildrenWithAllRoles` | |
| `parentRoleHasChildRoles` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `permissionsWithParents` | |
| `permissions` | |
| `parents` | |
| `usedDependencies` | |
| `roles` | |

### Examples

#### Example 1
Source: `sw-users-permissions/view/sw-users-permissions-role-view-general/sw-users-permissions-role-view-general.html.twig`
```twig
    <sw-users-permissions-permissions-grid
        :role="role"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}

    {% block sw_users_permissions_role_role_view_general_card_view_additional_permissions %}
    <sw-users-permissions-additional-permissions
        :role="role"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```

## sw-users-permissions-role-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `createNewRole` | |
| `getRole` | |
| `onSave` | |
| `saveRole` | |
| `updateCurrentUser` | |
| `onCloseConfirmPasswordModal` | |
| `saveFinish` | |
| `onCancel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `tooltipSave` | |
| `tooltipCancel` | |
| `languageId` | |
| `roleRepository` | |
| `roleId` | |

### Examples

#### Basic Usage
```twig
<sw-users-permissions-role-detail>
    <!-- content -->
</sw-users-permissions-role-detail>
```

## sw-users-permissions-role-listing

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| get-list | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `onSearch` | |
| `getItemToDelete` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `deleteRole` | |
| `onCloseConfirmPasswordModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `rolesColumns` | |
| `roleRepository` | |
| `roleCriteria` | |
| `showListingResults` | |

### Examples

#### Example 1
Source: `sw-users-permissions/page/sw-users-permissions/sw-users-permissions.html.twig`
```twig
            <sw-users-permissions-role-listing
                ref="roleListing"
                @get-list="reloadUserListing"
            />
            <sw-users-permissions-configuration
                ref="configuration"
                @loading-change="onChangeLoading"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

## sw-users-permissions-role-view-detailed

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| role | `any` | — | yes |  |
| detailedPrivileges | `any` | — | yes |  |

### Examples

#### Basic Usage
```twig
<sw-users-permissions-role-view-detailed
    role="..."
    detailedPrivileges="..."
>
    <!-- content -->
</sw-users-permissions-role-view-detailed>
```

## sw-users-permissions-role-view-general

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| role | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `roleNameError` | |
| `roleDescriptionError` | |

### Examples

#### Basic Usage
```twig
<sw-users-permissions-role-view-general
    role="..."
>
    <!-- content -->
</sw-users-permissions-role-view-general>
```

## sw-users-permissions-user-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `loadUser` | |
| `saveFinish` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `userPasswordError` | |

### Examples

#### Basic Usage
```twig
<sw-users-permissions-user-create>
    <!-- content -->
</sw-users-permissions-user-create>
```

## sw-users-permissions-user-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadLanguages` | |
| `loadUser` | |
| `loadCurrentUser` | |
| `loadKeys` | |
| `addAccessKey` | |
| `checkEmail` | |
| `checkUsername` | |
| `loadMediaItem` | |
| `setMediaItem` | |
| `onUnlinkLogo` | |
| `onDropMedia` | |
| `onOpenMedia` | |
| `onMediaSelectionChange` | |
| `getMediaDefaultFolderId` | |
| `onSearch` | |
| `saveFinish` | |
| `onSave` | |
| `saveUser` | |
| `updateCurrentUser` | |
| `onCancel` | |
| `setPassword` | |
| `onShowDetailModal` | |
| `onCloseDetailModal` | |
| `onSaveIntegration` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `onCloseConfirmPasswordModal` | |
| `updateAuthToken` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `userFirstNameError` | |
| `userLastNameError` | |
| `userEmailError` | |
| `userUsernameError` | |
| `userLocaleIdError` | |
| `userPasswordError` | |
| `identifier` | |
| `fullName` | |
| `userRepository` | |
| `userCriteria` | |
| `aclRoleCriteria` | |
| `languageRepository` | |
| `languageCriteria` | |
| `localeRepository` | |
| `avatarMedia` | |
| `isError` | |
| `hasLanguage` | |
| `disableConfirm` | |
| `isCurrentUser` | |
| `mediaRepository` | |
| `integrationColumns` | |
| `languageId` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `localeOptions` | |

### Examples

#### Basic Usage
```twig
<sw-users-permissions-user-detail>
    <!-- content -->
</sw-users-permissions-user-detail>
```

## sw-users-permissions-user-listing

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| get-list | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getItemToDelete` | |
| `onSearch` | |
| `getList` | |
| `onDelete` | |
| `onUserInvited` | |
| `openInvitationModal` | |
| `closeInvitationModal` | |
| `invitationFailed` | |
| `onConfirmDelete` | |
| `onCloseDeleteModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `userRepository` | |
| `currentUser` | |
| `userDetailRouterLink` | |
| `userCriteria` | |
| `userColumns` | |

### Examples

#### Example 1
Source: `sw-users-permissions/page/sw-users-permissions/sw-users-permissions.html.twig`
```twig
            <sw-users-permissions-user-listing
                ref="userListing"
            />
            <sw-users-permissions-role-listing
                ref="roleListing"
                @get-list="reloadUserListing"
            />
            <sw-users-permissions-configuration
                ref="configuration"
                @loading-change="onChangeLoading"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
```

## sw-users-permissions

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `reloadUserListing` | |
| `onChangeLoading` | |
| `onSave` | |
| `onSaveFinish` | |

### Examples

#### Example 1
Source: `sw-users-permissions/page/sw-users-permissions/sw-users-permissions.html.twig`
```twig
            <sw-users-permissions-user-listing
                ref="userListing"
            />
            <sw-users-permissions-role-listing
                ref="roleListing"
                @get-list="reloadUserListing"
            />
            <sw-users-permissions-configuration
                ref="configuration"
                @loading-change="onChangeLoading"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
```

#### Example 2
Source: `sw-users-permissions/view/sw-users-permissions-role-view-general/sw-users-permissions-role-view-general.html.twig`
```twig
    <sw-users-permissions-permissions-grid
        :role="role"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}

    {% block sw_users_permissions_role_role_view_general_card_view_additional_permissions %}
    <sw-users-permissions-additional-permissions
        :role="role"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```

#### Example 3
Source: `sw-users-permissions/view/sw-users-permissions-role-view-detailed/sw-users-permissions-role-view-detailed.html.twig`
```twig
    <sw-users-permissions-detailed-permissions-grid
        :role="role"
        :detailed-privileges="detailedPrivileges"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />

    {% block sw_users_permissions_role_role_view_general_card_view_additional_permissions %}
    <sw-users-permissions-detailed-additional-permissions
        :role="role"
        :detailed-privileges="detailedPrivileges"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```

## sw-verify-user-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| verified | — | |
| close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSubmitConfirmPassword` | |
| `onCloseConfirmPasswordModal` | |

### Examples

#### Example 1
Source: `sw-profile/page/sw-profile-index/sw-profile-index.html.twig`
```twig
        <sw-verify-user-modal
            v-if="confirmPasswordModal"
            @verified="onVerifyPasswordFinished"
            @close="onCloseConfirmPasswordModal"
        />
        {% endblock %}

        {% block sw_profile_index_media_upload_actions_media_modal %}
        <sw-media-modal-v2
            v-if="showMediaModal"
            :allow-multi-select="false"
            :initial-folder-id="mediaDefaultFolderId"
            :entity-context="user.getEntityName()"
            @modal-close="showMediaModal = false"
            @media-modal-selection-change="onMediaSelectionChange"
```

#### Example 2
Source: `sw-users-permissions/page/sw-users-permissions-user-detail/sw-users-permissions-user-detail.html.twig`
```twig
    <sw-verify-user-modal
        v-if="confirmPasswordModal"
        @verified="saveUser"
        @close="onCloseConfirmPasswordModal"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{%  block sw_setting_user_detail_card_integrations %}
<mt-card
    :title="$tc('sw-users-permissions.users.user-detail.labelIntegrationsCard')"
    position-identifier="sw-users-permissions-user-detail-integrations"
>
    {% block sw_settings_user_detail_grid_toolbar %}
```

#### Example 3
Source: `sw-users-permissions/page/sw-users-permissions-role-detail/sw-users-permissions-role-detail.html.twig`
```twig
        <sw-verify-user-modal
            v-if="confirmPasswordModal"
            @verified="saveRole"
            @close="onCloseConfirmPasswordModal"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 4
Source: `sw-users-permissions/components/sw-users-permissions-role-listing/sw-users-permissions-role-listing.html.twig`
```twig
<sw-verify-user-modal
    v-if="isConfirmingPasswordModalOpen"
    @verified="deleteRole"
    @close="onCloseConfirmPasswordModal"
/>
{% endblock %}

{% block sw_users_permissions_role_listing_grid %}
<sw-data-grid
    v-if="showListingResults"
    :data-source="roles"
    :columns="rolesColumns"
    identifier="roles-grid"
    :show-settings="true"
    :show-selection="false"
```

## sw-version

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getHumanReadableText` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `version` | |

### Examples

#### Basic Usage
```twig
<sw-version>
    <!-- content -->
</sw-version>
```

## sw-vnode-renderer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| node | `any` | — | yes |  |

### Examples

#### Basic Usage
```twig
<sw-vnode-renderer
    node="..."
>
    <!-- content -->
</sw-vnode-renderer>
```

## sw-wizard-dot-navigation

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| pages | `any` | — | yes |  |
| activePage | `any` | — | yes |  |

### Examples

#### Basic Usage
```twig
<sw-wizard-dot-navigation
    pages="..."
    activePage="..."
>
    <!-- content -->
</sw-wizard-dot-navigation>
```

## sw-wizard-page

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isActive | `any` | — | no |  |
| title | `any` | — | no |  |
| position | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
<sw-wizard-page
    :position="0"
    :title="pageTitleSnippet('sw-import-export.profile.generalTab')"
>
    <sw-import-export-new-profile-wizard-general-page
        :profile="profile"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
```

#### Example 2
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
<sw-wizard-page
    :position="csvUploadPagePosition"
    :title="pageTitleSnippet('sw-import-export.profile.csvUploadTab')"
>
    <sw-import-export-new-profile-wizard-csv-page
        :profile="profile"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
```

## sw-wizard

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| showNavigationDots | `any` | — | no |  |
| activePage | `any` | — | no |  |
| leftButtonDisabled | `any` | — | no |  |
| rightButtonDisabled | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| footer-left-button | — | |
| footer-dot-navigation | — | |
| footer-right-button | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| finish | — | |
| pages-updated | — | |
| current-page-change | — | |
| close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `addPage` | |
| `removePage` | |
| `nextPage` | |
| `previousPage` | |
| `changePage` | |
| `onClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasFooterSlot` | |
| `pagesCount` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
<sw-wizard
    ref="wizard"
    class="sw-import-export-new-profile-wizard"
    variant="full"
    :right-button-disabled="nextButtonDisabled"
    :active-page="currentlyActivePage"
    @close="onClose"
    @finish="onFinish"
    @current-page-change="onCurrentPageChange"
>
    {% block sw_import_export_new_profile_wizard_page_general %}
    <sw-wizard-page
        :position="0"
        :title="pageTitleSnippet('sw-import-export.profile.generalTab')"
    >
```

#### Example 2
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
<sw-wizard-page
    :position="2"
    :title="pageTitleSnippet('sw-import-export.profile.mappingsTab')"
>
    <sw-import-export-new-profile-wizard-mapping-page
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
{% endblock %}

{% block sw_import_export_new_profile_wizard_footer_right_button %}
<template #footer-right-button>
```
