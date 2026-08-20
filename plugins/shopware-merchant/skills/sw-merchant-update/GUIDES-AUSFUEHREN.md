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
→ `GUIDES-AUSFUEHREN-METHODEN.md`

Screenshots (Admin-Prozess): `assets/`

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten*
