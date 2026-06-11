# sw-extension-card-base

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extension | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-list | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `emitUpdateList` | |
| `getHelp` | |
| `openPrivacyAndSafety` | |
| `openRemovalModal` | |
| `openUninstallModal` | |
| `closeRemovalModal` | |
| `closeUninstallModal` | |
| `closeModalAndUninstallExtension` | |
| `updateExtension` | |
| `closeModalAndRemoveExtension` | |
| `openExtension` | |
| `openPermissionsModalForInstall` | |
| `openPermissionsModal` | |
| `closePermissionsModal` | |
| `closePermissionsModalAndInstallExtension` | |
| `changeExtensionStatus` | |
| `installExtension` | |
| `installAndActivateExtension` | |
| `removeExtension` | |
| `cancelAndRemoveExtension` | |
| `openPrivacyModal` | |
| `closePrivacyModal` | |
| `clearCacheAndReloadPage` | |
| `openConsentAffirmationModal` | |
| `closeConsentAffirmationModal` | |
| `closeConsentAffirmationModalAndUpdateExtension` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `dateFilter` | |
| `defaultThemeAsset` | |
| `extensionCardClasses` | |
| `licensedExtension` | |
| `image` | |
| `isActive` | |
| `allowDisable` | |
| `isInstalled` | |
| `privacyPolicyLink` | |
| `permissions` | |
| `assetFilter` | |
| `isRemovable` | |
| `isUninstallable` | |
| `isUpdateable` | |
| `openLinkExists` | |
| `extensionMainModule` | |
| `link` | |
| `consentAffirmationModalActionLabel` | |
| `consentAffirmationModalCloseLabel` | |
| `consentAffirmationModalTitle` | |
| `consentAffirmationModalDescription` | |
| `extensionManagementDisabled` | |
| `showContextMenu` | |

## Examples

### Basic Usage
```twig
<sw-extension-card-base
    extension="..."
>
    <!-- content -->
</sw-extension-card-base>
```
