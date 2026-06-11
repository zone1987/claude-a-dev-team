# sw-order-save-changes-beforehand-modal

> Shopware Administration component.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| confirm | — | |
| cancel | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |
| `onCancel` | |

## Examples

### Example 1
Source: `sw-order/page/sw-order-detail/sw-order-detail.html.twig`
```twig
<sw-order-save-changes-beforehand-modal
    v-if="askForSaveBeforehand"
    @cancel="onAskAndSaveEditsCancel"
    @confirm="onAskAndSaveEditsConfirm"
>
    {{ askForSaveBeforehand.reason }}
</sw-order-save-changes-beforehand-modal>
```
