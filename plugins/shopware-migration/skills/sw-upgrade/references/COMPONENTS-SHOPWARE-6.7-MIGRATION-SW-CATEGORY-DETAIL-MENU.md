# sw-category-detail-menu

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| category | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onMediaSelectionChange` | |
| `onSetMediaItem` | |
| `onRemoveMediaItem` | |
| `onMediaDropped` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `reversedVisibility` | |
| `mediaItem` | |
| `mediaRepository` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
<sw-category-detail-menu v-bind="{ category, isLoading }" />
```
