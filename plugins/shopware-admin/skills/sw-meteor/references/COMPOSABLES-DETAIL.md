# Meteor Component Library — composables & directives

Source: `packages/component-library/src/composables/`, `packages/component-library/src/directives/`,
`packages/component-library/src/plugin/`, `packages/component-library/src/index.ts`

**Important**: The Admin SDK composables (`useRepository`, `useSharedState`) are documented in the skill
`sw-meteor-admin-sdk`. This skill covers exclusively the composables and directives
of the **Component Library** (`@shopware-ag/meteor-component-library`).

---

## Contents

- [Exports from @shopware-ag/meteor-component-library](#exports-from-shopware-agmeteor-component-library)
- [Directives](#directives)
- [Composables](#composables)
- [Plugins](#plugins)
- [Internal composable: usePriorityPlusNavigation](#internal-composable-usepriorityplusnavigation)
- [Component-specific composables](#component-specific-composables)
- [Complete export list](#complete-export-list)
- [Scope boundary: Admin SDK composables](#scope-boundary-admin-sdk-composables)

## Exports from @shopware-ag/meteor-component-library

Besides components, the library exports the following utilities:

```ts
import {
  TooltipDirective,    // v-tooltip directive
  DeviceHelperPlugin,  // $device helper plugin
  useSnackbar,         // snackbar composable
} from "@shopware-ag/meteor-component-library";
```

---

## Directives

### v-tooltip

**File**: `src/directives/tooltip.directive.ts`

Shows a tooltip on the hover event of the associated element.

#### Simplest usage

```html
<!-- Tooltip with the default width of 200px and position top -->
<button v-tooltip="'Some text'">Hover me</button>
```

#### With a position modifier

```html
<!-- Position via modifier -->
<button v-tooltip.bottom="'Some text'">Hover me</button>
<button v-tooltip.right="'Some text'">Hover me</button>
<button v-tooltip.left="'Some text'">Hover me</button>
```

#### With object configuration

```html
<button v-tooltip="{ message: 'Some Text', width: 300, position: 'bottom' }">
  Hover me
</button>

<!-- Alternative: position via modifier -->
<button v-tooltip.bottom="{ message: 'Some Text', width: 300 }">
  Hover me
</button>

<!-- With delay -->
<button v-tooltip.bottom="{ message: 'Some Text', width: 200, showDelay: 200, hideDelay: 300 }">
  Hover me
</button>
```

#### Configuration options

| Option | Type | Default | Description |
|---|---|---|---|
| `message` | `string` | — | **Required** in the object form. Text of the tooltip |
| `position` | `'top' \| 'right' \| 'bottom' \| 'left'` | `'top'` | Position relative to the element |
| `width` | `number \| 'auto'` | `200` | Width of the tooltip in px or `'auto'` |
| `showDelay` | `number` | `100` | Delay in ms before showing |
| `hideDelay` | `number` | `showDelay` | Delay in ms before hiding |
| `disabled` | `boolean` | `false` | Disable the tooltip |
| `appearance` | `string` | `'dark'` | The CSS class `mt-tooltip--{appearance}` is set |
| `showOnDisabledElements` | `boolean` | `false` | Show the tooltip on disabled elements too (inserts a wrapper div) |
| `zIndex` | `number \| null` | `null` | z-index of the tooltip element |

**Note**: The `position` option takes precedence over the modifier. The tooltip adapts automatically to the viewport (it switches to the next possible position when outside the viewport).

#### Registering it as a global directive

```ts
import { createApp } from "vue";
import { TooltipDirective } from "@shopware-ag/meteor-component-library";
import App from "./App.vue";

const app = createApp(App);
app.directive("tooltip", TooltipDirective);
app.mount("#app");
```

#### Alternative: the mt-tooltip component

For more complex scenarios the component `MtTooltip` is available.

---

### v-draggable and v-droppable

**File**: `src/directives/dragdrop.directive.ts`

Two directives that belong together and provide drag-and-drop functionality.

#### v-draggable

Makes an element draggable:

```html
<div v-draggable="{ data: myData, onDrop: handleDrop }">Drag me</div>
```

#### v-droppable

Defines an element as a drop zone:

```html
<div v-droppable="{ data: zoneData, onDrop: handleDrop }">Drop here</div>
```

#### DragConfig options

| Option | Type | Default | Description |
|---|---|---|---|
| `delay` | `number` | `100` | Delay in ms before the drag starts |
| `dragGroup` | `number \| string` | `1` | Group ID — drag and drop must share the same group |
| `draggableCls` | `string` | `'is--draggable'` | CSS class when draggable |
| `draggingStateCls` | `string` | `'is--dragging'` | CSS class while dragging |
| `dragElementCls` | `string` | `'is--drag-element'` | CSS class of the drag proxy element |
| `validDragCls` | `string` | `'is--valid-drag'` | CSS class for a valid drop target |
| `invalidDragCls` | `string` | `'is--invalid-drag'` | CSS class for an invalid drop target |
| `preventEvent` | `boolean` | `true` | `preventDefault()` and `stopPropagation()` on drag events |
| `validateDrop` | `function \| null` | `null` | Custom validation: `(dragData, dropData) => boolean` |
| `validateDrag` | `function \| null` | `null` | Custom drag validation: `(dragData, dropData) => boolean` |
| `validateDragStart` | `function \| null` | `null` | Start validation: `(dragData, el, event) => boolean` |
| `onDragStart` | `function \| null` | `null` | Callback: `(dragConfig, el, dragElement) => void` |
| `onDragEnter` | `function \| null` | `null` | Callback: `(dragData, dropData, valid) => void` |
| `onDragLeave` | `function \| null` | `null` | Callback: `(dragData, dropData) => void` |
| `onDrop` | `function \| null` | `null` | Drop callback: `(dragData, dropData) => void` |
| `data` | `any` | `null` | Custom data associated with the drag element |
| `disabled` | `boolean` | `false` | Disable dragging |

#### DropConfig options

| Option | Type | Default | Description |
|---|---|---|---|
| `dragGroup` | `number \| string` | `1` | Must match the `dragGroup` of the draggable elements |
| `droppableCls` | `string` | `'is--droppable'` | CSS class when droppable |
| `validDropCls` | `string` | `'is--valid-drop'` | CSS class for a valid drag above it |
| `invalidDropCls` | `string` | `'is--invalid-drop'` | CSS class for an invalid drag above it |
| `validateDrop` | `function \| null` | `null` | Custom validation: `(dragData, dropData) => boolean` |
| `onDrop` | `function \| null` | `null` | Drop callback: `(dragData, dropData) => void` |
| `data` | `any` | `null` | Custom data of the drop zone |

#### Complete example

```html
<div
  v-draggable="{
    dragGroup: 'my-list',
    data: { id: item.id, name: item.name },
    onDragStart: (config, el, dragEl) => console.log('Started dragging', config.data),
    onDrop: (dragData, dropData) => moveItem(dragData, dropData),
    validateDragStart: (data, el, event) => !el.classList.contains('is--locked'),
  }"
>
  Drag item
</div>

<div
  v-droppable="{
    dragGroup: 'my-list',
    data: { position: 0 },
    onDrop: (dragData, dropData) => reorder(dragData, dropData),
    validateDrop: (dragData, dropData) => dragData.id !== dropData.id,
  }"
>
  Drop zone
</div>
```

#### Registering them as global directives

```ts
import { draggable, droppable } from "@shopware-ag/meteor-component-library/directives/dragdrop.directive";

app.directive("draggable", draggable);
app.directive("droppable", droppable);
```

---

### v-sticky-column

**File**: `src/directives/stickyColumn.directive.ts`

Makes table columns sticky (scroll horizontally, the column stays visible). Automatically computes the cumulative width of all preceding sticky columns.

```html
<td v-sticky-column>Sticky Column</td>
<!-- Multiple sticky columns: automatic positioning -->
<td v-sticky-column>First sticky</td>
<td v-sticky-column>Second sticky (positioned after first)</td>
```

Internally `data-sticky-column` is set on the element. A `MutationObserver` watches DOM changes and updates the `left` position.

---

### v-popover (deprecated)

**File**: `src/directives/popover.directive.ts`

> **Deprecated**: Do not use it any more. Use the `mt-floating-ui` component instead.

---

## Composables

### useId

**File**: `src/composables/useId.ts`

Generates a unique ID after the component has mounted (server-safe). Useful for `id`/`aria-labelledby` links.

```ts
import { useId } from "@shopware-ag/meteor-component-library/composables/useId";

const id = useId();
// id.value is undefined until mounted
// after mount: id.value = "unique-string"
```

```html
<label :for="id">Label</label>
<input :id="id" type="text" />
```

---

### useEmptySlotCheck

**File**: `src/composables/useEmptySlotCheck.ts`

Checks whether a slot is empty (ignores comment nodes and empty text nodes).

```ts
import useEmptySlotCheck from "@shopware-ag/meteor-component-library/composables/useEmptySlotCheck";

const { hasSlotContent, isSlotEmpty } = useEmptySlotCheck();
```

```vue
<script setup>
import { useSlots } from "vue";
import useEmptySlotCheck from "@shopware-ag/meteor-component-library/composables/useEmptySlotCheck";

const slots = useSlots();
const { hasSlotContent } = useEmptySlotCheck();

const hasFooter = computed(() => hasSlotContent(slots.footer));
</script>

<template>
  <div>
    <slot />
    <footer v-if="hasFooter">
      <slot name="footer" />
    </footer>
  </div>
</template>
```

**API:**

| Function | Signature | Description |
|---|---|---|
| `hasSlotContent` | `(slot, props?) => boolean` | Returns `true` when the slot has content |
| `isSlotEmpty` | `(slot, props?) => boolean` | Returns `true` when the slot is empty |

---

### useFutureFlags

**File**: `src/composables/useFutureFlags.ts`

Feature flags for upcoming breaking changes. Allows a gradual opt-in into new behaviour before a major release.

```ts
import { provideFutureFlags, useFutureFlags } from "@shopware-ag/meteor-component-library/composables/useFutureFlags";
import type { FutureFlags } from "@shopware-ag/meteor-component-library/composables/useFutureFlags";
```

#### Available flags

```ts
const defaultFutureFlags = {
  removeCardWidth: false,   // mt-card: remove the width prop
  removeDefaultMargin: false, // remove the default margins
};
```

#### Provider (root level or layout component)

```ts
import { provideFutureFlags } from "@shopware-ag/meteor-component-library/composables/useFutureFlags";

// In the setup() of a parent component
provideFutureFlags({
  removeCardWidth: true,
  removeDefaultMargin: true,
});
```

#### Consumer (in component implementations)

```ts
import { useFutureFlags } from "@shopware-ag/meteor-component-library/composables/useFutureFlags";

const flags = useFutureFlags();

if (flags.removeCardWidth) {
  // new behaviour
} else {
  // old behaviour
}
```

---

### useSnackbar

**File**: `src/components/feedback-indicator/mt-snackbar/composables/use-snackbar.ts`

Shows snackbar messages programmatically. Requires `MtSnackbar` in the layout.

```ts
import { useSnackbar } from "@shopware-ag/meteor-component-library";
```

```vue
<!-- Layout/root component: include MtSnackbar -->
<template>
  <div>
    <RouterView />
    <MtSnackbar />
  </div>
</template>

<script setup>
import { MtSnackbar } from "@shopware-ag/meteor-component-library";
</script>
```

```vue
<!-- In any component -->
<script setup>
import { useSnackbar } from "@shopware-ag/meteor-component-library";

const snackbar = useSnackbar();

function save() {
  // ...save...
  snackbar.dispatch({
    // snackbar configuration (matches the mt-snackbar props)
  });
}
</script>
```

---

## Plugins

### DeviceHelperPlugin

**File**: `src/plugin/device-helper.plugin.ts`

Registers a `$device` helper on the Vue instance for responsive queries and resize listeners.

```ts
import { DeviceHelperPlugin } from "@shopware-ag/meteor-component-library";

app.use(DeviceHelperPlugin);
```

After installation `this.$device` (Options API) or `inject('$device')` (Composition API) is available. The plugin mixin automatically cleans up resize listeners in the `unmounted` lifecycle hook.

---

## Internal composable: usePriorityPlusNavigation

**File**: `src/composables/_internal/usePriorityPlusNavigation.ts`

Internal composable for the priority-plus navigation (tabs that move into a "More" dropdown when space runs short). Not intended for external use.

---

## Component-specific composables

These composables are specific to individual components and are not intended as standalone utilities:

| Composable | Component | Purpose |
|---|---|---|
| `useModalContext` | `mt-modal` | Context for modal sub-components |
| `useIsInsideTooltip` | `mt-tooltip` | Checks whether inside the tooltip context |
| `useTooltipState` | `mt-tooltip` | Tooltip state management |
| `useScrollPossibilitiesClasses` | `mt-data-table` | Scroll indicator classes for tables |

---

## Complete export list

```ts
// Directives
export { TooltipDirective } from "@shopware-ag/meteor-component-library";

// Plugins
export { DeviceHelperPlugin } from "@shopware-ag/meteor-component-library";

// Composables
export { useSnackbar } from "@shopware-ag/meteor-component-library";

// Drag/drop (separate imports)
import { draggable, droppable } from "@shopware-ag/meteor-component-library/src/directives/dragdrop.directive";
```

---

## Scope boundary: Admin SDK composables

The following composables belong to the Admin SDK (`@shopware-ag/meteor-admin-sdk`), not to the Component Library:

- `composables.useRepository` — reactive repository composable for SDK extensions
- `composables.useSharedState` — state shared across SDK locations (via IndexedDB)

They are documented in the skill `sw-meteor-admin-sdk`.
