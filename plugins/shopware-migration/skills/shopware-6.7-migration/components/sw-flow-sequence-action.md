# sw-flow-sequence-action

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| isUnknownTrigger | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `openDynamicModal` | |
| `onSaveActionSuccess` | |
| `onCloseModal` | |
| `addAction` | |
| `editAction` | |
| `removeAction` | |
| `actionsWithoutStopFlow` | |
| `showMoveOption` | |
| `moveAction` | |
| `onEditAction` | |
| `removeActionContainer` | |
| `getActionTitle` | |
| `sortByPosition` | |
| `stopFlowStyle` | |
| `getActionDescriptions` | |
| `setFieldError` | |
| `removeFieldError` | |
| `isNotStopFlow` | |
| `capitalize` | |
| `isAppDisabled` | |
| `getStopFlowIndex` | |
| `sortActionOptions` | |
| `isValidAction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `sequenceRepository` | |
| `customFieldSetRepository` | |
| `actionOptions` | |
| `groups` | |
| `sequenceData` | |
| `showAddAction` | |
| `stopFlowActionName` | |
| `actionClasses` | |
| `errorArrow` | |
| `modalName` | |
| `currentLocale` | |
| `invalidSequences` | |
| `stateMachineState` | |
| `documentTypes` | |
| `mailTemplates` | |
| `customerGroups` | |
| `customFieldSets` | |
| `customFields` | |
| `triggerEvent` | |
| `triggerActions` | |
| `availableActions` | |
| `actionGroups` | |
| `sequences` | |
| `appActions` | |
| `getSelectedAppAction` | |
| `hasAvailableAction` | |

## Examples

### Example 1
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
<sw-flow-sequence-action
    v-show="isActionSequence"
    :sequence="sequenceData"
    :disabled="disabled"
    :is-unknown-trigger="isUnknownTrigger"
/>
{% endblock %}

{% block sw_flow_sequence_extension %}{% endblock %}

{% block sw_flow_sequence_true_block %}
<div
    v-if="sequenceData.trueBlock"
    class="sw-flow-sequence__true-block"
    :class="trueBlockClasses"
```

### Example 2
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
<sw-flow-sequence-action-error
    v-if="!isValidAction(item.actionName)"
    :sequence="item"
>
    <template #content>
        <div class="sw-flow-sequence-action__error-action">
            <div class="sw-flow-sequence-action__error-action-title">
                <mt-icon
                    name="regular-question-circle-s"
                    size="14px"
                    class="mt-icon-action"
                />

                <span>{{ $tc('sw-flow.actions.unknownLabel') }}</span>
            </div>
```
