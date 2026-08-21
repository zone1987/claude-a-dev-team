# sw-extension-uninstall-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionName | `any` | — | yes |  |
| isLicensed | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| uninstall-extension | — | |

## Methods

| Method | Description |
|--------|-------------|
| `emitClose` | |
| `emitUninstall` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `title` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-extension-uninstall-modal
    v-if="showUninstallModal"
    :extension-name="extension.label"
    :is-licensed="extension.storeLicense !== null"
    :is-loading="isLoading"
    @modal-close="closeUninstallModal"
    @uninstall-extension="closeModalAndUninstallExtension"
/>

<sw-extension-removal-modal
    v-if="showRemovalModal"
    :extension-name="extension.label"
    :is-licensed="extension.storeLicense !== null && extension.storeLicense.variant === 'rent'"
    :is-loading="isLoading"
    @modal-close="closeRemovalModal"
```
