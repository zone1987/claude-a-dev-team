---
name: shadcn-vue-label
description: >
  shadcn-vue Label component (Vue-Port von shadcn/ui, reka-ui Label, Tailwind v4).
  Triggers: "shadcn-vue label", "label vue", "form label vue", "beschriftung vue",
  "label component shadcn", "label reka-ui vue", "html-for label vue", "accessible label vue"
---

# shadcn-vue Label Component

## Triggers
shadcn-vue label, label vue, form label vue, beschriftung vue, label component shadcn,
label reka-ui vue, html-for label vue, accessible label vue

## Overview

The `Label` component wraps reka-ui's `Label` primitive to provide an accessible form label. It automatically handles `for`/`htmlFor` association, disabled-state opacity via `group-data-[disabled]` and `peer-disabled`, and SVG icon sizing.

## Sub-components

| Component | Base | Description |
|---|---|---|
| `Label` | `reka-ui Label` | Accessible form field label |

## Props

| Prop | Type | Description |
|---|---|---|
| `htmlFor` | `string` | ID of the associated form control |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `LabelProps` from reka-ui | — | Fully forwarded via `reactiveOmit` |

## Disabled State
Automatically applies `pointer-events-none opacity-50` when the parent has `data-disabled=true` (group pattern) or the associated input has `disabled`.

## References
- Source: `references/source.md`
- API: `references/api.md`
- Examples: `references/examples.md`
- Installation: `references/installation.md`
