# sw-datepicker-deprecated

> **Deprecated in 6.7** — Use `mt-datepicker` instead. Will be removed in 6.8.
> See [mt-datepicker](mt-datepicker.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-datepicker>` | `<mt-datepicker>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |
| config | `any` | — | no |  |
| dateType | `any` | `'date'` | no | Valid: `time`, `date`, `datetime` |
| placeholder | `any` | `''` | no |  |
| required | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| hideHint | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `setDatepickerValue` | |
| `getMergedConfig` | |
| `updateFlatpickrInstance` | |
| `createFlatpickrInstance` | |
| `getEventNames` | |
| `openDatepicker` | |
| `kebabToCamel` | |
| `unsetValue` | |
| `emitValue` | |
| `createConfig` | |
| `getDateStringFormat` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `locale` | |
| `currentFlatpickrConfig` | |
| `placeholderText` | |
| `suffixName` | |
| `noCalendar` | |
| `enableTime` | |
| `additionalAttrs` | |
| `userTimeZone` | |
| `timezoneFormattedValue` | |
| `showTimeZoneHint` | |
| `timeZoneHint` | |
| `is24HourFormat` | |

## Examples

### Basic Usage
```twig
<sw-datepicker-deprecated>
    <!-- content -->
</sw-datepicker-deprecated>
```
