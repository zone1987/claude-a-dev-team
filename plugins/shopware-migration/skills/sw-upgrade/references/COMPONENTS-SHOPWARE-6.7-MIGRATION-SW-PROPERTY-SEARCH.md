# sw-property-search

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| collapsible | `any` | `true` | no |  |
| overlay | `any` | `true` | no |  |
| options | `any` | — | yes |  |
| isAddOnly | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| toolbar | focus: onFocusSearch, input: onSearchOptions | |
| toolbar-search-field | — | |
| toolbar-items | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| option-select | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `selectGroup` | |
| `onOptionSelect` | |
| `onGroupPageChange` | |
| `onOptionPageChange` | |
| `onOptionSearchPageChange` | |
| `onFocusSearch` | |
| `onSearchOptions` | |
| `closeOnClickOutside` | |
| `selectOptions` | |
| `showSearch` | |
| `showTree` | |
| `loadGroups` | |
| `loadOptions` | |
| `sortOptions` | |
| `refreshSelection` | |
| `addOptionCount` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `swPropertySearchClasses` | |
| `propertyGroupRepository` | |
| `propertyGroupCriteria` | |
| `propertyGroupOptionRepository` | |
| `propertyGroupOptionCriteria` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-add-properties-modal/sw-product-add-properties-modal.html.twig`
```twig
<sw-property-search
    ref="propertySearch"
    class="sw-product-add-properties-modal__search"
    :options="newProperties"
    :overlay="false"
    :collapsible="false"
    @option-select="onSelectOption"
>
    <template
        #toolbar="{ focus, input, searchTerm }"
    >
        {% block sw_property_search_field %}
        <div class="sw-property-search__toolbar sw-product-add-properties-modal__toolbar">
            <slot name="toolbar">
                <div class="sw-property-search__search-field-container">
```
