# Shopware 6 — Watchers & Hot Module Replacement (vollständige Referenz)

Quelle: `guides/development/tooling/using-watchers.md`

## Überblick

Bei der Entwicklung mit Shopware erfordern JavaScript-Änderungen normalerweise Build-Befehle für Administration oder Storefront. HMR (Hot Module Replacement) ermöglicht es, Änderungen automatisch zu laden und vorauszuschauen.

**Wichtig**: HMR-Watcher ersetzen nicht den finalen Build-Prozess nach Abschluss der Entwicklung.

## JS/CSS bauen (regulärer Build)

### Source Code (composer run)

```bash
# Administration:
composer run build:js:admin

# Storefront:
composer run build:js:storefront
```

### Production Template (shopware-cli)

```bash
# Administration:
shopware-cli project admin-build

# Storefront:
shopware-cli project storefront-build
```

## Hot Module Replacement aktivieren

### Source Code (Shopware Source Code-Repository)

```bash
# Administration:
composer run watch:admin

# Storefront (ab Shopware 6.7.11.0):
composer run storefront:dev-server

# Storefront (vor Shopware 6.7.11.0):
composer run watch:storefront
```

### Production Template (shopware-cli)

```bash
# Administration:
shopware-cli project admin-watch

# Storefront:
shopware-cli project storefront-watch
```

## Umgebungsvariablen

Umgebungsvariablen beeinflussen Shopware und damit auch die Watcher. Unix-Präfix-Syntax setzt die Variable nur für diesen Befehl.

### APP_ENV

```bash
# Production Mode (kein Symfony-Toolbar, keine Debug-Features):
APP_ENV=prod composer run watch:storefront

# Development Mode (Standard):
# composer run watch:storefront  (APP_ENV=dev ist Default)
```

- `APP_ENV=dev`: Development Mode — Symfony Toolbar im Storefront, bessere Fehlermeldungen, Query-Logging
- `APP_ENV=prod`: Production Mode — keine Debug-Tools, Caching aktiv

### IPV4FIRST

Ab NodeJS v17.0.0 wird IPv6 gegenüber IPv4 bevorzugt. In manchen Setups kann IPv6 bei Watchern Probleme verursachen.

```bash
# IPv4 erzwingen (NodeJS v17+):
IPV4FIRST=1 composer run watch:storefront
IPV4FIRST=1 composer run watch:admin
```

## Hinweise

1. Watcher eignen sich für **aktive Entwicklung** — schnelleres Feedback
2. **Finaler Build** ist trotzdem nötig vor Deployment oder Plugin-Packaging
3. Bei `APP_ENV=dev` werden mehr Ressourcen verbraucht
4. Watcher-Prozesse laufen im Vordergrund — für Hintergrundausführung: `&` oder separate Terminals
