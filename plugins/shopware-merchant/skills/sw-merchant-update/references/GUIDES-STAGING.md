# Shopware 6 — Test environment & staging instance

Distilled from `developer.shopware.com/docs/guides/hosting/installation-updates/creating-a-staging-instance.html`.

## Staging mode vs. staging environment

| Term | Meaning |
|---|---|
| Staging environment | Separate server instance with its own hosting, domain, DB |
| Staging mode | Shopware mechanism since 6.6.1.0 (`system:setup:staging`) |

## Staging instance in 4 steps

1. **Set up a separate installation** — own domain/subdomain, adjust APP_URL
2. **Clone the database** — mysqldump or shopware-cli (anonymisation possible)
3. **Configure staging** — adjust .env, set the Elasticsearch prefix
4. **Activate staging mode** — `bin/console system:setup:staging`

## What staging mode does

- Deletes apps with external connections (no production data leaks)
- Disables e-mail sending
- Rewrites URLs to the staging domain
- Shows a banner in the admin and the storefront
- Verifies Elasticsearch indexes (no conflicts with live)

## Important commands

```bash
# Datenbank klonen (mit Anonymisierung)
shopware-cli project dump --clean --anonymize --output shop.sql shopware

# Staging-Modus aktivieren
bin/console system:setup:staging

# Nicht-interaktiv
bin/console system:setup:staging --no-interaction --force
```

Deep reference knowledge: `GUIDES-STAGING-STAGING.md`

---

*Source: https://developer.shopware.com/docs/guides/hosting/installation-updates/creating-a-staging-instance.html*
