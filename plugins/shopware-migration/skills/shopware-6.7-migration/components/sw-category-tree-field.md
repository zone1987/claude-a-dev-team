# sw-category-tree-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| categoriesCollection | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| placeholder | `any` | — | yes |  |
| categoryCriteria | `any` | — | no |  |
| singleSelect | `any` | `false` | no |  |
| pageId | `any` | `null` | no |  |
| isCategoriesLoading | `any` | `false` | no |  |
| allowedTypes | `any` | `null` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| labelProperty | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-add | — | |
| selection-remove | — | |
| categories-load-more | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `getTreeItems` | |
| `disableCategories` | |
| `onCheckSearchItem` | |
| `onCheckItem` | |
| `removeItem` | |
| `searchCategories` | |
| `isSearchItemChecked` | |
| `isSearchResultInFocus` | |
| `getBreadcrumb` | |
| `getLabelName` | |
| `onDeleteKeyup` | |
| `removeTagLimit` | |
| `openDropdown` | |
| `closeDropdown` | |
| `closeDropdownOnClickOutside` | |
| `handleGeneralKeyEvents` | |
| `handleArrowKeyEvents` | |
| `changeSearchSelection` | |
| `getFirstChildById` | |
| `getSibling` | |
| `toggleSelectedTreeItem` | |
| `findTreeItemVNodeById` | |
| `removeCheckedItems` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `globalCategoryRepository` | |
| `categoryRepository` | |
| `visibleTags` | |
| `numberOfHiddenTags` | |
| `selectedCategoriesItemsIds` | |
| `selectedCategoriesItemsTotal` | |
| `selectedCategoriesPathIds` | |
| `pageCategoryCriteria` | |

## Examples

### Example 1
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

### Example 2
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

### Example 3
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

### Example 4
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

### Example 5
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-category-tree-field
    v-if="!isProductComparison"
    :categories-collection="footerCategories"
    :placeholder="footerCategoryPlaceholder"
    :single-select="true"
    :label="$tc('sw-sales-channel.detail.footerCategory')"
    :disabled="!acl.can('sales_channel.editor')"
    class="sw-sales-channel-detail__select-footer-category-id"
    @selection-add="onFooterSelectionAdd"
    @selection-remove="onFooterSelectionRemove"
/>
{% endblock %}

{% block sw_sales_channel_detail_base_general_input_service_category %}
<sw-category-tree-field
```
