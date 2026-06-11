# sw-media-modal-folder-settings

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mediaFolderId | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-settings-modal-save | — | |
| media-settings-modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getItemName` | |
| `getUnusedThumbnailSizes` | |
| `getThumbnailSizes` | |
| `addThumbnail` | |
| `checkIfThumbnailExists` | |
| `deleteThumbnail` | |
| `isThumbnailSizeActive` | |
| `thumbnailSizeCheckboxName` | |
| `onActiveTabChanged` | |
| `onChangeThumbnailSize` | |
| `onChangeInheritance` | |
| `onClickSave` | |
| `ensureUniqueDefaultFolder` | |
| `onClickCancel` | |
| `closeModal` | |
| `onInputDefaultFolder` | |
| `loadMediaFolder` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `mediaDefaultFolderRepository` | |
| `mediaThumbnailSizeRepository` | |
| `mediaFolderConfigurationRepository` | |
| `unusedMediaThumbnailSizeCriteria` | |
| `mediaThumbnailSizeCriteria` | |
| `notEditable` | |
| `thumbnailSizeFilter` | |
| `mediaFolderNameError` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-modal-folder-settings
    v-if="showFolderSettings"
    :disabled="!acl.can('media.editor')"
    :media-folder-id="mediaFolder.id"
    @media-settings-modal-save="closeFolderSettings"
    @media-settings-modal-close="closeFolderSettings"
/>
{% endblock %}

{% block sw_media_folder_info_dissolve_modal %}
<sw-media-modal-folder-dissolve
    v-if="showFolderDissolve"
    :items-to-dissolve="[mediaFolder]"
    @media-folder-dissolve-modal-dissolve="onFolderDissolved"
    @media-folder-dissolve-modal-close="closeFolderDissolve"
```
