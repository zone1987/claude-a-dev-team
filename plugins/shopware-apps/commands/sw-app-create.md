---
name: sw-app-create
description: Scaffold einer Shopware-6-App (App-System): manifest.xml mit Meta/Permissions, optional Setup (Registrierung/Signatur) und Auswahl SDK (PHP/JS) bzw. App-Scripts.
argument-hint: <AppName> [--owner Ff|Adt|Ag|Pb] [--sdk php|js|scripts]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-app-create

Lege eine Shopware-App an. Skills: `shopware-apps`, `sw-app-php-sdk`/`sw-app-sdk-js`.

## Ablauf
1. App-Name (PascalCase, Owner-Präfix) + Zweck + Auslieferungsart (`--sdk`): `scripts` (nur App-Scripts, kein Server),
   `php` (app-php-sdk), `js` (app-sdk-js).
2. `manifest.xml` erzeugen: `<meta>` (name, label, version, author, license), `<permissions>` (minimal), bei Bedarf
   `<webhooks>`, `<admin>`/`<storefront>`, `<payments>`, `<custom-fields>`.
3. Je nach SDK: App-Server-Gerüst (Registrierung/Signatur, ShopRepository, Webhook-/ActionButton-Handler) oder
   `Resources/scripts/<hook>/` für App-Scripts.
4. Hinweis: App registrieren/installieren, Signatur verifizieren, Permissions prüfen.

Plugin statt App? → `shopware-core` (`/sw-plugin-create`). Manifest-Detailthemen in den References des Skills `shopware-apps`.
