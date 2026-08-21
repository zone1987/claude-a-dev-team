# sw-promotion-v2-detail-base

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |
| isCreateMode | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| generate-individual-codes-finish | — | |
| delete-individual-codes-finish | — | |
| clean-up-codes | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initialSort` | |
| `onChangeCodeType` | |
| `setNewCodeType` | |
| `loadCustomFieldSets` | |
| `onGenerateCodeFixed` | |
| `generateFinish` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `codeTypeOptions` | |
| `promotionNameError` | |
| `promotionValidUntilError` | |
| `showCustomFields` | |

## Examples

### Basic Usage
```twig
<sw-promotion-v2-detail-base
    isCreateMode="..."
>
    <!-- content -->
</sw-promotion-v2-detail-base>
```
