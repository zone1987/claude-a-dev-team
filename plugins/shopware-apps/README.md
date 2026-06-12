# shopware-apps

> Das App-System als cloud-fähige Alternative zum Plugin.

`shopware-apps` behandelt das **App-System** — die **cloud-fähige** Alternative zum klassischen Plugin, bei der die
Logik (optional) auf einem eigenen App-Server statt im Shop läuft.

Abgedeckt: das **Manifest** (Meta, Permissions, Webhooks, ActionButtons, Payment, Flow, CMS, Custom-Fields/-Entities),
der **Registrierungs-/Handshake**-Ablauf und die **HMAC-Signatur** aller Requests, **App-Scripts** (Logik ohne
eigenen Server), **Storefront-/Admin-Integration**, **Payment-/Tax-/CMS-/Flow-Gateways**, **In-App-Purchases** und
**Monetarisierung**. Für eigene App-Server stehen die offiziellen SDKs im Fokus: das **PHP-SDK** (`app-php-sdk`,
Symfony) und das **JS-SDK** (`app-sdk-js`, runtime-agnostisch: Node/Bun/Deno/Cloudflare Workers).

Spezialist: **`shopware-app-dev`**; Scaffolder **`/sw-app-create`**. **Wann nutzen:** wenn eine Erweiterung
SaaS/Cloud-fähig sein muss oder als App im Store vertrieben wird. Für klassische, im Shop laufende Erweiterungen
stattdessen die Plugin-Cluster (`shopware-core`, `shopware-data`, …).

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-apps@claude-a-dev-team
```

## Skills (5)

| Skill | Beschreibung |
|---|---|
| `shopware-apps` | Comprehensive guide for developing Shopware 6 Apps, covering manifest configuration, webhooks, authentication, app scripts, storefront/admin customization, payments, custom data, flow actions, gateways, and in-app purchases |
| `sw-app-manifest-reference` | Shopware 6 App manifest.xml Vollreferenz — alle Sektionen (meta, setup, requirements, permissions, webhooks, admin, custom-fields, cookies, payments, shipping-methods, rule-conditions, tax, storefront), Custom Entities XML, CMS-Blocks XML,  |
| `sw-app-php-sdk` | Exhaustive reference for `shopware/app-php-sdk` (PHP 8.1+, PSR-based, framework-agnostic) |
| `sw-app-sdk-js` | Exhaustive reference for `@shopware-ag/app-server-sdk` (TypeScript, runtime-agnostic: Node 20, Bun, Deno, Cloudflare Workers) |
| `sw-monetization-iap` | Shopware In-App Purchases (IAP) — Features hinter Paywall in Extensions |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-app-dev` | Spezialist für die Shopware-6 App-Entwicklung (App-System statt Plugin): Manifest, Registrierung/Signatur, Webhooks, App-Scripts, Admin-/Storefront-Integration, Custom-Data/-Entities/-CMS, Payment/Tax/Flow/Gateways, IAP, sowie die SDKs (app |

## Commands (1)

| Command | Beschreibung |
|---|---|
| `/sw-app-create` | Scaffold einer Shopware-6-App (App-System): manifest.xml mit Meta/Permissions, optional Setup (Registrierung/Signatur) und Auswahl SDK (PHP/JS) bzw |
