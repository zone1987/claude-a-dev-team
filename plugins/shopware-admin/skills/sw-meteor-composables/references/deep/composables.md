# Meteor Component Library — Composables & Direktiven

Quelle: `packages/component-library/src/composables/`, `packages/component-library/src/directives/`,
`packages/component-library/src/plugin/`, `packages/component-library/src/index.ts`

**Wichtig**: Die Composables des Admin SDK (`useRepository`, `useSharedState`) sind im Skill
`sw-meteor-admin-sdk` dokumentiert. Dieser Skill deckt ausschließlich die Composables und Direktiven
der **Component Library** (`@shopware-ag/meteor-component-library`) ab.

---

## Exports aus @shopware-ag/meteor-component-library

Neben Komponenten exportiert die Library folgende Utilities:

```ts
import {
  TooltipDirective,    // v-tooltip Direktive
  DeviceHelperPlugin,  // $device Helper Plugin
  useSnackbar,         // Snackbar Composable
} from "@shopware-ag/meteor-component-library";
```

---

## Direktiven

### v-tooltip

**Datei**: `src/directives/tooltip.directive.ts`

Zeigt einen Tooltip beim Hover-Ereignis auf dem zugehörigen Element.

#### Einfachste Verwendung

```html
<!-- Tooltip mit Standard-Breite 200px und Position top -->
<button v-tooltip="'Some text'">Hover me</button>
```

#### Mit Positions-Modifier

```html
<!-- Position durch Modifier -->
<button v-tooltip.bottom="'Some text'">Hover me</button>
<button v-tooltip.right="'Some text'">Hover me</button>
<button v-tooltip.left="'Some text'">Hover me</button>
```

#### Mit Objekt-Konfiguration

```html
<button v-tooltip="{ message: 'Some Text', width: 300, position: 'bottom' }">
  Hover me
</button>

<!-- Alternative: Position durch Modifier -->
<button v-tooltip.bottom="{ message: 'Some Text', width: 300 }">
  Hover me
</button>

<!-- Mit Delay -->
<button v-tooltip.bottom="{ message: 'Some Text', width: 200, showDelay: 200, hideDelay: 300 }">
  Hover me
</button>
```

#### Konfigurationsoptionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `message` | `string` | — | **Pflicht** wenn Object-Form. Text des Tooltips |
| `position` | `'top' \| 'right' \| 'bottom' \| 'left'` | `'top'` | Position relativ zum Element |
| `width` | `number \| 'auto'` | `200` | Breite des Tooltips in px oder `'auto'` |
| `showDelay` | `number` | `100` | Verzögerung in ms vor dem Einblenden |
| `hideDelay` | `number` | `showDelay` | Verzögerung in ms vor dem Ausblenden |
| `disabled` | `boolean` | `false` | Tooltip deaktivieren |
| `appearance` | `string` | `'dark'` | CSS-Klasse `mt-tooltip--{appearance}` wird gesetzt |
| `showOnDisabledElements` | `boolean` | `false` | Tooltip auch auf deaktivierten Elementen anzeigen (fügt Wrapper-Div ein) |
| `zIndex` | `number \| null` | `null` | z-Index des Tooltip-Elements |

**Hinweis**: `position`-Option hat höhere Priorität als Modifier. Tooltip passt sich automatisch an den Viewport an (wechselt zur nächstmöglichen Position wenn außerhalb des Viewports).

#### Registrieren als globale Direktive

```ts
import { createApp } from "vue";
import { TooltipDirective } from "@shopware-ag/meteor-component-library";
import App from "./App.vue";

const app = createApp(App);
app.directive("tooltip", TooltipDirective);
app.mount("#app");
```

#### Alternativ: mt-tooltip Komponente

Für komplexere Szenarien steht die Komponente `MtTooltip` zur Verfügung.

---

### v-draggable und v-droppable

**Datei**: `src/directives/dragdrop.directive.ts`

Zwei zusammengehörige Direktiven für Drag-and-Drop-Funktionalität.

#### v-draggable

Macht ein Element ziehbar:

```html
<div v-draggable="{ data: myData, onDrop: handleDrop }">Drag me</div>
```

#### v-droppable

Definiert ein Element als Drop-Zone:

```html
<div v-droppable="{ data: zoneData, onDrop: handleDrop }">Drop here</div>
```

