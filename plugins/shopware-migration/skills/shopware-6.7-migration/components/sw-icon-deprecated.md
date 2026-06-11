# sw-icon-deprecated

> **Deprecated in 6.7** — Use `mt-icon` instead. Will be removed in 6.8.
> See [mt-icon](mt-icon.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-icon>` | `<mt-icon>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `any` | — | yes |  |
| color | `any` | `null` | no |  |
| small | `any` | `false` | no |  |
| large | `any` | `false` | no |  |
| size | `any` | `null` | no |  |
| decorative | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `loadIconSvgData` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `iconName` | |
| `classes` | |
| `styles` | |

## Examples

### Basic Usage
```twig
<sw-icon-deprecated
    name="..."
>
    <!-- content -->
</sw-icon-deprecated>
```
