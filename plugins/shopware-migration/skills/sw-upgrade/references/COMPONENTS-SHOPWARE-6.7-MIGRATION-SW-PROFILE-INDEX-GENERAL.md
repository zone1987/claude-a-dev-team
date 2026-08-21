# sw-profile-index-general

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| user | `any` | — | yes |  |
| languages | `any` | — | yes |  |
| newPassword | `any` | `null` | no |  |
| newPasswordConfirm | `any` | `null` | no |  |
| avatarMediaItem | `any` | `null` | no |  |
| isUserLoading | `any` | — | yes |  |
| languageId | `any` | `null` | no |  |
| isDisabled | `any` | — | yes |  |
| userRepository | `any` | — | yes |  |
| timezoneOptions | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| new-password-change | — | |
| new-password-confirm-change | — | |
| media-upload | — | |
| media-remove | — | |
| media-open | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onUploadMedia` | |
| `onDropMedia` | |
| `onRemoveMedia` | |
| `onOpenMedia` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `userPasswordError` | |
| `computedNewPassword` | |
| `computedNewPasswordConfirm` | |
| `localeOptions` | |

## Examples

### Basic Usage
```twig
<sw-profile-index-general
    user="..."
    languages="..."
>
    <!-- content -->
</sw-profile-index-general>
```
