# sw-extension-permissions-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| permissions | `any` | — | yes |  |
| domains | `any` | — | no |  |
| extensionLabel | `any` | — | yes |  |
| actionLabel | `any` | `null` | no |  |
| closeLabel | `any` | `null` | no |  |
| title | `any` | `null` | no |  |
| description | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| close-with-action | — | |

## Methods

| Method | Description |
|--------|-------------|
| `close` | |
| `closeWithAction` | |
| `categoryLabel` | |
| `openDetailsModal` | |
| `closeDetailsModal` | |
| `toggleDomainsModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `permissionsWithGroupedOperations` | |
| `domainsList` | |
| `closeBtnLabel` | |
| `descriptionText` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-extension-permissions-modal
    v-if="showPermissionsModal"
    :extension-label="extension.label"
    :permissions="permissions"
    :domains="extension.domains"
    :action-label="permissionModalActionLabel"
    @modal-close="closePermissionsModal"
    @close-with-action="closePermissionsModalAndInstallExtension"
/>

<sw-extension-privacy-policy-extensions-modal
    v-if="showPrivacyModal"
    :extension-name="extension.label"
    :privacy-policy-extension="extension.privacyPolicyExtension"
    @modal-close="closePrivacyModal"
```

### Example 2
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
    <sw-extension-permissions-modal
        v-if="showPermissionsModal"
        :extension-label="service.label"
        :permissions="categorizedPermissions"
        :domains="service.domains"
        @modal-close="showPermissionsModal = false"
    />
</li>

```
