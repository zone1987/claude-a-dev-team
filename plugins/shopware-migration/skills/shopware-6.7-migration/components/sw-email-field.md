# sw-email-field

> **Migration wrapper** — Delegates to `mt-email-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-email-field](mt-email-field.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `any` | `null` | no |  |
| value | `any` | `null` | no |  |
| deprecated | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |
| `handleUpdateModelValue` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `compatValue` | |

## Examples

### Example 1
Source: `sw-custom-entity/component/sw-custom-entity-input-field/sw-custom-entity-input-field.html.twig`
```twig
<sw-email-field
    v-else-if="type === 'email'"
    class="sw-custom-entity-input-field__email"
    :value="currentValue"
    :label="label"
    :placeholder="placeholder"
    :help-text="helpText"
    @change="onChange"
/>-->

<!-- ToDo NEXT-22874 - Implement json field -->
<!--<sw-????
    v-else-if="type === 'json'"
    class="sw-custom-entity-input-field__json"
    :value="currentValue"
```
