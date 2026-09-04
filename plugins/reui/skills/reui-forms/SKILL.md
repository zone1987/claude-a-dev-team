---
name: reui-forms
description: Full APIs of the ReUI form primitives: autocomplete, number-field, phone-input, rating, file-upload, stepper. Use when building with @reui/autocomplete or @reui/stepper.
---

# ReUI form primitives

Input components beyond what shadcn/ui ships. All **free** — no licence key — installed with
`npx shadcn@latest add @reui/<name> --yes`.

## What is here, and what is not

ReUI adds an API for **six** form primitives, and this skill carries all six. Three further
selection primitives live in [reui-data](../reui-data/SKILL.md) because they edit data rather than
a single field: `cascader`, `date-selector` and `filters`.

Everything else in a form is **plain shadcn/ui** — ReUI ships examples for it but no API of its own:

| Control | Where its API lives | ReUI examples |
|---|---|---|
| `input`, `input-group`, `input-otp`, `textarea` | the `shadcn` plugin | 83 |
| `select`, `native-select`, `combobox` | the `shadcn` plugin | 67 |
| `checkbox`, `radio-group`, `switch`, `toggle`, `toggle-group` | the `shadcn` plugin | 83 |
| `calendar` | the `shadcn` plugin | 30 |
| `label`, `field`, `slider` | the `shadcn` plugin | 36 |

So a form is normally **both**: shadcn/ui for the ordinary controls and their validation
conventions, this skill for what shadcn does not solve. Reach for the `shadcn` plugin's
`shadcn-forms` skill for the generic half — do not look for an `@reui/input` that does not exist,
and do not hand-roll a control shadcn already ships.

The ReUI examples for those generic controls are still worth installing: they are free `c-*` items,
listed by family in
[reui-registry/EXAMPLES-FREE.md](../reui-registry/references/EXAMPLES-FREE.md).

## Read your build first

`components.json` → `style`: `base-nova` → Base UI, `radix-nova` → Radix UI. Write against that
build's API; the CLI installs the right variant, and you never pass a style. Each reference file
records the real difference in its **Base UI vs Radix UI** section.

## Where the API comes from

The MCP's batched `get_component` when it answers, these files when it cannot, and the installed
files as the final word. Never write a prop you have not read in one of the three.

## Reference map

- **[AUTOCOMPLETE.md](references/AUTOCOMPLETE.md)**: input that suggests options as you type.
- **[STEPPER.md](references/STEPPER.md)**: multi-step flows — the step state, navigation and
  validation contract.
- **[FILE-UPLOAD.md](references/FILE-UPLOAD.md)**: drag-and-drop and multi-file uploads with
  progress. Documented upstream as a pattern rather than a primitive.
- **[NUMBER-FIELD.md](references/NUMBER-FIELD.md)**: numeric input with increment, decrement and a
  scrub area.
- **[PHONE-INPUT.md](references/PHONE-INPUT.md)**: country selection and E.164 validation; also
  accepts every prop from `react-phone-number-input`.
- **[RATING.md](references/RATING.md)**: star rating, read-only and interactive.

## Source

Distilled from `https://reui.io/docs/components/base/<name>` and its `radix` twin, mirrored
2026-09-04.
