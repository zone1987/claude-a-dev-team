# sw-text-editor-toolbar-table-button

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| buttonConfig | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| mounted | — | |
| table-create | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `onMouseOverColumn` | |
| `setSelectedTableColsAndRows` | |
| `setSelectedCols` | |
| `setSelectedRows` | |
| `loopTableRows` | |
| `loopTableCols` | |
| `onMouseOut` | |
| `onLastRowMouseOut` | |
| `onLastColMouseOut` | |
| `emitTable` | |
| `createHtmlTable` | |

## Examples

### Basic Usage
```twig
<sw-text-editor-toolbar-table-button
    buttonConfig="..."
>
    <!-- content -->
</sw-text-editor-toolbar-table-button>
```
