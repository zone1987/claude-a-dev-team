# Shopware PaaS Native — Get Started

## 1. CLI installieren & authentifizieren

```bash
curl -L https://install.sw-paas-cli.shopware.systems | sh
sw-paas version
sw-paas auth          # Browser-Login
```

Spezifische Version: `curl -L https://install.sw-paas-cli.shopware.systems | sh -s 0.0.30`

## 2. Codebase vorbereiten

```bash
# Neues Projekt
composer create-project shopware/production <folder-name>
cd <folder-name>

# Existierendes Projekt: k8s-meta installieren
# SW 6.7:
composer require shopware/k8s-meta:^2.0 --ignore-platform-reqs
# SW 6.6:
composer require shopware/k8s-meta:^1.0 --ignore-platform-reqs

# config/packages/operator.yaml muss existieren!
```

## 3. application.yaml erstellen

```yaml
# Projektroot
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

## 4. Repository-Zugang einrichten

```bash
sw-paas vault create --type ssh   # SSH-Key generieren + in Vault speichern
# Public Key → GitHub: Settings → Deploy Keys → Add (Read-Only)
# GitLab: Settings → Repository → Deploy Keys
# Bitbucket: Repository settings → Access keys
```

## 5. Projekt & Application erstellen

```bash
sw-paas project create --name "my-shop" --repository "git@github.com:..."
sw-paas application create
sw-paas application deploy create
sw-paas watch                      # Deployment live verfolgen
```

Plugin-Management **nur via Composer**. Stateless, S3-Kompatibilität prüfen.

## Vertiefung

[GET-STARTED-DETAIL.md](GET-STARTED-DETAIL.md)
