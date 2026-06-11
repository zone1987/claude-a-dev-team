# sw-dashboard-statistics

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `calculateTodayBucket` | |
| `initializeOrderData` | |
| `getHistoryOrderData` | |
| `fetchHistoryOrderDataCount` | |
| `fetchHistoryOrderDataSum` | |
| `fetchHistory` | |
| `fetchTodayData` | |
| `formatDateToISO` | |
| `formatChartHeadlineDate` | |
| `orderGridColumns` | |
| `getVariantFromOrderState` | |
| `parseDate` | |
| `onOrdersRangeUpdate` | |
| `onTurnoverRangeUpdate` | |
| `getCardSubtitle` | |
| `getDateAgo` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `rangesValueMap` | |
| `availableRanges` | |
| `chartOptionsOrderCount` | |
| `chartOptionsOrderSum` | |
| `orderRepository` | |
| `orderCountSeries` | |
| `orderCountToday` | |
| `orderSumMonthSeries` | |
| `orderSumSeries` | |
| `orderSumToday` | |
| `hasOrderToday` | |
| `hasOrderInMonth` | |
| `today` | |
| `todayBucketCount` | |
| `todayBucketSum` | |
| `systemCurrencyISOCode` | |
| `isSessionLoaded` | |
| `currencyFilter` | |
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-dashboard/page/sw-dashboard-index/sw-dashboard-index.html.twig`
```twig
<sw-dashboard-statistics />
```
