# sw-user-sso-access-key-create-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | yes |  |
| isOpen | `any` | — | yes |  |
| accessKey | `any` | — | yes |  |
| secretAccessKey | `any` | — | yes |  |
| mode | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| access-key-modal-create:cancel | — | |
| access-key-modal-create:save | — | |
| access-key-modal-create:generate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onSave` | |
| `onGenerateNewAccessKey` | |

## Examples

### Example 1
Source: `sw-users-permissions/page/sw-sso-users-permission-user-detail/sw-sso-users-permission-user-detail.html.twig`
```twig
        <sw-user-sso-access-key-create-modal
            :is-loading="isLoading"
            :is-open="isCreateAccessKeyModalOpen"
            :access-key="newAccessKey"
            :secret-access-key="newSecretAccessKey"
            :mode="editMode"
            @access-key-modal-create:cancel="onAccessKeyCreateCancel"
            @access-key-modal-create:save="onSaveAccessKey"
            @access-key-modal-create:generate="onGenerateNewKey"
        />
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```
