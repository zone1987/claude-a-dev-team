# sw-sales-channel-menu

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `registerListener` | |
| `destroyedComponent` | |
| `getDomainLink` | |
| `loadEntityData` | |
| `openSalesChannelModal` | |
| `openStorefrontLink` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `canCreateSalesChannels` | |
| `salesChannelCriteria` | |
| `moreSalesChannelAvailable` | |
| `buildMenuTree` | |
| `moreItemsEntry` | |
| `salesChannelFavoritesService` | |
| `salesChannelFavorites` | |

## Examples

### Example 1
Source: `sw-sales-channel/component/structure/sw-admin-menu-extension/sw-admin-menu-extension.html.twig`
```twig
<sw-sales-channel-menu v-if="canViewSalesChannels" />
```
