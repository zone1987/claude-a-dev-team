---
name: reui-dev
description: Routes a ReUI task to the right reui-* skill: registry tiers, setup, MCP, theming, or a component API. Use when a request names ReUI or @reui and spans more than one of those.
---

# ReUI — where to start

The entry point for ReUI work. This is a **router**: it decides which `reui-*` skill answers the
question, then you read that skill rather than answering from memory.

ReUI ships 1,719 registry items across three licence tiers, and every component has an exact prop
API in two builds. A recalled prop name is a bug with a plausible spelling; a recalled licence tier
is an install that 401s halfway through. Read the source.

## Two facts that decide most tasks

**The tier, before proposing any install.** `@reui/c-*` examples and the bare primitives are free;
every other block name is Pro; `@reui/icons/...` and templates are Ultimate. A premium install needs
`REUI_LICENSE_KEY` **and** the authenticated `@reui` entry in `components.json` — one without the
other fails with a 401 only after resolving dependencies.

**The build, before writing component code.** `components.json` → `style`: `base-nova` is Base UI,
`radix-nova` is Radix UI. The two differ in imports and in some props. The CLI installs the right
variant; never pass a style yourself.

## Routing

| The task involves | Call the Skill tool with |
|---|---|
| Which items are free, which need a licence, an item's name or tier | `reui-registry` |
| Installing ReUI, `components.json`, `REUI_LICENSE_KEY`, RTL, prerequisites | `reui-setup` |
| The MCP server, sign-in, `reui_pat_` tokens, a failing `mcp__reui__*` call, CI | `reui-mcp` |
| Theme tokens, or a block rendering with the wrong success or warning colour | `reui-theming` |
| data-grid, filters, cascader, gantt, event-calendar, tree, date-selector, code-block | `reui-data` |
| autocomplete, number-field, phone-input, rating, file-upload, stepper | `reui-forms` |
| kanban, sortable, timeline, frame, alert, badge, scrollspy, icon-stack, icon-tile | `reui-layout` |
| A premium block, a full page, icons, templates | `reui-blocks` |

Most real tasks touch two or three, in an order that matters: "add ReUI and build a dashboard" is
`reui-setup` first, then `reui-blocks`. Anything premium needs `reui-setup` for the licence check
**before** a single install runs, or the install fails late and confusingly.

## The MCP leads, the references catch it when it falls

1. **The ReUI MCP** (`mcp__reui__*`) when it answers: `search` for one item, `compose_page` before a
   whole page, one **batched** `get_component`, `get_examples` for a real composition,
   `validate_usage` before writing an unread prop, `get_audit_checklist` before done.
2. **This plugin's reference files** when it cannot — a spent quota, an expired sign-in, no network.
3. **The files the install added**, which outrank both for what is available right now.

The free plan allows **100 MCP calls per day**. One search per intent, one batched `get_component`,
no `list_*` browsing. When the quota is gone, switch to the references and say so.

## ReUI sits on top of shadcn/ui

A generic control shadcn already ships — Button, Dialog, Select, Card — is plain shadcn work: use
the **`shadcn` plugin** for those and for the shared conventions. What shadcn does not solve —
data-grid, kanban, gantt, filters, cascader, event-calendar — is ReUI, and hand-rolling one of those
from shadcn parts is the failure this plugin exists to prevent.

ReUI ships **React only**. A Vue or Nuxt project cannot install `@reui` at all: say so and route to
the **`shadcn-vue` plugin** instead of adapting ReUI code by hand.

## When to hand off to an agent

- `reui-setup-assistant` — installing a project, or diagnosing a failing install.
- `reui-expert` — finding, installing and wiring an item once the project is set up.

Hand off when the work is a self-contained slice. Routing to one skill usually settles it without
either.

## Source

The routes above are this plugin's own skills, read 2026-09-04. ReUI facts are distilled from
[reui.io/docs](https://reui.io/docs) and
[reui.io/r/registry.json](https://reui.io/r/registry.json), mirrored 2026-09-04.
