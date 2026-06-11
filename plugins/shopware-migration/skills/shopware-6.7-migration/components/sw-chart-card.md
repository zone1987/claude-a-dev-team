# sw-chart-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| availableRanges | `any` | — | no |  |
| defaultRangeIndex | `any` | — | no |  |
| cardTitle | `any` | `''` | no |  |
| cardSubtitle | `any` | `''` | no |  |
| positionIdentifier | `any` | `''` | yes |  |
| helpText | `null \| null` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| header-title | — | |
| header-link | — | |
| range-option | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sw-chart-card-range-update | — | |

## Methods

| Method | Description |
|--------|-------------|
| `dispatchRangeUpdate` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasHeaderLink` | |

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

### Example 2
Source: `sw-dashboard/component/sw-dashboard-statistics/sw-dashboard-statistics.html.twig`
```twig
<sw-chart-card
    class="sw-dashboard-statistics__statistics-sum"
    :available-ranges="availableRanges"
    :card-subtitle="getCardSubtitle(turnoverDateRange)"
    :series="orderSumSeries"
    :options="chartOptionsOrderSum"
    :fill-empty-values="turnoverDateRange.aggregate"
    :card-title="$tc('sw-dashboard.monthStats.turnover')"
    :help-text="$tc('sw-dashboard.monthStats.helperText')"
    type="line"
    sort
    position-identifier=""
    @sw-chart-card-range-update="onTurnoverRangeUpdate"
>
    <template #range-option="{ range }">
```
