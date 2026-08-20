# Shopware 6 — Update guides (merchant overview)

Distilled from `docs.shopware.com/de/shopware-6-de/update-guides`. Merchant perspective: updating the shop — not code migration for developers.

## Overview: the update process in brief

1. **Set up a test environment** — never test an update directly on live
2. **Create a backup** — mandatory; Shopware does not create an automatic backup
3. **Check extensions** — verify compatibility in the Shopware Store / admin
4. **Run the update** — via admin panel, browser installer or Composer/CLI
5. **Reactivate extensions** — update them after the update and switch them back on

> **Warning:** Only start an update if you have the corresponding experience, or contact your partner agency.

## Update methods

| Method | Suitable for | Advantage |
|---|---|---|
| Admin panel | Standard hosting, simple shops | No shell required |
| Browser installer (PHP file) | Shared hosting, no SSH | Lightweight |
| Composer + CLI | Professional, CI/CD | More stable, no timeouts |

## Version-specific guides

| Migration | Particularity |
|---|---|
| 6.4 → 6.5 | Deactivate all extensions (mandatory), PHP 8.1+, Node 18 |
| 6.5 → 6.6 | Deactivate all extensions, PHP 8.2, Node 20, MariaDB 10.11+ |
| 6.5/6.6 → 6.6 | New Vue 3 system, Webpack 5 + SWC |
| 6.6 → 6.7 | Vite instead of Webpack, Vue 3 without compat mode, PHPUnit 11 |

## Detailed knowledge per topic

| Topic | Skill |
|---|---|
| Update process (admin, CLI, browser, troubleshooting) | `sw-merchant-update-guides-ausfuehren` |
| Version-specific update notes (6.4→6.7) | `sw-merchant-update-guides-versionen` |
| Test environment & staging instance | `sw-merchant-update-guides-staging` |

## Reference documents in this skill

| Document | Content |
|---|---|
| `GUIDES-UEBERBLICK.md` | System requirements of all versions, process overview |
| `GUIDES-BACKUP-UND-VORBEREITUNG.md` | Backup methods, checklists, screenshots |

Screenshots: `assets/` (admin panel steps)

---

*Source: https://docs.shopware.com/de/shopware-6-de/update-guides*
