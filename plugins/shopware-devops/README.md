# shopware-devops

> Werkzeuge & Betrieb: CLI, lokale Setups, Hosting, PaaS, Performance.

`shopware-devops` bündelt **Werkzeuge, lokale Entwicklung und Betrieb** rund um Shopware.

Enthalten: die **`shopware-cli`** (Extension build/validate/zip, Project-Commands, Account/Store-Upload) inkl.
Befehls-Referenz und **MCP-Server**; **Symfony-Flex-Recipes**; **Shopware PaaS** in der Tiefe (Fundamentals,
Get-Started, Umgebungen, Build/Deploy, Services, CDN, Monitoring, Skalierung, Composable Frontends); **lokale
Dev-Setups** (Docker/dockware, devenv/Nix, Symfony-CLI, ZIP→Composer-Migration); **Hosting & Infrastruktur**
(Systemanforderungen, Installation/Updates, Webserver, Datenbank, HTTP-Cache, Worker/Cron, Suche, Filesystem/S3,
Env-Config, Deployment, Observability); **Performance** und **Troubleshooting** (inkl. Dev-Tooling/IDE/Watcher).

Spezialist: **`shopware-devops`**. **Wann nutzen:** für CI/CD, Build/Release von Extensions, lokale Umgebungen,
Deployment und Hosting/Performance-Fragen. Qualitäts-Gates (Lint/Static-Analysis) liefert `shopware-quality`.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-devops@claude-a-dev-team
```

## Skills (37)

`sw-cli`, `sw-cli-account`, `sw-cli-commands-reference`, `sw-cli-extension`, `sw-cli-project`, `sw-cli-reference`, `sw-dal-reference`, `sw-hosting-caching-http`, `sw-hosting-database`, `sw-hosting-deployment`, `sw-hosting-env-config`, `sw-hosting-filesystem-s3`, `sw-hosting-installation`, `sw-hosting-observability`, `sw-hosting-performance`, `sw-hosting-requirements`, `sw-hosting-search`, `sw-hosting-updates`, `sw-hosting-webserver`, `sw-hosting-worker-cron`, `sw-mcp-server`, `sw-paas`, `sw-paas-build-deploy`, `sw-paas-cdn`, `sw-paas-composable-frontends`, `sw-paas-cron-worker`, `sw-paas-environments`, `sw-paas-fundamentals`, `sw-paas-get-started`, `sw-paas-monitoring`, `sw-paas-resources-scaling`, `sw-paas-services`, `sw-recipes`, `sw-tooling-fixture-bundle`, `sw-tooling-ide`, `sw-tooling-watchers`, `sw-troubleshooting`

## Agents (1)

- **`shopware-devops`** — Spezialist für Shopware-Tooling & Deployment: shopware-cli (Extension build/validate/zip, Project-Commands, Account/Store-Upload), Symfony-Flex-Recipes, Shopware PaaS (sw-paas) Deployment, Build/Deploy-Hooks, CI/CD.
