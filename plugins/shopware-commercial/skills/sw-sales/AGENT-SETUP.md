# Sales Agent — Installation & Setup

Vollständige Referenz: [AGENT-SETUP-SETUP.md](AGENT-SETUP-SETUP.md)

## Schnellstart

```bash
git clone https://github.com/shopware/swagsalesagent.git
cd swagsalesagent
cp .env.template .env
# .env befüllen (MySQL, Redis, APP_NAME, APP_SECRET, ...)
pnpm install --frozen-lockfile --prefer-offline
pnpm db:migration:deploy   # Datenbank migrieren
pnpm dev                    # Entwicklung
# oder:
pnpm build                  # Produktion
```

## Mit Shopware verbinden

```bash
pnpm app:build  # ZIP erstellen
# ZIP unter bundle/swagsalesagent.zip in Shopware Extensions hochladen
```
