# sw-order-select-document-type-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| value | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `documentTypeAvailable` | |
| `addHelpTextToOption` | |
| `onRadioFieldChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `creditItems` | |
| `documentRepository` | |
| `documentTypeRepository` | |
| `documentTypeCriteria` | |
| `documentCriteria` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-document-card/sw-order-document-card.html.twig`
```twig
<sw-order-select-document-type-modal
    v-if="showSelectDocumentTypeModal"
    v-model:value="currentDocumentType"
    :order="order"
    @modal-close="onCloseSelectDocumentTypeModal"
/>
{% endblock %}

{% block sw_order_document_card_grid_column_document_send_modal %}
<sw-order-send-document-modal
    v-if="showSendDocumentModal"
    :document="sendDocument"
    :order="order"
    @modal-close="onCloseSendDocumentModal"
    @document-sent="onDocumentSent"
```
