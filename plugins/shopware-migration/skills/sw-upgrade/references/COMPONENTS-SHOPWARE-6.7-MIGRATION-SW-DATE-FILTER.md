# sw-date-filter

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filter | `any` | — | yes |  |
| active | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| filter-reset | — | |
| filter-update | — | |

## Methods

| Method | Description |
|--------|-------------|
| `fromToFieldLabel` | |
| `updateFilter` | |
| `onTimeframeSelect` | |
| `resetFilter` | |
| `resetTimeframe` | |
| `getPreviousQuarterDates` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `dateType` | |
| `isDateTimeType` | |
| `showDivider` | |

## Examples

### Basic Usage
```twig
<sw-date-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-date-filter>
```
