# Drawer — API

## Sub-Komponenten

| Komponente | Beschreibung |
|---|---|
| `Drawer` | Root-Wrapper (DrawerRoot von vaul-vue), `shouldScaleBackground: true` als Standard |
| `DrawerTrigger` | Oeffnet den Drawer |
| `DrawerPortal` | Portiert Content (intern) |
| `DrawerOverlay` | Halbtransparentes Overlay |
| `DrawerContent` | Container des Drawers, Richtung via `data-[vaul-drawer-direction=*]` gesteuert |
| `DrawerHeader` | Bereich fuer Title/Description, `p-4` padding |
| `DrawerFooter` | Bereich fuer Buttons, `mt-auto p-4` |
| `DrawerTitle` | Semantischer Titel |
| `DrawerDescription` | Semantische Beschreibung |
| `DrawerClose` | Schliesst den Drawer |

## Drawer (Root)

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `open` | `boolean` | - | Kontrollierter Zustand |
| `defaultOpen` | `boolean` | `false` | Unkontrollierter Startwert |
| `direction` | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Slide-Richtung |
| `shouldScaleBackground` | `boolean` | `true` | Hintergrund skalieren |
| `modal` | `boolean` | `true` | Modal-Modus |

| Emit | Payload | Beschreibung |
|---|---|---|
| `update:open` | `boolean` | Zustand geaendert |

## DrawerContent

Nimmt `DialogContentProps` von reka-ui entgegen (intern). Die Richtung wird automatisch via `data-[vaul-drawer-direction=*]` CSS-Attribut gesteuert:

- `bottom` (Standard): `inset-x-0 bottom-0 mt-24 max-h-[80vh] rounded-t-lg` + Drag-Handle oben
- `top`: `inset-x-0 top-0 mb-24 max-h-[80vh] rounded-b-lg`
- `right`: `inset-y-0 right-0 w-3/4 sm:max-w-sm`
- `left`: `inset-y-0 left-0 w-3/4 sm:max-w-sm`

| Prop | Typ | Standard |
|---|---|---|
| `class` | `string` | - |

## Alle einfachen Wrapper

`DrawerHeader`, `DrawerFooter`, `DrawerTitle`, `DrawerDescription`, `DrawerOverlay` akzeptieren jeweils:

| Prop | Typ |
|---|---|
| `class` | `string` |
