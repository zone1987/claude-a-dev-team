# sw-category-link-settings

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| category | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `changeEntity` | |
| `createCategoryCollection` | |
| `onSelectionAdd` | |
| `onSelectionRemove` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `linkTypeValues` | |
| `entityValues` | |
| `mainType` | |
| `isExternal` | |
| `isInternal` | |
| `productCriteria` | |
| `categoryCriteria` | |
| `internalLinkCriteria` | |
| `categoryRepository` | |
| `categoryLinkPlaceholder` | |
| `allowedCategoryTypes` | |
| `categoryLinkHelpText` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
    <sw-category-link-settings
        v-if="category.type === 'link'"
        v-bind="{ category, isLoading }"
    />
    {% endblock %}

    <template v-if="category.type !== 'link'">
        {% block sw_category_detail_menu %}
        <sw-category-detail-menu v-bind="{ category, isLoading }" />
        {% endblock %}
    </template>

    {% block sw_category_detail_attribute_sets %}
    <mt-card
        v-if="customFieldSetsArray.length > 0"
```
