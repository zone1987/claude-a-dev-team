# Changelog

## 1.0.0

First release.

- Eight skills over the ReUI registry: `reui-registry`, `reui-setup`, `reui-mcp`, `reui-theming`,
  `reui-data`, `reui-forms`, `reui-layout`, `reui-blocks`.
- Registry references generated from `registry.json` (1,719 items) by
  `scripts/gen_registry_refs.py`, so the free / Pro / Ultimate split is read from the source rather
  than recalled.
- Component APIs distilled from all 74 documentation pages, with the Base UI and Radix UI builds
  diffed rather than duplicated.
- `reui-dev` router skill as the entry point, plus the `reui-expert` and
  `reui-setup-assistant` agents.
- Commands: `/reui-init`, `/reui-add`, `/reui-build`, `/reui-license`, `/reui-sync`.
- `MCP-FALLBACK.py` hands the session its local references when an `mcp__reui__*` call fails —
  including the free plan's 100 calls a day; `PREMIUM-GATE.py` warns before a premium install that
  is missing its licence key or the authenticated registry form.
- `.mcp.json` declares the ReUI MCP server over Streamable HTTP.
