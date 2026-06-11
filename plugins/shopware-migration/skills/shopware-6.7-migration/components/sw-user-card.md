# sw-user-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| user | `any` | — | yes |  |
| title | `any` | `''` | yes |  |
| isLoading | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| metadata-additional | — | |
| actions | — | |
| summary | — | |
| data-additional | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasActionSlot` | |
| `hasAdditionalDataSlot` | |
| `hasSummarySlot` | |
| `moduleColor` | |
| `salutationFilter` | |

## Examples

### Basic Usage
```twig
<sw-user-card
    user="..."
    title="..."
>
    <!-- content -->
</sw-user-card>
```
