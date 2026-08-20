# sw-media-list-selection-v2

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entity | `any` | — | yes |  |
| entityMediaItems | `any` | — | yes |  |
| uploadTag | `any` | `null` | no |  |
| defaultFolderName | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| open-sidebar | — | |
| upload-finish | — | |
| item-sort | — | |
| item-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `updateColumnCount` | |
| `createPlaceholders` | |
| `onUploadsAdded` | |
| `onMediaUploadButtonOpenSidebar` | |
| `successfulUpload` | |
| `onUploadFailed` | |
| `onMediaItemDragSort` | |
| `onDeboundDragDrop` | |
| `removeItem` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `currentCount` | |
| `mediaItems` | |
| `gridAutoRows` | |
| `uploadId` | |
| `defaultFolder` | |

## Examples

### Example 1
Source: `sw-cms/elements/image-slider/config/sw-cms-el-config-image-slider.html.twig`
```twig
        <sw-media-list-selection-v2
            :entity-media-items="mediaItems"
            :entity="entity"
            :upload-tag="uploadTag"
            :default-folder-name="defaultFolderName"
            :disabled="isInherited"
            @upload-finish="onImageUpload"
            @item-remove="onItemRemove"
            @open-sidebar="onOpenMediaModal"
            @item-sort="onItemSort"
        />
    </template>
</sw-cms-inherit-wrapper>
{% endblock %}

```

### Example 2
Source: `sw-cms/elements/image-gallery/config/sw-cms-el-config-image-gallery.html.twig`
```twig
<sw-media-list-selection-v2
    :entity-media-items="mediaItems"
    :entity="entity"
    :upload-tag="uploadTag"
    :default-folder-name="defaultFolderName"
    :disabled="isInherited"
    @upload-finish="onImageUpload"
    @item-remove="onItemRemove"
    @open-sidebar="onOpenMediaModal"
    @item-sort="onItemSort"
/>
{% endblock %}

{% block sw_cms_element_image_gallery_config_media_mapping_preview %}
<template #preview="{ demoValue }">
```
