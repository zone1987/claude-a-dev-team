# sw-flow-sequence-selector

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| title | — | |
| helpText | — | |

## Methods

| Method | Description |
|--------|-------------|
| `addIfCondition` | |
| `addThenAction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `title` | |
| `helpText` | |

## Examples

### Example 1
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
<sw-flow-sequence-selector
    v-if="isSelectorSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

{% block sw_flow_sequence_condition %}
<sw-flow-sequence-condition
    v-if="isConditionSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

```
