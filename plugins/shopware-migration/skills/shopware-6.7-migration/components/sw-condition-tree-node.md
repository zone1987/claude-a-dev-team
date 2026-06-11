# sw-condition-tree-node

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| level | `any` | — | yes |  |
| condition | `any` | — | yes |  |
| parentCondition | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| insertBefore | `any` | `null` | no |  |
| insertAfter | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `deleteNode` | |
| `insertNewNodeBefore` | |
| `insertNewNodeAfter` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `conditionNodeComponent` | |

## Examples

### Basic Usage
```twig
<sw-condition-tree-node
    level="..."
    condition="..."
>
    <!-- content -->
</sw-condition-tree-node>
```
