# API Reference

reka-ui API: https://reka-ui.com/docs/components/stepper#api-reference

## Sub-Komponenten

| Component | Description |
|-----------|-------------|
| `Stepper` | Root container (`StepperRoot`), manages step state |
| `StepperItem` | Individual step wrapper, provides step context |
| `StepperTrigger` | Clickable trigger button for a step |
| `StepperIndicator` | Visual indicator (number/icon) for a step |
| `StepperTitle` | Title text of a step |
| `StepperDescription` | Description text below the title |
| `StepperSeparator` | Visual line separator between steps |

## Stepper (Root) Props

Extends `StepperRootProps` from reka-ui:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `modelValue` | `number` | — | Controlled current step (1-based) |
| `defaultValue` | `number` | `1` | Uncontrolled initial step |
| `orientation` | `'horizontal' \| 'vertical'` | `'horizontal'` | Layout direction |
| `linear` | `boolean` | `true` | Enforce sequential navigation |
| `class` | `string` | — | Additional CSS classes |

## Stepper Emits

| Event | Payload | Description |
|-------|---------|-------------|
| `update:modelValue` | `number` | Emitted when active step changes |

## StepperItem Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `step` | `number` | required | Step number (1-based) |
| `disabled` | `boolean` | `false` | Disables this step |
| `completed` | `boolean` | `false` | Marks step as completed |
| `class` | `string` | — | Additional CSS classes |

## StepperIndicator Data Attributes (reka-ui)

| Attribute | Values | Description |
|-----------|--------|-------------|
| `data-state` | `active \| completed \| inactive` | Current step state |
| `data-disabled` | present | Step is disabled |

## Slots

All sub-components expose a default slot with reka-ui slot props:

| Component | Slot Props |
|-----------|------------|
| `Stepper` | `{ step, totalSteps, isNextDisabled, isPrevDisabled }` |
| `StepperItem` | `{ step, state }` |
| `StepperIndicator` | `{ step, state }` |
