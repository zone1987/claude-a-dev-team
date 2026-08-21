# mt-chart

> Chart component for data visualization (bar, line, pie charts).

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| series | `any[]` | — | yes | |
| options | `ChartOptions` | `'() => ({'` | no | |
| type | `ApexChart["type"]` | — | no | |
| width | `string | number` | — | no | |
| height | `string | number` | — | no | |

## Examples

### Basic Usage
```vue
<mt-chart
    series="..."
>
</mt-chart>
```
