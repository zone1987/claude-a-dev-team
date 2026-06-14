# Input — API

## Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `modelValue` | `string \| number` | - | v-model Binding |
| `defaultValue` | `string \| number` | - | Unkontrollierter Startwert |
| `class` | `string` | - | Zusaetzliche CSS-Klassen |
| Alle nativen `<input>`-Attribute | - | - | z.B. `type`, `placeholder`, `disabled`, `required`, `aria-invalid` |

## Emits

| Event | Payload | Beschreibung |
|---|---|---|
| `update:modelValue` | `string \| number` | Bei Eingabe |

## Wichtige native Attribute

| Attribut | Beschreibung |
|---|---|
| `type` | `text`, `email`, `password`, `number`, `tel`, `url`, `search`, `date`, `time`, `file` etc. |
| `disabled` | Deaktiviert das Feld (opacity-50, cursor-not-allowed) |
| `aria-invalid` | Aktiviert Fehler-Styling (roten Border + Ring) |
| `placeholder` | Platzhaltertext |

## CSS-Klassen (Zustände)

- **Focus**: `focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-3`
- **Error**: `aria-invalid:ring-destructive/20 aria-invalid:border-destructive`
- **Disabled**: `disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50`
