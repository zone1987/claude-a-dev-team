# sw-users-permissions-role-listing

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| get-list | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `onSearch` | |
| `getItemToDelete` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `deleteRole` | |
| `onCloseConfirmPasswordModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `rolesColumns` | |
| `roleRepository` | |
| `roleCriteria` | |
| `showListingResults` | |

## Examples

### Example 1
Source: `sw-users-permissions/page/sw-users-permissions/sw-users-permissions.html.twig`
```twig
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
</sw-page>
{% endblock %}

```
