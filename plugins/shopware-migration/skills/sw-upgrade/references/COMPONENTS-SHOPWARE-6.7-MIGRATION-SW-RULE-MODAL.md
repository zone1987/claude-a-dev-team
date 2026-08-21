# sw-rule-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowedRuleScopes | `any` | `null` | no |  |
| ruleAwareGroupKey | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadConditionData` | |
| `conditionsChanged` | |
| `getChildrenConditions` | |
| `validateRuleAwareness` | |
| `saveAndClose` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `ruleRepository` | |
| `ruleConditionRepository` | |
| `appScriptConditionRepository` | |
| `modalTitle` | |
| `ruleNameError` | |
| `rulePriorityError` | |

## Examples

### Basic Usage
```twig
<sw-rule-modal>
    <!-- content -->
</sw-rule-modal>
```
