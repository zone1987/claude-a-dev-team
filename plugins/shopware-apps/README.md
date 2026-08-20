# shopware-apps

> The app system as the cloud-capable alternative to a plugin.

`shopware-apps` deals with the **app system** — the **cloud-capable** alternative to the classic plugin, where the
logic (optionally) runs on a dedicated app server instead of inside the shop.

Covered: the **manifest** (meta, permissions, webhooks, action buttons, payment, flow, CMS, custom fields/entities),
the **registration/handshake** sequence and the **HMAC signature** on all requests, **app scripts** (logic without a
server of your own), **storefront/admin integration**, **payment/tax/CMS/flow gateways**, **in-app purchases** and
**monetisation**. For custom app servers the official SDKs are the focus: the **PHP SDK** (`app-php-sdk`,
Symfony) and the **JS SDK** (`app-sdk-js`, runtime-agnostic: Node/Bun/Deno/Cloudflare Workers).

Specialist: **`shopware-app-dev`**; scaffolder **`/sw-app-create`**. **When to use:** when an extension has to be
SaaS/cloud-capable or is distributed as an app in the store. For classic extensions running inside the shop use the
plugin clusters instead (`shopware-core`, `shopware-data`, …).

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official sources and embedded; each skill's depth sits in flat SCREAMING-CASE.md reference files next to its SKILL.md and is loaded progressively.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-apps@claude-a-dev-team
```

## Skills (2)

| Skill | Description |
|---|---|
| `sw-app-manifest` | Shopware apps: the app system versus plugins, the complete `manifest.xml` reference, registration and signatures, in-app purchases. Use when building a Shopware app or writing a `manifest.xml`. |
| `sw-app-sdk` | Shopware app SDKs: `app-php-sdk` and `app-sdk-js` — registration handling, request signing, webhooks, app scripts. Use when the request names the Shopware `app-php-sdk` or `app-sdk-js`. |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-app-dev` | Specialist for Shopware 6 app development (app system instead of plugin): manifest, registration/signature, webhooks, app scripts, admin/storefront integration, custom data/entities/CMS, payment/tax/flow/gateways, IAP, plus the SDKs (app… |

## Commands (1)

| Command | Description |
|---|---|
| `/sw-app-create` | Scaffolds a Shopware 6 app (app system): `manifest.xml` with meta/permissions, optional setup (registration/signature) and a choice of SDK (PHP/JS) or |
