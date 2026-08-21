# sw-import-export-new-profile-wizard-general-page

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| next-allow | — | |
| next-disable | — | |

## Methods

| Method | Description |
|--------|-------------|
| `isFieldFilled` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `inputValid` | |

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
