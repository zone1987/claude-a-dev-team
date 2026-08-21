# sw-flow-sequence-condition

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onCreateNewRule` | |
| `onCloseModal` | |
| `onSaveRuleSuccess` | |
| `onRuleChange` | |
| `deleteRule` | |
| `addIfCondition` | |
| `addThenAction` | |
| `showArrowIcon` | |
| `disabledAddSequence` | |
| `arrowClasses` | |
| `removeCondition` | |
| `createSequence` | |
| `setFieldError` | |
| `removeFieldError` | |
| `toggleAddButton` | |
| `onEditRule` | |
| `isRuleDisabled` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `restrictedRules` | |
| `flow` | |
| `invalidSequences` | |
| `sequences` | |
| `sequenceRepository` | |
| `ruleRepository` | |
| `ruleCriteria` | |
| `showHelpElement` | |
| `modalName` | |
| `ruleDescription` | |
| `advanceSelectionParameters` | |

## Examples

### Example 1
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
<sw-flow-sequence-condition
    v-if="isConditionSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

{% block sw_flow_sequence_action %}
<sw-flow-sequence-action
    v-show="isActionSequence"
    :sequence="sequenceData"
    :disabled="disabled"
    :is-unknown-trigger="isUnknownTrigger"
/>
{% endblock %}
```
