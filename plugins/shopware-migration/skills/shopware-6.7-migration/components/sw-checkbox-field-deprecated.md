# sw-checkbox-field-deprecated

> **Deprecated in 6.7** — Use `mt-checkbox` instead. Will be removed in 6.8.
> See [mt-checkbox](mt-checkbox.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-checkbox-field>` | `<mt-checkbox>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| id | `any` | — | no |  |
| disabled | `any` | `false` | no |  |
| label | `any` | — | no |  |
| value | `any` | `null` | no |  |
| inheritedValue | `any` | `null` | no |  |
| ghostValue | `any` | `null` | no |  |
| error | `any` | `null` | no |  |
| bordered | `any` | `false` | no |  |
| padded | `any` | `false` | no |  |
| partlyChecked | `any` | `false` | no |  |
| ariaLabel | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `swCheckboxFieldClasses` | |
| `swCheckboxFieldContentClasses` | |
| `identification` | |
| `hasError` | |
| `inputState` | |
| `isInheritanceField` | |
| `isInherited` | |
| `isPartlyChecked` | |
| `iconName` | |
| `attrsWithoutClass` | |

## Examples

### Basic Usage
```twig
<sw-checkbox-field-deprecated>
    <!-- content -->
</sw-checkbox-field-deprecated>
```
