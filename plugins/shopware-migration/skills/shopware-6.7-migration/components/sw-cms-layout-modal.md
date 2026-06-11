# sw-cms-layout-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| headline | `any` | `''` | no |  |
| cmsPageTypes | `any` | — | no |  |
| preSelection | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-layout-select | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `selectLayout` | |
| `selectInGrid` | |
| `selectItem` | |
| `onSearch` | |
| `toggleListMode` | |
| `gridItemClasses` | |
| `closeModal` | |
| `getPageType` | |
| `getDefaultLayouts` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `pageRepository` | |
| `cmsPageCriteria` | |
| `columnConfig` | |
| `gridPreSelection` | |
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-category/component/sw-category-layout-card/sw-category-layout-card.html.twig`
```twig
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :cms-page-types="pageTypes"
    :headline="headline"
    :pre-selection="cmsPage"
    @modal-layout-select="onLayoutSelect"
    @modal-close="closeLayoutModal"
/>
{% endblock %}

{% block sw_category_detail_layout_desc %}
<div class="sw-category-layout-card__desc">

    {% block sw_category_detail_layout_desc_info %}
    <div class="sw-category-layout-card__desc-info">
```

### Example 2
Source: `sw-category/component/sw-category-entry-point-modal/sw-category-entry-point-modal.html.twig`
```twig
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :pre-selection="selectedSalesChannel.homeCmsPage"
    :cms-page-types="pageTypes"
    @modal-layout-select="onLayoutSelect"
    @modal-close="closeLayoutModal"
/>
{% endblock %}

{% block sw_category_entry_point_modal_layout_desc %}
<div class="sw-category-entry-point-modal__desc">

    {% block sw_category_entry_point_modal_layout_desc_info %}
    <div class="sw-category-entry-point-modal__desc-info">

```

### Example 3
Source: `sw-custom-entity/component/sw-generic-cms-page-assignment/sw-generic-cms-page-assignment.html.twig`
```twig
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

### Example 4
Source: `sw-product/view/sw-product-detail-layout/sw-product-detail-layout.html.twig`
```twig
    <sw-cms-layout-modal
        v-if="showLayoutModal"
        :headline="$tc('sw-product.layoutAssignment.subtitle')"
        :pre-selection="currentPage"
        :cms-page-types="['product_detail']"
        @modal-layout-select="onSelectLayout"
        @modal-close="onCloseLayoutModal"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_product_detail_layout_cms_config %}
<template v-if="acl.can('product.editor') && currentPage">
    {% block sw_product_detail_layout_cms_config_form %}
```
