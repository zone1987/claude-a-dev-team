# sw-text-editor-toolbar

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| parentIsActive | `any` | `false` | no |  |
| isInlineEdit | `any` | `false` | no |  |
| selection | `any` | `null` | no |  |
| buttonConfig | `any` | — | yes |  |
| isCodeEdit | `any` | `false` | no |  |
| isTableEdit | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| itemsSlot | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| created-el | — | |
| destroyed-el | — | |
| remove-link | — | |
| text-style-change | — | |
| table-edit | — | |
| on-set-link | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `isOverlayingLeft` | |
| `destroyedComponent` | |
| `onMouseUp` | |
| `setToolbarPosition` | |
| `setSelectionRange` | |
| `setButtonValues` | |
| `isDisabled` | |
| `handleToolbarClick` | |
| `onButtonClick` | |
| `closeExpandedMenu` | |
| `setActiveTags` | |
| `setButtonPositions` | |
| `handleTextStyleChangeLink` | |
| `keepSelection` | |
| `onToggleMenu` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |

## Examples

### Basic Usage
```twig
<sw-text-editor-toolbar>
    <!-- content -->
</sw-text-editor-toolbar>
```
