# sw-flow-set-entity-custom-field-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| action | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getCustomFieldRendered` | |
| `onEntityChange` | |
| `onCustomFieldSetChange` | |
| `onCustomFieldChange` | |
| `validateOptionSelectFieldLabel` | |
| `onClose` | |
| `onAddAction` | |
| `fieldError` | |
| `getFieldOptions` | |
| `getEntityOptions` | |
| `convertToEntityTechnicalName` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customFieldRepository` | |
| `customFieldCriteria` | |
| `customFieldSetCriteria` | |
| `showFieldValue` | |
| `defaultFieldOptions` | |
| `multipleFieldOptions` | |
| `labelProperty` | |
| `triggerEvent` | |
| `customFieldSets` | |
| `customFields` | |
| `triggerActions` | |

## Examples

### Basic Usage
```twig
<sw-flow-set-entity-custom-field-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-set-entity-custom-field-modal>
```
