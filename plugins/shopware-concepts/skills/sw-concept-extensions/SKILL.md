---
name: sw-concept-extensions
description: >
  Shopware Extensions: App vs. Plugin — Unterschiede, Einsatzgebiete, Cloud-Kompatibilität.
  Trigger: "App vs Plugin", "was ist ein App", "was ist ein Plugin", "Extensions Shopware",
  "shopware plugin concept", "shopware app concept", "wann App wann Plugin",
  "Cloud-kompatibel Shopware", "Shopware SaaS App", "Plugin Cloud", "Symfony Bundle Plugin",
  "App Manifest", "Webhooks Shopware App", "shopware extensibility", "wie erweitere ich Shopware".
---

# Shopware Extensions — App vs. Plugin

Vollständige Konzept-Doku: `references/deep/extensions.md`

## Kurzüberblick

### Apps

- **Außerhalb des Shopware-Prozesses** — eigener Server, eigene Technologie (kein PHP erforderlich)
- Kommunikation: HTTP-Webhooks (Shopware → App) + Admin API (App → Shopware)
- **Cloud-kompatibel** — funktioniert mit Self-hosted und Shopware SaaS
- Registrierung via `manifest.xml`
- Kann: Webhooks, Store-API-Erweiterungen, Storefront-Assets, App Scripts, Payment, Rule Conditions, CMS-Blöcke

### Plugins

- **Im Shopware-Prozess ausgeführt** — direkter Zugriff auf DI-Container, Datenbank, Events
- Basieren auf **Symfony Bundles** + Abstract Base Class
- **Nicht Cloud-kompatibel** — nur Self-hosted
- Maximale Erweiterbarkeit: neue User Provider, Custom Search Engine, etc.

### Entscheidungskriterien

| Kriterium | App | Plugin |
|---|---|---|
| Cloud-Hosting | Ja | Nein |
| Technologie-Freiheit | Ja (beliebig) | Nein (PHP) |
| Tiefer Zugriff auf Shopware-Internals | Eingeschränkt | Vollständig |
| Sicherheitssensitivität | Hoch | Niedriger |

Technische Umsetzung: `shopware-apps` (Apps), `shopware-core` (Plugins) — Dev-Plugins
