# sw-extension-privacy-policy-extensions-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionName | `any` | — | yes |  |
| privacyPolicyExtension | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `close` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `title` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
    <sw-extension-privacy-policy-extensions-modal
        v-if="showPrivacyModal"
        :extension-name="extension.label"
        :privacy-policy-extension="extension.privacyPolicyExtension"
        @modal-close="closePrivacyModal"
    />

    <sw-extension-permissions-modal
        v-if="showConsentAffirmationModal"
        :title="consentAffirmationModalTitle"
        :extension-label="extension.label"
        :permissions="consentAffirmationDeltas.permissions"
        :domains="consentAffirmationDeltas.domains"
        :action-label="consentAffirmationModalActionLabel"
        :close-label="consentAffirmationModalCloseLabel"
```
