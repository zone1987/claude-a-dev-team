# InputGroup — API

## Sub-Komponenten

| Komponente | Beschreibung |
|---|---|
| `InputGroup` | Root-Container, steuert Focus- und Error-State via has-[...] |
| `InputGroupAddon` | Addon-Bereich (Icon, Text, Button), automatisch fokussiert Input bei Klick |
| `InputGroupInput` | Input-Ersatz mit `data-slot="input-group-control"` |
| `InputGroupTextarea` | Textarea-Ersatz mit `data-slot="input-group-control"` |
| `InputGroupButton` | Button innerhalb eines Addons (ghost, xs als Standard) |
| `InputGroupText` | Text-Span fuer statische Labels im Addon |

## InputGroupAddon

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `align` | `"inline-start" \| "inline-end" \| "block-start" \| "block-end"` | `"inline-start"` | Position des Addons |
| `class` | `string` | - | - |

### Ausrichtungen

| Wert | Verwendung | Platzierung |
|---|---|---|
| `inline-start` | Fuer `InputGroupInput` | Links/vorne, `order-first` |
| `inline-end` | Fuer `InputGroupInput` | Rechts/hinten, `order-last` |
| `block-start` | Fuer `InputGroupTextarea` | Oben, `order-first`, `w-full` |
| `block-end` | Fuer `InputGroupTextarea` | Unten, `order-last`, `w-full` |

Wichtig: Addon NACH dem Input in der DOM-Reihenfolge platzieren (CSS `order` regelt die visuelle Reihenfolge). So bleibt die Tab-Reihenfolge korrekt.

## InputGroupButton

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `size` | `"xs" \| "icon-xs" \| "sm" \| "icon-sm"` | `"xs"` | Button-Groesse |
| `variant` | `ButtonVariants["variant"]` | `"ghost"` | Button-Variante |
| `class` | `string` | - | - |

## Custom Input

Eigene Input-Elemente koennen mit `data-slot="input-group-control"` versehen werden, um Focus-State-Handling zu erhalten:

```vue
<InputGroup>
  <textarea
    data-slot="input-group-control"
    class="flex field-sizing-content min-h-16 w-full resize-none rounded-md bg-transparent px-3 py-2.5 text-base outline-none md:text-sm"
    placeholder="Autoresize textarea..."
  />
  <InputGroupAddon align="block-end">
    <InputGroupButton class="ml-auto" size="sm" variant="default">Submit</InputGroupButton>
  </InputGroupAddon>
</InputGroup>
```
