---
name: reui-forms
description: Full APIs of the ReUI form primitives: autocomplete, number-field, phone-input, rating, file-upload, stepper. Use when building with @reui/autocomplete or @reui/stepper.
---

# ReUI form primitives

Input components beyond what shadcn/ui ships. All **free** — no licence key — installed with
`npx shadcn@latest add @reui/<name> --yes`.

For a generic control shadcn/ui already has — Input, Select, Checkbox, Label, Field — use plain
shadcn/ui and its form conventions. Reach here only for what it does not solve.

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
