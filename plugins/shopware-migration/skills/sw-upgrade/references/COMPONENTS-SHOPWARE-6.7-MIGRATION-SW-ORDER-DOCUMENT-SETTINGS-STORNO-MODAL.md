# sw-order-document-settings-storno-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| currentDocumentType | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-document | — | |
| loading-preview | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCreateDocument` | |
| `onPreview` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `documentPreconditionsFulfilled` | |
| `invoices` | |
| `documentNumber` | |
| `invoiceOptions` | |

## Examples

### Basic Usage
```twig
<sw-order-document-settings-storno-modal
    order="..."
    currentDocumentType="..."
>
    <!-- content -->
</sw-order-document-settings-storno-modal>
```
