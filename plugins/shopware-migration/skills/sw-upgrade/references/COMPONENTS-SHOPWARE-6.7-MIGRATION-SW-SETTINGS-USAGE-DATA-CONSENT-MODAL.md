# sw-settings-usage-data-consent-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| initialStoreDataConsent | `any` | — | yes |  |
| initialUserDataConsent | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `savePreferences` | |
| `shareAll` | |
| `shareNothing` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `showConsentModal` | |
| `showStoreDataConsent` | |
| `showSavePreferences` | |

## Examples

### Basic Usage
```twig
<sw-settings-usage-data-consent-modal
    initialStoreDataConsent="..."
    initialUserDataConsent="..."
>
    <!-- content -->
</sw-settings-usage-data-consent-modal>
```
