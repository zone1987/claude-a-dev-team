# sw-flow-sequence-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| modalName | `any` | — | yes |  |
| action | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `processSuccess` | |
| `onClose` | |

## Examples

### Example 1
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
    <sw-flow-sequence-modal
        :sequence="currentSequence"
        :action="selectedAction"
        :modal-name="modalName"
        @process-finish="onSaveActionSuccess"
        @modal-close="onCloseModal"
    />
    {% endblock %}
</div>
{% endblock %}

```
