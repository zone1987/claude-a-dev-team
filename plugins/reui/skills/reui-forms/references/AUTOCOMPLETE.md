# Autocomplete

Custom Shadcn Autocomplete for React and Tailwind CSS. An input that suggests options as you type.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [API Reference](#api-reference)
- [Basic usage](#basic-usage)
- [Examples (titles enumerated upstream, 12 total)](#examples-titles-enumerated-upstream-12-total)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/autocomplete
```

## Import

```tsx
import {
  Autocomplete,
  AutocompleteContent,
  AutocompleteEmpty,
  AutocompleteInput,
  AutocompleteItem,
  AutocompleteList,
} from "@/components/reui/autocomplete"
```

Additional named exports used in the examples below: `AutocompleteCollection`, `AutocompleteGroup`,
`AutocompleteGroupLabel`, `AutocompleteStatus`.

## API Reference

reui.io does not document Autocomplete's props itself. Both the Base UI build page
(`docs/components/base/autocomplete`) and the Radix UI build page (`docs/components/radix/autocomplete`)
carry an "API Reference" badge, and on **both** pages that badge links to the same URL:
`https://base-ui.com/react/components/autocomplete`. Radix UI's own primitives documentation
(radix-ui.com) has **no `autocomplete` (or `combobox`) component page at all** — its 29-component
index (`primitives/docs/overview/introduction`, checked 2026-09-04) lists none, and the word
"combobox" appears there only in the introduction's prose about common UI patterns, not as a link to
a component. ReUI's "Radix UI" build of Autocomplete is therefore documented against the same Base UI
primitive as the "Base UI" build; there is no separate Radix-primitives table to report.

Every table below is copied verbatim from `https://base-ui.com/react/components/autocomplete` (its
markdown twin at `.../autocomplete.md`, "API reference" section), retrieved 2026-09-04. Column values
that are exact TypeScript unions are kept exact; multi-sentence descriptions keep every sentence.
Where the upstream default column shows `-`, that is upstream's own way of saying no default is
documented, not an omission by this file.

### Root

Groups all parts of the autocomplete. Doesn't render its own HTML element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `name` | `string` | - | Identifies the field when a form is submitted. |
| `defaultValue` | `string \| number \| string[]` | - | The uncontrolled input value of the autocomplete when it's initially rendered. To render a controlled autocomplete, use the `value` prop instead. |
| `value` | `string \| string[] \| number` | - | The input value of the autocomplete. Use when controlled. |
| `onValueChange` | `(value: string, eventDetails: Autocomplete.Root.ChangeEventDetails) => void` | - | Event handler called when the input value of the autocomplete changes. |
| `defaultOpen` | `boolean` | `false` | Whether the popup is initially open. To render a controlled popup, use the `open` prop instead. |
| `open` | `boolean` | - | Whether the popup is currently open. Use when controlled. |
| `onOpenChange` | `(open: boolean, eventDetails: Autocomplete.Root.ChangeEventDetails) => void` | - | Event handler called when the popup is opened or closed. |
| `autoHighlight` | `boolean \| 'always'` | `false` | Whether the first matching item is highlighted automatically. `true`: highlight after the user types and keep the highlight while the query changes. `'always'`: always highlight the first item. |
| `keepHighlight` | `boolean` | `false` | Whether the highlighted item should be preserved when the pointer leaves the list. |
| `highlightItemOnHover` | `boolean` | `true` | Whether moving the pointer over items should highlight them. Disabling this prop allows CSS `:hover` to be differentiated from the `:focus` (`data-highlighted`) state. |
| `actionsRef` | `React.RefObject<Autocomplete.Root.Actions \| null>` | - | A ref to imperative actions. `unmount`: Manually unmounts the autocomplete. Call this after any externally controlled closing animation finishes. |
| `filter` | `(item: ItemValue, query: string, itemToString?: (item: ItemValue) => string) => boolean \| null` | - | AutocompleteFilter function used to match items against the input query. |
| `filteredItems` | `any[] \| Group<any>[] \| ItemValue[] \| Group<ItemValue>[]` | - | Filtered items to display in the list. When provided, the list uses these items instead of filtering the `items` prop internally. When `items` is also provided, this array must preserve its flat or grouped structure. Nullish entries are not supported, as in `items`. Use when you want to control filtering logic externally with the `useFilter()` hook. |
| `form` | `string` | - | Identifies the form that owns the internal input. Useful when the autocomplete is rendered outside the form. |
| `grid` | `boolean` | `false` | Whether list items are presented in a grid layout. When enabled, arrow keys navigate across rows and columns inferred from DOM rows. |
| `inline` | `boolean` | `false` | Whether the list is rendered inline without using the component's own popup. Specify `open` unconditionally in conjunction with this prop so the list is considered visible: `<Autocomplete.Root inline open>`. |
| `itemToStringValue` | `(itemValue: ItemValue) => string` | - | When the item values are objects (`<Autocomplete.Item value={object}>`), this function converts the object value to a string representation for both display in the input and form submission. If the shape of the object is `{ value, label }`, the label will be used automatically without needing to specify this prop. |
| `items` | `({ items: any[] })[] \| ItemValue[]` | - | The items to be displayed in the list. Can be either a flat array of items or an array of groups with items. Nullish entries are not supported: remove them from the data before passing it. |
| `limit` | `number` | `-1` | The maximum number of items to display in the list. |
| `locale` | `Intl.LocalesArgument` | - | The locale to use for string comparison. Defaults to the user's runtime locale. |
| `loopFocus` | `boolean` | `true` | Whether to loop keyboard focus back to the input when the end of the list is reached while using the arrow keys. The first item can then be reached by pressing ArrowDown again from the input, or the last item can be reached by pressing ArrowUp from the input. The input is always included in the focus loop per [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/). When disabled, focus does not move when on the last element and the user presses ArrowDown, or when on the first element and the user presses ArrowUp. |
| `modal` | `boolean` | `false` | Determines if the popup enters a modal state when open. `true`: user interaction is limited to the popup: document page scroll is locked and pointer interactions on outside elements are disabled. `false`: user interaction with the rest of the document is allowed. On touch devices, a `true` modal blocks outside taps but leaves the page scrollable unless the popup spans nearly the full viewport width, matching native iOS behavior. |
| `mode` | `'list' \| 'both' \| 'inline' \| 'none'` | `'list'` | Controls how the autocomplete behaves with respect to list filtering and inline autocompletion. `list` (default): items are dynamically filtered based on the input value. The input value does not change based on the active item. `both`: items are dynamically filtered based on the input value, which will temporarily change based on the active item (inline autocompletion). `inline`: items are static (not filtered), and the input value will temporarily change based on the active item (inline autocompletion). `none`: items are static (not filtered), and the input value will not change based on the active item. |
| `onItemHighlighted` | `(highlightedValue: ItemValue \| undefined, eventDetails: Autocomplete.Root.HighlightEventDetails) => void` | - | Callback fired when an item is highlighted or unhighlighted. Receives the highlighted item value (or `undefined` if no item is highlighted) and event details with a `reason` property describing why the highlight changed. The `reason` can be: `'keyboard'`: the highlight changed due to keyboard navigation. `'pointer'`: the highlight changed due to pointer hovering. `'none'`: the highlight changed programmatically. |
| `onOpenChangeComplete` | `(open: boolean) => void` | - | Event handler called after any animations complete when the popup is opened or closed. |
| `openOnInputClick` | `boolean` | `false` | Whether the popup opens when clicking the input. |
| `submitOnItemClick` | `boolean` | `false` | Whether clicking an item should submit the autocomplete's owning form. By default, clicking an item via a pointer or Enter key does not submit the owning form. Useful when the autocomplete is used as a single-field form search input. |
| `virtualized` | `boolean` | `false` | Whether the items are being externally virtualized. |
| `disabled` | `boolean` | `false` | Whether the component should ignore user interaction. |
| `readOnly` | `boolean` | `false` | Whether the user should be unable to choose a different option from the popup. |
| `required` | `boolean` | `false` | Whether the user must choose a value before submitting a form. |
| `inputRef` | `React.Ref<HTMLInputElement>` | - | A ref to the hidden input element. |
| `id` | `string` | - | The id of the component. |
| `children` | `React.ReactNode` | - | (upstream leaves the description cell empty) |

**Root.State**: `{}` (empty object type — Root exposes no per-instance state fields itself).

**Root.Actions**: `{ unmount: () => void }`.

**Root.ChangeEventReason**: `'trigger-press' | 'input-press' | 'outside-press' | 'item-press' | 'close-press' | 'escape-key' | 'list-navigation' | 'focus-out' | 'input-change' | 'input-clear' | 'clear-press' | 'chip-remove-press' | 'cancel-open' | 'none'`.

**Root.HighlightEventReason**: `'keyboard' | 'pointer' | 'none'`.

### Trigger

A button that opens the popup. Renders a `<button>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `nativeButton` | `boolean` | `true` | Whether the component renders a native `<button>` element when replacing it via the `render` prop. Set to `false` if the rendered element is not a button (for example, `<div>`). |
| `disabled` | `boolean` | `false` | Whether the component should ignore user interaction. |
| `className` | `string \| ((state: Autocomplete.Trigger.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Trigger.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Trigger.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Trigger data attributes**: `data-popup-open` (present when the corresponding popup is open) · `data-popup-side` (`'top' | 'bottom' | 'left' | 'right' | 'inline-end' | 'inline-start' | null`, indicates which side the corresponding popup is positioned relative to its anchor) · `data-list-empty` (present when the corresponding items list is empty) · `data-pressed` (present when the trigger is pressed) · `data-disabled` (present when the component is disabled) · `data-readonly` (present when the component is readonly) · `data-required` (present when the component is required) · `data-valid` (present when the component is in a valid state, when wrapped in `Field.Root`) · `data-invalid` (present when the component is in an invalid state, when wrapped in `Field.Root`) · `data-dirty` (present when the component's value has changed, when wrapped in `Field.Root`) · `data-touched` (present when the component has been touched, when wrapped in `Field.Root`) · `data-filled` (present when the component has a value, when wrapped in `Field.Root`) · `data-focused` (present when the trigger is focused, when wrapped in `Field.Root`).

### Value

The current value of the autocomplete. Doesn't render its own HTML element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `children` | `React.ReactNode \| ((value: string) => React.ReactNode)` | - | (upstream leaves the description cell empty) |

### Input

A text input to search for items in the list. Renders an `<input>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `disabled` | `boolean` | `false` | Whether the component should ignore user interaction. |
| `className` | `string \| ((state: Autocomplete.Input.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Input.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Input.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Input data attributes**: same set as Trigger — `data-popup-open`, `data-popup-side`, `data-list-empty`, `data-pressed` (present when the input is pressed), `data-disabled`, `data-readonly`, `data-required`, `data-valid`, `data-invalid`, `data-dirty`, `data-touched`, `data-filled`, `data-focused` (present when the input is focused, when wrapped in `Field.Root`).

### InputGroup

A wrapper for the input and its associated controls. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: Autocomplete.InputGroup.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.InputGroup.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.InputGroup.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**InputGroup data attributes**: `data-popup-open`, `data-popup-side`, `data-list-empty`, `data-pressed` (present when the input group is pressed), `data-disabled`, `data-readonly`, `data-valid`, `data-invalid`, `data-dirty`, `data-touched`, `data-filled`, `data-focused` (present when the component is focused, when wrapped in `Field.Root`). Note: upstream's InputGroup attribute list omits `data-required` (present on Trigger/Input/Group but not listed for InputGroup).

### Icon

An icon that indicates that the trigger button opens the popup. Renders a `<span>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: Autocomplete.Icon.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Icon.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Icon.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

Icon has no documented data attributes upstream.

### Clear

Clears the value when clicked. Renders a `<button>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `nativeButton` | `boolean` | `true` | Whether the component renders a native `<button>` element when replacing it via the `render` prop. Set to `false` if the rendered element is not a button (for example, `<div>`). |
| `disabled` | `boolean` | `false` | Whether the component should ignore user interaction. |
| `className` | `string \| ((state: Autocomplete.Clear.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Clear.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `keepMounted` | `boolean` | `false` | Whether the component should remain mounted in the DOM when not visible. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Clear.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Clear data attributes**: `data-popup-open` (present when the corresponding popup is open) · `data-disabled` (present when the button is disabled) · `data-visible` (present when the clear button is visible) · `data-starting-style` (present when the button begins animating in) · `data-ending-style` (present when the button is animating out).

### List

A list container for the items. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `children` | `React.ReactNode \| ((item: any, index: number) => React.ReactNode)` | - | (upstream leaves the description cell empty) |
| `className` | `string \| ((state: Autocomplete.List.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.List.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.List.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

List has no documented data attributes upstream.

### Portal

A portal element that moves the popup to a different part of the DOM. By default, the portal element
is appended to `<body>`. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `container` | `HTMLElement \| ShadowRoot \| React.RefObject<HTMLElement \| ShadowRoot \| null> \| null` | - | A parent element to render the portal element into. |
| `className` | `string \| ((state: Autocomplete.Portal.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Portal.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `keepMounted` | `boolean` | `false` | Whether to keep the portal mounted in the DOM while the popup is hidden. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Portal.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

Portal has no documented data attributes upstream.

### Backdrop

An overlay displayed beneath the popup. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: Autocomplete.Backdrop.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Backdrop.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Backdrop.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Backdrop data attributes**: `data-open` (present when the popup is open) · `data-closed` (present when the popup is closed) · `data-starting-style` (present when the popup begins animating in) · `data-ending-style` (present when the popup is animating out).

### Positioner

Positions the popup against the trigger. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `disableAnchorTracking` | `boolean` | `false` | Whether to disable the popup from tracking any layout shift of its positioning anchor. |
| `align` | `Align` (`'start' \| 'center' \| 'end'`) | `'center'` | How to align the popup relative to the specified side. |
| `alignOffset` | `number \| OffsetFunction` | `0` | Additional offset along the alignment axis in pixels. Also accepts a function that returns the offset to read the dimensions of the anchor and positioner elements, along with its side and alignment. The function takes a `data` object parameter with the following properties: `data.anchor`: the dimensions of the anchor element with properties `width` and `height`. `data.positioner`: the dimensions of the positioner element with properties `width` and `height`. `data.side`: which side of the anchor element the positioner is aligned against. `data.align`: how the positioner is aligned relative to the specified side. |
| `side` | `Side` (`'top' \| 'bottom' \| 'left' \| 'right' \| 'inline-end' \| 'inline-start'`) | `'bottom'` | Which side of the anchor element to align the popup against. May automatically change to avoid collisions. |
| `sideOffset` | `number \| OffsetFunction` | `0` | Distance between the anchor and the popup in pixels. Also accepts a function that returns the distance, with the same `data` object shape described under `alignOffset`. |
| `arrowPadding` | `number` | `5` | Minimum distance to maintain between the arrow and the edges of the popup. Use it to prevent the arrow element from hanging out of the rounded corners of a popup. |
| `anchor` | `Element \| VirtualElement \| React.RefObject<Element \| null> \| (() => Element \| VirtualElement \| null) \| null` | - | An element to position the popup against. By default, the popup will be positioned against the trigger. |
| `collisionAvoidance` | `CollisionAvoidance` | - | Determines how to handle collisions when positioning the popup. `side` controls overflow on the preferred placement axis (`top`/`bottom` or `left`/`right`): `'flip'`: keep the requested side when it fits; otherwise try the opposite side (`top` and `bottom`, or `left` and `right`). `'shift'`: never change side; keep the requested side and move the popup within the clipping boundary so it stays visible. `'none'`: do not correct side-axis overflow. `align` controls overflow on the alignment axis (`start`/`center`/`end`): `'flip'`: keep side, but swap `start` and `end` when the requested alignment overflows. `'shift'`: keep side and requested alignment, then nudge the popup along the alignment axis to fit. `'none'`: do not correct alignment-axis overflow. `fallbackAxisSide` controls fallback behavior on the perpendicular axis when the preferred axis cannot fit: `'start'`: allow perpendicular fallback and try the logical start side first (`top` before `bottom`, or `left` before `right` in LTR). `'end'`: allow perpendicular fallback and try the logical end side first (`bottom` before `top`, or `right` before `left` in LTR). `'none'`: do not fallback to the perpendicular axis. When `side` is `'shift'`, explicitly setting `align` only supports `'shift'` or `'none'`. If `align` is omitted, it defaults to `'flip'`. |
| `collisionBoundary` | `Boundary` | `'clipping-ancestors'` | An element or a rectangle that delimits the area that the popup is confined to. |
| `collisionPadding` | `Padding` | `5` | Additional space to maintain from the edge of the collision boundary. |
| `sticky` | `boolean` | `false` | Whether to maintain the popup in the viewport after the anchor element was scrolled out of view. |
| `positionMethod` | `'absolute' \| 'fixed'` | `'absolute'` | Determines which CSS `position` property to use. |
| `className` | `string \| ((state: Autocomplete.Positioner.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Positioner.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Positioner.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

Upstream `alignOffset`/`sideOffset` function example:

```jsx
<Positioner
  alignOffset={({ side, align, anchor, positioner }) => {
    return side === 'top' || side === 'bottom' ? anchor.width : anchor.height;
  }}
/>
```

Upstream `collisionAvoidance` example:

```jsx
<Positioner
  collisionAvoidance={{
    side: 'shift',
    align: 'shift',
    fallbackAxisSide: 'none',
  }}
/>
```

**Positioner data attributes**: `data-open` · `data-closed` · `data-anchor-hidden` (present when the anchor is hidden) · `data-align` (`'start' | 'center' | 'end'`, indicates how the popup is aligned relative to specified side) · `data-empty` (present when the items list is empty) · `data-side` (`'top' | 'bottom' | 'left' | 'right' | 'inline-end' | 'inline-start'`, indicates which side the popup is positioned relative to the trigger).

**Positioner CSS variables**: `--anchor-height` (`number`, the anchor's height) · `--anchor-width` (`number`, the anchor's width) · `--available-height` (`number`, the available height between the trigger and the edge of the viewport) · `--available-width` (`number`, the available width between the trigger and the edge of the viewport) · `--transform-origin` (`string`, the coordinates that this element is anchored to, used for animations and transitions).

### Popup

A container for the list. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `initialFocus` | `boolean \| React.RefObject<HTMLElement \| null> \| ((openType: InteractionType) => boolean \| void \| HTMLElement \| null)` | - | Determines the element to focus when the popup is opened. `false`: Do not move focus. `true`: Move focus based on the default behavior (first tabbable element or popup). `RefObject`: Move focus to the ref element. `function`: Called with the interaction type (`mouse`, `touch`, `pen`, or `keyboard`). Return an element to focus, `true` to use the default behavior, or `false`/`undefined` to do nothing. |
| `finalFocus` | `boolean \| React.RefObject<HTMLElement \| null> \| ((closeType: InteractionType) => boolean \| void \| HTMLElement \| null)` | - | Determines the element to focus when the popup is closed. `false`: Do not move focus. `true`: Move focus based on the default behavior (trigger or previously focused element). `RefObject`: Move focus to the ref element. `function`: Called with the interaction type (`mouse`, `touch`, `pen`, or `keyboard`). Return an element to focus, `true` to use the default behavior, or `false`/`undefined` to do nothing. |
| `className` | `string \| ((state: Autocomplete.Popup.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Popup.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Popup.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Popup data attributes**: `data-open` · `data-closed` · `data-anchor-hidden` · `data-align` (`'start' | 'center' | 'end'`) · `data-empty` (present when the items list is empty) · `data-side` (`'top' | 'bottom' | 'left' | 'right' | 'inline-end' | 'inline-start'`) · `data-starting-style` (present when the popup begins animating in) · `data-ending-style` (present when the popup is animating out).

### Arrow

Displays an element positioned against the anchor. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: Autocomplete.Arrow.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Arrow.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Arrow.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Arrow data attributes**: `data-open` · `data-closed` · `data-uncentered` (present when the arrow is uncentered) · `data-align` (`'start' | 'center' | 'end'`) · `data-side` (`'top' | 'bottom' | 'left' | 'right' | 'inline-end' | 'inline-start'`).

### Item

An individual item in the list. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `any` | `null` | A unique value that identifies this item. |
| `onClick` | `(event: BaseUIEvent<React.MouseEvent<HTMLDivElement, MouseEvent>>) => void` | - | An optional click handler for the item when selected. It fires when clicking the item with the pointer, as well as when pressing `Enter` with the keyboard if the item is highlighted when the `Input` or `List` element has focus. |
| `index` | `number` | - | The index of the item in the list. Improves performance when specified by avoiding the need to calculate the index automatically from the DOM. |
| `nativeButton` | `boolean` | `false` | Whether the component renders a native `<button>` element when replacing it via the `render` prop. Set to `true` if the rendered element is a native button. |
| `disabled` | `boolean` | `false` | Whether the component should ignore user interaction. |
| `children` | `React.ReactNode` | - | (upstream leaves the description cell empty) |
| `className` | `string \| ((state: Autocomplete.Item.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Item.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Item.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Item data attributes**: `data-highlighted` (present when the item is highlighted) · `data-disabled` (present when the item is disabled).

### Group

Groups related items with the corresponding label. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `items` | `any[]` | - | Items to be rendered within this group. When provided, child `Collection` components will use these items. |
| `className` | `string \| ((state: Autocomplete.Group.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Group.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Group.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Group data attributes**: `data-popup-open` · `data-popup-side` · `data-list-empty` · `data-pressed` (present when the input group is pressed) · `data-disabled` · `data-readonly` · `data-valid` · `data-invalid` · `data-dirty` · `data-touched` · `data-filled` · `data-focused` (present when the component is focused, when wrapped in `Field.Root`). Note: upstream's Group attribute list, like InputGroup's, omits `data-required`.

### GroupLabel

An accessible label that is automatically associated with its parent group. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: Autocomplete.GroupLabel.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.GroupLabel.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.GroupLabel.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

GroupLabel has no documented data attributes upstream.

### Separator

A visual separator between items or groups. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `orientation` | `Orientation` (`'horizontal' \| 'vertical'`) | `'horizontal'` | The orientation of the separator. |
| `className` | `string \| ((state: Autocomplete.Separator.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Separator.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Separator.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

Separator has no documented data attributes upstream.

### Status

Displays a status message whose content changes are announced politely to screen readers. Useful for
conveying the status of an asynchronously loaded list. This component's root element must remain
mounted in the DOM to announce changes consistently across screen readers — upstream says to avoid
hiding or removing the component itself with `display: none`, `hidden`, `aria-hidden`, or conditional
rendering, and to prefer updating or conditionally rendering its children instead. Renders a `<div>`
element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: Autocomplete.Status.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Status.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Status.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

Status has no documented data attributes upstream.

### Empty

Renders its children only when the list is empty. Requires the `items` prop on the root component.
Announces changes politely to screen readers, with the same "keep it mounted" caveat as Status.
Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: Autocomplete.Empty.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Empty.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Empty.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

Empty has no documented data attributes upstream.

### Collection

Renders filtered list items. Doesn't render its own HTML element. If rendering a flat list, pass a
function child to the `List` component instead, which implicitly wraps it.

| Prop | Type | Default | Description |
|---|---|---|---|
| `children`\* | `(item: any, index: number) => React.ReactNode` | - | (upstream leaves the description cell empty; `*` marks it required upstream) |

### Row

Displays a single row of items in a grid list. Enable `grid` on the root component to turn the
listbox into a grid. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: Autocomplete.Row.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: Autocomplete.Row.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: Autocomplete.Row.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

Row has no documented data attributes upstream.

### Hooks

**`useFilter(options?: AutocompleteFilterOptions)`** — matches items against a query using
`Intl.Collator` for robust string matching, and returns an `AutocompleteFilter`:

```typescript
type AutocompleteFilter = {
  /** Returns whether the item matches the query anywhere. */
  contains: <Item>(item: Item, query: string, itemToString?: (item: Item) => string) => boolean;
  /** Returns whether the item starts with the query. */
  startsWith: <Item>(item: Item, query: string, itemToString?: (item: Item) => string) => boolean;
  /** Returns whether the item ends with the query. */
  endsWith: <Item>(item: Item, query: string, itemToString?: (item: Item) => string) => boolean;
};

type AutocompleteFilterOptions = {
  /** The locale to use for string comparison. Defaults to the user's runtime locale. */
  locale?: Intl.LocalesArgument;
};
```

`options` defaults to `{}` upstream.

**`useFilteredItems()`** — returns the internally filtered items as `T[]`. Upstream: "Treat the
result as read-only: it is internal state and may be a shared frozen array."

### ReUI additions

These props appear in ReUI's own example code (`@/components/reui/autocomplete`) on the reui.io page
but are **not** part of the Base UI `Autocomplete` API reference above. They are attested only by
usage in example code, with no upstream type or default — do not treat the bracketed guesses below
as verified types:

- `showClear` (on `AutocompleteInput`) — toggles a built-in clear button. Type not documented; used
  as a bare boolean attribute in examples.
- `showTrigger` (on `AutocompleteInput`) — toggles a built-in trigger button. Type not documented;
  used as a bare boolean attribute in examples.
- `size` (on `AutocompleteInput`) — seen with `"sm"` and `"lg"` values in examples; no upstream
  enum, default, or full value list documented. A third, unlabelled default size is implied but never
  named.
- `variant` — not observed in any example read for this file. Listed in the task's earlier findings
  as a ReUI addition; this pass found no occurrence of it in the mirrored example code, so it is
  reported here as unconfirmed rather than dropped silently.

`itemToStringValue`, `items`, `disabled`, `autoHighlight`, `value`, `onValueChange`, `filter`, `open`,
and `onOpenChange` all exist on `Autocomplete.Root` in the Base UI table above — they are not ReUI
additions. `placeholder` on `AutocompleteInput` is a native `<input>` attribute forwarded through, not
part of the Base UI table because `Input` passes through unlisted native props; it is not a ReUI
addition either.

## Basic usage

```tsx
const items = [
  { value: "apple", label: "Apple" },
  { value: "banana", label: "Banana" },
  { value: "orange", label: "Orange" },
  { value: "grape", label: "Grape" },
]

<Autocomplete items={items}>
  <AutocompleteInput placeholder="Search..." />
  <AutocompleteContent>
    <AutocompleteEmpty>No results found.</AutocompleteEmpty>
    <AutocompleteList>
      {(item) => <AutocompleteItem key={item.value} value={item}>{item.label}</AutocompleteItem>}
    </AutocompleteList>
  </AutocompleteContent>
</Autocomplete>
```

## Examples (titles enumerated upstream, 12 total)

Disabled, Auto Highlight, With Label, With Clear Button, With Trigger Button, With Trigger and Clear
Buttons, With Groups, Async Search, Size, Form (plus the two unlabelled "With Label" and "Form"
example bodies below).

### Disabled

```tsx
import {
  Autocomplete,
  AutocompleteContent,
  AutocompleteEmpty,
  AutocompleteInput,
  AutocompleteItem,
  AutocompleteList,
} from "@/components/reui/autocomplete"

export function Pattern() {
  return (
    <div className="w-full max-w-xs">
      <Autocomplete items={items} disabled>
        <AutocompleteInput placeholder="Search items" />
        <AutocompleteContent>
          <AutocompleteEmpty>No items found.</AutocompleteEmpty>
          <AutocompleteList>
            {(item) => (
              <AutocompleteItem key={item.id} value={item.value}>
                {item.value}
              </AutocompleteItem>
            )}
          </AutocompleteList>
        </AutocompleteContent>
      </Autocomplete>
    </div>
  )
}

interface Item {
  id: string
  value: string
}

const items: Item[] = [
  { id: "t1", value: "feature" },
  { id: "t2", value: "fix" },
  { id: "t3", value: "bug" },
  { id: "t4", value: "docs" },
  { id: "t5", value: "internal" },
  { id: "t6", value: "mobile" },
  { id: "c-accordion", value: "component: accordion" },
  // ... full option list continues with one entry per shadcn component in the docs registry
]
```

### Auto Highlight

Same structure as Disabled, with `autoHighlight` instead of `disabled` on `<Autocomplete>`.

### With Label

```tsx
import {
  Autocomplete,
  AutocompleteContent,
  AutocompleteEmpty,
  AutocompleteInput,
  AutocompleteItem,
  AutocompleteList,
} from "@/components/reui/autocomplete"
import { Label } from "@/components/ui/label"

export function Pattern() {
  return (
    <div className="w-full max-w-xs">
      <Autocomplete items={items} autoHighlight>
        <div className="flex flex-col items-start gap-2">
          <Label htmlFor="with-label">Label</Label>
          <AutocompleteInput id="with-label" placeholder="e.g. feature" />
        </div>
        <AutocompleteContent>
          <AutocompleteEmpty>No items found.</AutocompleteEmpty>
          <AutocompleteList>
            {(item) => (
              <AutocompleteItem key={item.id} value={item.value}>
                {item.value}
              </AutocompleteItem>
            )}
          </AutocompleteList>
        </AutocompleteContent>
      </Autocomplete>
    </div>
  )
}
```

### With Clear Button

```tsx
"use client"

import { useState } from "react"
import {
  Autocomplete,
  AutocompleteContent,
  AutocompleteEmpty,
  AutocompleteInput,
  AutocompleteItem,
  AutocompleteList,
} from "@/components/reui/autocomplete"

export function Pattern() {
  const [value, setValue] = useState<string>("")
  const filteredItems = items.filter((item) =>
    item.value.toLowerCase().includes(value.toLowerCase())
  )

  return (
    <div className="w-full max-w-xs">
      <Autocomplete
        value={value}
        onValueChange={setValue}
        items={filteredItems}
        itemToStringValue={(item: unknown) => (item as Item).value}
      >
        <AutocompleteInput placeholder="e.g. feature" showClear />
        <AutocompleteContent>
          <AutocompleteEmpty>No items found.</AutocompleteEmpty>
          <AutocompleteList>
            {(item) => (
              <AutocompleteItem key={item.id} value={item}>
                {item.value}
              </AutocompleteItem>
            )}
          </AutocompleteList>
        </AutocompleteContent>
      </Autocomplete>
    </div>
  )
}
```

### With Trigger Button

Identical structure to "With Clear Button", replacing `showClear` with `showTrigger` on
`<AutocompleteInput>`.

### With Trigger and Clear Buttons

Identical structure, `<AutocompleteInput placeholder="e.g. feature" showTrigger showClear />`.

### With Groups

```tsx
"use client"

import { useMemo, useState } from "react"
import {
  Autocomplete,
  AutocompleteCollection,
  AutocompleteContent,
  AutocompleteEmpty,
  AutocompleteGroup,
  AutocompleteGroupLabel,
  AutocompleteInput,
  AutocompleteItem,
  AutocompleteList,
} from "@/components/reui/autocomplete"
import { Autocomplete as AutocompletePrimitive } from "@base-ui/react/autocomplete"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

export function Pattern() {
  const [value, setValue] = useState("")
  const [open, setOpen] = useState(false)
  const { contains } = AutocompletePrimitive.useFilter({ sensitivity: "base" })
  const filteredItems = useMemo(() => {
    if (!value) return groupedUsers
    return groupedUsers
      .map((group) => ({
        ...group,
        items: (group.items || []).filter(
          (item) =>
            contains(item.name || "", value) ||
            contains(item.group || "", value) ||
            contains(item.position || "", value)
        ),
      }))
      .filter((group) => group.items && group.items.length > 0)
  }, [value, contains])

  return (
    <div className="w-full max-w-xs">
      <Autocomplete
        items={filteredItems}
        value={value}
        onValueChange={setValue}
        open={open}
        onOpenChange={setOpen}
        itemToStringValue={(item: unknown) => (item as User).name}
        filter={null}
      >
        <AutocompleteInput placeholder="e.g. John, Developer, Marketing" />
        {open && (
          <AutocompleteContent className="pt-0">
            {filteredItems.length === 0 ? (
              <AutocompleteEmpty>No matching users found.</AutocompleteEmpty>
            ) : (
              <AutocompleteList className="not-empty:py-0">
                {(group: UserGroup) => (
                  <AutocompleteGroup key={group.group} items={group.items} className="py-0">
                    <AutocompleteGroupLabel className="bg-background text-muted-foreground sticky top-0 z-10 me-1.5 py-2.5 text-xs font-medium">
                      {group.group}
                    </AutocompleteGroupLabel>
                    <AutocompleteCollection>
                      {(item: User) => (
                        <AutocompleteItem key={item.id} value={item} className="flex items-center gap-2.5 rounded-lg">
                          <Avatar className="size-9">
                            <AvatarImage src={item.avatar} alt={item.name || "User"} />
                            <AvatarFallback>
                              {(item.name || "U").split(" ").map((n) => n[0]).join("")}
                            </AvatarFallback>
                          </Avatar>
                          <div className="min-w-0 flex-1">
                            <div className="truncate font-medium">{item.name || "Unknown"}</div>
                            <div className="text-muted-foreground truncate text-sm">
                              {item.position || "No position available"}
                            </div>
                          </div>
                        </AutocompleteItem>
                      )}
                    </AutocompleteCollection>
                  </AutocompleteGroup>
                )}
              </AutocompleteList>
            )}
          </AutocompleteContent>
        )}
      </Autocomplete>
    </div>
  )
}

interface User {
  id: string
  name: string
  group: string
  position: string
  avatar: string
  status: "Active" | "Inactive" | "Away"
}

interface UserGroup {
  group: string
  items: User[]
}

// usersData: User[] grouped by "Development Team", "Design Team", "Marketing Team",
// "Sales Team", "Management Team", "Support Team" (26 users total upstream).

function groupUsers(users: User[]): UserGroup[] {
  const groups: { [key: string]: User[] } = {}
  users.forEach((item) => {
    ;(groups[item.group] ??= []).push(item)
  })
  // Sort by status within each group (Active first, then Away, then Inactive)
  Object.keys(groups).forEach((group) => {
    groups[group].sort((a, b) => {
      const statusOrder = { Active: 0, Away: 1, Inactive: 2 }
      return statusOrder[a.status] - statusOrder[b.status]
    })
  })
  const order = [
    "Management Team",
    "Development Team",
    "Design Team",
    "Marketing Team",
    "Sales Team",
    "Support Team",
  ]
  return order.map((group) => ({ group, items: groups[group] ?? [] }))
}

const groupedUsers: UserGroup[] = groupUsers(usersData)
```

### Async Search

```tsx
"use client"

import { ReactNode, useEffect, useState } from "react"
import {
  Autocomplete,
  AutocompleteContent,
  AutocompleteInput,
  AutocompleteItem,
  AutocompleteList,
  AutocompleteStatus,
} from "@/components/reui/autocomplete"
import { Autocomplete as AutocompletePrimitive } from "@base-ui/react/autocomplete"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { LoaderCircleIcon } from "lucide-react"

export function Pattern() {
  const [searchValue, setSearchValue] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [searchResults, setSearchResults] = useState<Developer[]>([])
  const [error, setError] = useState<string | null>(null)
  const { contains } = AutocompletePrimitive.useFilter({ sensitivity: "base" })

  useEffect(() => {
    if (!searchValue) {
      setSearchResults([])
      setIsLoading(false)
      return undefined
    }
    setIsLoading(true)
    setError(null)
    let ignore = false
    async function fetchDevelopers() {
      try {
        const results = await searchDevelopers(searchValue, contains)
        if (!ignore) setSearchResults(results)
      } catch {
        if (!ignore) {
          setError("Failed to fetch developers. Please try again.")
          setSearchResults([])
        }
      } finally {
        if (!ignore) setIsLoading(false)
      }
    }
    const timeoutId = setTimeout(fetchDevelopers, 300)
    return () => {
      clearTimeout(timeoutId)
      ignore = true
    }
  }, [searchValue, contains])

  let status: ReactNode = ""
  if (isLoading) {
    status = (
      <div className="flex items-center gap-2">
        <LoaderCircleIcon className="size-4 animate-spin" />
        Searching developers...
      </div>
    )
  } else if (error) {
    status = error
  } else if (searchResults.length === 0 && searchValue) {
    status = `No developers found for "${searchValue}"`
  } else if (searchResults.length > 0) {
    status = `${searchResults.length} developer${searchResults.length === 1 ? "" : "s"} found`
  } else if (!searchValue) {
    status = "Start typing to search developers..."
  }

  const shouldRenderPopup = searchValue !== ""

  return (
    <div className="w-full max-w-xs">
      <Autocomplete
        items={searchResults}
        value={searchValue}
        onValueChange={setSearchValue}
        itemToStringValue={(item: unknown) => (item as Developer).name}
        filter={null}
      >
        <AutocompleteInput placeholder="e.g. John Smith, React, San Francisco" showTrigger showClear />
        {shouldRenderPopup && (
          <AutocompleteContent>
            <AutocompleteStatus>{status}</AutocompleteStatus>
            <AutocompleteList>
              {(developer: Developer) => (
                <AutocompleteItem key={developer.id} value={developer} className="rounded-lg">
                  <div className="flex items-center gap-2.5 truncate">
                    <Avatar className="size-9">
                      <AvatarImage src={developer.avatar} alt={developer.name} />
                      <AvatarFallback>
                        {developer.name.split(" ").map((n) => n[0]).join("")}
                      </AvatarFallback>
                    </Avatar>
                    <div className="min-w-0 flex-1">
                      <div className="truncate font-medium">{developer.name}</div>
                      <div className="text-muted-foreground truncate text-sm">
                        {developer.role} • {developer.location}
                      </div>
                    </div>
                  </div>
                </AutocompleteItem>
              )}
            </AutocompleteList>
          </AutocompleteContent>
        )}
      </Autocomplete>
    </div>
  )
}

async function searchDevelopers(
  query: string,
  filter: (item: string, query: string) => boolean
): Promise<Developer[]> {
  // Simulate network delay
  await new Promise((resolve) => {
    setTimeout(resolve, Math.random() * 800 + 200)
  })
  // Simulate occasional network errors (2% chance)
  if (Math.random() < 0.02 || query === "error") {
    throw new Error("Network error")
  }
  return topDevelopers.filter(
    (developer) =>
      filter(developer.name, query) ||
      filter(developer.role, query) ||
      filter(developer.location, query) ||
      developer.skills.some((skill) => filter(skill, query))
  )
}

interface Developer {
  id: string
  name: string
  role: string
  location: string
  skills: string[]
  experience: number
  rating: number
  avatar: string
}

// topDevelopers: Developer[], 25 sample entries upstream.
```

### Size

```tsx
<AutocompleteInput placeholder="Search items" size="sm" showTrigger showClear />
```

and equivalently `size="lg"`. (Default size is unlabelled in the upstream markup; only `sm` and `lg`
example variants are shown.)

### Form

Same composition as the basic usage example, items are the same option-list dataset with capitalized
labels (`"Feature"`, `"Fix"`, `"Bug"`, …). No form-library integration code (e.g. react-hook-form) is
shown on this page beyond that composition — the page does not otherwise document a `Form`
sub-component or validation hook.

## Base UI vs Radix UI

The Base UI and Radix UI pages are otherwise identical: same installation command
(`@reui/autocomplete`), same import path (`@/components/reui/autocomplete`), same 12 example titles,
same code. The only textual difference is the marketing sentence under "Free Components":

- Base UI: "These examples use Base UI primitives from `@base-ui/react`..."
- Radix UI: "These examples follow the Radix UI implementation with accessible primitives from the
  Radix stack..."

No prop, no default, and no import path differs between builds for this component (the "With Groups"
example imports `Autocomplete as AutocompletePrimitive` from `@base-ui/react/autocomplete` on the Base
UI page — the Radix twin was not independently checked for a different primitive import here, but no
diff was reported by the file comparison beyond the marketing line and the component's own import
path is otherwise the same).

**The "API Reference" link is also identical between builds**: on both `docs/components/base/autocomplete`
and `docs/components/radix/autocomplete`, the badge points at
`https://base-ui.com/react/components/autocomplete`. Radix UI Primitives (radix-ui.com) has no
`autocomplete` or `combobox` component to link to — see the [API Reference](#api-reference) section
above.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI,
`style: "radix-nova"` means Radix UI.

## Source

- reui.io, Base UI build: `docs/components/base/autocomplete` — mirror captured 2026-09-04.
- reui.io, Radix UI build: `docs/components/radix/autocomplete` — mirror captured 2026-09-04. Its own
  "API Reference" link resolves to the same Base UI URL as the Base UI build (verified 2026-09-04).
- Primitive library for the API Reference section (both builds): Base UI,
  [`https://base-ui.com/react/components/autocomplete`](https://base-ui.com/react/components/autocomplete)
  (markdown twin `.../autocomplete.md`, "API reference" section) — retrieved 2026-09-04.
- Checked and found to have no counterpart: Radix UI Primitives component index at
  [`https://www.radix-ui.com/primitives/docs/overview/introduction`](https://www.radix-ui.com/primitives/docs/overview/introduction)
  lists 29 components, none named `autocomplete` or `combobox` — checked 2026-09-04.
