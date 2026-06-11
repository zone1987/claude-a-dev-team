# sw-users-permissions-detailed-permissions-grid

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
| `isEntitySelected` | |
| `isEntityDisabled` | |
| `changePermissionForEntity` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `allEntities` | |
| `allGeneralSelectedPrivileges` | |
| `permissionTypes` | |

## Examples

### Example 1
Source: `sw-users-permissions/view/sw-users-permissions-role-view-detailed/sw-users-permissions-role-view-detailed.html.twig`
```twig
    <sw-users-permissions-detailed-permissions-grid
        :role="role"
        :detailed-privileges="detailedPrivileges"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />

    {% block sw_users_permissions_role_role_view_general_card_view_additional_permissions %}
    <sw-users-permissions-detailed-additional-permissions
        :role="role"
        :detailed-privileges="detailedPrivileges"
        :disabled="!acl.can('users_and_permissions.editor') || undefined"
    />
    {% endblock %}
</div>

```
