# sw-media-index

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| routeFolderId | `any` | `null` | no |  |
| fileAccept | `any` | `'*/*'` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateFolder` | |
| `destroyedComponent` | |
| `onUploadsAdded` | |
| `onUploadFinished` | |
| `onUploadFailed` | |
| `onUploadCanceled` | |
| `onChangeLanguage` | |
| `onSearch` | |
| `onItemsDeleted` | |
| `onMediaFoldersDissolved` | |
| `reloadList` | |
| `decrementPendingUploads` | |
| `clearSelection` | |
| `onMediaUnselect` | |
| `updateRoute` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `mediaRepository` | |
| `rootFolder` | |
| `assetFilter` | |

## Examples

### Basic Usage
```twig
<sw-media-index>
    <!-- content -->
</sw-media-index>
```
