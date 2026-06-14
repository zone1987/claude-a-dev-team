# Menubar — API-Referenz

## Menubar (Root)

Basiert auf reka-ui `MenubarRoot`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `MenubarRootProps` | — | Weitergeleitet |

### Emits

| Event | Typ | Beschreibung |
|---|---|---|
| Alle `MenubarRootEmits` | — | Weitergeleitet |

---

## MenubarMenu

Kein eigenes Styling. Wrapper fur `MenubarTrigger` + `MenubarContent`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| Alle `MenubarMenuProps` | — | Weitergeleitet (value etc.) |

---

## MenubarTrigger

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `MenubarTriggerProps` | — | Weitergeleitet |

---

## MenubarContent

Wird in `MenubarPortal` gerendert.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `align` | `"start" \| "center" \| "end"` | `"start"` | Ausrichtung |
| `alignOffset` | `number` | `-4` | Versatz entlang der Alignment-Achse |
| `sideOffset` | `number` | `8` | Abstand zum Trigger |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

---

## MenubarItem

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `inset` | `boolean` | `false` | Linker Einzug (pl-8) fur Ausrichtung mit Icons |
| `variant` | `"default" \| "destructive"` | `"default"` | Farbvariante |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

### Emits

| Event | Beschreibung |
|---|---|
| `select` | Wird bei Klick/Enter ausgelost |

---

## MenubarLabel

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `inset` | `boolean` | Linker Einzug (pl-8) |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## MenubarCheckboxItem

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `checked` | `boolean` | Ausgewahlt-Zustand |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

### Slots

| Slot | Beschreibung |
|---|---|
| default | Item-Inhalt |
| `indicator-icon` | Benutzerdefiniertes Check-Icon (Standard: `<Check>`) |

---

## MenubarRadioGroup

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `modelValue` | `string` | Aktuell ausgewahlter Wert |

### Emits

| Event | Typ | Beschreibung |
|---|---|---|
| `update:modelValue` | `string` | Wert andert sich |

---

## MenubarRadioItem

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `value` | `string` | Wert dieses Radio-Items |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

### Slots

| Slot | Beschreibung |
|---|---|
| default | Item-Inhalt |
| `indicator-icon` | Benutzerdefiniertes Radio-Icon (Standard: `<Circle>`) |

---

## MenubarSub / MenubarSubTrigger / MenubarSubContent

| Prop | Typ | Beschreibung |
|---|---|---|
| `inset` (SubTrigger) | `boolean` | Linker Einzug |
| `open` / `defaultOpen` (Sub) | `boolean` | Kontrolliert/unkontrolliert |

---

## MenubarSeparator

Horizontale Trennlinie.

---

## MenubarShortcut

Rein prasentierende `<span>`-Komponente fur Tastaturkurzel.

## reka-ui Referenz
- https://reka-ui.com/docs/components/menubar
