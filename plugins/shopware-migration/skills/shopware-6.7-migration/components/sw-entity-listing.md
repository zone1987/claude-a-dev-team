# sw-entity-listing

> Extended data grid for entity listing with pagination, search, and CRUD operations.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| detailRoute | `any` | `null` | no |  |
| repository | `any` | — | yes |  |
| items | `any` | `null` | no |  |
| dataSource | `null \| null` | — | no |  |
| showSettings | `any` | `true` | no |  |
| steps | `any` | — | no |  |
| fullPage | `any` | `true` | no |  |
| allowInlineEdit | `any` | `true` | no |  |
| allowColumnEdit | `any` | `true` | no |  |
| criteriaLimit | `any` | `25` | no |  |
| allowEdit | `any` | `true` | no |  |
| allowView | `any` | `false` | no |  |
| allowDelete | `any` | `true` | no |  |
| disableDataFetching | `any` | `false` | no |  |
| naturalSorting | `any` | `false` | no |  |
| allowBulkEdit | `any` | `false` | no |  |
| showBulkEditModal | `any` | `false` | no |  |
| bulkGridEditColumns | `any` | — | no |  |
| maximumSelectItems | `any` | `1000` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| bulk-additional | — | |
| bulk-edit-modal | — | |
| bulk-modal-delete-confirm-text | — | |
| bulk-modal-cancel | — | |
| bulk-modal-delete-items | — | |
| bulk-modals-additional | — | |
| detail-action | — | |
| more-actions | — | |
| delete-action | — | |
| delete-confirm-text | — | |
| delete-modal-footer | — | |
| delete-modal-cancel | — | |
| delete-modal-delete-item | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-records | — | |
| delete-item-finish | — | |
| delete-item-failed | — | |
| delete-items-failed | — | |
| items-delete-finish | — | |
| inline-edit-save | — | |
| inline-edit-cancel | — | |
| column-sort | — | |
| page-change | — | |
| bulk-edit-modal-open | — | |
| bulk-edit-modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `applyResult` | |
| `deleteItem` | |
| `deleteItems` | |
| `deleteItemsFinish` | |
| `doSearch` | |
| `save` | |
| `revert` | |
| `sort` | |
| `paginate` | |
| `showDelete` | |
| `closeModal` | |
| `onClickBulkEdit` | |
| `onCloseBulkEditModal` | |
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

## Computed Properties

| Name | Description |
|------|-------------|
| `detailPageLinkText` | |
| `internalDataSource` | |
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
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-entity-listing
    ref="swSettingsCountryGrid"
    class="sw-settings-country-list-grid"
    :data-source="country"
    :columns="getCountryColumns()"
    :repository="countryRepository"
    :full-page="false"
    detail-route="sw.settings.country.detail"
    :show-selection="true"
    :is-loading="isLoading"
    :allow-view="acl.can('country.viewer') || undefined"
    :allow-edit="acl.can('country.editor') || undefined"
    :allow-inline-edit="acl.can('country.editor') || undefined"
    :allow-delete="acl.can('country.deleter') || undefined"
    @inline-edit-save="onInlineEditSave"
```

### Example 2
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
<sw-entity-listing
    :data-source="logs"
    :columns="logColumns"
    :full-page="true"
    :show-settings="true"
    :show-selection="undefined"
    :show-actions="true"
    :sort-by="sortBy"
    :sort-direction="sortDirection"
    :is-loading="isLoading"
    :allow-column-edit="true"
    :repository="logEntryRepository"
    identifier="sw-log-entry-list"
>

```

### Example 3
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-entity-listing
    v-if="!isEmpty"
    ref="swSettingsSearchableContentGrid"
    class="sw-settings-search__searchable-content-list"
    :columns="columns"
    :repository="repository"
    :allow-column-edit="false"
    :full-page="false"
    :show-settings="false"
    :show-selection="false"
    :is-loading="isLoading"
    :data-source="searchConfigs"
    :skeleton-item-amount="searchConfigs && searchConfigs.length"
    :allow-inline-edit="acl.can('product_search_config.editor')"
    @inline-edit-save="onInlineEditSave"
```

### Example 4
Source: `sw-settings-search/component/sw-settings-search-searchable-content-customfields/sw-settings-search-searchable-content-customfields.html.twig`
```twig
<sw-entity-listing
    v-if="!isEmpty"
    ref="customGrid"
    class="sw-settings-search__searchable-content-list"
    :columns="columns"
    :repository="repository"
    :allow-column-edit="false"
    :full-page="false"
    :show-settings="false"
    :show-selection="false"
    :is-loading="isLoading"
    :data-source="searchConfigs"
    :allow-inline-edit="acl.can('product_search_config.editor')"
    :allow-edit="acl.can('product_search_config.editor')"
    :allow-delete="acl.can('product_search_config.deleter')"
```

### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-list/sw-settings-salutation-list.html.twig`
```twig
                    <sw-entity-listing
                        class="sw-settings-salutation-list-grid"
                        :repository="salutationRepository"
                        :is-loading="isLoading"
                        :data-source="salutations"
                        :columns="columns"
                        identifier="sw-settings-salutation-list"
                        :sort-by="sortBy"
                        :sort-direction="sortDirection"
                        :full-page="false"
                        detail-route="sw.settings.salutation.detail"
                        :disable-data-fetching="true"
                        :show-selection="acl.can('salutation.deleter') || undefined"
                        :allow-edit="acl.can('salutation.editor') || undefined"
                        :allow-inline-edit="acl.can('salutation.editor') || undefined"
```
