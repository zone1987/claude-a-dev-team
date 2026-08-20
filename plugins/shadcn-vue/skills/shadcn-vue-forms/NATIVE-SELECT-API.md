# NativeSelect — API-Referenz

## NativeSelect

Rendert einen nativen `<select>` mit einem chevron-Icon-Wrapper.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `modelValue` | `AcceptableValue \| AcceptableValue[]` | `""` | v-model Wert |
| `class` | `HTMLAttributes["class"]` | — | Wird auf `<select>` angewendet |
| Alle nativen `<select>` attrs | — | Via `$attrs` weitergeleitet |

### Emits

| Event | Typ | Beschreibung |
|---|---|---|
| `update:modelValue` | `AcceptableValue` | Feuert bei Anderung |

### Slots

| Slot | Beschreibung |
|---|---|
| default | `NativeSelectOption` und `NativeSelectOptGroup` |

### Besonderheiten
- `inheritAttrs: false` — Attrs werden manuell auf `<select>` weitergeleitet
- `useVModel` mit `passive: true` und `defaultValue: ""`
- Wrapper-Div: `has-[select:disabled]:opacity-50`
- Chevron-Icon ist `pointer-events-none` und `aria-hidden`

---

## NativeSelectOptGroup

Renders `<optgroup>`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `label` | `string` | Gruppen-Label (natives HTML-Attr) |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## NativeSelectOption

Rendert `<option>`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `value` | `string` | Option-Wert |
| `disabled` | `boolean` | Deaktiviert |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## Hinweis
`NativeSelect` hat keine reka-ui-Basis und verwendet keine Custom-Dropdown-Logik. Das Dropdown-Verhalten kommt vollstandig vom Browser.
