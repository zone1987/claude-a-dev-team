# sw-extension-rating-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `emitClose` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-card-bought/sw-extension-card-bought.html.twig`
```twig
<sw-extension-rating-modal
    v-if="showRatingModal"
    :extension="extension"
    @modal-close="closeRatingModal"
/>

<sw-modal
    v-if="showExtensionInstallationFailedModal"
    :title="extension.label"
    variant="small"
    class="sw-extension-card-bought__installation-failed-modal"
    @modal-close="closeInstallationFailedNotification"
>
    <sw-extension-adding-failed
        :extension-name="extension.name"
```
