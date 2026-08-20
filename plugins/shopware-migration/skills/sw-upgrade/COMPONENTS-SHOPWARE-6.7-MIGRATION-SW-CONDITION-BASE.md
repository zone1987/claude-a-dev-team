# sw-condition-base

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| condition | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| create-before | — | |
| create-after | — | |
| condition-delete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onCreateBefore` | |
| `onCreateAfter` | |
| `onDeleteCondition` | |
| `ensureValueExist` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `conditionClasses` | |
| `conditionTypeError` | |
| `currentError` | |
| `hasError` | |
| `valueErrorPath` | |
| `value` | |
| `isDisabled` | |
| `hasNoComponent` | |
| `operator` | |
| `isEmpty` | |

## Examples

### Basic Usage
```twig
<sw-condition-base>
    <!-- content -->
</sw-condition-base>
```
