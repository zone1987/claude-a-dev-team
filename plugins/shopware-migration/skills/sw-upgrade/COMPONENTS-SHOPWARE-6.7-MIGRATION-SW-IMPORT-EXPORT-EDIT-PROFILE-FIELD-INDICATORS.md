# sw-import-export-edit-profile-field-indicators

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `profileDelimiterError` | |
| `profileEnclosureError` | |
| `supportedDelimiter` | |
| `supportedEnclosures` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
<sw-import-export-edit-profile-field-indicators :profile="profile" />
```

### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
<sw-import-export-edit-profile-field-indicators :profile="profile" />
```
