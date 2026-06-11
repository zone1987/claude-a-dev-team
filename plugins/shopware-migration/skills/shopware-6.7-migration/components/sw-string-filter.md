# sw-string-filter

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filter | `any` | — | yes |  |
| active | `any` | — | yes |  |
| criteriaFilterType | `any` | `'contains'` | no | Valid: `contains`, `equals`, `equalsAny`, `prefix`, `suffix` |

## Methods

| Method | Description |
|--------|-------------|
| `updateFilter` | |
| `resetFilter` | |

## Examples

### Basic Usage
```twig
<sw-string-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-string-filter>
```
