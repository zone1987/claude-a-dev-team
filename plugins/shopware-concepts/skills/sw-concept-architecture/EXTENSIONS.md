# Shopware Extensions — App vs. Plugin

Vollständige Konzept-Doku: `EXTENSIONS-DETAIL.md`

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
