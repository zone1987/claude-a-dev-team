---
name: sw-cli-extension
description: >
  shopware-cli extension * — alle Extension-Subcommands: build, validate, zip,
  watch, fix, format, get-version, get-name, prepare, changelog, config-schema.
  Trigger: "shopware-cli extension", "extension build", "extension zip flags",
  "extension validate --full", "extension watch", "sw-cli extension upload",
  "extension get-version", "extension prepare", "extension fix".
---

# shopware-cli extension

Commands zum Bauen, Validieren und Paketieren von Shopware Extensions.

```bash
shopware-cli extension build path/to/MyPlugin
shopware-cli extension validate --full path/to/MyPlugin
shopware-cli extension zip path/to/MyPlugin --disable-git
shopware-cli extension admin-watch path/to/MyPlugin http://localhost
```

## Command-Übersicht

| Command | Kurzfassung |
|---------|-------------|
| `build` | Admin/Storefront-Assets bauen (ESBuild/Webpack) |
| `validate` | Extension prüfen (schnell oder `--full` mit PHPStan/ESLint) |
| `zip` | Release-Zip erstellen (git-export oder `--disable-git`) |
| `admin-watch` | ESBuild Dev-Proxy starten |
| `fix` | Code-Fixer ausführen (PHPCSFixer, ESLint) |
| `format` | Formatter ausführen (Prettier, PHP-CS-Fixer) |
| `get-name` | Technical Name ausgeben |
| `get-version` | Version ausgeben |
| `get-changelog` | Changelog ausgeben |
| `prepare` | Composer-Deps installieren, Clean-up vor Zip |
| `config-schema` | JSON-Schema für `.shopware-extension.yml` |

## Vertiefung

- [references/deep/extension-commands.md](references/deep/extension-commands.md) — Alle Flags, Beispiele, Edge-Cases
