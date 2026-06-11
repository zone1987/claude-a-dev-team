# sw-cms-list

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadGridUserSettings` | |
| `updateLimit` | |
| `saveGridUserSettings` | |
| `setPageContext` | |
| `getList` | |
| `addLinkedLayoutsAggregation` | |
| `showDefaultLayoutContextMenu` | |
| `getDefaultLayouts` | |
| `onOpenLayoutSetAsDefault` | |
| `onCloseLayoutSetAsDefault` | |
| `onConfirmLayoutSetAsDefault` | |
| `layoutIsLinked` | |
| `resetList` | |
| `getDefaultFolderId` | |
| `onChangeLanguage` | |
| `onListItemClick` | |
| `onSortingChanged` | |
| `onSearch` | |
| `onSortPageType` | |
| `onPageChange` | |
| `onCreateNewLayout` | |
| `onListModeChange` | |
| `onPreviewChange` | |
| `onPreviewImageRemove` | |
| `onModalClose` | |
| `onPreviewImageChange` | |
| `onRenameCmsPage` | |
| `onCloseRenameModal` | |
| `onConfirmPageRename` | |
| `onDeleteCmsPage` | |
| `onDuplicateCmsPage` | |
| `onCloseDeleteModal` | |
| `onConfirmPageDelete` | |
| `saveCmsPage` | |
| `deleteCmsPage` | |
| `getColumnConfig` | |
| `deleteDisabledToolTip` | |
| `getPageType` | |
| `getPageCategoryCount` | |
| `getPageProductCount` | |
| `getPageLandingPageCount` | |
| `getPageCount` | |
| `getPages` | |
| `getPagesString` | |
| `getPagesTooltip` | |
| `optionContextDeleteDisabled` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `pageRepository` | |
| `defaultFolderRepository` | |
| `columnConfig` | |
| `sortPageTypes` | |
| `listCriteria` | |
| `associatedCategoryBuckets` | |
| `associatedProductBuckets` | |
| `isLinkedCriteria` | |
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-category/component/sw-category-layout-card/sw-category-layout-card.html.twig`
```twig
    <sw-cms-list-item
        :page="cmsPage"
        :disabled="!acl.can('category.editor')"
        active
    />
</div>
{% endblock %}

{% block sw_category_detail_layout_modal %}
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :cms-page-types="pageTypes"
    :headline="headline"
    :pre-selection="cmsPage"
    @modal-layout-select="onLayoutSelect"
```

### Example 2
Source: `sw-category/component/sw-category-entry-point-modal/sw-category-entry-point-modal.html.twig`
```twig
    <sw-cms-list-item
        class="sw-category-entry-point-modal__layout-item"
        :page="selectedSalesChannel.homeCmsPage"
        :disabled="!acl.can('category.editor') || undefined"
        active
    />
</div>
{% endblock %}

{% block sw_category_entry_point_modal_layout_modal %}
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :pre-selection="selectedSalesChannel.homeCmsPage"
    :cms-page-types="pageTypes"
    @modal-layout-select="onLayoutSelect"
```

### Example 3
Source: `sw-cms/page/sw-cms-list/sw-cms-list.html.twig`
```twig
<sw-cms-list-item
    v-for="(cmsPage, index) in pages"
    :key="cmsPage.id"
    :class="'sw-cms-list-item--' + index"
    :page="cmsPage"
    :active="layoutIsLinked(cmsPage.id)"
    :is-default="[defaultProductId, defaultCategoryId].includes(cmsPage.id)"
    @item-click="onListItemClick"
    @preview-image-change="onPreviewChange"
    @cms-page-delete="onDeleteCmsPage"
>
    <template #contextMenu>
        <sw-context-button class="sw-cms-list-item__options">
            {% block sw_cms_list_listing_list_item_option_add_preview %}
            <sw-context-menu-item
```

### Example 4
Source: `sw-cms/component/sw-cms-layout-modal/sw-cms-layout-modal.html.twig`
```twig
            <sw-cms-list-item
                :page="cmsPage"
                :is-default="[defaultProductId, defaultCategoryId].includes(cmsPage.id)"
                @element-click="selectItem(cmsPage)"
                @item-click="selectItem(cmsPage)"
            />
            {% endblock %}

            {% endblock %}
        </div>
    </sw-container>

    {% block sw_cms_layout_modal_content_pagination %}
    <sw-pagination
        class="sw-cms-layout-modal__content-pagination"
```

### Example 5
Source: `sw-custom-entity/component/sw-generic-cms-page-assignment/sw-generic-cms-page-assignment.html.twig`
```twig
<sw-cms-list-item
    active
    :page="cmsPage"
    @on-item-click="openLayoutModal"
/>

<div class="sw-generic-cms-page-assignment__page-selection">
    <div class="sw-generic-cms-page-assignment__page-selection-info">
        <div
            class="sw-generic-cms-page-assignment__page-selection-headline"
            :class="{ 'is--empty': !cmsPage }"
        >
            {{ cmsPage ? cmsPage.name : $tc('sw-category.base.cms.defaultTitle') }}
        </div>
        <div
```
