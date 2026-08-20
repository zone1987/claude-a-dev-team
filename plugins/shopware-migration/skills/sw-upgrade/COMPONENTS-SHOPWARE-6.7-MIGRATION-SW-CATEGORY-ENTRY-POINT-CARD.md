# sw-category-entry-point-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| category | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `getInitialEntryPointFromCategory` | |
| `onEntryPointChange` | |
| `onSalesChannelChange` | |
| `resetSalesChannelCollections` | |
| `openConfigureHomeModal` | |
| `closeConfigureHomeModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `entryPoints` | |
| `associatedCollection` | |
| `helpText` | |
| `hasExistingNavigation` | |
| `salesChannelSelectionLabel` | |
| `salesChannelCriteria` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
<sw-category-entry-point-card
    v-if="(category.type === 'folder' || category.type === 'page') && !isCategoryColumn"
    v-bind="{ category, isLoading }"
/>
{% endblock %}

{% block sw_category_detail_link %}
<sw-category-link-settings
    v-if="category.type === 'link'"
    v-bind="{ category, isLoading }"
/>
{% endblock %}

<template v-if="category.type !== 'link'">
    {% block sw_category_detail_menu %}
```
