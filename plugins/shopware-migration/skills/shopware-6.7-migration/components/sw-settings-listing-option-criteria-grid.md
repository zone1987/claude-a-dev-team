# sw-settings-listing-option-criteria-grid

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productSortingEntity | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| criteria-add | — | |
| criteria-delete | — | |
| inline-edit-save | — | |
| inline-edit-cancel | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchCustomFieldSetIds` | |
| `fetchCustomFields` | |
| `isItemACustomField` | |
| `getCustomFieldByName` | |
| `onAddCriteria` | |
| `getOrderSnippet` | |
| `onRemoveCriteria` | |
| `getCriteriaTemplate` | |
| `onSaveInlineEdit` | |
| `onCancelInlineEdit` | |
| `filterEmptyCustomFields` | |
| `stripCustomFieldPath` | |
| `getCriteriaSnippetByFieldName` | |
| `criteriaIsAlreadyUsed` | |
| `getCustomFieldLabelByCriteriaName` | |
| `getCustomFieldName` | |
| `customFieldCriteriaSingleSelect` | |
| `changeCustomField` | |
| `getProductSortingFieldsByName` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customFieldRepository` | |
| `customFieldSetRepository` | |
| `customFieldSetRelationsRepository` | |
| `customFieldCriteria` | |
| `customFieldsRelationsCriteria` | |
| `sortedProductSortingFields` | |
| `productSortingEntityColumns` | |
| `criteriaOptions` | |
| `orderOptions` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-settings-listing/page/sw-settings-listing-option-create/sw-settings-listing-option-create.html.twig`
```twig
<sw-settings-listing-option-criteria-grid
    v-if="productSortingEntity"
    :product-sorting-entity="productSortingEntity"
    @criteria-delete="onDeleteCriteria"
    @criteria-add="onAddCriteria"
/>
{% endblock %}

{% block sw_settings_listing_option_base_language_switch %}
<!-- eslint-disable vue/valid-v-slot -->
<template #language-switch>
    <sw-language-switch
        :disabled="isNewProductSorting"
        @on-change="onChangeLanguage"
    />
```

### Example 2
Source: `sw-settings-listing/page/sw-settings-listing-option-base/sw-settings-listing-option-base.html.twig`
```twig
        <sw-settings-listing-option-criteria-grid
            v-if="productSortingEntity"
            :product-sorting-entity="productSortingEntity"
            @criteria-delete="onDeleteCriteria"
            @criteria-add="onAddCriteria"
            @inline-edit-save="onSave"
            @inline-edit-cancel="onCancelEditCriteria"
        />
        {% endblock %}

        {% block sw_settings_listing_option_base_smart_bar_actions_grid_delete_modal %}
        <sw-settings-listing-delete-modal
            v-if="toBeDeletedCriteria"
            :title="$tc('sw-settings-listing.base.delete.modalTitle')"
            :description="$tc('sw-settings-listing.base.delete.modalDescription')"
```
