# Shopware IDE-Tools

## PHPStorm: Shopware 6 Toolbox

JetBrains Marketplace: https://plugins.jetbrains.com/plugin/17632-shopware-6-toolbox

### Installation

PHPStorm → Settings → Plugins → "Shopware 6 Toolbox" suchen → Install → Restart

### Features

**Live Templates** (Cmd/Ctrl + J): Vorgefertigte Code-Snippets für häufige Shopware-Konstrukte.

**Code-Generatoren:**
- Vue.js Admin-Komponenten
- `config.xml`-Gerüste
- Storefront-Block-Erweiterungen (inkl. automatische Datei-Erstellung)
- Vue-Module
- Scheduled Tasks
- Changelogs

**Static Code Checks:**
- Inspection: Warnung bei falsch verwendeten abstrakten Klassen im Constructor (Guideline Check)

**Auto-Completion:**
- Admin-Komponenten
- Snippets in Administration und Storefront
- Storefront-Funktionen: `theme_config`, `config`, `seoUrl`, `sw_include`, `sw_extends`
- Repository via `this.repositoryFactory.create`
- `Module.register`-Labels
- Context-aware Admin-Komponenten (Twig-Datei neben `index.js`)
- Feature Flags

## VS Code Extension

Marketplace: https://marketplace.visualstudio.com/items?itemName=shopware.shopware-lsp

Language Server Protocol (LSP) für Shopware-spezifische Auto-Completion und Diagnosen in VS Code.
