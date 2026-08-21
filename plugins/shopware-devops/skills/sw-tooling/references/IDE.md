# Shopware IDE tools

## PHPStorm: Shopware 6 Toolbox

JetBrains Marketplace: https://plugins.jetbrains.com/plugin/17632-shopware-6-toolbox

### Installation

PHPStorm → Settings → Plugins → search for "Shopware 6 Toolbox" → Install → Restart

### Features

**Live templates** (Cmd/Ctrl + J): ready-made code snippets for common Shopware constructs.

**Code generators:**
- Vue.js admin components
- `config.xml` scaffolds
- Storefront block extensions (including automatic file creation)
- Vue modules
- Scheduled tasks
- Changelogs

**Static code checks:**
- Inspection: warning about abstract classes used incorrectly in the constructor (guideline check)

**Auto-completion:**
- Admin components
- Snippets in administration and storefront
- Storefront functions: `theme_config`, `config`, `seoUrl`, `sw_include`, `sw_extends`
- Repository via `this.repositoryFactory.create`
- `Module.register` labels
- Context-aware admin components (Twig file next to `index.js`)
- Feature flags

## VS Code extension

Marketplace: https://marketplace.visualstudio.com/items?itemName=shopware.shopware-lsp

Language Server Protocol (LSP) for Shopware-specific auto-completion and diagnostics in VS Code.
