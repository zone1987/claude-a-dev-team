# sw-order-state-history-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadHistory` | |
| `getStateHistoryEntries` | |
| `buildStateHistory` | |
| `createEntry` | |
| `getVariantState` | |
| `onClose` | |
| `onPageChange` | |
| `enumerateTransaction` | |
| `getStateChangeAuthor` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineHistoryRepository` | |
| `stateMachineHistoryCriteria` | |
| `columns` | |
| `hasMultipleTransactions` | |
| `statesLoading` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
    <sw-order-state-history-modal
        v-if="showStateHistoryModal"
        :order="order"
        @modal-close="showStateHistoryModal = false"
    />
    {% endblock %}
</div>
{% endblock %}

```
