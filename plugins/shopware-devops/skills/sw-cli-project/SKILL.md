---
name: sw-cli-project
description: >
  shopware-cli project * — alle Projekt-Subcommands: create, ci, admin-build,
  storefront-build, admin-watch, storefront-watch, console, dump, worker, doctor,
  extension lifecycle, autofix, config, generate-jwt, image-proxy, validate.
  Trigger: "shopware-cli project", "project ci", "project create flags",
  "project dump", "project worker", "project admin-build", "project console",
  "project extension list", "project autofix flex", "project generate-jwt".
---

# shopware-cli project

Commands für das gesamte Shopware-Projekt-Management.

```bash
shopware-cli project create my-shop --version latest --deployment shopware-paas
shopware-cli project ci .                    # CI-Build-Pipeline
shopware-cli project admin-build .           # Admin-Assets bauen
shopware-cli project storefront-build .      # Storefront + theme:compile
shopware-cli project worker 2                # 2 Messenger-Consumer starten
shopware-cli project dump --clean --anonymize
```

## Command-Übersicht

| Command | Kurzfassung |
|---------|-------------|
| `create` | Neues Shopware-Projekt anlegen (interaktiv oder mit Flags) |
| `ci` | Vollständige CI-Pipeline (composer + Assets + Cache + Checksums) |
| `admin-build` | Admin-JS/CSS für alle Extensions bauen |
| `storefront-build` | Storefront-Assets + `theme:compile` |
| `admin-watch` | Admin webpack Dev-Server starten |
| `storefront-watch` | Storefront webpack Hot-Proxy starten |
| `console` | `bin/console`-Passthrough mit Tab-Completion |
| `dump` | MySQL-Dump (parallel, anonymize, gzip/zstd) |
| `worker` | Messenger-Consumer (restart on failure, SIGTERM-safe) |
| `doctor` | Projekt auf Probleme prüfen |
| `validate` | Gesamtes Projekt validieren |
| `fix` | Code-Fixer auf Projekt ausführen |
| `format` | Formatter auf Projekt ausführen |
| `generate-jwt` | RSA-Schlüsselpaar für JWT generieren |
| `image-proxy` | Lokaler Image-Proxy mit Upstream-Fallback |
| `admin-api` | Authenticated Admin-REST-API-Wrapper |
| `clear-cache` | Cache leeren (API oder lokal) |
| `upgrade-check` | Extension-Kompatibilität mit neuer SW-Version prüfen |
| `config init` | `.shopware-project.yml` interaktiv erstellen |
| `config-schema` | JSON-Schema für `.shopware-project.yml` |
| `extension *` | Extension Lifecycle via Admin API (list/install/activate/...) |
| `autofix composer-plugins` | Plugins zu Composer migrieren |
| `autofix flex` | Zu Symfony-Flex migrieren |

## Vertiefung

- [references/deep/project-commands.md](references/deep/project-commands.md) — Alle Flags, Beispiele, Edge-Cases
