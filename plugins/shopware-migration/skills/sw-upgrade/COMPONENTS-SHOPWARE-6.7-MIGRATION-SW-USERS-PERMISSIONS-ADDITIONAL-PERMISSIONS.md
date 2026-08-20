# sw-users-permissions-additional-permissions

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| role | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `isPrivilegeSelected` | |
| `onSelectPrivilege` | |
| `changeAllAppPermissionsForKey` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `additionalPermissions` | |
| `appPermissions` | |

## Examples

### Example 1
Source: `sw-users-permissions/view/sw-users-permissions-role-view-general/sw-users-permissions-role-view-general.html.twig`
```twig
    <sw-users-permissions-additional-permissions
        :role="role"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```
