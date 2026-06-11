# sw-flow-mail-send-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

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
| `getRecipientData` | |
| `isRecipientGridError` | |
| `onAddAction` | |
| `onCreateMailTemplate` | |
| `onCloseCreateMailTemplateModal` | |
| `onCreateMailTemplateSuccess` | |
| `onChangeMailTemplate` | |
| `onChangeRecipient` | |
| `addRecipient` | |
| `saveRecipient` | |
| `cancelSaveRecipient` | |
| `onEditRecipient` | |
| `onDeleteRecipient` | |
| `mailTemplateError` | |
| `setNameError` | |
| `setMailError` | |
| `validateRecipient` | |
| `resetError` | |
| `allowDeleteRecipient` | |
| `changeShowReplyToField` | |
| `buildReplyToTooltip` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mailTemplateCriteria` | |
| `documentTypeRepository` | |
| `isNewMail` | |
| `recipientCustomer` | |
| `recipientAdmin` | |
| `recipientCustom` | |
| `recipientDefault` | |
| `recipientContactFormMail` | |
| `entityAware` | |
| `recipientOptions` | |
| `recipientColumns` | |
| `replyToOptions` | |
| `replyToSelection` | |
| `showReplyToField` | |
| `mailTemplates` | |
| `triggerEvent` | |
| `triggerActions` | |

## Examples

### Basic Usage
```twig
<sw-flow-mail-send-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-mail-send-modal>
```
