# sw-order-document-settings-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| currentDocumentType | `any` | — | yes |  |
| isLoadingDocument | `any` | — | yes |  |
| isLoadingPreview | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-document | — | |
| document-create | — | |
| preview-show | — | |
| page-leave-confirm | — | |
| page-leave | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCreateDocument` | |
| `callDocumentCreate` | |
| `reserveDocumentNumber` | |
| `addAdditionalInformationToDocument` | |
| `onPreview` | |
| `onConfirm` | |
| `onCancel` | |
| `openMediaModal` | |
| `closeMediaModal` | |
| `onAddMediaFromLibrary` | |
| `successfulUploadFromUrl` | |
| `validateFile` | |
| `removeCustomDocument` | |
| `onAddDocument` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `invalidInput` | |
| `documentNumberErrorMessage` | |
| `documentPreconditionsFulfilled` | |
| `modalTitle` | |
| `mediaRepository` | |
| `htmlPreviewDisabled` | |
| `documentNumber` | |

## Examples

### Basic Usage
```twig
<sw-order-document-settings-modal
    order="..."
    currentDocumentType="..."
    isLoadingDocument="..."
>
    <!-- content -->
</sw-order-document-settings-modal>
```
