# sw-number-field-deprecated

> **Deprecated in 6.7** — Use `mt-number-field` instead. Will be removed in 6.8.
> See [mt-number-field](mt-number-field.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-number-field>` | `<mt-number-field>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| numberType | `any` | `'float'` | no | Valid: `float`, `int` |
| step | `any` | `null` | no |  |
| min | `any` | `null` | no |  |
| max | `any` | `null` | no |  |
| value | `any` | `null` | no |  |
| digits | `any` | `2` | no |  |
| fillDigits | `any` | `false` | no |  |
| allowEmpty | `any` | `false` | no |  |
| numberAlignEnd | `any` | `false` | no |  |
| ariaLabel | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| prefix | — | |
| suffix | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| input-change | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |
| ends-with-decimal-separator | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChange` | |
| `onInput` | |
| `increaseNumberByStep` | |
| `decreaseNumberByStep` | |
| `computeValue` | |
| `parseValue` | |
| `checkBoundaries` | |
| `getNumberFromString` | |
| `checkForInteger` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `realStep` | |
| `realMinimum` | |
| `realMaximum` | |
| `stringRepresentation` | |

## Examples

### Basic Usage
```twig
<sw-number-field-deprecated>
    <!-- content -->
</sw-number-field-deprecated>
```
