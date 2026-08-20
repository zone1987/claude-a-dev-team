# sw-upload-status

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `registerListeners` | |
| `getUploadId` | |
| `findByTargetId` | |
| `onUploadEvent` | |
| `onUploadAdded` | |
| `onUploadFinished` | |
| `onUploadFailed` | |
| `onUploadProgress` | |
| `onUploadCancel` | |
| `updateSnackbar` | |
| `showErrorNotification` | |
| `getTransportErrorSnippet` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `snackbar` | |
| `uploadCount` | |
| `hasFailedUploads` | |
| `uploadProgress` | |
| `processedUploadCount` | |
| `uploadComplete` | |
| `snackbarMessage` | |
| `snackbarConfig` | |

## Examples

### Basic Usage
```twig
<sw-upload-status>
    <!-- content -->
</sw-upload-status>
```
