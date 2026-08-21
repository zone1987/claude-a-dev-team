# mt-popover-item

> Menu item within a popover menu.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| extension-logo | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-checkbox | — | |
| change-switch | — | |
| change-visibility | — | |
| click-options | — | |

## Examples

### Example 1
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
            <mt-popover-item
                v-if="!service.active"
                :label="$t('sw-settings-services.general.activate')"
                :disabled="isLoading"
                :on-label-click="() => setActive(true, toggleFloatingUi)"
            />

            <mt-popover-item
                v-if="service.active"
                :label="$t('sw-settings-services.general.deactivate')"
                :disabled="isLoading"
                :on-label-click="() => openDeactivateModal(toggleFloatingUi)"
            />

            <mt-popover-item
```
