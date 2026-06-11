# sw-order-send-document-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| document | `any` | — | yes |  |
| order | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| document-sent | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setEmailTemplateAccordingToDocumentType` | |
| `onMailTemplateChange` | |
| `onSendDocument` | |
| `loadTheLinksForA11y` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `truncateFilter` | |
| `mailTemplateRepository` | |
| `mailHeaderFooterRepository` | |
| `mailTemplateCriteria` | |
| `mailTemplateSendCriteria` | |
| `primaryActionDisabled` | |
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-document-card/sw-order-document-card.html.twig`
```twig
<sw-order-send-document-modal
    v-if="showSendDocumentModal"
    :document="sendDocument"
    :order="order"
    @modal-close="onCloseSendDocumentModal"
    @document-sent="onDocumentSent"
/>
{% endblock %}

{% block sw_order_document_card_empty_state %}
<mt-empty-state
    v-if="documentsEmpty && !isDataLoading && !term"
    class="sw-order-document-card__empty-state"
    :icon="$route.meta.$module.icon"
    :headline="emptyStateTitle"
```
