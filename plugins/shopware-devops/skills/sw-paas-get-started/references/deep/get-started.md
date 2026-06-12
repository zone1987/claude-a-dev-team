# Shopware PaaS Native — Get Started (Deep Reference)

Quellen: `products/paas/shopware/get-started/` (index.md, quickstart.md, cli.md,
prepare-codebase.md) + `products/paas/shopware/guides/setting-up-repository-access.md`

---

## CLI Installation

```bash
# Standard
curl -L https://install.sw-paas-cli.shopware.systems | sh

# Spezifische Version
curl -L https://install.sw-paas-cli.shopware.systems | sh -s 0.0.30
```

Installiert nach `~/.sw-paas/bin/sw-paas`. Verzeichnis via `SW_PAAS_DIR` anpassbar.
PATH wird automatisch ergänzt.

```bash
sw-paas version     # Installation prüfen
sw-paas auth        # Browser-Login, Token wird gespeichert
sw-paas             # Alle verfügbaren Befehle anzeigen
```

Bugs/Feedback: https://github.com/shopware/sw-paas/issues

---

## Codebase vorbereiten

### Voraussetzungen

- macOS oder Linux empfohlen für lokale Entwicklung
- Windows: Docker oder WSL2 verwenden
- Plugin-Management **NUR via Composer** (HA/Cluster-Setup = stateless)
- S3-Kompatibilität jedes Plugins prüfen!

### Neues Projekt

```bash
composer create-project shopware/production <folder-name>
cd <folder-name>
```

### Existierendes Projekt

```bash
cd <your-project-folder>

# Shopware 6.7
composer require shopware/k8s-meta:^2.0 --ignore-platform-reqs

# Shopware 6.6
composer require shopware/k8s-meta:^1.0 --ignore-platform-reqs
```

### Was k8s-meta konfiguriert

`config/packages/operator.yaml` muss nach Installation existieren.
Enthält: S3-Storage, Redis Cache+Session, Cluster-Mode, Admin-Worker deaktiviert.

### application.yaml erstellen

Am Projektroot anlegen:

```yaml
app:
  php:
    version: "8.3"
  environment_variables: []
services:
  mysql:
    version: "8.0"
  opensearch:
    enabled: false
```

### Plugins deinstallieren

Über Deployment Helper mit `.shopware-project.yml`:
1. Extension auf `remove` setzen → Deployen (Deinstallation)
2. Extension aus Source-Code entfernen → Erneut deployen

---

## Repository-Zugang einrichten

### Option 1: Automatisch via CLI (empfohlen)

```bash
# Auf Organization-Ebene (alle Projekte)
sw-paas vault create --type ssh

# Auf Projekt-Ebene (nur ein Projekt)
sw-paas vault create --type ssh --project <project-id>
```

Public Key aus CLI-Output kopieren und in Git-Provider eintragen.

### Option 2: Manuell

```bash
# RSA 4096 (PEM-Format, passwordless)
ssh-keygen -t rsa -b 4096 -m PEM -f ./sw-paas
# Alternativ: ED25519 oder ECDSA (ebenfalls PEM, passwordless)

# Public Key (sw-paas.pub) in Git-Provider eintragen (Read-Only)
# GitHub: Settings → Deploy Keys
# GitLab/Bitbucket: Deploy Keys

# Private Key in Vault speichern
cat sw-paas | sw-paas vault create --type ssh --password-stdin
```

**Wichtig:** Pro Level (org/project) nur ein SSH-Key möglich.
Projekt-Level überschreibt Org-Level.

---

## Quickstart — Vollständig

### Schritt 1: CLI installieren

```bash
curl -L https://install.sw-paas-cli.shopware.systems | sh
sw-paas version
```

### Schritt 2: SSH-Key für Git-Repo

```bash
sw-paas vault create --type ssh
# Public Key → Repository Deploy Keys
```

### Schritt 3: Projekt erstellen

```bash
sw-paas project create --name "my-shopware-app" --repository "git@github.com:username/repo.git"
```

### Schritt 4: Application erstellen & deployen

```bash
sw-paas application create
sw-paas application deploy create
sw-paas watch          # Live-Monitoring
```

---

## Berechtigungen & Rollen

| Rolle | Beschreibung |
|-------|-------------|
| `read-only` | Nur `get` und `list` |
| `developer` | Alle Aktionen auf Projekten/Applications |
| `project-admin` | Alle Aktionen auf Projekten/Applications |
| `account-admin` | User-Management |

Neuen User hinzufügen (als account-admin):
```bash
# User gibt Sub-ID bekannt:
sw-paas account whoami --output json | jq ".sub"

# Admin fügt User hinzu:
sw-paas account user add --sub "<sub-id>"
```

---

## Häufige Fragen beim Start

**Q: Kann ich verschiedene Anwendungen (z.B. Node.js) betreiben?**
Nein, PaaS Native unterstützt nur Shopware-Projekte.

**Q: Kann ich zur Basis-Auth eine Application schützen?**
Nicht empfohlen — unerwartetes Verhalten im Platform-Setup.
Stattdessen: Shopware Maintenance Mode nutzen.

**Q: Welche Cloud-Provider werden unterstützt?**
Aktuell nur AWS.
