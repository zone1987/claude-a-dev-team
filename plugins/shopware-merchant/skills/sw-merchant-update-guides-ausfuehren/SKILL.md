---
name: sw-merchant-update-guides-ausfuehren
description: >
  Shopware 6 Update ausführen — alle Methoden: Update per Admin-Panel (Einstellungen > System >
  Shopware-Update), Update per Browser-Installer (shopware-installer.phar.php), Update per
  Composer + CLI (system:update:prepare, system:update:finish). Wartungsmodus aktivieren
  (sales-channel:maintenance:enable), Erweiterungen deaktivieren, Troubleshooting wenn
  Extensions nicht deaktivierbar (SQL), Rollback-Prozess. Trigger: "Shopware Update per Admin",
  "Shopware per Composer updaten", "system:update:prepare", "Wartungsmodus Shopware aktivieren",
  "Extensions vor Update deaktivieren", "Update schlägt fehl Shopware", "Shopware Update
  Troubleshooting", "shopware-installer.phar.php", "Rollback nach Shopware Update",
  "Shopware Update CLI Befehle". Shopware 6.5–6.7.
---

# Shopware 6 — Update ausführen (alle Methoden)

Destilliert aus `docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten`.

## Update-Methoden im Überblick

| Methode | Geeignet für | Risiko Timeout |
|---|---|---|
| Admin-Panel | Standard-Hosting, kleine Shops | Möglich |
| Browser-Installer | Shared Hosting, kein SSH | Gering |
| Composer + CLI | Professionell, CI/CD | Kein |

## Composer + CLI (Kurzfassung)

```bash
bin/console sales-channel:maintenance:enable --all
bin/console system:update:prepare
# composer.json: Version anpassen
composer update --no-scripts
composer recipes:update
bin/console system:update:finish
bin/console theme:compile
bin/console cache:clear
bin/console sales-channel:maintenance:disable --all
```

## Troubleshooting: Extensions nicht deaktivierbar

```sql
-- Alle Plugins deaktivieren (Major-Update)
UPDATE plugin SET active = 0;
```

Vollständige Anleitungen (alle Methoden, Rollback, Wartungsmodus, SQL-Troubleshooting):
→ `references/deep/update-methoden.md`

Screenshots (Admin-Prozess): `assets/`

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten*
