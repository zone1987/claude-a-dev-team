# sw-import-export-new-profile-wizard-mapping-page

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |
| systemRequiredFields | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| next-allow | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mergeMappings` | |
| `updateMapping` | |
| `countAutomatedValues` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
    <sw-import-export-new-profile-wizard-mapping-page
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
{% endblock %}

{% block sw_import_export_new_profile_wizard_footer_right_button %}
<template #footer-right-button>
    <div class="sw-import-export-new-profile-wizard__footer-right-button-group">
        {% block sw_import_export_new_profile_wizard_footer_right_button_finish %}
        <mt-button
            v-if="showNextButton"
```
