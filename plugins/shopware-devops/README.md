# shopware-devops

> Tooling and operations: CLI, local setups, hosting, PaaS, performance.

`shopware-devops` bundles **tooling, local development and operations** around Shopware.

Included: the **`shopware-cli`** (extension build/validate/zip, project commands, account/store upload) including the
command reference and the **MCP server**; **Symfony Flex recipes**; **Shopware PaaS** in depth (fundamentals,
getting started, environments, build/deploy, services, CDN, monitoring, scaling, composable frontends); **local
dev setups** (Docker/dockware, devenv/Nix, Symfony CLI, ZIP→Composer migration); **hosting and infrastructure**
(system requirements, installation/updates, webserver, database, HTTP cache, worker/cron, search, filesystem/S3,
env config, deployment, observability); **performance** and **troubleshooting** (including dev tooling/IDE/watchers).

Specialist: **`shopware-devops`**. **When to use:** for CI/CD, building/releasing extensions, local environments,
deployment and hosting/performance questions. Quality gates (lint/static analysis) come from `shopware-quality`.

Part of the marketplace **[claude-a-dev-team](../../README.md)**. The knowledge is distilled from the official sources and embedded; each skill keeps its depth in flat SCREAMING-CASE.md reference files next to its `SKILL.md`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-devops@claude-a-dev-team
```

## Skills (5)

| Skill | Description |
|---|---|
| `sw-cli` | shopware-cli: extension build, validate and zip, project commands, account and store upload, the full command reference, MCP server. Use when the request names shopware-cli |
| `sw-hosting` | Shopware self-hosted operations: requirements, installation, webserver, database, search, HTTP caching, S3, env config, worker and cron, performance, observability, updates, deployment |
| `sw-paas` | Shopware PaaS: fundamentals, getting started, environments, build and deploy, services, cron and worker, CDN, monitoring, scaling, composable frontends. Use when the request names Shopware PaaS |
| `sw-support` | Shopware troubleshooting: diagnosing installation, cache, permission, performance and worker problems. Use when a Shopware shop misbehaves and the cause is unclear |
| `sw-tooling` | Shopware development tooling: IDE setup, file watchers, the fixture bundle, Symfony Flex recipes, the DAL reference. Use when setting up a Shopware development environment |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-devops` | Specialist for Shopware tooling and deployment: shopware-cli (extension build/validate/zip, project commands, account/store upload), Symfony Flex recipes, Shopware PaaS (sw-paas) deployment, build/deploy hooks, CI/CD |
