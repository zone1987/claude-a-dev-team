# sw-bulk-edit-save-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemTotal | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| processStatus | `any` | — | yes |  |
| bulkEditData | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| bulk-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `addEventListeners` | |
| `removeEventListeners` | |
| `beforeUnloadListener` | |
| `onModalClose` | |
| `applyChanges` | |
| `redirect` | |
| `setTitle` | |
| `updateButtons` | |
| `onButtonClick` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentStep` | |
| `buttons` | |

## Examples

### Basic Usage
```twig
<sw-bulk-edit-save-modal
    itemTotal="..."
    isLoading="..."
    processStatus="..."
>
    <!-- content -->
</sw-bulk-edit-save-modal>
```
