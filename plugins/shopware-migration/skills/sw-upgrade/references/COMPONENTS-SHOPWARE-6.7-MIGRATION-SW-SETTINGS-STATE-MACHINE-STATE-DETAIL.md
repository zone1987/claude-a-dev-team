# sw-settings-state-machine-state-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentStateMachineState | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCancel` | |
| `onSave` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineStateRepository` | |
| `stateMachineStateNameError` | |

## Examples

### Example 1
Source: `sw-settings-state-machine/component/sw-settings-state-machine-state-list/sw-settings-state-machine-state-list.html.twig`
```twig
    <sw-settings-state-machine-state-detail
        v-if="currentStateMachineState !== null"
        :current-state-machine-state="currentStateMachineState"
        @modal-close="onModalClose"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```
