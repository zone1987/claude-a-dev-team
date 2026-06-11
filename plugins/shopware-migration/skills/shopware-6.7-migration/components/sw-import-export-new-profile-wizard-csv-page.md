# sw-import-export-new-profile-wizard-csv-page

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| next-disable | — | |
| next-allow | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onFileChange` | |
| `transformMapping` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
    <sw-import-export-new-profile-wizard-csv-page
        :profile="profile"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
{% endblock %}

{% block sw_import_export_new_profile_wizard_page_mapping %}
<sw-wizard-page
    :position="2"
    :title="pageTitleSnippet('sw-import-export.profile.mappingsTab')"
>
    <sw-import-export-new-profile-wizard-mapping-page
        :profile="profile"
```
