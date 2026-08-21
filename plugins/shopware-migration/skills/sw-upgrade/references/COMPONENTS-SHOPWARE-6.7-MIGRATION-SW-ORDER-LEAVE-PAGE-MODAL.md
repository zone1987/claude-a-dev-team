# sw-order-leave-page-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-leave-confirm | — | |
| page-leave-cancel | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |
| `onCancel` | |

## Examples

### Example 1
Source: `sw-order/page/sw-order-detail/sw-order-detail.html.twig`
```twig
<sw-order-leave-page-modal
    v-if="isDisplayingLeavePageWarning"
    @page-leave-cancel="onLeaveModalClose"
    @page-leave-confirm="onLeaveModalConfirm"
/>
{% endblock %}
{% block sw_order_detail_content_save_changes_beforehand_modal %}
<sw-order-save-changes-beforehand-modal
    v-if="askForSaveBeforehand"
    @cancel="onAskAndSaveEditsCancel"
    @confirm="onAskAndSaveEditsConfirm"
>
    {{ askForSaveBeforehand.reason }}
</sw-order-save-changes-beforehand-modal>
{% endblock %}
```
