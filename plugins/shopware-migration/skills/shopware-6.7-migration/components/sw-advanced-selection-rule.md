# sw-advanced-selection-rule

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleAwareGroupKey | `any` | — | yes |  |
| restrictedRuleIds | `any` | — | no |  |
| restrictedRuleIdsTooltipLabel | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-submit | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getColumnClass` | |
| `tooltipConfig` | |
| `isRestricted` | |
| `isRecordSelectable` | |
| `getCounts` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `getRuleDefinition` | |
| `assignmentProperties` | |
| `context` | |
| `columns` | |
| `filters` | |
| `conditionFilterOptions` | |
| `groupFilterOptions` | |
| `associationFilterOptions` | |
| `associations` | |
| `aggregations` | |
| `dateFilter` | |

## Examples

### Basic Usage
```twig
<sw-advanced-selection-rule
    ruleAwareGroupKey="..."
>
    <!-- content -->
</sw-advanced-selection-rule>
```
