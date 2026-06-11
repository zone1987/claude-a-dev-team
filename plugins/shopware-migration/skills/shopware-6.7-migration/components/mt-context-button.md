# mt-context-button

> Button that triggers a context menu dropdown.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| menuWidth | `number` | — | no | |
| menuHorizontalAlign | `"right" | "left"` | — | no | |
| menuVerticalAlign | `"bottom" | "top"` | — | no | |
| icon | `string` | — | no | |
| disabled | `boolean` | — | no | |
| hasError | `boolean` | — | no | |
| autoClose | `boolean` | — | no | |
| title | `string` | — | no | |
| childViews | `View[]` | — | no | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| button | — | |
| button-text | — | |

## Examples

### Basic Usage
```vue
<mt-context-button
>
    <!-- content -->
</mt-context-button>
```
