# NumberField — API-Referenz

## Contents

- [NumberField (Root)](#numberfield-root)
- [NumberFieldContent](#numberfieldcontent)
- [NumberFieldInput](#numberfieldinput)
- [NumberFieldDecrement](#numberfielddecrement)
- [NumberFieldIncrement](#numberfieldincrement)
- [reka-ui Referenz](#reka-ui-referenz)

## NumberField (Root)

Basiert auf reka-ui `NumberFieldRoot`. Verwaltet Wert, Min/Max, Step und Disabled-State.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `modelValue` | `number` | — | Kontrollierter Wert |
| `defaultValue` | `number` | — | Unkontrollierter Startwert |
| `min` | `number` | — | Minimaler Wert |
| `max` | `number` | — | Maximaler Wert |
| `step` | `number` | `1` | Schrittweite |
| `disabled` | `boolean` | `false` | Deaktiviert das gesamte Feld |
| `id` | `string` | — | Fur `<Label>`-Verknupfung |
| `locale` | `string` | — | Lokale fur Zahlenformatierung |
| `formatOptions` | `Intl.NumberFormatOptions` | — | Zahlenformatierung |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

### Emits

| Event | Typ | Beschreibung |
|---|---|---|
| `update:modelValue` | `number` | Feuert bei Wertanderung |

### Slot Props

```ts
// v-slot="{ modelValue, ... }"
```

---

## NumberFieldContent

Positionierungs-Wrapper fur Input + Buttons.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

### Verhalten
Passt automatisch das Padding des Inputs an, wenn Decrement/Increment vorhanden ist (`has-[[data-slot=increment]]`, `has-[[data-slot=decrement]]`).

---

## NumberFieldInput

Basiert auf reka-ui `NumberFieldInput`. Kein eigenes `v-model` — Zustand wird von `NumberFieldRoot` verwaltet.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## NumberFieldDecrement

Minus-Button (absolut links positioniert).

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `NumberFieldDecrementProps` | — | Weitergeleitet |

### Slots

| Slot | Beschreibung |
|---|---|
| default | Benutzerdefiniertes Icon (Standard: `<Minus>`) |

---

## NumberFieldIncrement

Plus-Button (absolut rechts positioniert).

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `NumberFieldIncrementProps` | — | Weitergeleitet |

### Slots

| Slot | Beschreibung |
|---|---|
| default | Benutzerdefiniertes Icon (Standard: `<Plus>`) |

---

## reka-ui Referenz
- https://reka-ui.com/docs/components/number-field
