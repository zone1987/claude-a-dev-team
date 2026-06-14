# Dialog — API

Reka-UI API-Referenz: https://reka-ui.com/docs/components/dialog#api-reference

## Sub-Komponenten

| Komponente | Beschreibung |
|---|---|
| `Dialog` | Root-Wrapper (DialogRoot von reka-ui) |
| `DialogTrigger` | Button/Element, das den Dialog oeffnet |
| `DialogPortal` | Portiert Content in `<body>` (intern verwendet) |
| `DialogOverlay` | Halbtransparentes Overlay hinter dem Dialog |
| `DialogContent` | Der eigentliche Dialog-Container mit Close-Button |
| `DialogScrollContent` | Scrollbarer Dialog-Container (Overlay scrollt) |
| `DialogHeader` | Bereich fuer Title und Description |
| `DialogFooter` | Bereich fuer Aktions-Buttons |
| `DialogTitle` | Semantischer Titel (aria-labelledby) |
| `DialogDescription` | Semantische Beschreibung (aria-describedby) |
| `DialogClose` | Button zum Schliessen des Dialogs |

## Dialog (Root)

Leitet alle Props/Emits an `DialogRoot` weiter.

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `open` | `boolean` | - | Kontrollierter Open-Zustand |
| `defaultOpen` | `boolean` | `false` | Unkontrollierter Startwert |
| `modal` | `boolean` | `true` | Ob Dialog modal ist |

| Emit | Payload | Beschreibung |
|---|---|---|
| `update:open` | `boolean` | Open-Zustand geaendert |

## DialogContent

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `class` | `string` | - | Zusaetzliche CSS-Klassen |
| `showCloseButton` | `boolean` | `true` | X-Button oben rechts anzeigen |
| Alle `DialogContentProps` | - | - | Werden an reka-ui weitergeleitet |

| Emit | Beschreibung |
|---|---|
| `closeAutoFocus` | Fokus nach Schliessen |
| `escapeKeyDown` | Escape-Taste gedrueckt |
| `interactOutside` | Klick ausserhalb |
| `openAutoFocus` | Fokus beim Oeffnen |
| `pointerDownOutside` | Pointer-Event ausserhalb |

## DialogFooter

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `class` | `string` | - | Zusaetzliche CSS-Klassen |
| `showCloseButton` | `boolean` | `false` | Automatischer Close-Button |

## DialogLegend / Label (Header/Footer/Title/Description)

Alle einfachen Wrapper-Komponenten akzeptieren:

| Prop | Typ | Standard |
|---|---|---|
| `class` | `string` | - |

## DialogOverlay

Erbt alle `DialogOverlayProps` von reka-ui plus `class`.

## Slots

Alle Komponenten verwenden Standard-Default-Slots (`<slot />`). `Dialog` und `DialogRoot` stellen zusaetzlich `slotProps` bereit (open-Zustand etc.).
