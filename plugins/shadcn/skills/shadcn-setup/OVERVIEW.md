# shadcn/ui — Overview

shadcn/ui is **not a component library**. It is a code distribution platform
and the foundation for building your own component library.

## Core Principles

- **Open Code** — You receive the actual component source. No hidden abstractions.
  Edit directly. AI models can read and improve the code.
- **Composition** — Every component shares a common, composable interface (predictable
  APIs for your team and for LLMs).
- **Distribution** — Flat-file schema + CLI enables cross-framework component sharing.
- **Beautiful Defaults** — Carefully chosen default styles; components work together
  as a consistent system out-of-the-box.
- **AI-Ready** — Open code and a consistent API let LLMs generate new components
  that integrate with your existing design.

## How it differs from a traditional library

Traditional library: `npm install` → import → fight overrides.

shadcn/ui: CLI copies component source into your repo. You own the code.
Upstream primitive fixes arrive via dependency updates (radix-ui, input-otp, etc.)
without touching your design layer.

## Base UI vs Radix UI

shadcn/ui supports two component bases:

- **Radix UI** (`-b radix`, default) — battle-tested primitives from
  `@radix-ui/react-*` (now unified as `radix-ui` package).
- **Base UI** (`-b base`) — newer `@base-ui-components/react` primitives.

Select via `npx shadcn@latest init -b radix|base` or the `--base` flag.

## Reference files

- [OVERVIEW-DETAIL.md](OVERVIEW-DETAIL.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/index.mdx`
