# sw-meteor-single-select

> A compact single-select dropdown component with search functionality. Displays a label and selected value inline, opening a result list on click. Automatically enables search when there are 7 or more options.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| options | `Array` | — | yes | Array of option objects to select from |
| value | `any` | — | yes | The currently selected value |
| label | `String` | `''` | no | Label text displayed before the selected value |
| isLoading | `Boolean` | `false` | no | Shows a loading state in the result list |
| highlightSearchTerm | `Boolean` | `true` | no | Whether to highlight matching search terms in results |
| placeholder | `String` | `''` | no | Placeholder text when no value is selected |
| labelProperty | `String` | `'label'` | no | Property path to use as the display label in option objects |
| valueProperty | `String` | `'value'` | no | Property path to use as the value in option objects |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| before-item-list | — | Content before the result items (default: search field when searchable) |
| result-item | `{ item, index, labelProperty, searchTerm, highlightSearchTerm, isSelected, setValue, getKey }` | Custom rendering for each result item |
| result-label-property | `{ item, index, labelProperty, valueProperty, searchTerm, highlightSearchTerm, getKey }` | Custom rendering for the label within a result item |
| after-item-list | — | Content after the result items |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | `value: any` | Emitted when the selected value changes |
| search | `searchTerm: String` | Emitted when the search term changes |
| paginate | — | Emitted when pagination is triggered in the result list |

## Methods

| Method | Parameters | Return | Description |
|--------|-----------|--------|-------------|
| isSelected | `(item: Object)` | `Boolean` | Checks if the given item is currently selected |
| toggleResultList | — | `void` | Toggles the result dropdown open/closed |
| openResultList | — | `void` | Opens the result dropdown and resets results to all options |
| closeResultList | — | `void` | Closes the result dropdown and clears the search term |
| setValue | `(item: Object)` | `void` | Sets the selected value from the given item and closes the dropdown |
| onInputSearchTerm | — | `void` | Triggers a debounced search on input |
| search | — | `void` | Filters options by search term and emits the search event |
| getKey | `(object: Object, keyPath: String, defaultValue?: any)` | `any` | Gets a nested value from an object by key path |

## Data

| Name | Type | Default | Description |
|------|------|---------|-------------|
| searchTerm | `String` | `''` | Current search/filter term |
| isExpanded | `Boolean` | `false` | Whether the result dropdown is open |
| results | `Array` | `options` | Filtered result list (initially all options) |
| itemRecentlySelected | `Boolean` | `false` | Tracks if an item was just selected |

## Computed Properties

| Name | Type | Description |
|------|------|-------------|
| currentValue | `any` | Get/set wrapper for the value prop, emits `update:value` on set |
| inputClasses | `Object` | CSS classes based on expanded state |
| selectionTextClasses | `Object` | CSS classes for selection text (placeholder styling) |
| singleSelection | `Object \| undefined` | The currently selected option object |
| selectedValueLabel | `String` | Display label of the selected option, or placeholder if none |
| searchable | `Boolean` | Whether search is enabled (true when options >= 7) |

## Examples

### Example 1: Basic Usage
```html
<sw-meteor-single-select
    label="Sort by"
    :options="sortOptions"
    :value="currentSort"
    @update:value="currentSort = $event"
/>
```

### Example 2: With Custom Label and Value Properties
```html
<sw-meteor-single-select
    label="Language"
    :options="languages"
    :value="selectedLanguageId"
    label-property="name"
    value-property="id"
    placeholder="Select a language..."
    @update:value="onLanguageChange"
/>
```

### Example 3: With Loading State
```html
<sw-meteor-single-select
    label="Category"
    :options="categories"
    :value="selectedCategory"
    :is-loading="isCategoriesLoading"
    @update:value="selectedCategory = $event"
    @paginate="loadMoreCategories"
/>
```

### Example 4: Custom Result Item Rendering
```html
<sw-meteor-single-select
    label="Status"
    :options="statusOptions"
    :value="currentStatus"
    @update:value="currentStatus = $event"
>
    <template #result-item="{ item, isSelected, setValue }">
        <sw-select-result
            :selected="isSelected(item)"
            @item-select="setValue"
        >
            <sw-color-badge :color="item.color" />
            {{ item.label }}
        </sw-select-result>
    </template>
</sw-meteor-single-select>
```

### Example 5: Disabled Search Highlighting
```html
<sw-meteor-single-select
    label="Filter"
    :options="filterOptions"
    :value="activeFilter"
    :highlight-search-term="false"
    @update:value="activeFilter = $event"
/>
```
