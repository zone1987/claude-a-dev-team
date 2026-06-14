---
name: shadcn-vue-alert-dialog
description: >
  shadcn-vue AlertDialog component (Vue-Port von shadcn/ui, reka-ui, Tailwind v4, SFC .vue).
  Triggers: "shadcn-vue alert-dialog", "alert dialog vue", "bestätigungsdialog vue",
  "confirmation dialog vue", "modal confirm vue", "destructive action dialog vue",
  "delete confirmation dialog vue", "dialog bestätigung vue", "alert dialog reka-ui"
---

# shadcn-vue: AlertDialog

A modal dialog that interrupts the user with important content and expects a response.
Used for destructive or irreversible actions (delete, overwrite) that require explicit confirmation before proceeding.
Built on top of reka-ui AlertDialogRoot with a full overlay, animated entry/exit, and keyboard focus trap.

## Sub-Components

- `AlertDialog` — Root container (wraps reka-ui `AlertDialogRoot`, forwards all props/emits)
- `AlertDialogTrigger` — Button or element that opens the dialog
- `AlertDialogContent` — Modal panel rendered in a portal over an overlay; animated zoom + fade
- `AlertDialogHeader` — Layout wrapper for title and description (flex column, text-center on mobile / text-left on sm+)
- `AlertDialogTitle` — Heading of the dialog (`text-lg font-semibold`)
- `AlertDialogDescription` — Explanatory text below the title (`text-muted-foreground text-sm`)
- `AlertDialogFooter` — Layout wrapper for action buttons (stacked on mobile, row on sm+)
- `AlertDialogAction` — Primary confirmation button (styled via `buttonVariants()`)
- `AlertDialogCancel` — Secondary dismiss button (styled via `buttonVariants({ variant: "outline" })`)

## Key Features

- **Portal + Overlay**: Content renders in a portal; a semi-transparent `bg-black/80` overlay covers the page
- **Animations**: Entry/exit via Tailwind `data-[state=open/closed]` — fade + zoom (`zoom-in-95` / `zoom-out-95`)
- **Keyboard Focus Trap**: Focus is trapped inside the dialog while open; `Escape` key closes it
- **Inherits Button Styles**: `AlertDialogAction` and `AlertDialogCancel` reuse `buttonVariants` from the Button component — no extra styling needed
- **Responsive Layout**: Footer stacks vertically on mobile, renders as a row on `sm:` breakpoint
- **Fully Accessible**: WAI-ARIA `alertdialog` role, labeled by title and described by description

## Reference Files

- `references/installation.md` — CLI and manual installation steps
- `references/source.md` — Complete Vue source code for all 9 component files + index.ts
- `references/api.md` — Props, emits, slots per component; notes on buttonVariants usage
- `references/examples.md` — Core examples: basic, small, destructive, nested in Dialog
