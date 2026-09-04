---
name: reui-add
description: Finds a ReUI component, example or block for what you describe, states its licence tier, installs it, and wires it to real data.
argument-hint: <what you want>
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
model: sonnet
---

Find and install the right ReUI item for: `$ARGUMENTS`

## Steps

1. **Find.** Ask the ReUI MCP `search` with the intent plus any hints you can infer (`type`,
   `component`, `category`, `features`, `free`). If the MCP cannot answer, use
   `npx shadcn@latest search @reui -q "..."`, and the registry references under
   `skills/reui-registry/references/` and `skills/reui-blocks/references/`.
2. **State the tier before installing.** Free (`c-*` example or primitive), Pro (block) or Ultimate
   (icon, template). For anything premium, verify `REUI_LICENSE_KEY` *and* the authenticated `@reui`
   entry in `components.json` are both present — otherwise the install 401s. Offer a free
   alternative when they are not.
3. **Show the preview.** Include each candidate's `previewUrl` when the MCP returned one, so the
   choice is made on sight. Present the top options when several score closely.
4. **Install** non-interactively: `npx shadcn@latest add @reui/<name> --yes`.
5. **Read the real API.** `get_component` batched over everything the item uses, or the component's
   reference file under `skills/reui-data|reui-forms|reui-layout/references/`. Then read the files
   the install actually added — they are the ground truth.
6. **Adapt by reuse.** Keep the composition, swap demo data for real data, fix icon imports, keep
   styling on semantic tokens. Do not redesign.
7. **Finish**: typecheck and lint, and run the MCP `get_audit_checklist` when it is reachable.

## Report

The item installed with its tier, the files added, what you wired to real data, and the
typecheck/lint result — stated plainly, including failures.