#### DragConfig Optionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `delay` | `number` | `100` | Verzögerung in ms bevor Drag startet |
| `dragGroup` | `number \| string` | `1` | Gruppen-ID — Drag und Drop müssen gleiche Gruppe haben |
| `draggableCls` | `string` | `'is--draggable'` | CSS-Klasse wenn draggable |
| `draggingStateCls` | `string` | `'is--dragging'` | CSS-Klasse während des Dragging |
| `dragElementCls` | `string` | `'is--drag-element'` | CSS-Klasse des Drag-Proxy-Elements |
| `validDragCls` | `string` | `'is--valid-drag'` | CSS-Klasse bei validem Drop-Ziel |
| `invalidDragCls` | `string` | `'is--invalid-drag'` | CSS-Klasse bei invalidem Drop-Ziel |
| `preventEvent` | `boolean` | `true` | `preventDefault()` und `stopPropagation()` auf Drag-Events |
| `validateDrop` | `function \| null` | `null` | Custom-Validierung: `(dragData, dropData) => boolean` |
| `validateDrag` | `function \| null` | `null` | Custom-Drag-Validierung: `(dragData, dropData) => boolean` |
| `validateDragStart` | `function \| null` | `null` | Start-Validierung: `(dragData, el, event) => boolean` |
| `onDragStart` | `function \| null` | `null` | Callback: `(dragConfig, el, dragElement) => void` |
| `onDragEnter` | `function \| null` | `null` | Callback: `(dragData, dropData, valid) => void` |
| `onDragLeave` | `function \| null` | `null` | Callback: `(dragData, dropData) => void` |
| `onDrop` | `function \| null` | `null` | Drop-Callback: `(dragData, dropData) => void` |
| `data` | `any` | `null` | Custom-Daten die mit dem Drag-Element verbunden werden |
| `disabled` | `boolean` | `false` | Dragging deaktivieren |

#### DropConfig Optionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `dragGroup` | `number \| string` | `1` | Muss mit `dragGroup` der draggable Elemente übereinstimmen |
| `droppableCls` | `string` | `'is--droppable'` | CSS-Klasse wenn droppable |
| `validDropCls` | `string` | `'is--valid-drop'` | CSS-Klasse bei validem Drag darüber |
| `invalidDropCls` | `string` | `'is--invalid-drop'` | CSS-Klasse bei invalidem Drag darüber |
| `validateDrop` | `function \| null` | `null` | Custom-Validierung: `(dragData, dropData) => boolean` |
| `onDrop` | `function \| null` | `null` | Drop-Callback: `(dragData, dropData) => void` |
| `data` | `any` | `null` | Custom-Daten der Drop-Zone |

#### Vollständiges Beispiel

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

#### Registrieren als globale Direktiven

```ts
import { draggable, droppable } from "@shopware-ag/meteor-component-library/directives/dragdrop.directive";

app.directive("draggable", draggable);
app.directive("droppable", droppable);
```

---

### v-sticky-column

**Datei**: `src/directives/stickyColumn.directive.ts`

Macht Tabellenspalten sticky (horizontal scrollen, Spalte bleibt sichtbar). Berechnet automatisch die kumulierte Breite aller vorangehenden sticky Spalten.

```html
<td v-sticky-column>Sticky Column</td>
<!-- Mehrere sticky Spalten: automatische Positionierung -->
<td v-sticky-column>First sticky</td>
<td v-sticky-column>Second sticky (positioned after first)</td>
```

Intern wird `data-sticky-column` auf das Element gesetzt. Ein `MutationObserver` überwacht DOM-Änderungen und aktualisiert die `left`-Position.

---

### v-popover (deprecated)

**Datei**: `src/directives/popover.directive.ts`

> **Deprecated**: Nicht mehr verwenden. Stattdessen `mt-floating-ui` Komponente nutzen.

---

## Composables

### useId

**Datei**: `src/composables/useId.ts`

Generiert eine eindeutige ID nach dem Mounten der Komponente (server-safe). Nützlich für `id`/`aria-labelledby` Verknüpfungen.

```ts
import { useId } from "@shopware-ag/meteor-component-library/composables/useId";

const id = useId();
// id.value ist undefined bis mounted
// nach mount: id.value = "einzigartiger-string"
```

```html
<label :for="id">Label</label>
<input :id="id" type="text" />
```

---

### useEmptySlotCheck

**Datei**: `src/composables/useEmptySlotCheck.ts`

Prüft ob ein Slot leer ist (ignoriert Comment-Nodes und leere Text-Nodes).

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

| Funktion | Signatur | Beschreibung |
|---|---|---|
| `hasSlotContent` | `(slot, props?) => boolean` | Gibt `true` zurück wenn der Slot Inhalt hat |
| `isSlotEmpty` | `(slot, props?) => boolean` | Gibt `true` zurück wenn der Slot leer ist |

