# sw-user-sso-invitation-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| user-invited | — | |
| invitation-failed | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `componentCreated` | |
| `loadLanguages` | |
| `sendInvitation` | |
| `closeModal` | |
| `validateEmail` | |
| `validateLanguage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `invitationService` | |
| `languageRepository` | |
| `languageCriteria` | |
| `hasError` | |

## Examples

### Example 1
Source: `sw-users-permissions/components/sw-users-permissions-user-listing/sw-users-permissions-user-listing.html.twig`
```twig
            <sw-user-sso-invitation-modal
                v-if="showInvitationModal"
                @modal-close="closeInvitationModal"
                @user-invited="onUserInvited"
                @invitation-failed="invitationFailed"
            />
            {% endblock %}
        {% endblock %}
        </sw-container>
    </div>

{% block sw_settings_user_list_content %}
    {% block sw_settings_user_list_content_grid %}
    <sw-data-grid
        :data-source="user"
```
