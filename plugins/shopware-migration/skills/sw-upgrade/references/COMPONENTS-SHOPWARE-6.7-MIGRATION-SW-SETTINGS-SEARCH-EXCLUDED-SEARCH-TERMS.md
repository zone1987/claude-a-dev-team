# sw-settings-search-excluded-search-terms

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchConfigs | `any` | `null` | no |  |
| isExcludedTermsLoading | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| edit-change | — | |
| data-load | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `resetData` | |
| `addExcludedSearchTerms` | |
| `onInsertTerm` | |
| `renderComponent` | |
| `filterItems` | |
| `sliceItems` | |
| `onPagePagination` | |
| `onDeleteExcludedTerm` | |
| `onSearchTermChange` | |
| `selectionChanged` | |
| `onSaveEdit` | |
| `getOriginItem` | |
| `onCancelEdit` | |
| `onBulkDeleteExcludedTerm` | |
| `saveConfig` | |
| `onResetExcludedSearchTermDefault` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `searchRepository` | |
| `getSearchableGeneralColumns` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-settings-search/view/sw-settings-search-view-general/sw-settings-search-view-general.html.twig`
```twig
    <sw-settings-search-excluded-search-terms
        :search-configs="productSearchConfigs"
        :is-excluded-terms-loading="isLoading"
        @data-load="loadData"
    />
    {% endblock %}
</div>
{% endblock %}

```
