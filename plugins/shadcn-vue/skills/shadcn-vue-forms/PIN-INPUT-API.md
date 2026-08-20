# PinInput — API-Referenz

## PinInput (Root)

Basiert auf reka-ui `PinInputRoot`. Generischer Typ `Type extends 'text' | 'number' = 'text'`.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `modelValue` | `string[]` | — | Kontrollierter Wert (Array pro Slot) |
| `defaultValue` | `string[]` | — | Unkontrollierter Startwert |
| `otp` | `boolean` | `true` | OTP-Autocomplete aktivieren |
| `mask` | `boolean` | `false` | Eingabe maskieren (Passwort-Modus) |
| `type` | `"text" \| "number"` | `"text"` | Input-Typ |
| `placeholder` | `string` | — | Platzhalter fur alle Slots |
| `disabled` | `boolean` | `false` | Alle Slots deaktivieren |
| `id` | `string` | — | Fur `<Label>`-Verknupfung |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

### Emits

| Event | Typ | Beschreibung |
|---|---|---|
| `update:modelValue` | `string[]` | Bei Anderung eines Slots |
| `complete` | `string[]` | Wenn alle Slots ausgefullt sind |

---

## PinInputGroup

Basiert auf reka-ui `Primitive`.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `as` | `string \| Component` | `"div"` | HTML-Element |
| `asChild` | `boolean` | `false` | Rendert als Kind-Element |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

---

## PinInputSlot

Basiert auf reka-ui `PinInputInput`. Jeder Slot ist ein eigenstandiges Input-Element.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `index` | `number` | **Erforderlich**: 0-basierte Position im PIN |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `PinInputInputProps` | — | Weitergeleitet |

### Styling-Besonderheiten
- `first:rounded-l-md first:border-l` — nur erster Slot hat linken Rand und Abrundung
- `last:rounded-r-md` — nur letzter Slot hat rechte Abrundung
- `focus:z-10` — aktiver Slot liegt uber Nachbarn

---

## PinInputSeparator

Basiert auf reka-ui `Primitive`. Standard-Icon: `<Minus>`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `as` | `string \| Component` | HTML-Element (Standard: `"div"`) |
| `asChild` | `boolean` | Kind-Element-Modus |

### Slots

| Slot | Beschreibung |
|---|---|
| default | Benutzerdefiniertes Trennzeichen (Standard: `<Minus>`) |

---

## reka-ui Referenz
- https://reka-ui.com/docs/components/pin-input
