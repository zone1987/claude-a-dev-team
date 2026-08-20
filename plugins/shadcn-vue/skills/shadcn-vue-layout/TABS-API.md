# API Reference

reka-ui API: https://reka-ui.com/docs/components/tabs#api-reference

## Sub-components

| Component | Description |
|-----------|-------------|
| `Tabs` | Root container (`TabsRoot`), manages active tab |
| `TabsList` | Container for trigger buttons |
| `TabsTrigger` | Individual tab button |
| `TabsContent` | Content panel shown when tab is active |

## Tabs (Root) Props

Extends `TabsRootProps` from reka-ui:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `modelValue` | `string` | — | Controlled active tab value |
| `defaultValue` | `string` | — | Uncontrolled initial active tab |
| `orientation` | `'horizontal' \| 'vertical'` | `'horizontal'` | Layout direction |
| `activationMode` | `'automatic' \| 'manual'` | `'automatic'` | When tab is activated |
| `class` | `string` | — | Additional CSS classes |

## Tabs Emits

| Event | Payload | Description |
|-------|---------|-------------|
| `update:modelValue` | `string` | Emitted when active tab changes |

## TabsList Props

Extends `TabsListProps` from reka-ui:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `'default' \| 'line'` | `'default'` | Visual variant |
| `loop` | `boolean` | `true` | Keyboard navigation loops |
| `class` | `string` | — | Additional CSS classes |

## TabsTrigger Props

Extends `TabsTriggerProps` from reka-ui:

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `value` | `string` | yes | Unique identifier matching TabsContent |
| `disabled` | `boolean` | — | Disables this tab |
| `class` | `string` | — | Additional CSS classes |

## TabsContent Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `value` | `string` | yes | Matching TabsTrigger value |
| `forceMount` | `boolean` | — | Mount even when inactive |
| `class` | `string` | — | Additional CSS classes |

## Data Attributes (reka-ui)

| Attribute | Values | Description |
|-----------|--------|-------------|
| `data-state` | `active \| inactive` | Whether the tab/content is active |
| `data-disabled` | present | Tab trigger is disabled |
| `data-orientation` | `horizontal \| vertical` | Layout direction |
