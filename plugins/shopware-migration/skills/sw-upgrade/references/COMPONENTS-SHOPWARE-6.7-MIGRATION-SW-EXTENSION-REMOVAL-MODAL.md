# sw-extension-removal-modal

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
| remove-extension | — | |

## Methods

| Method | Description |
|--------|-------------|
| `emitClose` | |
| `emitRemoval` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `title` | |
| `alert` | |
| `btnLabel` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-extension-removal-modal
    v-if="showRemovalModal"
    :extension-name="extension.label"
    :is-licensed="extension.storeLicense !== null && extension.storeLicense.variant === 'rent'"
    :is-loading="isLoading"
    @modal-close="closeRemovalModal"
    @remove-extension="closeModalAndRemoveExtension"
/>

<sw-extension-permissions-modal
    v-if="showPermissionsModal"
    :extension-label="extension.label"
    :permissions="permissions"
    :domains="extension.domains"
    :action-label="permissionModalActionLabel"
```
