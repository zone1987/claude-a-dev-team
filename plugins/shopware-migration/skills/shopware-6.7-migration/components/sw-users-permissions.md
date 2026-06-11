# sw-users-permissions

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `reloadUserListing` | |
| `onChangeLoading` | |
| `onSave` | |
| `onSaveFinish` | |

## Examples

### Example 1
Source: `sw-users-permissions/page/sw-users-permissions/sw-users-permissions.html.twig`
```twig
            <sw-users-permissions-user-listing
                ref="userListing"
            />
            <sw-users-permissions-role-listing
                ref="roleListing"
                @get-list="reloadUserListing"
            />
            <sw-users-permissions-configuration
                ref="configuration"
                @loading-change="onChangeLoading"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
```

### Example 2
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

### Example 3
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
