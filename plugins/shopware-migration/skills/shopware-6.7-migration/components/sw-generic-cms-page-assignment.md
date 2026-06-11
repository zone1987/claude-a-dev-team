# sw-generic-cms-page-assignment

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| cmsPageId | `any` | `null` | no |  |
| slotOverrides | `any` | `null` | no |  |
| allowedPageTypes | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `openLayoutModal` | |
| `closeLayoutModal` | |
| `onLayoutSelect` | |
| `openInCmsEditor` | |
| `createNewLayout` | |
| `applySlotOverrides` | |
| `getCmsPage` | |
| `deleteSpecificKeys` | |
| `emitCmsPageOverrides` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `cmsPageRepository` | |
| `changesetGenerator` | |
| `cmsPageCriteria` | |
| `pageTypeTitle` | |

## Examples

### Example 1
Source: `sw-custom-entity/page/sw-generic-custom-entity-detail/sw-generic-custom-entity-detail.html.twig`
```twig
<sw-generic-cms-page-assignment
    v-if="active === 'cms-aware-tab-layout'"
    :cms-page-id="customEntityData?.swCmsPageId"
    :slot-overrides="customEntityData?.swSlotConfig"
    class="sw-generic-custom-entity-detail__tab sw-generic-custom-entity-detail__tab-cms-aware"
    @update:cms-page-id="updateCmsPageId"
    @update:slot-overrides="updateCmsSlotOverwrites"
    @create-layout="onCreateLayout"
/>

<template
    v-else-if="active === 'cms-aware-tab-seo'"
>
    <sw-generic-seo-general-card
        :seo-meta-title="customEntityData?.swSeoMetaTitle"
```
