# Shopware extensions — app vs. plugin

Complete concept documentation: `EXTENSIONS-DETAIL.md`

## Brief overview

### Apps

- **Outside the Shopware process** — own server, own technology (no PHP required)
- Communication: HTTP webhooks (Shopware → app) + Admin API (app → Shopware)
- **Cloud-compatible** — works with self-hosted and Shopware SaaS
- Registration via `manifest.xml`
- Can do: webhooks, Store API extensions, storefront assets, app scripts, payment, rule conditions, CMS blocks

### Plugins

- **Executed inside the Shopware process** — direct access to the DI container, database, events
- Built on **Symfony bundles** + an abstract base class
- **Not cloud-compatible** — self-hosted only
- Maximum extensibility: new user providers, custom search engine, etc.

### Decision criteria

| Criterion | App | Plugin |
|---|---|---|
| Cloud hosting | Yes | No |
| Freedom of technology | Yes (any) | No (PHP) |
| Deep access to Shopware internals | Limited | Complete |
| Security sensitivity | High | Lower |

Technical implementation: `shopware-apps` (apps), `shopware-core` (plugins) — dev plugins
