# mt-modal-trigger

> Meteor component from the `@shopware-ag/meteor-component-library` package.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| as | `Component` | — | yes | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Examples

### Example 1
Source: `sw-settings-services/component/sw-settings-services-revoke-permissions-modal/sw-settings-services-revoke-permissions-modal.html.twig`
```twig
<mt-modal-trigger as="button">
    {{ $t('sw-settings-services.revoke-permissions-modal.label-button-revoke-permissions') }}
</mt-modal-trigger>
```

### Example 2
Source: `sw-settings-services/component/sw-settings-services-deactivate-modal/sw-settings-services-deactivate-modal.html.twig`
```twig
<mt-modal-trigger as="button">
    {{ $t('sw-settings-services.general.deactivate') }}
</mt-modal-trigger>
```
