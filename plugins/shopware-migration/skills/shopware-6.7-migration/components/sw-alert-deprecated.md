# sw-alert-deprecated

> **Deprecated in 6.7** — Use `mt-banner` instead. Will be removed in 6.8.
> See [mt-banner](mt-banner.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-alert>` | `<mt-banner>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `'info'` | no | Valid: `info`, `warning`, `error`, `success`, `neutral` |
| appearance | `any` | `'default'` | no | Valid: `default`, `notification`, `system` |
| title | `any` | `''` | no |  |
| showIcon | `any` | `true` | no |  |
| closable | `any` | `false` | no |  |
| notificationIndex | `any` | `null` | no |  |
| icon | `any` | `null` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| customIcon | — | |
| actions | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `alertIcon` | |
| `hasActionSlot` | |
| `alertClasses` | |
| `alertBodyClasses` | |

## Examples

### Basic Usage
```twig
<sw-alert-deprecated>
    <!-- content -->
</sw-alert-deprecated>
```
