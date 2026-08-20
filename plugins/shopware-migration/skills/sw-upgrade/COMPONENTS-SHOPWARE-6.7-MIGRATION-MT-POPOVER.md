# mt-popover

> Popover overlay positioned relative to a trigger element.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| trigger | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:isOpened | — | |

## Examples

### Example 1
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<mt-popover
    :child-views="[{ name: 'base' }]"
>
    <template
        #trigger="{ toggleFloatingUi }"
    >
        <mt-button
            variant="secondary"
            square
            @click="toggleFloatingUi"
        >
            <mt-icon name="solid-ellipsis-h-s" />
        </mt-button>
    </template>

```

### Example 2
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
        <mt-popover-item
            :label="$t('sw-settings-services.service-card.permissions')"
            :on-label-click="() => openPermissionsModal(toggleFloatingUi)"
        />
    </template>
</mt-popover>
```
