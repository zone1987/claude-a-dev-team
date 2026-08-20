# sw-verify-user-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| verified | — | |
| close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSubmitConfirmPassword` | |
| `onCloseConfirmPasswordModal` | |

## Examples

### Example 1
Source: `sw-profile/page/sw-profile-index/sw-profile-index.html.twig`
```twig
        <sw-verify-user-modal
            v-if="confirmPasswordModal"
            @verified="onVerifyPasswordFinished"
            @close="onCloseConfirmPasswordModal"
        />
        {% endblock %}

        {% block sw_profile_index_media_upload_actions_media_modal %}
        <sw-media-modal-v2
            v-if="showMediaModal"
            :allow-multi-select="false"
            :initial-folder-id="mediaDefaultFolderId"
            :entity-context="user.getEntityName()"
            @modal-close="showMediaModal = false"
            @media-modal-selection-change="onMediaSelectionChange"
```

### Example 2
Source: `sw-users-permissions/page/sw-users-permissions-user-detail/sw-users-permissions-user-detail.html.twig`
```twig
    <sw-verify-user-modal
        v-if="confirmPasswordModal"
        @verified="saveUser"
        @close="onCloseConfirmPasswordModal"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{%  block sw_setting_user_detail_card_integrations %}
<mt-card
    :title="$tc('sw-users-permissions.users.user-detail.labelIntegrationsCard')"
    position-identifier="sw-users-permissions-user-detail-integrations"
>
    {% block sw_settings_user_detail_grid_toolbar %}
```

### Example 3
Source: `sw-users-permissions/page/sw-users-permissions-role-detail/sw-users-permissions-role-detail.html.twig`
```twig
        <sw-verify-user-modal
            v-if="confirmPasswordModal"
            @verified="saveRole"
            @close="onCloseConfirmPasswordModal"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 4
Source: `sw-users-permissions/components/sw-users-permissions-role-listing/sw-users-permissions-role-listing.html.twig`
```twig
<sw-verify-user-modal
    v-if="isConfirmingPasswordModalOpen"
    @verified="deleteRole"
    @close="onCloseConfirmPasswordModal"
/>
{% endblock %}

{% block sw_users_permissions_role_listing_grid %}
<sw-data-grid
    v-if="showListingResults"
    :data-source="roles"
    :columns="rolesColumns"
    identifier="roles-grid"
    :show-settings="true"
    :show-selection="false"
```
