# sw-category-tree

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| categoryId | `any` | `null` | no |  |
| currentLanguageId | `any` | — | yes |  |
| allowEdit | `any` | `true` | no |  |
| allowCreate | `any` | `true` | no |  |
| allowDelete | `any` | `true` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| category-checked-elements-count | — | |
| unsaved-changes | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `openInitialTree` | |
| `loadActiveCategory` | |
| `onUpdatePositions` | |
| `syncProducts` | |
| `indexProducts` | |
| `checkedElementsCount` | |
| `deleteCheckedItems` | |
| `onDeleteCategory` | |
| `fixSortingForCategories` | |
| `getNextCategory` | |
| `changeCategory` | |
| `onGetTreeItems` | |
| `getChildrenFromParent` | |
| `loadRootCategories` | |
| `createNewElement` | |
| `createNewCategory` | |
| `syncSiblings` | |
| `addCategory` | |
| `addCategories` | |
| `removeFromStore` | |
| `getDeletedIds` | |
| `getCategoryUrl` | |
| `isHighlighted` | |
| `isErrorNavigationEntryPoint` | |
| `entryPointWarningMessage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `categoriesToDelete` | |
| `categoryRepository` | |
| `category` | |
| `categories` | |
| `disableContextMenu` | |
| `contextMenuTooltipText` | |
| `criteria` | |
| `criteriaWithChildren` | |
| `cmsPageRepository` | |
| `productRepository` | |

## Examples

### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
        <sw-category-tree
            ref="categoryTree"
            :category-id="categoryId"
            :current-language-id="currentLanguageId"
            :allow-edit="acl.can('category.editor')"
            :allow-create="acl.can('category.creator')"
            :allow-delete="acl.can('category.deleter')"
            @unsaved-changes="openChangeModal"
            @category-checked-elements-count="categoryCheckedElementsCount"
        />
        {% endblock %}

    </template>
</sw-sidebar-collapse>
{% endblock %}
```

### Example 2
Source: `sw-category/component/sw-category-link-settings/sw-category-link-settings.html.twig`
```twig
    <sw-category-tree-field
        :allowed-types="allowedCategoryTypes"
        :categories-collection="categoriesCollection"
        :placeholder="categoryLinkPlaceholder"
        :category-criteria="categoryCriteria"
        :single-select="true"
        :label="$t('global.entities.category')"
        :help-text="categoryLinkHelpText"
        class="sw-category-link-settings__selection-category"
        @selection-add="onSelectionAdd"
        @selection-remove="onSelectionRemove"
    />
</template>
{% endblock %}

```

### Example 3
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
    <sw-category-tree-field
        key="categorySelect"
        :categories-collection="page.categories"
        :label="$tc('sw-cms.components.cmsLayoutAssignmentModal.labelCategories')"
        :placeholder="$tc('sw-cms.components.cmsLayoutAssignmentModal.placeholderCategories')"
        :page-id="page.id"
        :is-categories-loading="isCategoriesLoading"
        class="sw-cms-layout-assignment-modal__category-select"
        @categories-load-more="onExtraCategories"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_cms_layout_assignment_modal_shop_pages_select %}
```

### Example 4
Source: `sw-product/component/sw-product-category-form/sw-product-category-form.html.twig`
```twig
            <sw-category-tree-field
                :key="isInherited"
                class="sw-product-detail__select-category"
                :categories-collection="currentValue ? currentValue : []"
                :disabled="isInherited || !allowEdit"
                :placeholder="$tc('sw-product.categoryForm.placeholderCategory')"
            />
        </template>
    </sw-inherit-wrapper>
</sw-container>
{% endblock %}

{% block sw_product_category_form_tags_field %}
<sw-inherit-wrapper
    v-if="showModeSetting"
```

### Example 5
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
    <sw-category-tree-field
        v-if="!isProductComparison"
        id="navigationCategoryId"
        required
        :categories-collection="mainCategories"
        :placeholder="navigationCategoryPlaceholder"
        :single-select="true"
        :label="$tc('sw-sales-channel.detail.navigationCategoryId')"
        :disabled="!acl.can('sales_channel.editor') || undefined"
        :help-text="$tc('sw-sales-channel.detail.navigationCategoryHelpText')"
        :error="salesChannelNavigationCategoryIdError"
        class="sw-sales-channel-detail__select-navigation-category-id"
        @selection-add="onMainSelectionAdd"
        @selection-remove="onMainSelectionRemove"
    />
```
