# sw-import-export-new-profile-wizard

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| profile-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onClose` | |
| `onFinish` | |
| `pageTitleSnippet` | |
| `onNextAllow` | |
| `onNextDisable` | |
| `loadSystemRequiredFieldsForEntity` | |
| `saveProfile` | |
| `getParentProfileSelected` | |
| `checkValidation` | |
| `resetViolations` | |
| `onCurrentPageChange` | |
| `onNextPage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `profileRepository` | |
| `showValidationError` | |
| `showNextButton` | |
| `showCsvSkipButton` | |
| `parentProfileCriteria` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
    <sw-import-export-new-profile-wizard-general-page
        :profile="profile"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
{% endblock %}

{% block sw_import_export_new_profile_wizard_page_csv %}
<sw-wizard-page
    :position="csvUploadPagePosition"
    :title="pageTitleSnippet('sw-import-export.profile.csvUploadTab')"
>
    <sw-import-export-new-profile-wizard-csv-page
        :profile="profile"
```

### Example 2
Source: `sw-import-export/view/sw-import-export-view-profiles/sw-import-export-view-profiles.html.twig`
```twig
    <sw-import-export-new-profile-wizard
        v-if="showNewProfileWizard"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @close="onCloseNewProfileWizard"
    />
    {% endblock %}
</div>
{% endblock %}

```
