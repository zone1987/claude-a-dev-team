# Shopware extensions — complete concept documentation

Sources: `concepts/extensions/index.md`, `apps-concept.md`, `plugins-concept.md`

---

## Contents

- [Extensions overview (index.md)](#extensions-overview-indexmd)
- [Apps (apps-concept.md)](#apps-apps-conceptmd)
- [Plugins (plugins-concept.md)](#plugins-plugins-conceptmd)

## Extensions overview (index.md)

The Shopware core is designed so that extensibility is possible without impairing maintainability
or structural integrity.

**Two extension types:**

| | Apps | Plugins |
|---|---|---|
| Execution | Outside the Shopware process | Inside the Shopware process |
| Communication | HTTP webhooks + Admin API | Direct code access |
| Cloud-compatible | Yes (SaaS + self-hosted) | **No** (self-hosted only) |
| Technology | Any | PHP (Symfony bundle) |

---

## Apps (apps-concept.md)

### Design goal: decoupling

The app system is decoupled from Shopware itself — two advantages:

1. **Freedom of technology** — only the HTTP interface has to be understood; no Shopware internals needed. Any language/framework for the app backend server.
2. **Cloud-compatible** — works with multi-tenant cloud systems (Shopware SaaS).

### The central interface: manifest (`manifest.xml`)

- Connects Shopware and the app
- Defines the app's features and how Shopware connects to it
- Must be shipped with every app

### Communication

**Shopware → app**: HTTP POST to defined endpoints (webhooks); the app reacts to events
**App → Shopware**: Admin REST API for data access and modification

On installation: **registration handshake** — Shopware verifies the app server, the app receives API credentials.

### App capabilities

#### Adapt the storefront appearance

- Ship Twig templates, JavaScript, SCSS, snippets
- Shopware rebuilds the storefront automatically on app installation
- No need to serve them from an external server

#### Integrate payment providers (from 6.4.1.0)

- **Synchronous payments** — no user interaction; background request for approval
- **Asynchronous payments** — user redirect; the app supplies the redirect URL; after the return: Shopware verifies the status with the app

#### App scripts (from 6.4.8.0)

- Execute custom business logic **inside the Shopware execution stack**
- Use cases: load additional data for the storefront, manipulate the cart
- Twig-based (safe, no direct PHP calls)

#### Rule builder conditions (from 6.4.12.0)

- Add custom conditions for the rule builder
- Declare them via `manifest.xml`

---

## Plugins (plugins-concept.md)

### Concept

Plugins are **Symfony bundle extensions** — they build on Symfony bundles and extend them.

Bundles/plugins can provide:
- Assets (templates, CSS, JS)
- Controllers
- Services (DI container)
- Tests

### Base class

An abstract base class (`PluginBaseClass`) with helper methods:
- Initialise plugin name and root path in the DI container
- Helpers for the lifecycle (install, update, uninstall, activate, deactivate)

Every plugin = a Composer package (can define dependencies).

### Deep access

Plugins can do almost anything:
- Custom user provider
- Custom search engine
- Override or decorate any Symfony services

### Cloud incompatibility

**Important**: because of their direct process and database access, plugins are **not** compatible
with Shopware Cloud. For cloud: use the app system.
