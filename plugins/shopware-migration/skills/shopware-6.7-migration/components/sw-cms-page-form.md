# sw-cms-page-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |
| elementUpdate | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `sortSlots` | |
| `initVisibility` | |
| `getBlockTitle` | |
| `displaySectionType` | |
| `getSectionName` | |
| `getSectionPosition` | |
| `getDeviceActive` | |
| `displayNotification` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `cmsBlocks` | |
| `cmsElements` | |
| `slotPositions` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-cms/sw-category-detail-cms.html.twig`
```twig
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
    <sw-cms-page-form
        v-if="cmsPage"
        :page="cmsPage"
    />
    {% endblock %}

</div>
{% endblock %}

```

### Example 3
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
    <sw-cms-page-form
        v-if="!isLoading"
        :page="page"
    />
</div>
{% endblock %}

{% block sw_cms_detail_stage_wrapper %}
<div
    v-else
    class="sw-cms-detail__stage"
>

    {% block sw_cms_detail_toolbar_notification %}
    {% block sw_cms_detail_toolbar_notification_errors %}
```

### Example 4
Source: `sw-custom-entity/component/sw-generic-cms-page-assignment/sw-generic-cms-page-assignment.html.twig`
```twig
    <sw-cms-page-form
        v-if="cmsPage"
        :page="cmsPage"
    />

    <sw-cms-layout-modal
        v-if="showLayoutSelection"
        :cms-page-types="allowedPageTypes"
        :pre-selection="cmsPage"
        @modal-layout-select="onLayoutSelect"
        @modal-close="closeLayoutModal"
    />
</div>
{% endblock %}

```

### Example 5
Source: `sw-product/view/sw-product-detail-layout/sw-product-detail-layout.html.twig`
```twig
        <sw-cms-page-form
            v-if="showCmsForm"
            :page="currentPage"
            :element-update="elementUpdate"
        />

        <mt-card
            v-else
            class="sw-product-detail-layout__no-config"
            position-identifier="sw-product-detail-layout-no-config"
            :is-loading="isConfigLoading"
        >
            <p>{{ $tc('sw-product.layout.textNoConfig') }}</p>
        </mt-card>
        {% endblock %}
```
