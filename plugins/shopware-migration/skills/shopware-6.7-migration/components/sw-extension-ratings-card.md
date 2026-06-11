# sw-extension-ratings-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extension | `any` | — | yes |  |
| producerName | `any` | — | yes |  |
| isInstalledAndLicensed | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-extension | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchReviews` | |
| `loadMoreReviews` | |
| `getReviews` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `canShowMore` | |
| `numberOfRatingsHasChanged` | |
| `extensionStoreDataService` | |
| `hasReviews` | |

## Examples

### Basic Usage
```twig
<sw-extension-ratings-card
    extension="..."
    producerName="..."
>
    <!-- content -->
</sw-extension-ratings-card>
```
