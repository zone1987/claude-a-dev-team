# sw-wizard

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| showNavigationDots | `any` | — | no |  |
| activePage | `any` | — | no |  |
| leftButtonDisabled | `any` | — | no |  |
| rightButtonDisabled | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| footer-left-button | — | |
| footer-dot-navigation | — | |
| footer-right-button | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| finish | — | |
| pages-updated | — | |
| current-page-change | — | |
| close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `addPage` | |
| `removePage` | |
| `nextPage` | |
| `previousPage` | |
| `changePage` | |
| `onClose` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasFooterSlot` | |
| `pagesCount` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
<sw-wizard
    ref="wizard"
    class="sw-import-export-new-profile-wizard"
    variant="full"
    :right-button-disabled="nextButtonDisabled"
    :active-page="currentlyActivePage"
    @close="onClose"
    @finish="onFinish"
    @current-page-change="onCurrentPageChange"
>
    {% block sw_import_export_new_profile_wizard_page_general %}
    <sw-wizard-page
        :position="0"
        :title="pageTitleSnippet('sw-import-export.profile.generalTab')"
    >
```

### Example 2
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
<sw-wizard-page
    :position="2"
    :title="pageTitleSnippet('sw-import-export.profile.mappingsTab')"
>
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
```
