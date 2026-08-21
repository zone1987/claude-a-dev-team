# Shopware 6 — code structure: complete reference

Sources: `guides/development/extensions/code-structure.md`, `guides/development/extensions/index.md`

---

## Contents

- [Extension types compared](#extension-types-compared)
- [Shared patterns (all extension types)](#shared-patterns-all-extension-types)
- [Project/bundle structure](#projectbundle-structure)
- [Plugin structure (static/custom + managed/store)](#plugin-structure-staticcustom-managedstore)
- [App structure](#app-structure)
- [Upgrade-oriented structure](#upgrade-oriented-structure)
- [MCP server extendability](#mcp-server-extendability)
- [References](#references)

## Extension types compared

Shopware offers two primary extension types:

- **Plugins**: full system access, self-hosted only
- **Apps**: API-based, cloud-compatible

Themes are not a separate extension type but reduced plugins (storefront UI only); in cloud environments they ship via apps.

### Decision table

| Task | Plugin (incl. theme) | App | Note |
|------|---------------------|-----|---------|
| Change storefront appearance | ✅ | ✅ | Themes are storefront plugins; in the cloud via apps |
| Add admin modules | ✅ | ✅ | Themes cannot provide admin modules |
| Execute webhooks | ✅ | ✅ | Apps are webhook-first |
| Custom entities | ✅ | ✅ | |
| Change the database structure | ✅ | ❌ | Apps cannot change the DB schema |
| Integrate a payment provider | ✅ | ✅ | |
| Publish in the Shopware Store | ✅ | ✅ | |
| Install in Shopware Cloud | ❌ | ✅ | Plugins do not run in the cloud |
| Install self-hosted | ✅ | ✅ | Apps also run self-hosted since 6.4.0.0 |
| Custom logic/routes/commands | ✅ | ⚠️ | Apps implement logic externally via webhooks |
| Style/template inheritance | ✅ | ✅ | Theme plugins only |

---

## Shared patterns (all extension types)

### Namespaces and autoloading

- Map PSR-4 to folder names; avoid deep nesting that hides ownership
- The namespace root must match the bundle name

```json
{
  "autoload": {
    "psr-4": {
      "MyVendor\\MyPlugin\\": "src/"
    }
  }
}
```

### Configuration

- Centralize defaults and document override points
- Use environment variables only in the project layer — NOT in store plugins

### Documentation

- Every extension should have a README covering purpose, install/update steps and known limitations

---

## Project/bundle structure

Bundles are for bespoke installations where you claim full control.

```
src/
├── Bundle/
│   └── MyFeatureBundle.php     # Symfony bundle class
├── Service/
│   └── MyFeatureService.php    # domain logic
├── Event/
│   └── MyFeatureEvent.php
├── Migration/
│   └── V6_7/
│       └── Migration*.php
└── Resources/
    └── config/
        └── services.xml
```

**Conventions:**
- Domain logic in bundles, NOT in templates or controllers
- Expose services via dependency injection
- `composer.json` type: `shopware-bundle`
- Align namespaces with the bundle name
- Encapsulate integration points (events, DAL extensions) behind service classes

---

## Plugin structure (static/custom + managed/store)

### Required directory structure

```
MyPlugin/
├── composer.json
├── src/
│   ├── MyPlugin.php              # plugin class (extends Plugin)
│   ├── Migration/
│   │   └── V6_7/
│   │       └── Migration*.php
│   ├── Resources/
│   │   ├── config/
│   │   │   ├── services.xml
│   │   │   └── config.xml       # plugin configuration
│   │   ├── views/               # Twig templates (overrides)
│   │   ├── storefront/          # storefront JS/SCSS assets
│   │   └── administration/      # admin modules (if any)
│   └── [Domain]/               # domain-specific classes
└── tests/
```

### Rules

- Use the standard plugin skeleton — no custom autoloaders or custom entry points
- Keep configuration, migrations, administration and storefront assets in the default folders
- No cross-wiring between plugins
- DB schema changes exclusively via migrations; install/update code must be idempotent
- For store plugins: no project assumptions (host names, queues, cron timing, file access); document requirements and provide safe fallbacks

### Required composer.json fields

```json
{
  "type": "shopware-platform-plugin",
  "extra": {
    "shopware-plugin-class": "MyVendor\\MyPlugin\\MyPlugin",
    "label": {
      "de-DE": "Mein Plugin",
      "en-GB": "My Plugin"
    }
  }
}
```

---

## App structure

Apps implement logic on an external server; Shopware communicates via webhooks/HTTP.

```
my-app/
├── manifest.xml           # app manifest (required)
├── Resources/
│   ├── views/             # Twig templates (admin modules)
│   └── app/
│       └── storefront/
│           └── src/       # storefront overrides
└── src/
    └── (app backend code — hosted separately)
```

**Rules:**
- Keep the manifest minimal and explicit: document permissions, webhooks and actions exactly
- Separate the app backend (API/webhook handlers) from UI assets
- No stateful coupling to the shop runtime; design for multi-tenancy
- Direct PHP extensions are not possible (no schema changes via DB migrations)

---

## Upgrade-oriented structure

The less surface area you expose to the platform core, the less upgrade effort you incur.

**Dos:**
- Isolate integration points (events, decorators, DAL extensions) behind service classes
- Keep related logic in one repository
- Consistent tooling across the whole repository
- Minimal cross-plugin dependencies

**Don'ts:**
- Split related logic across several independent plugins
- Direct dependencies on other plugins (without clear API contracts)
- Extend core classes without the decoration pattern

---

## MCP server extendability

Both plugins and apps can add their own tools, prompts and resources to the Shopware built-in MCP server:

- Plugins: `guides/plugins/plugins/mcp-server.md`
- Apps: `guides/plugins/apps/mcp-server.md`

---

## References

- `guides/development/extensions/code-structure.md`
- `guides/development/extensions/index.md`
- Plugin Base Guide: `guides/plugins/plugins/plugin-base-guide.md`
- Bundle Guide: `guides/plugins/plugins/bundle.md`
- App Base Guide: `guides/plugins/apps/app-base-guide.md`
- Theme Base Guide: `guides/plugins/themes/theme-base-guide.md`
