# sw-flow-rule-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleId | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadConditionData` | |
| `createRule` | |
| `loadRule` | |
| `loadConditions` | |
| `syncConditions` | |
| `onConditionsChanged` | |
| `getRuleDetail` | |
| `onSaveRule` | |
| `saveRule` | |
| `showErrorNotification` | |
| `onClose` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `ruleRepository` | |
| `conditionRepository` | |
| `appScriptConditionRepository` | |
| `availableModuleTypes` | |
| `moduleTypes` | |
| `scopesOfRuleAwarenessKey` | |
| `flow` | |
| `ruleNameError` | |
| `rulePriorityError` | |

## Examples

### Example 1
Source: `sw-flow/component/sw-flow-sequence-condition/sw-flow-sequence-condition.html.twig`
```twig
    <sw-flow-rule-modal
        v-if="showCreateRuleModal"
        :rule-id="selectedRuleId"
        @process-finish="onSaveRuleSuccess"
        @modal-close="onCloseModal"
    />
    {% endblock %}
</div>
{% endblock %}

```
