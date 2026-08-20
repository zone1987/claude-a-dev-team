# sw-category-layout-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| category | `any` | — | yes |  |
| cmsPage | `any` | `null` | no |  |
| isLoading | `any` | `false` | no |  |
| pageTypes | `any` | — | no |  |
| headline | `any` | `''` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onLayoutSelect` | |
| `onLayoutReset` | |
| `openInPagebuilder` | |
| `openLayoutModal` | |
| `closeLayoutModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `pageTypeTitle` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-cms/sw-category-detail-cms.html.twig`
```twig
    <sw-category-layout-card
        v-if="category.type === 'page'"
        v-bind="{ category, cmsPage, isLoading }"
    />
    {% endblock %}

    {% block sw_category_detail_cms_form %}
    <sw-cms-page-form
        v-if="cmsPage && acl.can('category.editor')"
        :page="cmsPage"
    />
    {% endblock %}

</div>
{% endblock %}
```

### Example 2
Source: `sw-category/view/sw-landing-page-detail-cms/sw-landing-page-detail-cms.html.twig`
```twig
    <sw-category-layout-card
        v-bind="{ cmsPage, isLoading }"
        :category="landingPage"
        :page-types="['landingpage']"
        :headline="$tc('sw-landing-page.base.cms.cmsLayoutModalHeadline')"
    />
    {% endblock %}

    {% block sw_landing_page_detail_cms_form %}
    <sw-cms-page-form
        v-if="cmsPage"
        :page="cmsPage"
    />
    {% endblock %}

```
