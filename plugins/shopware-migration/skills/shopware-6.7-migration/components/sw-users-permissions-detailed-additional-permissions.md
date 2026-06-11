# sw-users-permissions-detailed-additional-permissions

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| role | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| detailedPrivileges | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setDetailedAdditionalPermissions` | |
| `isEntitySelected` | |
| `isEntityDisabled` | |
| `changePermissionForEntity` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `allGeneralSelectedPrivileges` | |

## Examples

### Example 1
Source: `sw-users-permissions/view/sw-users-permissions-role-view-detailed/sw-users-permissions-role-view-detailed.html.twig`
```twig
    <sw-users-permissions-detailed-additional-permissions
        :role="role"
        :detailed-privileges="detailedPrivileges"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```
