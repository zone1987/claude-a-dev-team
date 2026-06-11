# sw-filter-panel

> Filter panel with multiple configurable filter types.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filters | `any` | — | yes |  |
| defaults | `any` | — | yes |  |
| storeKey | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| criteria-changed | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateFilter` | |
| `resetFilter` | |
| `resetAll` | |
| `showFilter` | |
| `getBreadcrumb` | |
| `getLabelName` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `criteria` | |
| `isFilterActive` | |
| `activeFiltersNumber` | |
| `listFilters` | |

## Examples

### Basic Usage
```twig
<sw-filter-panel
    filters="..."
    defaults="..."
    storeKey="..."
>
    <!-- content -->
</sw-filter-panel>
```
