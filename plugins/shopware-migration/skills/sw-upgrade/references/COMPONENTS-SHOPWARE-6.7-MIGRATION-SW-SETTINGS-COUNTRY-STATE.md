# sw-settings-country-state

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| country | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| countryStateRepository | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getStateColumns` | |
| `countryStateSelectionChanged` | |
| `onSearchCountryState` | |
| `onDeleteCountryStates` | |
| `onAddCountryState` | |
| `onSaveCountryState` | |
| `onCancelCountryState` | |
| `onClickCountryState` | |
| `refreshCountryStateList` | |
| `getCountryStateName` | |
| `checkEmptyState` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `stateColumns` | |
| `countryStates` | |

## Examples

### Basic Usage
```twig
<sw-settings-country-state
    country="..."
>
    <!-- content -->
</sw-settings-country-state>
```
