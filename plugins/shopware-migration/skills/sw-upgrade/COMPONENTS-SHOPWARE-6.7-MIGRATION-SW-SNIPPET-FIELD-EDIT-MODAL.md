# sw-snippet-field-edit-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| snippets | `any` | — | yes |  |
| snippetSets | `any` | — | yes |  |
| translationKey | `any` | — | yes |  |
| fieldType | `any` | — | yes | Valid: `text`, `textarea` |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `closeModal` | |
| `getNoPermissionsTooltip` | |
| `onSave` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `currentAuthor` | |
| `snippetRepository` | |
| `textField` | |
| `textArea` | |

## Examples

### Basic Usage
```twig
<sw-snippet-field-edit-modal
    snippets="..."
    snippetSets="..."
    translationKey="..."
>
    <!-- content -->
</sw-snippet-field-edit-modal>
```
