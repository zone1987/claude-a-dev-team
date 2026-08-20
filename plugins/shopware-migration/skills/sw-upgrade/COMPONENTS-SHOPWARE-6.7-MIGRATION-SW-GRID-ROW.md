# sw-grid-row

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| index | `any` | `null` | no |  |
| allowInlineEdit | `any` | `true` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| actions | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inline-edit-finish | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onInlineEditStart` | |
| `onInlineEditCancel` | |
| `onInlineEditFinish` | |
| `startInlineEditing` | |

## Examples

### Basic Usage
```twig
<sw-grid-row
    item="..."
>
    <!-- content -->
</sw-grid-row>
```
