---
name: sw-guidelines
description: Shopware coding guidelines: code structure, domain exceptions, extendability rules, ADR knowledge, documentation guidelines, plus our own plugin ground rules, ADR, CLAUDE.md/CONTEXT.md and workflow conventions. Use when reviewing Shopware code against the platform's own conventions or against our plugin working method.
---

# Shopware coding guidelines

The platform's own rules for platform-shaped code. Domain exceptions and extendability are where most plugins diverge.
The `PLUGIN-*` references carry our own working method for the plugins we write — distinct from the core's rules.

## Reference map

- **[ADR-KNOWLEDGE.md](references/ADR-KNOWLEDGE.md)**: The ADRs document binding architecture decisions of the core. [ADR-KNOWLEDGE-ADR-INDEX](references/ADR-KNOWLEDGE-ADR-INDEX.md).
- **[CODE-STRUCTURE.md](references/CODE-STRUCTURE.md)**:
- **[CODING-GUIDELINES.md](references/CODING-GUIDELINES.md)**: Binding guidelines from the core. [CODING-GUIDELINES-CODE-GUIDELINES-FULL](references/CODING-GUIDELINES-CODE-GUIDELINES-FULL.md).
- **[DOCUMENTATION-GUIDELINES.md](references/DOCUMENTATION-GUIDELINES.md)**:
- **[DOMAIN-EXCEPTIONS.md](references/DOMAIN-EXCEPTIONS.md)**: Instead of many individual exception classes: **one factory per domain** with static methods that return typed….
- **[EXTENDABILITY.md](references/EXTENDABILITY.md)**:
- **[PLUGIN-ADR.md](references/PLUGIN-ADR.md)**: The ADRs a plugin writes **for itself** — file name, frontmatter, Context/Decision/Consequences, `_superseded/`, and why an accepted ADR is never edited. Not the core's ADRs.
- **[PLUGIN-CLAUDE-MD.md](references/PLUGIN-CLAUDE-MD.md)**: What is documented where: `CLAUDE.md` (layout, 200-line limit), `CONTEXT.md` (purpose, 90/95/98 % rewrites, gitignored) and the rule that there is no general `TODO.md`.
- **[PLUGIN-GROUND-RULES.md](references/PLUGIN-GROUND-RULES.md)**: The nine non-negotiable rules of our own plugins — English everywhere but the README, no prose comments, no copyright headers, the git rule, foreign code, `shopware-cli`, DDEV, credentials, one task at a time. Plus the placeholder table.
- **[PLUGIN-WORKFLOW.md](references/PLUGIN-WORKFLOW.md)**: The 15-step order inside a task, two browser tabs, Conventional Commits, measured versus asserted — and the 15-point definition of "done".

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20. Coding guidelines and ADRs come from the shopware/shopware repository. The `PLUGIN-*` references come from our own `working-method.md` (Shopware 6.7, PHP 8.3, DDEV, `shopware-cli`).
