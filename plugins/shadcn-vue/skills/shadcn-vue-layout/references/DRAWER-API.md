# Drawer — API

## Sub-components

| Component | Description |
|---|---|
| `Drawer` | Root wrapper (DrawerRoot from vaul-vue), `shouldScaleBackground: true` by default |
| `DrawerTrigger` | Opens the drawer |
| `DrawerPortal` | Portals the content (internal) |
| `DrawerOverlay` | Semi-transparent overlay |
| `DrawerContent` | Container of the drawer, direction controlled via `data-[vaul-drawer-direction=*]` |
| `DrawerHeader` | Area for title/description, `p-4` padding |
| `DrawerFooter` | Area for buttons, `mt-auto p-4` |
| `DrawerTitle` | Semantic title |
| `DrawerDescription` | Semantic description |
| `DrawerClose` | Closes the drawer |

## Drawer (Root)

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | `boolean` | - | Controlled state |
| `defaultOpen` | `boolean` | `false` | Uncontrolled initial value |
| `direction` | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Slide direction |
| `shouldScaleBackground` | `boolean` | `true` | Scale the background |
| `modal` | `boolean` | `true` | Modal mode |

| Emit | Payload | Description |
|---|---|---|
| `update:open` | `boolean` | State changed |

## DrawerContent

Accepts `DialogContentProps` from reka-ui (internal). The direction is controlled automatically via the `data-[vaul-drawer-direction=*]` CSS attribute:

- `bottom` (default): `inset-x-0 bottom-0 mt-24 max-h-[80vh] rounded-t-lg` + drag handle on top
- `top`: `inset-x-0 top-0 mb-24 max-h-[80vh] rounded-b-lg`
- `right`: `inset-y-0 right-0 w-3/4 sm:max-w-sm`
- `left`: `inset-y-0 left-0 w-3/4 sm:max-w-sm`

| Prop | Type | Default |
|---|---|---|
| `class` | `string` | - |

## All simple wrappers

`DrawerHeader`, `DrawerFooter`, `DrawerTitle`, `DrawerDescription`, `DrawerOverlay` each accept:

| Prop | Type |
|---|---|
| `class` | `string` |
