# Shopware PaaS Native — Umgebungen & Applications (Deep Reference)

Quellen: `products/paas/shopware/guides/clone-application.md`,
`products/paas/shopware/guides/update-shopware.md`,
`products/paas/shopware/fundamentals/applications.md`,
`products/paas/shopware/faq.md`, `products/paas/shopware/known-issues.md`

---

## Application Cloning

### Einsatzzwecke

- **Feature-Testing**: Clone ohne Auswirkung auf Original
- **Disaster Recovery**: Backups in andere Projekte
- **Dev-Umgebungen**: Produktionsdaten für realistischen Test

### Voraussetzungen

- Quelle und Ziel in derselben **Organisation** (kein cross-org cloning)
- Letztes Deployment der Quelle: Status `DEPLOYING_STORE_SUCCESS`
- Ziel-Application muss bereits existieren

```bash
# Status prüfen
sw-paas app deploy list
```

### Clone-Prozess

1. **Snapshot erstellen** der Quell-Application (DB + Filesystem)
2. **Snapshot wiederherstellen** auf Ziel-Application (überschreibt vorhandene Daten)

**Warnung:** Keine Anonymisierung der Daten! Vollständiger DB-Dump.

### Interaktiver Modus

```bash
sw-paas application clone
```

Auswahl:
1. Quell-Organization → Quell-Projekt → Quell-Application → Deployment
2. Ziel-Projekt → Ziel-Application

### Manueller Modus

```bash
sw-paas application clone \
  --organization-id <org-id> \
  --project-id <source-project-id> \
  --application-id <source-application-id> \
  --target-application-id <target-application-id> \
  --target-project-id <target-project-id>
```

### Fortschritt verfolgen

```bash
sw-paas app deploy list
sw-paas app deploy get
# Warten bis: DEPLOYING_STORE_SUCCESS
```

### Post-Clone Tasks

#### Admin-Passwort aktualisieren

App B hat identisches Passwort wie App A.

```bash
# App B Admin-Zugang mit App A Credentials öffnen
sw-paas open admin    # → App A auswählen für Credentials

# Im Shell von App B
sw-paas exec --new
bin/console user:change-password admin
```

Oder via Shopware-Admin-UI:
1. Login mit App-A-Credentials
2. Profil → Passwort-Sektion
3. Neues Passwort: App-B-Admin-Passwort (`sw-paas open admin` für App B)

#### OpenSearch Reindexieren (wenn aktiviert)

```bash
sw-paas exec --new
bin/console dal:refresh:index --use-queue
```

#### Domain in Sales Channel aktualisieren

1. Shopware-Admin der geklonten Application öffnen
2. Sales Channel → Domains
3. Domain auf neues `shopware.shop`-Subdomain oder Custom-Domain ändern

---

## Shopware aktualisieren

### Voraussetzung

Letztes Deployment muss `DEPLOYING_STORE_SUCCESS` sein:

```bash
sw-paas app deploy list
```

Bei `DEPLOYING_STORE_FAILED`: Erst Deployment-Problem beheben!

### Schritt 1: Snapshot erstellen (Empfehlung)

```bash
sw-paas snapshot create
# Warten bis Snapshot fertig ist
```

### Schritt 2: Code aktualisieren

```bash
git checkout -b my-update-branch

# composer.json: shopware/core Version anpassen
composer update --no-scripts
composer recipes:update
# ACHTUNG: Recipe-Updates sorgfältig prüfen — können Breaking Changes enthalten!

git add .
git commit -m "Update Shopware to X.Y.Z"
git push -u origin my-update-branch
```

### Schritt 3: System vorbereiten

```bash
sw-paas exec --new
# Im Container:
bin/console system:update:prepare
```

### Schritt 4: Application deployen

```bash
sw-paas application update
# Fortschritt:
sw-paas app deploy list
sw-paas app deploy get
```

### Schritt 5: Update abschließen

```bash
sw-paas exec --new
# Im Container:
bin/console system:update:finish
```

---

## exec vs. command — Details

### `exec` (Interaktive Shell)

