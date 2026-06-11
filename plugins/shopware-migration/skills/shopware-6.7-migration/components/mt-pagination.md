# mt-pagination

> Pagination control with page navigation and items-per-page selector.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentPage | `number` | — | yes | |
| limit | `number` | — | yes | |
| totalItems | `number` | — | yes | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-current-page | value: number | |

## Examples

### Basic Usage
```vue
<mt-pagination
    currentPage="..."
    limit="..."
    totalItems="..."
>
</mt-pagination>
```
