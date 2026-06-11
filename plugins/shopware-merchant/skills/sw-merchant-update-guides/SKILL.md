---
name: sw-merchant-update-guides
description: >
  Shopware 6 Shop aktualisieren — Betreibersicht: Update-Prozess planen, Backup erstellen,
  Testumgebung aufsetzen, Erweiterungs-Kompatibilität prüfen, Update per Admin/Browser/CLI,
  Wartungsmodus, Rollback, Troubleshooting. Versionsspezifische Hinweise 6.4→6.5, 6.5→6.6,
  6.6, 6.7. Trigger: "Shopware updaten", "Shopware aktualisieren", "Update Shopware 6",
  "wie update ich Shopware", "Shopware neue Version einspielen", "Update Guide Shopware",
  "Shopware 6.7 update", "Shopware 6.6 update", "Update Voraussetzungen Shopware",
  "Backup vor Shopware Update", "Erweiterungen vor Update prüfen". Shopware 6.4–6.7.
---

# Shopware 6 — Update Guides (Betreiber-Überblick)

Destilliert aus `docs.shopware.com/de/shopware-6-de/update-guides`. Betreibersicht: Shop aktualisieren — nicht Code-Migration für Entwickler.

## Überblick: Update-Prozess in Kurzform

1. **Testumgebung anlegen** — Update nie direkt auf Live testen
2. **Backup erstellen** — Pflicht; Shopware erstellt kein Auto-Backup
3. **Erweiterungen prüfen** — Kompatibilität im Shopware Store / Admin prüfen
4. **Update durchführen** — via Admin-Panel, Browser-Installer oder Composer/CLI
5. **Erweiterungen reaktivieren** — nach Update aktualisieren und wieder einschalten

> **Warnung:** Starte ein Update nur, wenn du über entsprechende Erfahrung verfügst oder kontaktiere deine Partneragentur.

## Update-Methoden

| Methode | Geeignet für | Vorteil |
|---|---|---|
| Admin-Panel | Standard-Hosting, einfache Shops | Keine Shell nötig |
| Browser-Installer (PHP-Datei) | Shared Hosting, kein SSH | Leichtgewichtig |
| Composer + CLI | Professionell, CI/CD | Stabiler, keine Timeouts |

## Versionsspezifische Guides

| Migration | Besonderheit |
|---|---|
| 6.4 → 6.5 | Alle Extensions deaktivieren (Pflicht), PHP 8.1+, Node 18 |
| 6.5 → 6.6 | Alle Extensions deaktivieren, PHP 8.2, Node 20, MariaDB 10.11+ |
| 6.5/6.6 → 6.6 | Neues Vue 3-System, Webpack 5 + SWC |
| 6.6 → 6.7 | Vite statt Webpack, Vue 3 ohne Compat-Mode, PHPUnit 11 |

## Detailwissen je Thema

| Thema | Skill |
|---|---|
| Update-Prozess (Admin, CLI, Browser, Troubleshooting) | `sw-merchant-update-guides-ausfuehren` |
| Versionsspezifische Update-Hinweise (6.4→6.7) | `sw-merchant-update-guides-versionen` |
| Testumgebung & Staging-Instanz | `sw-merchant-update-guides-staging` |

## Referenz-Dokumente in diesem Skill

| Dokument | Inhalt |
|---|---|
| `references/deep/ueberblick.md` | Systemanforderungen aller Versionen, Prozess-Überblick |
| `references/deep/backup-und-vorbereitung.md` | Backup-Methoden, Checklisten, Screenshots |

Screenshots: `assets/` (Admin-Panel-Schritte)

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/update-guides*
