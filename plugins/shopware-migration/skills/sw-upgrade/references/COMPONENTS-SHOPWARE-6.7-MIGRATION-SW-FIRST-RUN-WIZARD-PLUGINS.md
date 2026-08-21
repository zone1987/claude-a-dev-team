# sw-first-run-wizard-plugins

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| extension-activated | — | |
| frw-set-title | — | |
| buttons-update | — | |
| loading-finished | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |
| `regionVariant` | |
| `categoryVariant` | |
| `onSelectRegion` | |
| `onSelectCategory` | |
| `getRecommendations` | |
| `getRecommendationRegions` | |
| `reloadRecommendations` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `categoryLead` | |
| `notCategoryLead` | |
| `showSpacer` | |
| `showCategoryLead` | |
| `showNotCategoryLead` | |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-recommendation/sw-extension-store-recommendation.html.twig`
```twig
<sw-first-run-wizard-plugins @loading-finished="finishLoading" />
```
