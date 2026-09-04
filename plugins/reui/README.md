# reui

The [ReUI](https://reui.io) registry for Claude Code: a shadcn-compatible registry of React
components, examples and premium blocks, with an explicit free / Pro / Ultimate split and the
hosted ReUI MCP server wired in.

## What this plugin is for

ReUI ships a hosted MCP server that answers against the live registry, and that stays the primary
source. This plugin adds three things around it:

1. **A fallback that works when the MCP does not.** The free plan allows **100 MCP tool calls a
   day**; a spent quota, an expired sign-in or no network all leave an agent guessing. The
   reference files carry the whole registry and every documented component API offline.
2. **An explicit licence tier on every item.** A premium install without both `REUI_LICENSE_KEY`
   and the authenticated `@reui` entry in `components.json` fails with a 401 *after* resolving
   dependencies. The plugin states the tier before proposing an install, and a `PreToolUse` hook
   catches the case where the setup cannot succeed.
3. **The full installation and configuration path** — prerequisites, both registry forms, licence
   setup, RTL, the extended theme tokens, and MCP setup for 15 clients.

## Layout

| Skill | Covers |
|---|---|
| `reui-registry` | the free/premium split, every primitive and `c-*` example by name |
| `reui-setup` | installation, `components.json`, the licence, RTL, prerequisites |
| `reui-mcp` | the MCP server, its tools, authentication, the daily quota, troubleshooting |
| `reui-theming` | the extended semantic tokens ReUI adds to shadcn/ui |
| `reui-data` | data-grid, filters, cascader, gantt, event-calendar, tree, date-selector, code-block |
| `reui-forms` | autocomplete, number-field, phone-input, rating, file-upload, stepper |
| `reui-layout` | kanban, sortable, timeline, frame, alert, badge, scrollspy, icon-stack, icon-tile |
| `reui-blocks` | the 533 premium blocks by group, plus icons and templates |

**Agents.** `reui-dev` is the orchestrator and default entry point; `reui-expert` finds, installs
and wires an item; `reui-setup-assistant` handles installation and diagnoses a failing one.

**Commands.** `/reui-init`, `/reui-add`, `/reui-build`, `/reui-license`, `/reui-sync`.

**Hooks.** `MCP-FALLBACK.py` fires when an `mcp__reui__*` call fails and points the session at the
local references; `PREMIUM-GATE.py` warns before a premium install that cannot succeed.

**MCP.** `.mcp.json` declares the ReUI server (`https://mcp.reui.io`, Streamable HTTP). Sign in once
with `/mcp`.

## Relationship to the shadcn plugins

ReUI is a registry *for* shadcn projects, not a replacement. Use the **`shadcn`** plugin for the
generic controls shadcn/ui already ships (Button, Dialog, Select, Card) and for the shared
conventions; use this plugin for what shadcn does not solve — data grids, kanban boards, gantt
charts, filter builders, event calendars.

ReUI ships **React only**. For a Vue or Nuxt project, use the **`shadcn-vue`** plugin instead; ReUI
cannot be installed there.

## Licence tiers

| Tier | What it covers |
|---|---|
| Free | 22 primitives, 1,105 `c-*` examples, the registry, the MCP at 100 calls/day |
| Pro | adds all 533 premium blocks and removes the MCP daily limit |
| Ultimate | adds 638 icons (2,552 variants) and 14 full-page templates |

## Keeping it current

`/reui-sync` re-fetches `https://reui.io/r/registry.json`, reports what changed, and regenerates the
registry references through `scripts/gen_registry_refs.py`. The generated files carry the source
hash, so drift is visible rather than silent.

## Source and credit

The knowledge here is distilled from ReUI's own documentation and registry, which remain the
property of their authors:

- [`https://reui.io/docs`](https://reui.io/docs) — 74 pages, mirrored 2026-09-04
- [`https://reui.io/r/registry.json`](https://reui.io/r/registry.json) — 1,719 items,
  sha256 `a598d3b8b544a0fa1fc834d7a590b2b04642c080890c46790c7a5df5e1ea239f`
- [`https://reui.io/llms.txt`](https://reui.io/llms.txt) — the upstream index

Component prop tables that ReUI documents by linking out (autocomplete, number-field) are attributed
to the primitive library they come from in the file itself.

This plugin is not affiliated with ReUI. Premium ReUI content requires a licence purchased from
ReUI; nothing licensed is redistributed here.
