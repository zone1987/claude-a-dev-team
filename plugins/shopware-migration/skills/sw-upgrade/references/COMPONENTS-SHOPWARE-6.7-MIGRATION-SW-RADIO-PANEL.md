# sw-radio-panel

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| modelValue | `any` | — | no |  |
| title | `any` | `''` | no |  |
| description | `any` | `''` | no |  |
| icon | `any` | `''` | no |  |
| id | `any` | — | no |  |
| name | `any` | `null` | no |  |
| required | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| truncate | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:modelValue | — | |

## Methods

| Method | Description |
|--------|-------------|
| `toggle` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `checked` | |

## Examples

### Basic Usage
```twig
<sw-radio-panel>
    <!-- content -->
</sw-radio-panel>
```
