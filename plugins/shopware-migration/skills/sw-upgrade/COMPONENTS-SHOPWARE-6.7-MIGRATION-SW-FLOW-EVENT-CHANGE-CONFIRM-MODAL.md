# sw-flow-event-change-confirm-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-confirm | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |
| `onClose` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `sequences` | |

## Examples

### Example 1
Source: `sw-flow/component/sw-flow-trigger/sw-flow-trigger.html.twig`
```twig
    <sw-flow-event-change-confirm-modal
        v-if="showConfirmModal"
        @modal-confirm="onConfirm"
        @modal-close="onCloseConfirm"
    />
    {% endblock %}
</div>
{% endblock %}

```
