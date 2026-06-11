# sw-import-export-edit-profile-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | no |  |
| show | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| profile-close | — | |
| profile-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `saveProfile` | |
| `updateMapping` | |
| `getParentProfileSelected` | |
| `checkValidation` | |
| `resetViolations` | |
| `loadSystemRequiredFieldsForEntity` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `profileNameError` | |
| `profileSourceEntityError` | |
| `profileDelimiterError` | |
| `profileEnclosureError` | |
| `profileTypeError` | |
| `isNew` | |
| `modalTitle` | |
| `saveLabelSnippet` | |
| `showValidationError` | |
| `profileRepository` | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-import-export-edit-profile-modal
        v-if="selectedProfile"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @profile-close="closeSelectedProfile"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 2
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-mapping-page/sw-import-export-new-profile-wizard-mapping-page.html.twig`
```twig
    <sw-import-export-edit-profile-modal-mapping
        class="sw-import-export-new-profile-wizard-mapping-page__mapping"
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @update-mapping="updateMapping"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 3
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
    <sw-import-export-edit-profile-modal-mapping
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @update-mapping="updateMapping"
    />
    {% endblock %}
    {% endblock %}
</template>

<template v-if="active === 'advanced' && profile.type !== 'export' && profile.config.updateEntities !== false">
    {% block sw_import_export_edit_profile_modal_tabs_advanced %}
    {% block sw_import_export_edit_profile_modal_tabs_advanced_text %}
    <p class="sw-import-export-edit-profile-modal__text">
        {{ $tc('sw-import-export.profile.advancedDescription') }}
    </p>
```

### Example 4
Source: `sw-import-export/view/sw-import-export-view-profiles/sw-import-export-view-profiles.html.twig`
```twig
    <sw-import-export-edit-profile-modal
        :show="showProfileEditModal"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @profile-close="closeSelectedProfile"
    />
    {% endblock %}

    {% block sw_import_export_view_new_profile_wizard %}
    <sw-import-export-new-profile-wizard
        v-if="showNewProfileWizard"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @close="onCloseNewProfileWizard"
    />
```
