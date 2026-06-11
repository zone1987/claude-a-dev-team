# sw-settings-state-machine-state-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| stateMachineId | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadStateMachineStates` | |
| `onInlineEditCancel` | |
| `onInlineEditSave` | |
| `showModal` | |
| `onModalClose` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineStateRepository` | |
| `stateMachineStateCriteria` | |
| `stateMachineStateColumns` | |

## Examples

### Example 1
Source: `sw-settings-state-machine/page/sw-settings-state-machine-detail/sw-settings-state-machine-detail.html.twig`
```twig
            <sw-settings-state-machine-state-list
                ref="stateMachineStateList"
                :state-machine-id="stateMachineId"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```
