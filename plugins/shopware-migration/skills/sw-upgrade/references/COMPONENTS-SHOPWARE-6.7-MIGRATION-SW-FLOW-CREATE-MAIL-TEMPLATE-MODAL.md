# sw-flow-create-mail-template-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClose` | |
| `onAddMailTemplate` | |
| `getMailTemplateType` | |
| `onChangeType` | |
| `getMailTemplate` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mailTemplateRepository` | |
| `mailTemplateTypeRepository` | |
| `mailTemplateCriteria` | |
| `outerCompleterFunction` | |
| `mailTemplateContentHtmlError` | |
| `mailTemplateContentPlainError` | |
| `mailTemplateMailTemplateTypeIdError` | |
| `mailTemplateSubjectError` | |

## Examples

### Example 1
Source: `sw-flow/component/modals/sw-flow-mail-send-modal/sw-flow-mail-send-modal.html.twig`
```twig
<sw-flow-create-mail-template-modal
    v-if="showCreateMailTemplateModal"
    class="sw-flow-mail-send-modal__create-mail-template"
    @process-finish="onCreateMailTemplateSuccess"
    @modal-close="onCloseCreateMailTemplateModal"
/>
{% endblock %}

{% block sw_flow_mail_send_modal_custom %}
{% endblock %}

{% block sw_flow_mail_send_modal_footer %}
<template #modal-footer>
    {% block sw_flow_mail_send_modal_footer_cancel_button %}
    <mt-button
```
