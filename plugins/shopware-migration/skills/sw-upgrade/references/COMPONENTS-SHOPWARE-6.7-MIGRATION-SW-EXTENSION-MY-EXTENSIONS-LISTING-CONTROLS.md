# sw-extension-my-extensions-listing-controls

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:active-state | — | |
| update:sorting-option | — | |

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
