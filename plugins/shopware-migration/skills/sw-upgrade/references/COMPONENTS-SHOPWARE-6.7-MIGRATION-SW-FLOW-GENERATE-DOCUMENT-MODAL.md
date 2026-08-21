# sw-flow-generate-document-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClose` | |
| `onAddAction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `documentTypeRepository` | |
| `documentTypeCriteria` | |
| `documentTypes` | |

## Examples

### Basic Usage
```twig
<sw-flow-generate-document-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-generate-document-modal>
```
