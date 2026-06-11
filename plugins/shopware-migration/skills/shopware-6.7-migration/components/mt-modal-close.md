# mt-modal-close

> Meteor component from the `@shopware-ag/meteor-component-library` package.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| as | `Component | string` | — | no | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Examples

### Example 1
Source: `sw-settings-services/component/sw-settings-services-revoke-permissions-modal/sw-settings-services-revoke-permissions-modal.html.twig`
```twig
<mt-modal-close
    as="mt-button"
    variant="secondary"
>
    {{ $t('global.default.cancel') }}
</mt-modal-close>
```

### Example 2
Source: `sw-settings-services/component/sw-settings-services-deactivate-modal/sw-settings-services-deactivate-modal.html.twig`
```twig
<mt-modal-close
    as="mt-button"
    variant="secondary"
>
    {{ $t('global.default.cancel') }}
</mt-modal-close>
```

### Example 3
Source: `sw-settings-services/component/sw-settings-services-grant-permissions-modal/sw-settings-services-grant-permissions-modal.html.twig`
```twig
<mt-modal-close
    as="mt-button"
    variant="secondary"
    size="small"
>
    {{ $t('global.default.cancel') }}
</mt-modal-close>
```
