# sw-select-base

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| showClearableButton | `any` | — | no |  |
| size | `any` | `'default'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-select-selection | — | |
| results-list | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| select-expanded | — | |
| select-collapsed | — | |
| clear | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onMounted` | |
| `onBeforeUnmount` | |
| `handleKeydown` | |
| `toggleExpand` | |
| `expand` | |
| `collapse` | |
| `focusPreviousFormElement` | |
| `listenToClickOutside` | |
| `computePath` | |
| `emitClear` | |
| `focusParentSelect` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `swFieldClasses` | |
| `isClearable` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
<sw-select-base
    class="sw-multi-snippet-select"
    :is-loading="isLoading"
    :error="errorObject"
    v-bind="$attrs"
>
    <template #sw-select-selection="{ identification, error, disabled, size, expand, collapse }">
        <ul
            ref="selectionList"
            class="sw-select-selection-list"
        >
            <!-- eslint-disable vue/no-use-v-if-with-v-for -->
            <li
                v-for="(snippet, index) in value"
                :key="index"
```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-select-base
    class="sw-multi-snippet-select"
    :is-loading="isLoading"
    :error="null"
    v-bind="$attrs"
>
    <template #sw-select-selection="{ identification, error, disabled, size, expand, collapse }">
        <ul
            ref="selectionList"
            class="sw-select-selection-list"
        >
            <!-- eslint-disable vue/no-use-v-if-with-v-for -->
            <li
                v-for="(snippet, index) in selection"
                :key="index"
```

### Example 3
Source: `sw-import-export/component/sw-import-export-entity-path-select/sw-import-export-entity-path-select.html.twig`
```twig
<sw-select-base
    ref="selectBase"
    class="sw-import-export-entity-path-select"
    :is-loading="isLoading"
    v-bind="$attrs"
    @select-expanded="onSelectExpanded"
    @select-collapsed="onSelectCollapsed"
>
    {% block sw_import_export_entity_path_select_base %}
    {% block sw_import_export_entity_path_select_base_selection %}
    <template #sw-select-selection="{ identification, error, disabled, size, setFocusClass, removeFocusClass }">
        {% block sw_import_export_entity_path_select_base_selection_slot %}
        <div class="sw-import-export-entity-path-select__selection">
            {% block sw_import_export_entity_path_select_single_selection_inner %}
            {% block sw_import_export_entity_path_select_single_selection_inner_label %}
```

### Example 4
Source: `sw-cms/component/sw-cms-product-assignment/sw-cms-product-assignment.html.twig`
```twig
<sw-select-base
    v-bind="$attrs"
    ref="selectBase"
    class="sw-cms-product-assignment-select"
    :disabled="disabled"
    :label="selectLabel"
    :is-loading="isLoadingResults"
    @select-expanded="onSelectExpanded"
    @select-collapsed="onSelectCollapsed"
>

    <template #sw-select-selection="{ identification, error, disabled, size, expand, collapse }">
        {% block sw_cms_product_assignment_search_field %}
        <input
            ref="searchInput"
```

### Example 5
Source: `sw-settings-cache/page/sw-settings-cache-index/sw-settings-cache-index.html.twig`
```twig
<sw-select-base
    class="sw-settings-cache__indexers-select"
    :label="indexingMethod === 'skip' ? $tc('sw-settings-cache.section.indexesSkipSelectLabel') : $tc('sw-settings-cache.section.indexesOnlySelectLabel')"
    :disabled="processes.updateIndexes"
>
    <template #sw-select-selection>
        <sw-label
            v-for="(selection, index) in indexerSelection"
            :key="index"
            @dismiss="changeSelection(false, selection)"
        >
            {{ selection }}
        </sw-label>
        <sw-label
            ghost
```
