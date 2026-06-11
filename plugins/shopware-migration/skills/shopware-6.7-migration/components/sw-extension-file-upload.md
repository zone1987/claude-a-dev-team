# sw-extension-file-upload

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClickUpload` | |
| `onFileInputChange` | |
| `handleUpload` | |
| `showStoreError` | |
| `showConfirmModal` | |
| `closeConfirmModal` | |
| `getUserConfig` | |
| `saveConfig` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `userConfigRepository` | |
| `currentUser` | |
| `userConfigCriteria` | |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-index/sw-extension-my-extensions-index.html.twig`
```twig
<sw-extension-file-upload v-if="acl.can('system.plugin_upload') || !extensionManagementDisabled" />
```
