# sw-users-permissions-user-listing

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| get-list | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getItemToDelete` | |
| `onSearch` | |
| `getList` | |
| `onDelete` | |
| `onUserInvited` | |
| `openInvitationModal` | |
| `closeInvitationModal` | |
| `invitationFailed` | |
| `onConfirmDelete` | |
| `onCloseDeleteModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `userRepository` | |
| `currentUser` | |
| `userDetailRouterLink` | |
| `userCriteria` | |
| `userColumns` | |

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
