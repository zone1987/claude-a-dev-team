# sw-many-to-many-assignment-card

> Card component for managing many-to-many entity relationships.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| columns | `any` | — | yes |  |
| entityCollection | `any` | — | yes |  |
| localMode | `any` | — | yes |  |
| resultLimit | `any` | `25` | no |  |
| criteria | `any` | — | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| labelProperty | `any` | `'name'` | no |  |
| selectLabel | `any` | `''` | no |  |
| placeholder | `any` | — | no |  |
| searchableFields | `any` | — | no |  |
| disabled | `any` | `false` | no |  |
| displayVariants | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| prepend-select | — | |
| select | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |
| data-grid | — | |
| `column-${column.property}` | — | |
| empty-state | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:entityCollection | — | |
| paginate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initData` | |
| `onSearchTermChange` | |
| `debouncedSearch` | |
| `onSelectExpanded` | |
| `paginateResult` | |
| `searchItems` | |
| `onItemSelect` | |
| `removeItem` | |
| `isSelected` | |
| `resetActiveItem` | |
| `onSelectCollapsed` | |
| `resetSearchCriteria` | |
| `getKey` | |
| `paginateGrid` | |
| `setGridFilter` | |
| `addContainsFilter` | |
| `removeFromGrid` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `context` | |
| `languageId` | |
| `assignmentRepository` | |
| `searchRepository` | |
| `page` | |
| `limit` | |
| `total` | |
| `focusEl` | |
| `originalFilters` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-products/sw-category-detail-products.html.twig`
```twig
<sw-many-to-many-assignment-card
    v-if="category.type !== 'folder'"
    display-variants
    :title="$tc('sw-category.base.products.productAssignmentHeadline')"
    :entity-collection="category.products"
    :columns="productColumns"
    :is-loading="isLoading"
    :disabled="!acl.can('category.editor')"
    :local-mode="category.isNew()"
    :criteria="productCriteria"
    :select-label="$tc('sw-category.base.products.productAssignmentLabel')"
    :placeholder="$tc('sw-category.base.products.productAssignmentPlaceholder')"
    @paginate="onPaginateManualProductAssignment"
>

```

### Example 2
Source: `sw-category/view/sw-category-detail-custom-entity/sw-category-detail-custom-entity.html.twig`
```twig
<sw-many-to-many-assignment-card
    v-else
    :entity-collection="customEntityAssignments"
    :title="$tc('sw-category.base.customEntity.cardTitle')"
    :columns="customEntityColumns"
    :local-mode="category.isNew()"
    label-property="cmsAwareTitle"
    :criteria="sortingCriteria"
    :select-label="$tc('sw-category.base.customEntity.instanceAssignment.label')"
    :placeholder="$tc('sw-category.base.customEntity.instanceAssignment.placeholder')"
    @update:entity-collection="onAssignmentChange"
>
    <template #prepend-select>
        <sw-entity-single-select
            class="sw-category-detail-custom-entity__assignment"
```
