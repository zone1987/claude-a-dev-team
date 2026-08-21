# sw-flow-detail-flow

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |
| isNewFlow | `any` | `false` | no |  |
| isTemplate | `any` | `false` | no |  |
| isUnknownTrigger | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getTriggerActions` | |
| `convertSequenceData` | |
| `convertToTreeData` | |
| `createSequence` | |
| `onEventChange` | |
| `onAddRootSequence` | |
| `getSequenceId` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `sequenceRepository` | |
| `formatSequences` | |
| `rootSequences` | |
| `showActionWarning` | |
| `flow` | |
| `triggerActions` | |
| `sequences` | |
| `availableActions` | |
| `hasAvailableAction` | |

## Examples

### Basic Usage
```twig
<sw-flow-detail-flow>
    <!-- content -->
</sw-flow-detail-flow>
```
