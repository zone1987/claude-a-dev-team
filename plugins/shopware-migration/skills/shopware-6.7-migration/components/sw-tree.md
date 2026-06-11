# sw-tree

> Tree view component with drag & drop reordering.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | — | yes |  |
| rootParentId | `any` | — | no |  |
| parentProperty | `any` | — | no |  |
| afterIdProperty | `any` | — | no |  |
| childCountProperty | `any` | — | no |  |
| searchable | `any` | — | no |  |
| activeTreeItemId | `any` | — | no |  |
| routeParamsActiveElementId | `any` | — | no |  |
| translationContext | `any` | — | no |  |
| onChangeRoute | `any` | — | no |  |
| disableContextMenu | `any` | — | no |  |
| bindItemsToFolder | `any` | — | no |  |
| sortable | `any` | — | no |  |
| checkItemsInitial | `any` | — | no |  |
| allowDeleteCategories | `any` | — | no |  |
| allowCreateCategories | `any` | — | no |  |
| initiallyExpandedRoot | `any` | — | no |  |
| ariaLabel | `any` | `null` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| search | — | |
| headline | — | |
| items | sortable: sortable | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| checked-elements-count | — | |
| get-tree-items | — | |
| search-tree-items | — | |
| drag-start | — | |
| drag-end | — | |
| delete-element | — | |
| editing-end | — | |
| batch-delete | — | |
| save-tree-items | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeUnmountedComponent` | |
| `handleFocusIn` | |
| `handleKeyDown` | |
| `getItems` | |
| `searchItems` | |
| `getTreeItems` | |
| `updateSorting` | |
| `startDrag` | |
| `endDrag` | |
| `moveDrag` | |
| `openTreeById` | |
| `findTreeByParentId` | |
| `findById` | |
| `onCreateNewItem` | |
| `addSubElement` | |
| `duplicateElement` | |
| `addElement` | |
| `getNewTreeItem` | |
| `deleteElement` | |
| `abortCreateElement` | |
| `onFinishNameingElement` | |
| `deleteSelectedElements` | |
| `checkItem` | |
| `saveItems` | |
| `onDeleteElements` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `activeElementId` | |
| `isSortable` | |
| `isSearched` | |
| `hasActionSlot` | |
| `hasNoItems` | |
| `selectedItemsPathIds` | |
| `checkedItemIds` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-tree
    :sortable="false"
    :items="searchResults"
    :searchable="false"
    :disable-context-menu="true"
    bind-items-to-folder
    :active-tree-item-id="activeFocusId"
    initially-expanded-root
    route-params-active-element-id="snippet"
>

    <template #headline>
        <span></span>
    </template>

```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
        <sw-tree-item
            v-for="item in treeItems"
            :key="item.id"
            should-focus
            :display-checkbox="false"
            :item="item"
            :active="item.active"
            :sortable="sortable"
            :on-change-route="onChangeRoute"
            :active-parent-ids="selectedItemsPathIds"
            :active-item-ids="checkedItemIds"
            @check-item="checkItem"
        >

            <template #actions="{ item }">
```

### Example 3
Source: `sw-category/component/sw-landing-page-tree/sw-landing-page-tree.html.twig`
```twig
<sw-tree
    v-if="!isLoadingInitialData"
    ref="landingPageTree"
    class="sw-landing-page-tree__inner"
    :items="landingPages"
    :sortable="false || undefined"
    :searchable="false"
    :translation-context="translationContext"
    :on-change-route="changeLandingPage"
    :disable-context-menu="disableContextMenu"
    :allow-delete-categories="allowDelete || undefined"
    :allow-create-categories="false"
    :active-tree-item-id="landingPageId"
    @batch-delete="deleteCheckedItems"
    @delete-element="onDeleteLandingPage"
```

### Example 4
Source: `sw-category/component/sw-landing-page-tree/sw-landing-page-tree.html.twig`
```twig
<sw-tree-item
    v-for="item in treeItems"
    :key="item.id"
    :item="item"
    :should-show-active-state="true"
    :allow-duplicate="true"
    :allow-new-categories="false || undefined"
    :allow-delete-categories="allowDelete || undefined"
    :active="item.active"
    :translation-context="translationContext"
    :on-change-route="onChangeRoute"
    :sortable="sortable || undefined"
    :dragged-item="draggedItem"
    :disable-context-menu="disableContextMenu"
    :display-checkbox="allowEdit || undefined"
```

### Example 5
Source: `sw-category/component/sw-category-tree/sw-category-tree.html.twig`
```twig
<sw-tree
    v-if="!isLoadingInitialData"
    ref="categoryTree"
    class="sw-category-tree__inner"
    after-id-property="afterCategoryId"
    :items="categories"
    :sortable="sortable"
    :searchable="false"
    :active-tree-item-id="categoryId"
    :translation-context="translationContext"
    :on-change-route="changeCategory"
    :disable-context-menu="disableContextMenu"
    :allow-delete-categories="allowDelete || undefined"
    initially-expanded-root
    @batch-delete="deleteCheckedItems"
```
