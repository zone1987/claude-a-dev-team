# sw-import-export-edit-profile-general

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `shouldDisableProfileType` | |
| `shouldDisableObjectType` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `profileNameError` | |
| `profileSourceEntityError` | |
| `profileTypeError` | |
| `supportedProfileTypes` | |
| `supportedEntities` | |
| `mappingLength` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
<sw-import-export-edit-profile-general :profile="profile" />
```

### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
<sw-import-export-edit-profile-general :profile="profile" />
```
