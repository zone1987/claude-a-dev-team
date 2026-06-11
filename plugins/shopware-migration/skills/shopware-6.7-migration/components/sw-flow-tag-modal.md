# sw-flow-tag-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| action | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getTagCollection` | |
| `createTagCollection` | |
| `onAddTag` | |
| `onRemoveTag` | |
| `getEntityOptions` | |
| `getConfig` | |
| `fieldError` | |
| `onSaveTag` | |
| `onClose` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `tagCriteria` | |
| `isNewTag` | |
| `tagRepository` | |
| `tagTitle` | |
| `triggerEvent` | |
| `triggerActions` | |

## Examples

### Basic Usage
```twig
<sw-flow-tag-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-tag-modal>
```
