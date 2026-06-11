# sw-media-upload-v2

> Media upload component supporting drag & drop, URL upload, and multi-file upload.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| source | `null \| null \| null` | `null` | no |  |
| variant | `any` | `'regular'` | no | Valid: `compact`, `regular`, `small` |
| uploadTag | `any` | — | yes |  |
| allowMultiSelect | `any` | `true` | no |  |
| addFilesOnMultiselect | `any` | `false` | no |  |
| label | `any` | `null` | no |  |
| buttonLabel | `any` | `''` | no |  |
| defaultFolder | `any` | `null` | no |  |
| targetFolderId | `any` | `null` | no |  |
| helpText | `any` | `null` | no |  |
| sourceContext | `any` | `null` | no |  |
| fileAccept | `any` | `'*/*'` | no |  |
| extensionAccept | `any` | `null` | no |  |
| maxFileSize | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| privateFilesystem | `any` | `false` | no |  |
| useFileData | `any` | `false` | no |  |
| required | `any` | `false` | no |  |
| onMediaUploadSidebarOpen | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-drop | — | |
| media-upload-sidebar-open | — | |
| media-upload-remove-image | — | |
| media-upload-add-file | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `onDrop` | |
| `onDropMedia` | |
| `onDragEnter` | |
| `onDragLeave` | |
| `stopEventPropagation` | |
| `onClickUpload` | |
| `useUrlUpload` | |
| `useFileUpload` | |
| `onClickOpenMediaSidebar` | |
| `onRemoveMediaItem` | |
| `onUrlUpload` | |
| `onFileInputChange` | |
| `handleUpload` | |
| `getMediaEntityForUpload` | |
| `getDefaultFolderId` | |
| `handleMediaServiceUploadEvent` | |
| `checkFileSize` | |
| `checkFileType` | |
| `handleFileCheck` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `defaultFolderRepository` | |
| `mediaRepository` | |
| `showPreview` | |
| `hasOpenMediaButtonListener` | |
| `isDragActiveClass` | |
| `mediaFolderId` | |
| `isUrlUpload` | |
| `isFileUpload` | |
| `uploadUrlFeatureEnabled` | |
| `swFieldLabelClasses` | |
| `buttonFileUploadLabel` | |
| `mediaNameFilter` | |

## Examples

### Example 1
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
<sw-media-upload-v2
    :key="category.id + 'upload'"
    :label="$tc('sw-category.base.menu.imageLabel')"
    variant="regular"
    :disabled="!acl.can('category.editor')"
    :source="mediaItem"
    :upload-tag="category.id"
    :allow-multi-select="false"
    :default-folder="category.getEntityName()"
    @media-drop="onMediaDropped"
    @media-upload-sidebar-open="showMediaModal = true"
    @media-upload-remove-image="onRemoveMediaItem"
/>
{% endblock %}

```

### Example 2
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
<sw-media-upload-v2
    variant="regular"
    :upload-tag="uploadTag"
    :source="previewSource"
    :allow-multi-select="false"
    :default-folder="cmsPageState.pageEntityName"
    :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
    :disabled="isInherited"
    file-accept="video/*"
    @media-upload-sidebar-open="onOpenMediaModal"
    @media-upload-remove-image="onVideoRemove"
/>

<template #preview="{ demoValue }">
    <div class="sw-cms-el-config-video__mapping-preview">
```

### Example 3
Source: `sw-cms/elements/youtube-video/config/sw-cms-el-config-youtube-video.html.twig`
```twig
<sw-media-upload-v2
    variant="regular"
    :upload-tag="uploadTag"
    :source="previewSource"
    :allow-multi-select="false"
    :default-folder="cmsPageState.pageEntityName"
    :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
    :disabled="isInherited"
    @media-upload-sidebar-open="onOpenMediaModal"
    @media-upload-remove-image="onImageRemove"
/>

{% block sw_cms_element_youtube_video_config_preview_media_display %}
<template #preview="{ demoValue }">
    <div class="sw-cms-el-config-image__mapping-preview">
```

### Example 4
Source: `sw-cms/elements/image/config/sw-cms-el-config-image.html.twig`
```twig
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        @media-upload-sidebar-open="onOpenMediaModal"
        @media-upload-remove-image="onImageRemove"
    />

    <template #preview="{ demoValue }">
        <div class="sw-cms-el-config-image__mapping-preview">
            <img
```

### Example 5
Source: `sw-cms/elements/vimeo-video/config/sw-cms-el-config-vimeo-video.html.twig`
```twig
<sw-media-upload-v2
    variant="regular"
    :upload-tag="uploadTag"
    :source="previewSource"
    :allow-multi-select="false"
    :default-folder="cmsPageState.pageEntityName"
    :caption="$tc('sw-cms.elements.general.config.caption.mediaUpload')"
    :disabled="isInherited"
    @media-upload-sidebar-open="onOpenMediaModal"
    @media-upload-remove-image="onImageRemove"
/>

{% block sw_cms_element_vimeo_video_config_preview_media_display %}
<template #preview="{ demoValue }">
    <div class="sw-cms-el-config-image__mapping-preview">
```
