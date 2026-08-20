# HoverCard — API

Reka-UI API-Referenz: https://reka-ui.com/docs/components/hover-card#api-reference

## Sub-Komponenten

| Komponente | Beschreibung |
|---|---|
| `HoverCard` | Root-Wrapper (HoverCardRoot) |
| `HoverCardTrigger` | Element, das beim Hovern die Karte oeffnet |
| `HoverCardContent` | Inhalt der Karte (w-64, p-4, rounded-md) |

## HoverCard (Root)

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `open` | `boolean` | - | Kontrollierter Zustand |
| `defaultOpen` | `boolean` | `false` | - |
| `openDelay` | `number` | `700` | Verzoegerung beim Oeffnen (ms) |
| `closeDelay` | `number` | `300` | Verzoegerung beim Schliessen (ms) |

| Emit | Payload | Beschreibung |
|---|---|---|
| `update:open` | `boolean` | Zustand geaendert |

## HoverCardContent

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `side` | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Anzeigeseite |
| `sideOffset` | `number` | `4` | Abstand zum Trigger |
| `align` | `"start" \| "center" \| "end"` | `"center"` | Ausrichtung |
| `alignOffset` | `number` | `0` | Offset zur Ausrichtung |
| `class` | `string` | - | - |

## Slots

Alle Komponenten nutzen Default-Slots. `HoverCard` stellt slotProps bereit (open-Zustand).
