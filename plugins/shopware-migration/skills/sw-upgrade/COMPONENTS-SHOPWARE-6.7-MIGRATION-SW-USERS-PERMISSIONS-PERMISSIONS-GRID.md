# sw-users-permissions-permissions-grid

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| role | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `changePermission` | |
| `addPermission` | |
| `addDependenciesForRole` | |
| `removePermission` | |
| `isPermissionSelected` | |
| `isPermissionDisabled` | |
| `changeAllPermissionsForKey` | |
| `allPermissionsForKeySelected` | |
| `getPermissionsForParent` | |
| `areAllChildrenRolesSelected` | |
| `areAllChildrenWithAllRolesSelected` | |
| `areSomeChildrenRolesSelected` | |
| `areSomeChildrenWithAllRolesSelected` | |
| `isParentRoleDisabled` | |
| `toggleAllChildrenWithRole` | |
| `toggleAllChildrenWithAllRoles` | |
| `parentRoleHasChildRoles` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `permissionsWithParents` | |
| `permissions` | |
| `parents` | |
| `usedDependencies` | |
| `roles` | |

## Examples

### Example 1
Source: `sw-users-permissions/view/sw-users-permissions-role-view-general/sw-users-permissions-role-view-general.html.twig`
```twig
    <sw-users-permissions-permissions-grid
        :role="role"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}

    {% block sw_users_permissions_role_role_view_general_card_view_additional_permissions %}
    <sw-users-permissions-additional-permissions
        :role="role"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```
