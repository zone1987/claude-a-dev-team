# Shopware IDE tools (complete reference)

Source: `guides/development/tooling/shopware-toolbox.md`, `guides/development/tooling/index.md`

## PHPStorm: Shopware 6 Toolbox

Plugin URL: https://plugins.jetbrains.com/plugin/17632-shopware-6-toolbox

Shopware Toolbox is not a standalone tool — it runs inside PHPStorm (and other JetBrains IDEs) and provides Shopware-specific development helpers.

### Installation

1. Open PHPStorm
2. Settings → Plugins
3. Search for "Shopware 6 Toolbox"
4. Install → restart the IDE

### Live templates

Ready-made code snippets for common Shopware patterns.

Access: `Cmd/Ctrl + J` → list of all available live templates

### Code generators

- **Vue.js admin component**: scaffold for new admin components
- **config.xml**: plugin configuration file template
- **Extend storefront blocks**: automatic file creation for block overrides
- **Vue modules**: admin module scaffold
- **Scheduled task**: task class + service definition
- **Changelog**: changelog file following the Shopware standard

### Static code checks

**Inspection**: reports an error when an abstract class is used incorrectly in the constructor (Shopware coding guideline).

### Auto-completion

| Area | What gets completed |
|---|---|
| Admin components | All registered admin components |
| Administration snippets | Snippet keys of the administration |
| Storefront snippets | Snippet keys of the storefront |
| Storefront functions | `theme_config`, `config`, `seoUrl`, `sw_include`, `sw_extends` |
| Repository | `this.repositoryFactory.create` with entity names |
| Module labels | `Module.register` label keys |
| Context-aware | Admin component completion (only when a Twig file sits next to `index.js`) |
| Feature flags | All registered feature flags |

## VS Code extension

Marketplace: https://marketplace.visualstudio.com/items?itemName=shopware.shopware-lsp

Shopware Language Server Protocol (LSP) extension for VS Code:
- Shopware-specific auto-completion
- Code diagnostics
- Navigation in Shopware projects

## Further development tools

From `guides/development/tooling/index.md`:

### Admin Extension SDK

NPM library for Shopware 6 apps and plugins that extend or customize the administration:
https://developer.shopware.com/resources/admin-extension-sdk/

### `bin/console`

Shopware's built-in CLI for:
- Installing/activating plugins
- Database migrations
- Clearing caches
- Running scheduled tasks
- Inspecting the system status

Command reference: Commands Reference

### Deployment Helper

Supports database and maintenance operations for deployments (migrations, cache handling).

### Shopware CLI

The central command-line tool for Shopware projects and extensions:
- Scaffolding
- Builds
- Validation
- Packaging
- Store interaction
- CI support
- Watchers and formatters

### MCP Server

Native Model Context Protocol server for AI clients (Claude Desktop, Cursor, Claude Code):
- Tools, resources and prompts for shop interaction
- Extensible via plugins and apps
