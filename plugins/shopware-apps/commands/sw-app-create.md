---
name: sw-app-create
description: Scaffolds a Shopware 6 app (app system): manifest.xml with meta and permissions, optional setup (registration and signing), and a choice of SDK (PHP/JS) or app scripts.
argument-hint: <AppName> [--owner Ff|Adt|Ag|Pb] [--sdk php|js|scripts]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-app-create

Create a Shopware app. Skills: `sw-app-manifest`, `sw-app-sdk`.

## Steps
1. App name (PascalCase, owner prefix), purpose and delivery shape (`--sdk`): `scripts` (app scripts only,
   no server), `php` (app-php-sdk), `js` (app-sdk-js).
2. Write `manifest.xml`: `<meta>` (name, label, version, author, license), `<permissions>` (minimal), and
   where needed `<webhooks>`, `<admin>`/`<storefront>`, `<payments>`, `<custom-fields>`.
3. Per SDK: the app-server skeleton (registration and signing, ShopRepository, webhook and action-button
   handlers), or `Resources/scripts/<hook>/` for app scripts.
4. Note the follow-up: register and install the app, verify the signature, review the permissions.

A plugin rather than an app? Use `shopware-core` (`/sw-plugin-create`). Manifest detail lives in the
references of the `sw-app-manifest` skill.
