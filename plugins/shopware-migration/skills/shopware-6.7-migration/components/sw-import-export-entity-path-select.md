# sw-import-export-entity-path-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| entityType | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| placeholder | `any` | `''` | no |  |
| valueProperty | `any` | `'value'` | no |  |
| searchFunction | `any` | — | no |  |
| currencies | `any` | — | no |  |
| languages | `any` | — | no |  |
| customFieldSets | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| paginate | — | |
| update:value | — | |
| before-selection-clear | — | |
| search | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getDefinition` | |
| `propertyFilter` | |
| `isSelected` | |
| `onSelectExpanded` | |
| `tryGetSearchText` | |
| `onSelectCollapsed` | |
| `closeResultList` | |
| `setValue` | |
| `resetActiveItem` | |
| `onInputSearch` | |
| `debouncedSearch` | |
| `search` | |
| `getKey` | |
| `processTranslations` | |
| `getTranslationProperties` | |
| `processPrice` | |
| `getPriceProperties` | |
| `generatePriceProperties` | |
| `processLineItems` | |
| `generateLineItemProperties` | |
| `processTransactions` | |
| `generateTransactionsProperties` | |
| `processDeliveries` | |
| `generateDeliveryProperties` | |
| `processProperties` | |
| `processVisibilities` | |
| `getVisibilityProperties` | |
| `processMedia` | |
| `getMediaProperties` | |
| `processAssignedProducts` | |
| `getAssignedProductsProperties` | |
| `processCategories` | |
| `getCategoryProperties` | |
| `sortOptions` | |
| `getCustomFields` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |
| `inputClasses` | |
| `selectionTextClasses` | |
| `resultListClasses` | |
| `singleSelection` | |
| `visibleResults` | |
| `actualPathPrefix` | |
| `actualPathParts` | |
| `currentEntity` | |
| `processFunctions` | |
| `options` | |
| `results` | |
| `availableIsoCodes` | |
| `lowerCaseIsoCodes` | |
| `availableLocales` | |
| `lowerCaseLocales` | |
| `searchTerm` | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-identifiers/sw-import-export-edit-profile-modal-identifiers.html.twig`
```twig
<sw-import-export-entity-path-select
    v-else
    :value="item.selected"
    :languages="languages"
    :currencies="currencies"
    :entity-type="item.entityName"
    :disabled="profile.systemDefault"
    :custom-field-sets="customFieldSets"
    @update:value="onChangeIdentifier($event, item.entityName)"
>
    <template #before-item-list>
        <span></span>
    </template>
</sw-import-export-entity-path-select>
```

### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-mapping/sw-import-export-edit-profile-modal-mapping.html.twig`
```twig
    <sw-import-export-entity-path-select
        v-model:value="item.key"
        :languages="languages"
        :currencies="currencies"
        :entity-type="profile.sourceEntity"
        :disabled="profile.systemDefault"
        :custom-field-sets="customFieldSets"
    />
</template>
{% endblock %}

{% block sw_import_export_edit_profile_modal_mapping_grid_required_column %}
<template #column-required="{ item }">
    <mt-switch
        v-show="isRequiredBySystem(item)"
```
