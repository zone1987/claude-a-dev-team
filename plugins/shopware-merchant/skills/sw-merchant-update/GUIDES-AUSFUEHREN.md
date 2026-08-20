# Shopware 6 — Running the update (all methods)

Distilled from `docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten`.

## Update methods at a glance

| Method | Suitable for | Timeout risk |
|---|---|---|
| Admin panel | Standard hosting, small shops | Possible |
| Browser installer | Shared hosting, no SSH | Low |
| Composer + CLI | Professional, CI/CD | None |

## Composer + CLI (short version)

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

## Troubleshooting: extensions cannot be deactivated

```sql
-- Alle Plugins deaktivieren (Major-Update)
UPDATE plugin SET active = 0;
```

Complete instructions (all methods, rollback, maintenance mode, SQL troubleshooting):
→ `GUIDES-AUSFUEHREN-METHODEN.md`

Screenshots (admin process): `assets/`

---

*Source: https://docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten*
