# sw-text-editor-toolbar-button

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| buttonConfig | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| isInlineEdit | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| buttonSlot | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| button-click | — | |
| menu-toggle | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `buttonHandler` | |
| `childActive` | |
| `handleButtonClick` | |
| `onToggleMenu` | |
| `getDropdownClasses` | |
| `onChildMounted` | |
| `getTooltipConfig` | |
| `positionLinkMenu` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `tooltipAppearance` | |

## Examples

### Basic Usage
```twig
<sw-text-editor-toolbar-button
    buttonConfig="..."
>
    <!-- content -->
</sw-text-editor-toolbar-button>
```
