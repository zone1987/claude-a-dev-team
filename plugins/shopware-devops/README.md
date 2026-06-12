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

| Skill | Beschreibung |
|---|---|
| `sw-cli` | shopware-cli — das offizielle Go-CLI für Shopware 6. Überblick: Installation, globale Flags, alle Command-Gruppen (account, extension, project) |
| `sw-cli-account` | shopware-cli account * — Login, Logout, Producer Extension Upload/Info/List |
| `sw-cli-commands-reference` | shopware-cli — vollständige Befehls-Referenz aller Subcommands mit allen Flags und Optionen: extension build/validate/zip/upload/fix/format/admin-watch, project create/ci/admin-build/storefront-build/dump/worker/image-proxy/autofix, account |
| `sw-cli-extension` | shopware-cli extension * — alle Extension-Subcommands: build, validate, zip, watch, fix, format, get-version, get-name, prepare, changelog, config-schema |
| `sw-cli-project` | shopware-cli project * — alle Projekt-Subcommands: create, ci, admin-build, storefront-build, admin-watch, storefront-watch, console, dump, worker, doctor, extension lifecycle, autofix, config, generate-jwt, image-proxy, validate |
| `sw-cli-reference` | Shopware 6 bin/console CLI — vollständige Befehlsreferenz aller Gruppen (cache, plugin, dal, es, scheduled-task, theme, system, sales-channel, media, make:plugin u.v.m.) plus Composer-Dev-Commands |
| `sw-dal-reference` | Shopware 6 DAL Referenz: alle Filter-Typen (equals, equalsAny, contains, range, not, multi, prefix, suffix), alle Aggregations-Typen (avg, count, max, min, sum, stats, terms, filter, entity, histogram, range), Flags-Referenz (ApiAware, Requ |
| `sw-hosting-caching-http` | Shopware 6 Caching — HTTP-Cache, Object-Cache, Redis-Cache, Session, Cart, Lock-Store, Increment, Number-Ranges |
| `sw-hosting-database` | Shopware 6 Datenbank-Setup — MySQL/MariaDB Cluster, Read Replicas, ProxySQL, Reconnect, Redis-Konfiguration |
| `sw-hosting-deployment` | Shopware 6 Deployment — Deployment Helper, Deployer, CI/CD, Blue-Green, Build without DB, one-time tasks |
| `sw-hosting-env-config` | Shopware 6 Environment-Konfiguration — .env, APP_SECRET, DATABASE_URL, Feature-Flags, Static System Config, shopware.yaml |
| `sw-hosting-filesystem-s3` | Shopware 6 Filesystem — S3, GCS, lokaler Adapter, CDN, private/public Dateien, Cluster-Shared-Dirs |
| `sw-hosting-installation` | Shopware 6 Installation, Docker-Setup und Extension Management via Composer |
| `sw-hosting-observability` | Shopware 6 Observability — Logging, Monolog, OpenTelemetry, Grafana, Profiling |
| `sw-hosting-performance` | Shopware 6 Performance-Tuning — PHP OPcache, classmap-authoritative, MySQL-Tuning, HTTP-Cache, zstd, Logging |
| `sw-hosting-requirements` | Shopware 6 Server-Anforderungen, empfohlener Stack und Versionen |
| `sw-hosting-search` | Shopware 6 Elasticsearch / OpenSearch Setup, Indexing, Cluster, N-Gram, Admin Search |
| `sw-hosting-updates` | Shopware 6 Updates durchführen — Minor, Major, Staging, Rollback, Security-Plugin |
| `sw-hosting-webserver` | Shopware 6 Webserver-Konfiguration — Nginx, Apache, Caddy, FrankenPHP, Trusted Proxies, Varnish, Fastly |
| `sw-hosting-worker-cron` | Shopware 6 Message Queue Worker, Scheduled Tasks, Cron-Jobs, systemd, supervisord |
| `sw-mcp-server` | Shopware MCP-Server — nativer Model Context Protocol Server in Shopware 6.7+: Zweck, Setup, Authentifizierung, alle eingebauten Tools/Resources/Prompts, Konfiguration, Allowlists, Erweiterung via Plugin/App/Bundle |
| `sw-paas` | Shopware PaaS — Platform.sh-basiertes Managed Hosting. Konfiguration via .platform/-Dateien (applications.yaml, services.yaml, routes.yaml), Build-Hook mit shopware-cli, Deploy-Hook mit deployment-helper, Mounts, Worker, Crons, sw-paas CLI |
| `sw-paas-build-deploy` | Shopware PaaS (Platform.sh/Upsun) Build & Deploy: .platform/-Konfiguration, Build-Hook, Deploy-Hook, Post-Deploy, Mounts, Worker, Automatic Env Vars, shopware/paas-meta Recipe, Composer Auth, Rebuild triggern |
| `sw-paas-cdn` | Shopware PaaS Native CDN: Fastly Integration, Custom Domains (Apex/Subdomain), DNS-Konfiguration, Fastly Snippets, Web Application Firewall (WAF), NGWAF |
| `sw-paas-composable-frontends` | Shopware PaaS Composable Frontends: Performance-Optimierung, Fastly-Caching für Nuxt.js-Frontend, Store-API Cache via SwagStoreApiCache, CORS-Vermeidung, Blackfire Node.js Profiling, ISR-Konfiguration |
| `sw-paas-cron-worker` | Shopware PaaS Native Cron Jobs und Worker: Konfiguration in application.yaml, CLI-Verwaltung, History, Logs, Aktivierung/Deaktivierung, Timezones |
| `sw-paas-environments` | Shopware PaaS Native Umgebungen und Application-Management: Cloning, Shopware-Update, Domain-Verwaltung, exec vs |
| `sw-paas-fundamentals` | Shopware PaaS Native Grundkonzepte: Organisationen, Projekte, Applikationen, application.yaml, Umgebungsvariablen, Vault-Secrets, PHP-Einstellungen, k8s-meta Package, Plugin Store Auth |
| `sw-paas-get-started` | Shopware PaaS Native Quickstart: CLI installieren, Repository verbinden, Codebase vorbereiten, erstes Projekt und Application erstellen |
| `sw-paas-monitoring` | Shopware PaaS Native Monitoring: Logs (Loki/Grafana), Traces (Tempo), Events (sw-paas watch), LogQL Queries, Log-Filterung nach Komponenten, Deployment-Logs |
| `sw-paas-resources-scaling` | Shopware PaaS Native Ressourcen und Skalierung: Compute-Profile, horizontale Skalierung, Snapshots, Datenbankzugriff, Object Storage Limits |
| `sw-paas-services` | Shopware PaaS Native und PaaS Services: MySQL/MariaDB, Redis, OpenSearch, Elasticsearch, RabbitMQ, S3 Object Storage |
| `sw-recipes` | Symfony Flex Recipes für Shopware — Repository-Struktur, manifest.json-Format (alle Keys), wie Recipes genutzt und erstellt werden, verfügbare Shopware-Packages |
| `sw-tooling-fixture-bundle` | Shopware Fixture Bundle — Testdaten und Demo-Daten in Shopware 6 laden |
| `sw-tooling-ide` | Shopware IDE-Tools: PHPStorm-Plugin "Shopware 6 Toolbox" (Live Templates, Code-Generatoren, Auto-Completion, Inspections) und VS Code Extension |
| `sw-tooling-watchers` | Shopware 6 Hot Module Replacement (HMR) — Watchers für Admin und Storefront |
| `sw-troubleshooting` | Shopware 6 Troubleshooting & Debugging: Xdebug aktivieren (compose.override.yaml), Blackfire/Tideways/PCOV, DB-Verbindung lokal (Port via docker compose ps), Linux-File-Permissions, PHPStan EntityRepository Generic-Types, Null-Safety mit fi |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-devops` | Spezialist für Shopware-Tooling & Deployment: shopware-cli (Extension build/validate/zip, Project-Commands, Account/Store-Upload), Symfony-Flex-Recipes, Shopware PaaS (sw-paas) Deployment, Build/Deploy-Hooks, CI/CD |
