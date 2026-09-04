# MCP Tools

The ReUI MCP server (`https://mcp.reui.io`, Streamable HTTP) exposes tools grouped by upstream
into four categories. The Introduction page states the server exposes **18 tools** total; the MCP
Server doc page and the mcp.md landing page enumerate the following named tools (list below is
every tool named across both pages — no count reconciliation is offered by upstream beyond the
"18 tools" figure).

Every tool answers against the current registry, scored and ranked.

## Contents

- [Find](#find)
- [Read](#read)
- [Plan and validate](#plan-and-validate)
- [Install and unlock](#install-and-unlock)
- [Marketing-page tool highlights (mcp.md — same tools, restated with more detail)](#marketing-page-tool-highlights-mcpmd-same-tools-restated-with-more-detail)
- [The Agent Skill (companion to the MCP server)](#the-agent-skill-companion-to-the-mcp-server)
- [Source](#source)

## Find

- **`search`** — ranked matches across components, examples, blocks, and icons for a
  natural-language query. Each result includes: an install command, a live preview, a docs link,
  and the components it uses.
- **`search_icons`** — the best-matching icon for many concepts (e.g. "save", "user settings") in
  one call, optionally pinned to one icon style.
- **`list_components`** — the 21 free ReUI building blocks (data-grid, event-calendar, gantt,
  cascader, kanban, filters, icon-tile, ...).
- **`list_block_groups`** — the top-level block groups (application, ecommerce, marketing, ...)
  with counts.
- **`list_block_categories`**, **`list_example_categories`**, **`list_icon_categories`** — the
  categories of each item type with item counts, for narrowing a search.

## Read

- **`get_component`** — the inline API (props and usage) for one or many components in a single
  call, so props come from the docs, never from memory.
- **`get_examples`** — a component's real, working example compositions to copy instead of
  hand-rolling.
- **`get_block`**, **`get_example`**, **`get_icon`** — full metadata for one item by name:
  description, components used, dependencies, install command, docs and preview links.

## Plan and validate

- **`compose_page`** — turns a whole-page intent into ordered sections, each matched to the best
  block for the job.
- **`validate_usage`** — checks planned components and props against the documented API before
  any code is written.
- **`get_audit_checklist`** — the ReUI-specific checks to run after installing and adapting an
  item.

## Install and unlock

- **`get_install_command`** — the exact shadcn CLI command for an item, validated against the
  registry (wrong names get did-you-mean suggestions, not a fabricated command).
- **`get_project_context`** — the `components.json` registry config and license-key setup so
  `shadcn add @reui/...` works.
- **`get_agent_skill`** — the full ReUI build skill, served at runtime to agents that cannot
  install files locally (any MCP client can pull it on demand).

## Marketing-page tool highlights (mcp.md — same tools, restated with more detail)

- `search` — ranked matches "with a score and a `whyMatch` reason - the right item, not the first
  name hit."
- `compose_page` — "turns an intent into ordered sections, each matched to the best block for the
  job."
- `get_component` — "reads up to 20 component APIs in one call, so your agent wires from the real
  props." (This is the only place upstream states a numeric batch limit — 20 — for
  `get_component`.)
- `validate_usage` — "checks planned components and props against the documented API before code
  is written."

## The Agent Skill (companion to the MCP server)

The ReUI Agent Skill is a small set of markdown files that teaches a coding agent how to build
with ReUI: find the right item, install it, read its real API, adapt it by reuse. It is free and
works with every supported agent (see CLIENT-SETUP.md for per-client install/availability).

### Division of labor

- **The MCP server is the live data and the hands.** It answers `search`, returns real component
  APIs (`get_component`), validates prop usage (`validate_usage`), and hands back the exact
  shadcn install command — all against the current registry, scored and ranked.
- **The skill is the workflow brain.** It tells the agent when to reach for ReUI, which tool to
  call next, and how to adapt what it installs (reuse the block, wire real data, keep the design,
  never invent props).

**Without the skill an agent can still call the tools**, but it tends to over-customize,
hand-roll what ReUI already ships, or invent APIs. The skill keeps it on rails.

### The workflow the skill teaches

1. **Find** — call `search` with the user's intent. Returns ranked matches across components,
   examples, blocks, and icons, each with an install command, preview, docs link, and the
   components it uses.
2. **Install** — run the returned shadcn command non-interactively. The CLI resolves dependencies
   and the base style from `components.json`.
3. **Read the API** — call `get_component` for each component the item uses and read its inline
   API (no guessing), then `get_examples` to copy a real, working composition.
4. **Adapt by reuse** — swap demo data for real data, fix icon imports, align to theme tokens.
   Keep the block's structure and styling; do not redesign what ReUI already provides.
   `validate_usage` flags any prop or name the agent invented before it ships.

### How the skill reaches each agent

- Local CLIs and editors (Claude Code, Codex, Cursor, OpenCode) get it written into the project
  by the one-line installer (`curl -fsSL https://mcp.reui.io/install | node -`).
- Every other agent receives it at runtime through the MCP, with nothing to install.
- Any MCP client can pull it on demand with the `get_agent_skill` tool.

### Licensing note (stated plainly, not as a pitch)

The skill and the MCP server are free and only require a ReUI account. A Pro or Ultimate license
unlocks premium blocks and animated icons, and removes the daily MCP request limit (100/day on
Free — see TROUBLESHOOTING.md), so the same workflow can install and adapt the paid parts of the
registry too.

## Tools the vendor skill documents and the docs pages do not

ReUI's own agent skill (shipped by the installer as `SKILL.md` + `tools.md`) names two tools and one
result field that no `reui.io/docs` page mentions. Recorded here with that provenance, because a
reader must be able to tell the two sources apart.

- **`whats_new`** — reach for it when registry knowledge might be stale: a name 404s, or the user
  names an item you do not know. Returns items added and removed per build, newest first.
- **`report_issue`** — for an installed item that is genuinely broken (bad source, wrong dependency,
  broken preview). Goes to the ReUI team, rate-limited to 5 an hour. Not for usage questions.

Result fields the same source documents:

- **`score`** is relative to the top hit, which is ~100 by construction — not an absolute quality.
  Compare results against each other, and show the user the close contenders rather than guessing.
- **`termCoverage`** (0–1) is the share of the query an item matched. A low value means a weak match
  even when the score looks high: rephrase or widen the search.
- **`componentDigests`** is a top-level map carrying a compact API contract per referenced
  component — often enough to wire an item with no `get_component` call at all.
- **`found: false`** carries `suggestions`. Use them, or search again; never run a fabricated
  install command.

That skill also states the batching rule this file's guidance rests on: **one** `get_component` call
with the whole `componentsUsed` array, never one call per name.

## Source

https://reui.io/docs/mcp, https://reui.io/mcp, https://reui.io/docs, https://reui.io/docs/agent-skills — mirrored 2026-09-04.

The vendor-skill section above is distilled from ReUI's own agent skill (`tools.md`, skill version `3bdbad788a`), which the ReUI installer writes into a project and which the MCP also serves through `get_agent_skill`. Retrieved 2026-09-04.
