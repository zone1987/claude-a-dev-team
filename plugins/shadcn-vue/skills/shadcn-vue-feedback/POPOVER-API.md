# Popover — API-Referenz

## Popover (Root)

Basiert auf reka-ui `PopoverRoot`.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `open` | `boolean` | — | Kontrollierter Offenzustand |
| `defaultOpen` | `boolean` | `false` | Unkontrollierter Startzustand |
| `modal` | `boolean` | `false` | Modal-Modus (Fokus-Trap) |

### Emits

| Event | Typ | Beschreibung |
|---|---|---|
| `update:open` | `boolean` | Feuert beim Offnen/Schliessen |

### Slot Props

```ts
// v-slot="{ open }"
```

---

## PopoverTrigger

Basiert auf reka-ui `PopoverTrigger`. Kein eigenes Styling.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `asChild` | `boolean` | Rendert das Kind als Trigger |
| Alle `PopoverTriggerProps` | — | Weitergeleitet |

---

## PopoverContent

Basiert auf reka-ui `PopoverContent`, gerendert in `PopoverPortal`.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `align` | `"start" \| "center" \| "end"` | `"center"` | Horizontale Ausrichtung |
| `sideOffset` | `number` | `4` | Abstand zum Trigger (px) |
| `side` | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Bevorzugte Seite |
| `alignOffset` | `number` | — | Versatz entlang der Alignment-Achse |
| `avoidCollisions` | `boolean` | `true` | Flippt bei Viewport-Kollision |
| `collisionBoundary` | `Element \| null \| Array` | — | Kollisionsgrenzen |
| `collisionPadding` | `number \| Partial<Record<Side, number>>` | `0` | Padding bei Kollisionspruferung |
| `sticky` | `"partial" \| "always"` | `"partial"` | Klebrigkeit |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

### Animationen
Werden via `data-[state]` und `data-[side]` gesteuert:
- `data-[state=open]`: fade-in + zoom-in-95
- `data-[state=closed]`: fade-out + zoom-out-95
- `data-[side=*]`: slide-in-from-*

---

## PopoverAnchor

Entkoppelt Anker vom Trigger. Ermoglicht das Positionieren des Popovers relativ zu einem anderen Element.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| Alle `PopoverAnchorProps` | — | Weitergeleitet |

---

## reka-ui Referenz
- https://reka-ui.com/docs/components/popover
