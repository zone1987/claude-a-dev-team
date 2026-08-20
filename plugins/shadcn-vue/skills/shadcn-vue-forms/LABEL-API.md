# Label — API-Referenz

## Label

Basiert auf reka-ui `Label`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `htmlFor` | `string` | ID des verknupften Form-Elements |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `LabelProps` von reka-ui | — | Vollstandig weitergeleitet via `reactiveOmit` |

### Slots

| Slot | Beschreibung |
|---|---|
| default | Label-Text oder kombinierter Inhalt (Text + Icon) |

### Automatische Disabled-Styles

| Selector | Effekt |
|---|---|
| `group-data-[disabled=true]` | `pointer-events-none opacity-50` |
| `peer-disabled` | `cursor-not-allowed opacity-50` |

### data-slot
`data-slot="label"` wird automatisch gesetzt.

## reka-ui Referenz
- https://reka-ui.com/docs/utilities/label
