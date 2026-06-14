# Kbd — API-Referenz

## Kbd

Rendert als natives `<kbd>` HTML-Element. Kein reka-ui-Primitiv.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

### Slots

| Slot | Beschreibung |
|---|---|
| default | Text oder SVG-Icon der Taste |

### Styling
- Hintergrund: `bg-muted`
- Text: `text-muted-foreground`
- Grosse: `h-5 min-w-5 text-xs`
- Innerhalb `[data-slot=tooltip-content]`: transparenter Hintergrund (automatisch)

---

## KbdGroup

Rendert ebenfalls als `<kbd>`, gruppiert mehrere `Kbd`-Elemente mit `gap-1`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

### Slots

| Slot | Beschreibung |
|---|---|
| default | Mehrere `<Kbd>`-Komponenten |

---

## Hinweis
`Kbd` und `KbdGroup` haben keine reka-ui-Basis — sie sind reine Tailwind-CSS-Wrapper.
