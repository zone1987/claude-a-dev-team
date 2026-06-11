# sw-step-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabledIcon | `any` | `'regular-circle-xs'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Methods

| Method | Description |
|--------|-------------|
| `registerStep` | |
| `setActive` | |
| `setVariant` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modifierClasses` | |
| `icon` | |
| `stepDisplay` | |

## Examples

### Example 1
Source: `sw-first-run-wizard/component/sw-first-run-wizard-modal/sw-first-run-wizard-modal.html.twig`
```twig
<sw-step-item v-if="!extensionManagementDisabled">
    {{ $tc('sw-first-run-wizard.stepItemTitle.dataImport') }}
</sw-step-item>
```

### Example 2
Source: `sw-first-run-wizard/component/sw-first-run-wizard-modal/sw-first-run-wizard-modal.html.twig`
```twig
<sw-step-item>
    {{ $tc('sw-first-run-wizard.stepItemTitle.defaults') }}
</sw-step-item>
```
