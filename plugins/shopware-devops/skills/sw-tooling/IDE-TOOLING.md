# Shopware IDE-Tools (vollständige Referenz)

Quelle: `guides/development/tooling/shopware-toolbox.md`, `guides/development/tooling/index.md`

## PHPStorm: Shopware 6 Toolbox

Plugin URL: https://plugins.jetbrains.com/plugin/17632-shopware-6-toolbox

Shopware Toolbox ist kein eigenständiges Tool — es läuft innerhalb von PHPStorm (und anderen JetBrains IDEs) und bietet Shopware-spezifische Entwicklungshelfer.

### Installation

1. PHPStorm öffnen
2. Settings → Plugins
3. "Shopware 6 Toolbox" suchen
4. Install → IDE neu starten

### Live Templates

Vorgefertigte Code-Snippets für häufige Shopware-Muster.

Zugriff: `Cmd/Ctrl + J` → Liste aller verfügbaren Live Templates

### Code-Generatoren

- **Vue.js Admin-Komponente**: Gerüst für neue Admin-Komponenten
- **config.xml**: Plugin-Konfigurationsdatei-Vorlage
- **Storefront-Blöcke erweitern**: Automatische Datei-Erstellung für Block-Overrides
- **Vue-Module**: Admin-Modul-Gerüst
- **Scheduled Task**: Task-Klasse + Service-Definition
- **Changelog**: Changelog-Datei nach Shopware-Standard

### Static Code Checks

**Inspection**: Zeigt Fehler an, wenn eine abstrakte Klasse falsch im Constructor verwendet wird (Shopware Coding Guideline).

### Auto-Completion

| Bereich | Was wird vervollständigt |
|---|---|
| Admin-Komponenten | Alle registrierten Admin-Komponenten |
| Snippets Administration | Snippet-Keys der Administration |
| Snippets Storefront | Snippet-Keys des Storefronts |
| Storefront-Funktionen | `theme_config`, `config`, `seoUrl`, `sw_include`, `sw_extends` |
| Repository | `this.repositoryFactory.create` mit Entity-Namen |
| Module-Labels | `Module.register`-Label-Keys |
| Context-aware | Admin-Komponenten-Completion (nur wenn Twig-Datei neben `index.js`) |
| Feature Flags | Alle registrierten Feature Flags |

## VS Code Extension

Marketplace: https://marketplace.visualstudio.com/items?itemName=shopware.shopware-lsp

Shopware Language Server Protocol (LSP) Extension für VS Code:
- Shopware-spezifische Auto-Completion
- Code-Diagnosen
- Navigation in Shopware-Projekten

## Weitere Entwicklungstools

Aus `guides/development/tooling/index.md`:

### Admin Extension SDK

NPM-Bibliothek für Shopware 6 Apps und Plugins, die die Administration erweitern oder anpassen:
https://developer.shopware.com/resources/admin-extension-sdk/

### `bin/console`

Shopware's built-in CLI für:
- Plugins installieren/aktivieren
- Datenbank-Migrationen
- Caches leeren
- Scheduled Tasks ausführen
- System-Status inspizieren

Befehlsreferenz: Commands Reference

### Deployment Helper

Unterstützt Datenbank- und Wartungsoperationen für Deployments (Migrationen, Cache-Handling).

### Shopware CLI

Das zentrale Command-Line-Tool für Shopware-Projekte und -Erweiterungen:
- Scaffolding
- Builds
- Validierung
- Packaging
- Store-Interaktion
- CI-Support
- Watcher und Formatter

### MCP Server

Nativer Model Context Protocol Server für AI-Clients (Claude Desktop, Cursor, Claude Code):
- Tools, Resources und Prompts für Shop-Interaktion
- Erweiterbar via Plugins und Apps
