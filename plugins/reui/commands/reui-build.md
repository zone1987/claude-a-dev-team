---
name: reui-build
description: Composes a full ReUI page or section — plans the sections, picks a block per section, installs, and adapts each one.
argument-hint: <page or feature to build>
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
model: sonnet
---

Build with ReUI: `$ARGUMENTS`

## Steps

1. **Plan the page first.** Ask the ReUI MCP `compose_page` with the intent before searching block by
   block — it returns ordered sections, each matched to the best block, and names the sections with
   no real inventory in `unavailableSections`. Compose those from primitives instead of forcing a
   bad block. Without the MCP, plan from `skills/reui-blocks/references/`.
2. **Check the licence up front.** Premium blocks need Pro; icons and templates need Ultimate, plus
   `REUI_LICENSE_KEY` and the authenticated `@reui` entry. If they are absent, say so before
   installing anything and offer the free composition — primitives plus `c-*` examples — instead of
   producing a page that cannot install.
3. **Show the previews** for the planned sections, then confirm the plan with the user before
   installing a long list.
4. **Install** each chosen item with `npx shadcn@latest add @reui/<name> --yes`.
5. **Read the APIs** for everything used — batched `get_component`, or the component references
   under `skills/reui-data|reui-forms|reui-layout/references/` — and read the installed files.
6. **Adapt each section**: real data, correct icon imports, semantic tokens, the empty, loading and
   error states, responsive from mobile up.
7. **Audit**: `get_audit_checklist` when reachable, then typecheck and lint.

## Report

The section plan, the block chosen per section with its tier, anything that had to be composed from
primitives instead, and the verification result — green or red with the real output.
