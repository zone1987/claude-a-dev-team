# sw-step-display

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemIndex | `any` | — | yes |  |
| itemVariant | `any` | — | yes |  |
| initialItemVariants | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Methods

| Method | Description |
|--------|-------------|
| `addStep` | |
| `setItemVariants` | |
| `setItemVariant` | |
| `setVariantForCurrentItem` | |
| `setItemActive` | |

## Examples

### Example 1
Source: `sw-first-run-wizard/component/sw-first-run-wizard-modal/sw-first-run-wizard-modal.html.twig`
```twig
<sw-step-display
    :item-index="stepIndex"
    :item-variant="stepVariant"
    :initial-item-variants="stepInitialItemVariants"
>
    <sw-step-item v-if="!extensionManagementDisabled">
        {{ $tc('sw-first-run-wizard.stepItemTitle.dataImport') }}
    </sw-step-item>

    <sw-step-item>
        {{ $tc('sw-first-run-wizard.stepItemTitle.defaults') }}
    </sw-step-item>

    <sw-step-item>
        {{ $tc('sw-first-run-wizard.stepItemTitle.mailer') }}
```
