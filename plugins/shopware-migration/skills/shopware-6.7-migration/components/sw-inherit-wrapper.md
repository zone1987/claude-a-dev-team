# sw-inherit-wrapper

> Wrapper component that handles value inheritance from parent entities.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| inheritedValue | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| label | `any` | `null` | no |  |
| required | `any` | `false` | no |  |
| isAssociation | `any` | `false` | no |  |
| hasParent | `any` | — | no |  |
| customInheritationCheckFunction | `any` | `null` | no |  |
| customRestoreInheritanceFunction | `any` | `null` | no |  |
| customRemoveInheritanceFunction | `any` | `null` | no |  |
| helpText | `any` | `null` | no |  |
| error | `any` | `null` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `updateCurrentValue` | |
| `updateValue` | |
| `toggleInheritance` | |
| `restoreInheritance` | |
| `removeInheritance` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |
| `isInheritField` | |
| `isInherited` | |
| `labelClasses` | |

## Examples

### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-visibility/sw-bulk-edit-product-visibility.html.twig`
```twig
<sw-inherit-wrapper
    ref="productVisibilitiesInheritance"
    v-model:value="product.visibilities"
    :inherited-value="product.visibilities"
    class="sw-product-category-form__visibility_field"
    :custom-remove-inheritance-function="visibilitiesRemoveInheritanceFunction"
    is-association
>
    <template #content="{ currentValue, isInherited, updateCurrentValue }">
        <sw-product-visibility-select
            ref="productVisibility"
            :key="isInherited"
            class="sw-product-detail__select-visibility"
            :entity-collection="currentValue"
            :placeholder="$tc('sw-product.visibility.placeholderVisibility')"
```

### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-custom-fields/sw-bulk-edit-custom-fields.html.twig`
```twig
<sw-inherit-wrapper
    v-if="entity && customField.config"
    v-model:value="entity.customFields[customField.name]"
    v-bind="getInheritWrapperBind(customField)"
    :class="'sw-form-field-renderer-field__' + customField.name"
    :has-parent="hasParent"
    :required="customField.config.validation === 'required'"
    :inherited-value="getInheritedCustomField(customField.name)"
    @update:value="updateCustomField(customField)"
>
    <template #content="props">
        <sw-form-field-renderer
            v-bind="getBind(customField, props)"
            :key="props.isInherited"
            :class="'sw-form-field-renderer-input-field__' + customField.name"
```

### Example 3
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
<sw-inherit-wrapper
    v-if="config && index === 0"
    v-model:value="config['core.listing.defaultSorting']"
    :label="$tc('sw-settings-listing.general.labelDefaultSorting')"
    :has-parent="isNotDefaultSalesChannel"
    :inherited-value="inheritance['core.listing.defaultSorting']"
    required
>
    <template #content="{ isInherited, currentValue, updateCurrentValue }">
        <sw-single-select
            class="sw-settings-listing-index__default-sorting-select"
            :placeholder="$tc('sw-settings-listing.general.placeholderDefaultSorting')"
            :disabled="isInherited"
            :value="currentValue"
            :options="productSortingOptions"
```

### Example 4
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
<sw-inherit-wrapper
    v-if="config && index === 0"
    v-model:value="config['core.listing.defaultSearchResultSorting']"
    :label="$tc('sw-settings-listing.general.labelDefaultSearchResultSorting')"
    :has-parent="isNotDefaultSalesChannel"
    :inherited-value="inheritance['core.listing.defaultSearchResultSorting']"
    required
>
    <template #content="{ isInherited, currentValue, updateCurrentValue }">
        <sw-single-select
            class="sw-settings-listing-index__default-search-result-sorting-select"
            :placeholder="$tc('sw-settings-listing.general.placeholderDefaultSearchResultSorting')"
            :disabled="isInherited"
            :value="currentValue"
            :options="searchResultSortingOptions"
```

### Example 5
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
<sw-inherit-wrapper
    v-model:value="selectedShopPages[shopPageSalesChannelId]"
    :inherited-value="selectedShopPages.null"
    :has-parent="shopPageSalesChannelId !== null"
    :label="$tc('sw-cms.components.cmsLayoutAssignmentModal.labelShopPages')"
>
    <template #content="props">
        <sw-multi-select
            class="sw-cms-layout-assignment-modal__shop-page-select"
            :options="shopPages"
            :disabled="props.isInherited"
            :value="props.currentValue"
            :map-inheritance="props"
            @update:value="props.updateCurrentValue"
        />
```
