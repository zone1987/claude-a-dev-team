# sw-select-result-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| options | `any` | — | no |  |
| emptyMessage | `any` | `null` | no |  |
| focusEl | `null \| null` | — | no |  |
| isLoading | `any` | `false` | no |  |
| popoverClasses | `any` | — | no |  |
| popoverResizeWidth | `any` | `true` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| before-item-list | — | |
| result-item | — | |
| after-item-list | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-select | — | |
| active-item-change | — | |
| outside-click | — | |
| paginate | — | |
| item-select-by-keyboard | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyedComponent` | |
| `setActiveItemIndex` | |
| `addEventListeners` | |
| `removeEventListeners` | |
| `onItemSelect` | |
| `emitActiveItemIndex` | |
| `checkOutsideClick` | |
| `navigate` | |
| `navigateNext` | |
| `navigatePrevious` | |
| `updateScrollPosition` | |
| `emitClicked` | |
| `onScroll` | |
| `getBottomDistance` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `emptyMessageText` | |
| `popoverClass` | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-entity-path-select/sw-import-export-entity-path-select.html.twig`
```twig
<sw-select-result-list
    ref="resultsList"
    :options="visibleResults"
    :is-loading="isLoading"
    :empty-message="$tc('global.sw-single-select.messageNoResults', { term: searchInput }, 0)"
    :focus-el="$refs.swSelectInput"
    :popover-classes="resultListClasses"
    @paginate="$emit('paginate')"
    @item-select="setValue"
>
    {% block sw_import_export_entity_path_select_base_results_list %}
    {% block sw_import_export_entity_path_select_base_results_list_before %}
    <template #before-item-list>
        <slot name="before-item-list">
            <sw-select-result
```

### Example 2
Source: `sw-cms/component/sw-cms-product-assignment/sw-cms-product-assignment.html.twig`
```twig
<sw-select-result-list
    ref="swSelectResultList"
    :options="resultCollection"
    :is-loading="isLoadingResults"
    :empty-message="$tc('global.sw-entity-many-to-many-select.messageNoResults', { term: searchTerm }, 0)"
    :focus-el="$refs.searchInput"
    @paginate="paginateResult"
    @item-select="onItemSelect"
>

    {% block sw_cms_product_assignment_results_list_before %}
    <template #before-item-list>
        {% block sw_cms_product_assignment_results_list_before_content %}
        <slot name="before-item-list"></slot>
    {% endblock %}
```

### Example 3
Source: `sw-settings-cache/page/sw-settings-cache-index/sw-settings-cache-index.html.twig`
```twig
<sw-select-result-list :options="[indexers]">
    <template #result-item="{ item, index }">
        <ul
            class="sw-settings-cache__indexers-list"
            @click.stop
        >
            <li
                v-for="(updaters, indexer) in item"
                :key="indexer"
            >
                <mt-checkbox
                    class="sw-settings-cache__indexers-entry"
                    :checked="indexerSelection.includes(indexer)"
                    :label="indexer"
                    :name="indexer"
```
