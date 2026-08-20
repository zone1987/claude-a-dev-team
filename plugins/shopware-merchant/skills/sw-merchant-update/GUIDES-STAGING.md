# Shopware 6 — Testumgebung & Staging-Instanz

Destilliert aus `developer.shopware.com/docs/guides/hosting/installation-updates/creating-a-staging-instance.html`.

## Staging-Modus vs. Staging-Umgebung

| Begriff | Bedeutung |
|---|---|
| Staging-Umgebung | Separate Server-Instanz mit eigenem Hosting, Domain, DB |
| Staging-Modus | Shopware-Mechanismus seit 6.6.1.0 (`system:setup:staging`) |

## Staging-Instanz in 4 Schritten

1. **Separate Installation einrichten** — eigene Domain/Subdomain, APP_URL anpassen
2. **Datenbank klonen** — mysqldump oder shopware-cli (mit Anonymisierung möglich)
3. **Staging konfigurieren** — .env anpassen, Elasticsearch-Prefix setzen
4. **Staging-Modus aktivieren** — `bin/console system:setup:staging`

## Was der Staging-Modus tut

- Löscht Apps mit externen Verbindungen (keine Produktions-Datenlecks)
- Deaktiviert E-Mail-Versand
- Schreibt URLs zur Staging-Domain um
- Zeigt Banner in Admin und Storefront
- Verifiziert Elasticsearch-Indizes (keine Konflikte mit Live)

## Wichtige Befehle

```bash
# Datenbank klonen (mit Anonymisierung)
shopware-cli project dump --clean --anonymize --output shop.sql shopware

# Staging-Modus aktivieren
bin/console system:setup:staging

# Nicht-interaktiv
bin/console system:setup:staging --no-interaction --force
```

Tiefes Referenzwissen: `GUIDES-STAGING-STAGING.md`

---

*Quelle: https://developer.shopware.com/docs/guides/hosting/installation-updates/creating-a-staging-instance.html*
