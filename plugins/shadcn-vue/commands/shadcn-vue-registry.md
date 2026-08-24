---
name: shadcn-vue-registry
description: Scaffolds a shadcn-vue-compatible registry of your own — writes registry.json and registry-item.json to schema, the shadcn-vue build step, hosting and consumer notes, and optionally MCP compatibility.
argument-hint: [--item-type ui|block|theme|hook|lib|page] [--name "@acme/my-component"] [--mcp]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-registry

Build a registry of your own. Skill: `shadcn-vue-setup`.

## Steps
1. Item type and name from `$ARGUMENTS`.
2. **`registry.json`**: the index — `$schema`, `name`, `homepage`, `items`.
3. **`registry-item.json`** per item: `$schema`, `name`, `type` (`registry:ui`, `registry:block`,
   `registry:theme`, …), `files` with their `path` and `type`, plus `dependencies` and
   `registryDependencies` where needed.
4. **Build:** `npx shadcn-vue@latest build`, then host the output as static JSON.
5. Consumer side: the `registries` entry in `components.json`, and `--mcp` for MCP compatibility.

Use the documented schema fields and `registry:*` types only (source: `shadcn-vue-setup`). Never put
a token in the registry URL — reference an env var.
