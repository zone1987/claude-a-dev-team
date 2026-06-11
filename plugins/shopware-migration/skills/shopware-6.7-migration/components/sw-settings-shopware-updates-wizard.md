# sw-settings-shopware-updates-wizard

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-started | — | |
| update-stopped | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onRequirementsResponse` | |
| `startUpdateProcess` | |
| `stopUpdateProcess` | |
| `downloadRecovery` | |
| `deactivatePlugins` | |
| `redirectToPage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `updatePossible` | |
| `updateButtonTooltip` | |
| `displayIncompatiblePluginsWarning` | |
| `displayUnknownPluginsWarning` | |
| `displayAllPluginsOkayInfo` | |
| `optionDeactivateIncompatibleTranslation` | |
| `optionDeactivateAllTranslation` | |

## Examples

### Basic Usage
```twig
<sw-settings-shopware-updates-wizard>
    <!-- content -->
</sw-settings-shopware-updates-wizard>
```
