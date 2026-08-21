# sw-media-save-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| initialFolderId | `any` | `null` | no |  |
| initialFileName | `any` | `null` | no |  |
| fileType | `any` | `'png'` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save-media | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `addResizeListener` | |
| `removeOnResizeListener` | |
| `getComponentWidth` | |
| `fetchCurrentFolder` | |
| `getMediaEntityForUpload` | |
| `onSaveMedia` | |
| `onEmitModalClosed` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `mediaRepository` | |

## Examples

### Basic Usage
```twig
<sw-media-save-modal>
    <!-- content -->
</sw-media-save-modal>
```