```bash
sw-paas exec --new
```

- Öffnet interaktive Shell im laufenden Container
- Arbeitsverzeichnis: `/var/www/html`
- Netzwerk-Hinweis: Nicht kompatibel mit NAT (VM/WSL → Host/Mirrored Mode)

### `command` (Nicht-interaktiver Befehl)

```bash
sw-paas command create
sw-paas command logs
sw-paas command logs --command-id <id>
```

- Neuer, isolierter Container pro Befehl
- TTL: 1 Stunde
- Standardpfad: `/var/www/html`
- Ideal für CI/CD und Automatisierung

---

## Domain-Verwaltung

### Automatische Domain

Beim ersten Deployment erhält jede Application eine `shopware.shop`-Subdomain.

### Custom Domain

#### Nicht-Apex Domain (Subdomain, z.B. `shop.example.com`)

```dns
CNAME: cdn.shopware.shop
```

#### Apex Domain (z.B. `example.com`)

```dns
# A Records (IPv4)
151.101.3.52
151.101.67.52
151.101.131.52
151.101.195.52

# AAAA Records (IPv6)
2a04:4e42::820
2a04:4e42:200::820
2a04:4e42:400::820
2a04:4e42:600::820

# TXT Record (Domain Ownership)
_shopware-challenge.<domain> IN TXT "shopware-challenge=<organization-id>"
```

```bash
# Organization-ID ermitteln
sw-paas org list

# Domain anlegen (nach DNS-Propagation!)
sw-paas domain create

# Application redeployen
sw-paas application deploy create
```

DNS-Propagation: 15-30 Minuten, bis zu 48 Stunden.

---

## Deployment-Status Übersicht

| Status | Bedeutung |
|--------|-----------|
| `PENDING` | Deployment wartet |
| `BASE` | Basis-Infrastruktur wird deployed |
| `BASE_FAILED` | Basis-Infrastruktur fehlgeschlagen |
| `BASE_SUCCESS` | Basis-Infrastruktur erfolgreich |
| `SHOP` | Shop-Infrastruktur wird deployed |
| `SHOP_FAILED` | Shop-Infrastruktur fehlgeschlagen |
| `SHOP_SUCCESS` | Shop-Infrastruktur erfolgreich |
| `DEPLOYING_STORE` | Shopware Store wird deployed |
| `DEPLOYING_STORE_FAILED` | Store-Deployment fehlgeschlagen |
| `DEPLOYING_STORE_SUCCESS` | Store-Deployment erfolgreich |
| `DEPLOYMENT_SUCCESS` | Vollständig erfolgreich |
| `DEPLOYMENT_FAILED` | Deployment fehlgeschlagen |

---

## Known Issues

### Message Queue Größe

Shopware limitiert aktuell keine Nachrichtengröße (wird in 6.7 geändert).
Lokale Log-Dateien auf kritische Log-Messages prüfen.

### Plugin S3-Kompatibilität

Nicht alle Third-Party-Plugins unterstützen S3-Storage.
Kompatibilität vor Einsatz beim Plugin-Anbieter prüfen.

### Netzwerk-Kompatibilität

`exec` und `service` nutzen mTLS-Tunnel — inkompatibel mit NAT.
In VM/WSL: Netzwerk-Modus auf `Host` oder `Mirrored` stellen.

---

## FAQ

**Kann ich zu einem alten Stand zurückrollen, wenn ich Git-History verloren habe?**
Nein, bei Force-Push ohne Git-History ist kein Rollback möglich.

**Kann ich in den lokalen Filesystem schreiben?**
Nein, Container sind stateless. Persistenz via S3 oder externe Storage.

**Application mit neuem Branch verbinden?**
Application ist an Commit SHA gebunden, nicht an Branch.
`sw-paas application update` mit neuem Commit SHA.

**Wie oft läuft der Scheduler?**
Alle 5 Minuten.

**Gibt es Zero-Downtime Deployments?**
Ja, via Kubernetes Rolling Updates.

**Kann ich zusätzliche Queues konfigurieren?**
Nein, aktuell nicht unterstützt.
