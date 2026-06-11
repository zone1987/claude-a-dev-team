# sw-order-document-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| attachView | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-loading | — | |
| document-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `convertStoreEventToVueEvent` | |
| `getList` | |
| `documentTypeAvailable` | |
| `invoiceExists` | |
| `onSearchTermChange` | |
| `createDocument` | |
| `onCancelCreation` | |
| `onPrepareDocument` | |
| `openDocument` | |
| `downloadDocument` | |
| `markDocumentAsSent` | |
| `markDocumentAsUnsent` | |
| `onCreateDocument` | |
| `onPreview` | |
| `onOpenDocument` | |
| `onDownload` | |
| `onSendDocument` | |
| `onMarkDocumentAsSent` | |
| `onMarkDocumentAsUnsent` | |
| `onCloseSendDocumentModal` | |
| `onDocumentSent` | |
| `onLoadingDocument` | |
| `onLoadingPreview` | |
| `onShowSelectDocumentTypeModal` | |
| `onCloseSelectDocumentTypeModal` | |
| `availableFormatsFilter` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isEditing` | |
| `creditItems` | |
| `documentTypeRepository` | |
| `documentRepository` | |
| `documentsEmpty` | |
| `documentModal` | |
| `documentCardStyles` | |
| `documentTypeCriteria` | |
| `documentCriteria` | |
| `getDocumentColumns` | |
| `isDataLoading` | |
| `showCardFilter` | |
| `showCreateDocumentButton` | |
| `emptyStateTitle` | |
| `tooltipCreateDocumentButton` | |
| `assetFilter` | |
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-state-change-modal/sw-order-state-change-modal-attach-documents/sw-order-state-change-modal-attach-documents.html.twig`
```twig
<sw-order-document-card
    ref="attachDocuments"
    class="sw-order-detail-base__documents-grid"
    :order="order"
    :is-loading="isLoading"
    attach-view
/>
{% endblock %}

{% block sw_order_state_change_modal_attach_documents_internal_comment %}
<mt-textarea
    v-model="internalComment"
    :label="$tc('sw-order.stateCard.labelInternalComment')"
    :is-loading="isLoading"
/>
```

### Example 2
Source: `sw-order/view/sw-order-detail-documents/sw-order-detail-documents.html.twig`
```twig
    <sw-order-document-card
        :order="order"
        @document-save="saveAndReload"
    />
    {% endblock %}
</div>
{% endblock %}

```
