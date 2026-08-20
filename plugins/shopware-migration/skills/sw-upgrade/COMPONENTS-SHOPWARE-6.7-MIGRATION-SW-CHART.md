# sw-chart

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `any` | — | yes | Valid: `line`, `area`, `bar`, `radar`, `histogram`, `pie`, `donut`, `scatter`, `bubble`, `heatmap` |
| options | `any` | — | yes |  |
| series | `any` | — | yes |  |
| height | `any` | `400` | no |  |
| fillEmptyValues | `any` | `null` | no |  |
| sort | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `sortSeries` | |
| `addZeroValuesToSeries` | |
| `setDateTime` | |
| `incrementByTimeUnit` | |
| `getZeroValues` | |
| `loadLocaleConfig` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mergedOptions` | |
| `mergedLabels` | |
| `optimizedSeries` | |
| `convertedSeriesStructure` | |
| `generatedLabels` | |
| `needOneDimensionalArray` | |
| `defaultLocale` | |
| `defaultOptions` | |

## Examples

### Example 1
Source: `sw-dashboard/component/sw-dashboard-statistics/sw-dashboard-statistics.html.twig`
```twig
<sw-chart-card
    class="sw-dashboard-statistics__statistics-count"
    :available-ranges="availableRanges"
    :card-subtitle="getCardSubtitle(ordersDateRange)"
    :series="orderCountSeries"
    :options="chartOptionsOrderCount"
    :fill-empty-values="ordersDateRange.aggregate"
    :card-title="$tc('sw-dashboard.monthStats.orderNumber')"
    type="line"
    sort
    position-identifier=""
    @sw-chart-card-range-update="onOrdersRangeUpdate"
>
    <template #range-option="{ range }">
        {{ $tc(`sw-dashboard.monthStats.dateRanges.${range}`) }}
```