---

### useFutureFlags

**Datei**: `src/composables/useFutureFlags.ts`

Feature-Flags für zukünftige Breaking Changes. Ermöglicht schrittweises Opt-in in neue Verhaltensweisen vor einem Major-Release.

```ts
import { provideFutureFlags, useFutureFlags } from "@shopware-ag/meteor-component-library/composables/useFutureFlags";
import type { FutureFlags } from "@shopware-ag/meteor-component-library/composables/useFutureFlags";
```

#### Verfügbare Flags

```ts
const defaultFutureFlags = {
  removeCardWidth: false,   // mt-card: Breiten-Prop entfernen
  removeDefaultMargin: false, // Standard-Margins entfernen
};
```

#### Provider (Root-Ebene oder Layout-Komponente)

```ts
import { provideFutureFlags } from "@shopware-ag/meteor-component-library/composables/useFutureFlags";

// Im setup() einer übergeordneten Komponente
provideFutureFlags({
  removeCardWidth: true,
  removeDefaultMargin: true,
});
```

#### Consumer (in Komponentenimplementierungen)

```ts
import { useFutureFlags } from "@shopware-ag/meteor-component-library/composables/useFutureFlags";

const flags = useFutureFlags();

if (flags.removeCardWidth) {
  // neues Verhalten
} else {
  // altes Verhalten
}
```

---

### useSnackbar

**Datei**: `src/components/feedback-indicator/mt-snackbar/composables/use-snackbar.ts`

Programmatisches Anzeigen von Snackbar-Meldungen. Benötigt `MtSnackbar` im Layout.

```ts
import { useSnackbar } from "@shopware-ag/meteor-component-library";
```

```vue
<!-- Layout/Root-Komponente: MtSnackbar einbinden -->
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
<!-- In einer beliebigen Komponente -->
<script setup>
import { useSnackbar } from "@shopware-ag/meteor-component-library";

const snackbar = useSnackbar();

function save() {
  // ...speichern...
  snackbar.dispatch({
    // Snackbar-Konfiguration (entspricht mt-snackbar Props)
  });
}
</script>
```

---

## Plugins

### DeviceHelperPlugin

**Datei**: `src/plugin/device-helper.plugin.ts`

Registriert einen `$device`-Helper auf der Vue-Instanz für Responsive-Abfragen und Resize-Listener.

```ts
import { DeviceHelperPlugin } from "@shopware-ag/meteor-component-library";

app.use(DeviceHelperPlugin);
```

Nach der Installation ist `this.$device` (Options API) oder `inject('$device')` (Composition API) verfügbar. Der Plugin-Mixin räumt automatisch Resize-Listener beim `unmounted`-Lifecycle-Hook auf.

---

## Internes Composable: usePriorityPlusNavigation

**Datei**: `src/composables/_internal/usePriorityPlusNavigation.ts`

Internes Composable für die Priority-Plus-Navigation (Tabs, die bei zu wenig Platz in einem "More"-Dropdown verschwinden). Nicht für externe Verwendung vorgesehen.

---

## Komponentenspezifische Composables

Diese Composables sind spezifisch für einzelne Komponenten und nicht als eigenständige Utils vorgesehen:

| Composable | Komponente | Zweck |
|---|---|---|
| `useModalContext` | `mt-modal` | Context für Modal-Unterkomponenten |
| `useIsInsideTooltip` | `mt-tooltip` | Prüft ob im Tooltip-Context |
| `useTooltipState` | `mt-tooltip` | Tooltip-State-Management |
| `useScrollPossibilitiesClasses` | `mt-data-table` | Scroll-Indicator-Klassen für Tabellen |

---

## Vollständige Export-Liste

```ts
// Direktiven
export { TooltipDirective } from "@shopware-ag/meteor-component-library";

// Plugins
export { DeviceHelperPlugin } from "@shopware-ag/meteor-component-library";

// Composables
export { useSnackbar } from "@shopware-ag/meteor-component-library";

// Drag/Drop (separate Importe)
import { draggable, droppable } from "@shopware-ag/meteor-component-library/src/directives/dragdrop.directive";
```

---

## Abgrenzung: Admin-SDK Composables

Die folgenden Composables gehören zum Admin SDK (`@shopware-ag/meteor-admin-sdk`), nicht zur Component Library:

- `composables.useRepository` — Reaktives Repository-Composable für SDK-Extensions
- `composables.useSharedState` — Geteilter State über SDK-Locations hinweg (via IndexedDB)

Diese sind im Skill `sw-meteor-admin-sdk` dokumentiert.
