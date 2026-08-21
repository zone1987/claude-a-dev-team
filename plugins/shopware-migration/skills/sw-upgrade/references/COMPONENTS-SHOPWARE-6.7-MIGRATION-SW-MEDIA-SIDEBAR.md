# sw-media-sidebar

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | — | yes |  |
| currentFolderId | `any` | `null` | no |  |
| editable | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-sidebar-folder-renamed | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchCurrentFolder` | |
| `onMediaFolderRenamed` | |
| `onFirstItemUpdated` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `mediaNameFilter` | |
| `mediaSidebarClasses` | |
| `isSingleFile` | |
| `isMultipleFile` | |
| `headLine` | |
| `getSelectedFilesCount` | |
| `firstEntity` | |
| `assetFilter` | |
| `filteredAttributes` | |

## Examples

### Example 1
Source: `sw-media/page/sw-media-index/sw-media-index.html.twig`
```twig
            <sw-media-sidebar
                :items="selectedItems"
                :current-folder-id="routeFolderId"
                editable
                @media-sidebar-folder-renamed="updateFolder"
                @media-sidebar-items-delete="onItemsDeleted"
                @media-sidebar-folder-items-dissolve="onMediaFoldersDissolved"
                @media-sidebar-items-move="reloadList"
                @media-item-replaced="reloadList"
                @media-item-selection-remove="onMediaUnselect"
            />
            {% endblock %}

            {% block sw_media_index_list_grid_loader %}
            <sw-loader v-if="isLoading" />
```

### Example 2
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
    <sw-media-sidebar
        :items="selection"
        :current-folder-id="null"
        @media-sidebar-items-delete="onItemsDeleted"
        @media-sidebar-folder-items-dissolve="onMediaFoldersDissolved"
        @media-sidebar-items-move="refreshList"
        @media-item-selection-remove="onMediaRemoveSelected"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_media_modal_v2_modal_footer %}
<template #footer>
    <div class="sw-media-modal-v2__footer">
```
