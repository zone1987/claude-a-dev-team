# sw-data-grid

> Advanced data grid with sorting, filtering, inline editing, column resizing, and selection.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| dataSource | `any` | — | yes |  |
| columns | `any` | — | yes |  |
| identifier | `any` | `''` | no |  |
| showSelection | `any` | `true` | no |  |
| showActions | `any` | `true` | no |  |
| showHeader | `any` | `true` | no |  |
| showSettings | `any` | `false` | no |  |
| fullPage | `any` | `false` | no |  |
| allowInlineEdit | `any` | `false` | no |  |
| allowColumnEdit | `any` | `false` | no |  |
| isLoading | `any` | `false` | no |  |
| skeletonItemAmount | `any` | `7` | no |  |
| sortBy | `any` | `null` | no |  |
| sortDirection | `any` | `'ASC'` | no |  |
| naturalSorting | `any` | `false` | no |  |
| compactMode | `any` | `true` | no |  |
| plainAppearance | `any` | `false` | no |  |
| showPreviews | `any` | `true` | no |  |
| isRecordEditable | `any` | — | no |  |
| isRecordSelectable | `any` | — | no |  |
| rowsClickable | `any` | `false` | no |  |
| itemIdentifierProperty | `any` | `'id'` | no |  |
| maximumSelectItems | `any` | `null` | no |  |
| preSelection | `any` | `null` | no |  |
| isRecordDisabled | `any` | — | no |  |
| contextButtonMenuWidth | `any` | `220` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| bulk | — | |
| bulk-modals | — | |
| `column-label-${column.property}` | — | |
| additionalSettings | — | |
| customSettings | — | |
| selection-content | — | |
| `preview-${column.property}` | — | |
| `column-${column.property}` | — | |
| actions | item: item | |
| action-modals | item: item | |
| pagination | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-change | — | |
| select-all-items | — | |
| select-item | — | |
| inline-edit-assign | — | |
| inline-edit-save | — | |
| inline-edit-cancel | — | |
| column-sort | — | |
| row-click | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `initGridColumns` | |
| `findUserSetting` | |
| `findUserSettingById` | |
| `applyUserSettings` | |
| `findResizeColumns` | |
| `findPreviewSlots` | |
| `getDefaultColumns` | |
| `createUserGridSetting` | |
| `saveUserSettings` | |
| `getHeaderCellClasses` | |
| `getRowClasses` | |
| `getCellClasses` | |
| `onChangeCompactMode` | |
| `onChangePreviews` | |
| `onChangeColumnVisibility` | |
| `onChangeColumnOrder` | |
| `orderColumns` | |
| `enableInlineEdit` | |
| `hasColumnWithInlineEdit` | |
| `isInlineEdit` | |
| `disableInlineEdit` | |
| `hideColumn` | |
| `renderColumn` | |
| `selectAll` | |
| `selectItem` | |
| `isSelected` | |
| `resetSelection` | |
| `onClickSaveInlineEdit` | |
| `onClickCancelInlineEdit` | |
| `onDbClickCell` | |
| `onClickHeaderCell` | |
| `onRowClick` | |
| `onStartResize` | |
| `onStopResize` | |
| `onResize` | |
| `_handleColumnResizeClasses` | |
| `enableResizeMode` | |
| `setAllColumnElementWidths` | |
| `trackScrollX` | |
| `save` | |
| `revert` | |
| `sort` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `selectionCount` | |
| `reachMaximumSelectionExceed` | |
| `isSelectAllDisabled` | |
| `allSelectedChecked` | |
| `userConfigRepository` | |
| `currentUser` | |
| `userGridSettingCriteria` | |
| `hasInvisibleSelection` | |
| `currentVisibleColumns` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
<sw-data-grid
    class="sw-settings-country-currency-dependent-modal__grid"
    :data-source="currencyDependsValue"
    :is-loading="isLoading"
    :show-selection="false || undefined"
    :plain-appearance="true"
    :columns="countryCurrencyColumns"
>

    {% block sw_settings_country_currency_dependent_modal_content_hamburger_menu %}
    <template #customSettings>
        <sw-settings-country-currency-hamburger-menu
            :options="menuOptions"
            @currency-change="changeCurrencyDependentRow"
        />
```

### Example 2
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
<sw-data-grid
    v-if="items.length !== 0"
    ref="dataGrid"
    :data-source="items"
    :allow-inline-edit="acl.can('product_search_config.editor')"
    :is-loading="isLoading || isExcludedTermsLoading"
    :columns="getSearchableGeneralColumns"
    class="sw-settings-search__grid sw-settings-search-excluded-search-terms_grid"
    @inline-edit-save="onSaveEdit"
    @inline-edit-cancel="onCancelEdit"
    @select-item="selectionChanged"
>
    <template #bulk>
        <mt-button
            variant="critical"
```

### Example 3
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-data-grid
    v-if="products && products.length > 0"
    class="sw-settings-search-live-search__grid-result"
    :plain-appearance="true"
    :show-selection="false"
    :show-actions="false"
    :data-source="products"
    :is-loading="searchInProgress"
    :columns="searchColumns"
>

    {% block sw_settings_search_view_live_search_results_search_grid_columns %}
    {% block sw_settings_search_view_live_search_results_search_grid_name %}
    <template #column-name="{ item }">
        <sw-product-variant-info
```

### Example 4
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-data-grid-column-boolean v-model:value="item.searchable" />
```

### Example 5
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-data-grid-column-boolean v-model:value="item.tokenize" />
```
