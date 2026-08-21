# sw-icon

> **Migration wrapper** — Delegates to `mt-icon` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-icon](COMPONENTS-SHOPWARE-6.7-MIGRATION-MT-ICON.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `any` | — | yes |  |
| deprecated | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Examples

### Basic Usage
```twig
<sw-icon
    name="..."
>
    <!-- content -->
</sw-icon>
```
