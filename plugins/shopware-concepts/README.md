# shopware-concepts

> The "why" behind Shopware: architecture and domain concepts.

`shopware-concepts` conveys the **"why"** behind Shopware — the architecture and domain concepts that underlie the
concrete how-to skills of the other plugins.

It contains the distilled **concept documents** of the official documentation: the **framework architecture** (bundles,
DI, adapters, rule system, translations), the **data concept** (the DAL as an idea, not as an API), the
**commerce domains** (catalogue/products, checkout concept, content/CMS), the **API concept** (why three APIs), the
**extension/app system** and **messaging**. These skills explain relationships and design decisions — ideal for
onboarding and for making well-founded architecture decisions.

Specialist: **`shopware-concepts`**. **When to use:** to understand the background, during onboarding or before
larger architecture decisions. The concrete implementation then comes from `shopware-data`, `shopware-framework`,
`shopware-checkout` and so on; the binding decisions are covered in depth by `shopware-quality`
(`sw-adr-knowledge`).

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official sources and embedded; each skill's depth sits in flat SCREAMING-CASE.md reference files next to its SKILL.md and is loaded progressively.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-concepts@claude-a-dev-team
```

## Skills (2)

| Skill | Description |
|---|---|
| `sw-concept-architecture` | How Shopware works: overall architecture, the DAL, data stores, extension mechanisms, the APIs, the app system, messaging. Use when asked why Shopware works a certain way rather than how to code it. |
| `sw-concept-domain` | Shopware domain concepts: catalogue, checkout, content and CMS, the rule system, translations. Use when asked how a Shopware domain is modelled conceptually. |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-concepts` | Shopware 6 concept advisor. Answers architectural and conceptual questions about Shopware — "how does X work in Shopware", "what is the difference between an app and a plugin", "how does the cart work", "how does the rule system work… |
