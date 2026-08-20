# AlertDialog — API Reference

reka-ui API: https://reka-ui.com/docs/components/alert-dialog#api-reference

## Contents

- [Anatomy](#anatomy)
- [AlertDialog (Root)](#alertdialog-root)
- [AlertDialogTrigger](#alertdialogtrigger)
- [AlertDialogContent](#alertdialogcontent)
- [AlertDialogHeader](#alertdialogheader)
- [AlertDialogFooter](#alertdialogfooter)
- [AlertDialogTitle](#alertdialogtitle)
- [AlertDialogDescription](#alertdialogdescription)
- [AlertDialogAction](#alertdialogaction)
- [AlertDialogCancel](#alertdialogcancel)

## Anatomy

```vue
<AlertDialog>
  <AlertDialogTrigger>Open</AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you sure?</AlertDialogTitle>
      <AlertDialogDescription>This action cannot be undone.</AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction>Continue</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

---

## AlertDialog (Root)

Forwards all props and emits to reka-ui `AlertDialogRoot`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `defaultOpen` | `boolean` | `false` | Open state on initial render (uncontrolled) |
| `open` / `v-model:open` | `boolean` | — | Controlled open state |

**Emits:** `update:open`

**Slots:** default (receives reka-ui slot props)

---

## AlertDialogTrigger

Renders the element that opens the dialog. Forwards all `AlertDialogTriggerProps` to reka-ui.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `asChild` | `boolean` | `false` | Merge trigger behavior onto the first child element instead of rendering its own element |

**Slots:** default

---

## AlertDialogContent

Modal panel rendered in a portal. Includes overlay automatically. `inheritAttrs: false` — extra attrs are spread onto the reka-ui element alongside forwarded props.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes merged onto the content panel |
| `forceMount` | `boolean` | — | Keep content mounted even when closed (useful for animations) |

**Emits:** `openAutoFocus`, `closeAutoFocus`, `escapeKeyDown`, `interactOutside` (all from reka-ui `AlertDialogContentEmits`)

**Slots:** default

**Built-in styles:**
- Centered via `fixed top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%]`
- `max-w-[calc(100%-2rem)]` on mobile, `sm:max-w-lg` on larger screens
- Entry: `animate-in fade-in-0 zoom-in-95` / Exit: `animate-out fade-out-0 zoom-out-95`
- `duration-200`

---

## AlertDialogHeader

Pure layout div. No reka-ui primitive.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

**Built-in styles:** `flex flex-col gap-2 text-center sm:text-left`

**Slots:** default

---

## AlertDialogFooter

Pure layout div. No reka-ui primitive.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

**Built-in styles:** `flex flex-col-reverse gap-2 sm:flex-row sm:justify-end`

Note: `flex-col-reverse` places Cancel visually below Action on mobile, but DOM order is Cancel first (so Tab order puts Cancel before Action).

**Slots:** default

---

## AlertDialogTitle

Rendered via reka-ui `AlertDialogTitle` (sets `aria-labelledby` on the content).

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |
| `asChild` | `boolean` | `false` | Render as child element |

**Built-in styles:** `text-lg font-semibold`

**Slots:** default

---

## AlertDialogDescription

Rendered via reka-ui `AlertDialogDescription` (sets `aria-describedby` on the content).

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |
| `asChild` | `boolean` | `false` | Render as child element |

**Built-in styles:** `text-muted-foreground text-sm`

**Slots:** default

---

## AlertDialogAction

Confirmation button rendered via reka-ui `AlertDialogAction`. Closes the dialog when clicked.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes merged with `buttonVariants()` |
| `asChild` | `boolean` | `false` | Render as child element |

**Button styling:** `buttonVariants()` — default variant (solid primary). Pass a custom `class` to override, e.g. `class="bg-destructive text-white hover:bg-destructive/90"` for a destructive action.

**Slots:** default

---

## AlertDialogCancel

Dismiss button rendered via reka-ui `AlertDialogCancel`. Closes the dialog without confirming.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes merged with `buttonVariants({ variant: "outline" })` |
| `asChild` | `boolean` | `false` | Render as child element |

**Button styling:** `buttonVariants({ variant: "outline" })` plus `mt-2 sm:mt-0` for correct footer spacing. The `mt-2 sm:mt-0` handles stacked mobile layout (Cancel renders below Action visually).

**Slots:** default
