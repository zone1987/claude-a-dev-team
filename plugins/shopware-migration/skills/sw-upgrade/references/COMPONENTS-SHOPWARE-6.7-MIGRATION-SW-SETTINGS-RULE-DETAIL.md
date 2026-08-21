# sw-settings-rule-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `loadConditionData` | |
| `createRule` | |
| `loadEntityData` | |
| `extractEntityCount` | |
| `unsavedDataLeaveHandler` | |
| `checkUnsavedData` | |
| `setTreeFinishedLoading` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `loadConditions` | |
| `conditionsChanged` | |
| `validateRuleAwareness` | |
| `getChildrenConditions` | |
| `validateDateRange` | |
| `onSave` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `saveRule` | |
| `syncConditions` | |
| `showErrorNotification` | |
| `tabHasError` | |
| `onCancel` | |
| `onDuplicate` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `ruleRepository` | |
| `ruleCriteria` | |
| `appScriptConditionRepository` | |
| `conditionRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `tabItems` | |
| `conditionTreeFlat` | |
| `ruleNameError` | |
| `rulePriorityError` | |

## Examples

### Basic Usage
```twig
<sw-settings-rule-detail>
    <!-- content -->
</sw-settings-rule-detail>
```
