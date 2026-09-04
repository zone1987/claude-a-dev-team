---
name: reui-init
description: Sets up the @reui registry in this project — components.json, the style, and the licence key when premium items are wanted.
argument-hint: [--premium]
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
model: sonnet
---

Set up ReUI in this project. `$ARGUMENTS` may carry `--premium` to configure for premium installs.

## Steps

1. **Read the ground state**: `components.json`, `package.json`, and `.env.local` if present. Report
   what is already there rather than overwriting it blindly.
2. **Check the prerequisites**: React 19 and Tailwind CSS v4, shadcn/ui initialised. Name anything
   missing and stop rather than guessing around it.
3. **Confirm the build.** `components.json` → `style` decides everything downstream:
   `base-nova` → Base UI, `radix-nova` → Radix UI. If absent, ask which the project wants.
4. **Add the `@reui` registry entry.** Without `--premium`, the plain string form. With `--premium`,
   the authenticated object form plus `REUI_LICENSE_KEY` in `.env.local`, and check `.env.local` is
   ignored by git.
5. **Verify** with one free install, then remove it again if it was only a probe:
   `npx shadcn@latest add @reui/c-alert-1 --yes`
6. **Offer the MCP.** `claude mcp add --transport http reui https://mcp.reui.io`, then `/mcp` to sign
   in. Note the free plan's limit of 100 tool calls a day.

Follow `skills/reui-setup/references/INSTALLATION.md`, `REGISTRY-CONFIG.md` and `LICENSE-SETUP.md`
for the exact snippets. Never write a real licence key into a committed file.

## Report

The files changed, the resulting registry form (free or authenticated), the detected build, and the
verification result — green or red, with the actual output when red.
