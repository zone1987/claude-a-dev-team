# mt-modal-action

> Meteor component from the `@shopware-ag/meteor-component-library` package.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| as | `Component | string` | — | yes | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

## Examples

### Example 1
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="primary"
    @click="savePreferences"
>
    {{ $t('sw-settings-usage-data.consent-modal.actions.save-preferences') }}
</mt-modal-action>
```

### Example 2
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="primary"
    @click="shareNothing"
>
    <template #iconFront="{ size }">
        <mt-icon
            name="solid-times"
            :size="size"
        />
    </template>
    {{ $t('sw-settings-usage-data.consent-modal.actions.share-nothing') }}
</mt-modal-action>
```

### Example 3
Source: `sw-settings-services/component/sw-settings-services-revoke-permissions-modal/sw-settings-services-revoke-permissions-modal.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="critical"
    :is-loading="isLoading"
    @click="revokePermissions"
>
    {{ $t('sw-settings-services.revoke-permissions-modal.label-button-revoke-permissions') }}
</mt-modal-action>
```

### Example 4
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="secondary"
    @click="showDeactivateModal = false"
>
    {{ $t('global.default.cancel') }}
</mt-modal-action>
```

### Example 5
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="critical"
    :is-loading="isLoading"
    @click="setActive(false, () => { showDeactivateModal = false })"
>
    {{ $t('sw-settings-services.general.deactivate') }}
</mt-modal-action>
```
