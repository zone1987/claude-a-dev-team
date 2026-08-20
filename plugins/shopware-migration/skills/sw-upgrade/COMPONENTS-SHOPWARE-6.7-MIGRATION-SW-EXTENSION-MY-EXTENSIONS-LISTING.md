# sw-extension-my-extensions-listing

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `updateList` | |
| `openStore` | |
| `openThemesStore` | |
| `updateRouteQuery` | |
| `changePage` | |
| `filterExtensionsByType` | |
| `sortExtensions` | |
| `changeSortingOption` | |
| `changeActiveState` | |
| `filterExtensionsByActiveState` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isAppUrlReachable` | |
| `isLoading` | |
| `myExtensions` | |
| `extensionList` | |
| `extensionListPaginated` | |
| `extensionListSearched` | |
| `isAppRoute` | |
| `isThemeRoute` | |
| `total` | |
| `limit` | |
| `page` | |
| `term` | |
| `skeletonVariant` | |
| `assetFilter` | |
| `extensionManagementDisabled` | |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-listing/sw-extension-my-extensions-listing.html.twig`
```twig
<sw-extension-my-extensions-listing-controls
    @update:active-state="changeActiveState"
    @update:sorting-option="changeSortingOption"
/>

<sw-extension-component-section
    v-if="isThemeRoute"
    position-identifier="sw-extension-my-extensions-listing__before-content"
/>

<sw-meteor-card
    v-if="!extensionListPaginated.length && filterByActiveState"
    class="sw-extension-my-extensions-listing__empty-state"
>
    <img
```
