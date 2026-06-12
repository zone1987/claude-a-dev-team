---
name: sw-paas-environments
description: >
  Shopware PaaS Native Umgebungen und Application-Management: Cloning,
  Shopware-Update, Domain-Verwaltung, exec vs. command, Snapshot erstellen.
  Trigger: "paas application klonen", "paas staging clone", "paas shopware
  update", "sw-paas application clone", "paas umgebung kopieren", "paas
  snapshot", "sw-paas exec", "sw-paas command", "paas deployment rollback",
  "paas custom domain", "paas domain konfigurieren".
---

# Shopware PaaS Native — Umgebungen & Applications

## Application Cloning

```bash
sw-paas application clone            # Interaktiv

# Manuell
sw-paas application clone \
  --organization-id <org-id> \
  --project-id <source-project-id> \
  --application-id <source-app-id> \
  --target-application-id <target-app-id> \
  --target-project-id <target-project-id>
```

**Voraussetzung:** Letztes Deployment muss `DEPLOYING_STORE_SUCCESS` sein.

Nach Clone:
1. Admin-Passwort ändern (`sw-paas open admin`)
2. OpenSearch reindexieren: `bin/console dal:refresh:index --use-queue`
3. Domain in Sales Channel aktualisieren

## Shopware-Version aktualisieren

```bash
# 1. Snapshot erstellen
sw-paas snapshot create

# 2. Neue Branch, composer.json updaten
git checkout -b update-shopware
# shopware/core Version anpassen
composer update --no-scripts
composer recipes:update
git add . && git commit -m "Update Shopware X.Y.Z"
git push

# 3. Vorbereitung im laufenden System
sw-paas exec --new
bin/console system:update:prepare

# 4. Deployment
sw-paas application update

# 5. Abschluss
sw-paas exec --new
bin/console system:update:finish
```

## exec vs. command

| | `exec` | `command` |
|---|---|---|
| Container | Existierender | Neuer |
| Modus | Interaktiv | Nicht-interaktiv |
| Use Case | Debugging, Wartung | CI/CD, Automatisierung |
| TTL | Session | 1 Stunde |

```bash
sw-paas exec --new           # Interaktive Shell
sw-paas command create       # Einmaligen Befehl ausführen
```

## Vertiefung

[references/deep/environments.md](references/deep/environments.md)
