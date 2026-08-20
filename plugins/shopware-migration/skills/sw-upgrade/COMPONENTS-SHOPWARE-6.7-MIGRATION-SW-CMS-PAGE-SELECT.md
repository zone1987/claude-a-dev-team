# sw-cms-page-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| pageType | `any` | — | yes |  |
| value | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getTranslations` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `bind` | |
| `translations` | |
| `pageTypeCriteria` | |

## Examples

### Basic Usage
```twig
<sw-cms-page-select
    pageType="..."
>
    <!-- content -->
</sw-cms-page-select>
```
