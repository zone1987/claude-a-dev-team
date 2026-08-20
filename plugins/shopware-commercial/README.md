# shopware-commercial

> The commercial extensions from a developer's point of view.

`shopware-commercial` documents the **commercial Shopware extensions from a developer's point of view** — that is,
extending/integrating the licensed features technically (operating them from a merchant's point of view lives in
`shopware-merchant`).

Covered: the **Commercial bundle** (sub-bundle architecture, feature toggles), **B2B** in its modern form
(**B2B Components**: employee management, quotes/shopping lists, order approval, individual pricing) as well as its
legacy form (**B2B Suite**, including migration), **Subscriptions**, **Advanced Search** (ES/OpenSearch-based), the
**Migration Assistant** (data migration from SW5/other systems, including custom profiles/readers/converters/writers),
plus **Digital Sales Rooms**, **Sales Agent** and **Nexus**.

Specialist: **`shopware-commercial-dev`**. **When to use:** when a project builds on commercial extensions and these
need to be extended/integrated. The standard mechanics behind them (DAL/events/Store API) come from the developer
plugins.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official sources and embedded; each skill's depth sits in flat SCREAMING-CASE.md reference files next to its SKILL.md and is loaded progressively.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-commercial@claude-a-dev-team
```

## Skills (4)

| Skill | Description |
|---|---|
| `sw-b2b` | Shopware B2B: B2B Suite, B2B Components, employee management, quotes, order approval, migration from Suite to Components. Use when the request names Shopware B2B, a quote or order approval. |
| `sw-features` | Shopware Commercial features: the Commercial bundle itself, Subscriptions, Advanced Search, Nexus. Use when the request names Shopware Subscriptions, Advanced Search or Nexus. |
| `sw-migration` | Shopware Migration Assistant: migrating shop data from Shopware 5 or another system, and writing a custom migration profile. Use when the request names the Shopware Migration Assistant. |
| `sw-sales` | Shopware sales tools: Sales Agent app with setup and deployment, Digital Sales Rooms with installation and config. Use when the request names Sales Agent or Digital Sales Rooms. |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-commercial-dev` | Specialist for Shopware 6 commercial extensions from a developer's point of view: Commercial bundle, B2B Suite & B2B Components, Subscriptions, Advanced Search, Migration Assistant (SW5->6 data migration), Digital Sales Rooms, Sales Agent, Nexus |
