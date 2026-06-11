# sw-select-result

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| index | `any` | — | yes |  |
| item | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| selected | `any` | `false` | no |  |
| descriptionPosition | `any` | `'right'` | no | Valid: `bottom`, `right`, `left` |
| ariaLabel | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| preview | — | |
| description | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `checkIfSelected` | |
| `checkIfActive` | |
| `onClickResult` | |
| `onMouseEnter` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `resultClasses` | |
| `hasDescriptionSlot` | |

## Examples

### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-select-result
    :selected="isSelected(item)"
    :disabled="!!priceRuleGroups[item.id] || undefined"
    v-bind="{ item, index }"
    @item-select="addItem"
>
    {{ getKey(item,labelProperty) || getKey(item, `translated.${labelProperty}`) }}
</sw-select-result>
```

### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-general/sw-import-export-edit-profile-general.html.twig`
```twig
<sw-select-result
    v-tooltip="{
        showDelay: 300,
        message: $tc('sw-import-export.profile.objectTypeDisabledText'),
        disabled: !shouldDisableObjectType(item)
    }"
    :disabled="item.disabled || shouldDisableObjectType(item)"
    :class="'sw-select-option--' + item.value"
    :selected="isSelected(item)"
    v-bind="{ item, index }"
    @item-select="setValue"
>
    {% block sw_import_export_edit_profile_general_container_object_type_select_result_highlight %}
    <sw-highlight-text
        v-if="highlightSearchTerm && !isSelected(item)"
```

### Example 3
Source: `sw-import-export/component/sw-import-export-edit-profile-general/sw-import-export-edit-profile-general.html.twig`
```twig
<sw-select-result
    v-tooltip="{
        showDelay: 300,
        message: $tc('sw-import-export.profile.profileTypeDisabledText'),
        disabled: !shouldDisableProfileType(item)
    }"
    :disabled="item.disabled || shouldDisableProfileType(item)"
    :class="'sw-select-option--' + item.value"
    :selected="isSelected(item)"
    v-bind="{ item, index }"
    @item-select="setValue"
>
    {% block sw_import_export_edit_profile_general_container_type_result_highlight %}
    <sw-highlight-text
        v-if="highlightSearchTerm && !isSelected(item)"
```

### Example 4
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

### Example 5
Source: `sw-import-export/component/sw-import-export-entity-path-select/sw-import-export-entity-path-select.html.twig`
```twig
<sw-select-result
    :selected="isSelected(item)"
    v-bind="{ item, index }"
    @item-select="setValue"
>
    {% block sw_import_export_entity_path_select_base_results_list_result_label %}
    <slot
        name="result-label-property"
        v-bind="{ item, index, labelProperty, valueProperty, searchTerm, highlightSearchTerm, getKey }"
    >
        <sw-highlight-text
            v-if="highlightSearchTerm"
            :text="getKey(item, labelProperty)"
            :search-term="searchTerm"
        />
```
