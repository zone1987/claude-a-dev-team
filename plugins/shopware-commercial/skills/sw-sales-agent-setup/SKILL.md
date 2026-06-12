---
name: sw-sales-agent-setup
description: >
  Installation und lokales Setup der Sales-Agent-App: Repository klonen,
  .env konfigurieren, Datenbank migrieren, App-Bundle für Shopware bauen.
  Triggers: "sales agent installieren", "install sales agent", "swagsalesagent setup",
  "pnpm db:migration sales agent", "app:build sales agent", "sales agent local setup",
  "sales agent env", "sales agent mysql prisma", "sales agent vitest"
---

# Sales Agent — Installation & Setup

Vollständige Referenz: [references/deep/setup.md](references/deep/setup.md)

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
