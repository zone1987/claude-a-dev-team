# sw-promotion-v2-empty-state-hero

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| assetPath | `any` | `''` | no |  |
| description | `any` | `''` | no |  |
| hideDescription | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| actions | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `imagePath` | |
| `showDescription` | |
| `assetFilter` | |
| `actionSlotsAvailable` | |

## Examples

### Basic Usage
```twig
<sw-promotion-v2-empty-state-hero
    title="..."
>
    <!-- content -->
</sw-promotion-v2-empty-state-hero>
```
