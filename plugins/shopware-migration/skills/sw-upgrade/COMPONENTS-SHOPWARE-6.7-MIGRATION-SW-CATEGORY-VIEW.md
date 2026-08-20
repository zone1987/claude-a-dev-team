# sw-category-view

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | yes |  |
| type | `any` | `'page'` | no |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `category` | |
| `isCategoryColumn` | |
| `cmsPage` | |
| `isPage` | |
| `isCustomEntity` | |
| `swCategoryViewError` | |

## Examples

### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-category-view
    v-if="category"
    ref="categoryView"
    :is-loading="isLoading"
    :type="category.type"
/>
{% endblock %}

{% block sw_category_content_entry_point_overwrite_modal %}
<sw-category-entry-point-overwrite-modal
    v-if="showEntryPointOverwriteModal"
    :sales-channels="entryPointOverwriteSalesChannels"
    @cancel="cancelEntryPointOverwrite"
    @confirm="confirmEntryPointOverwrite"
/>
```
