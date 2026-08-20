# Shopware PaaS Native — Fundamentals

PaaS Native = Kubernetes/AWS-Managed Hosting exklusiv für Shopware, fully managed Infra.

## Hierarchie

```
Organization → Project → Application(s)
```

- **Organization**: Top-Level, Rollen: `read-only`, `developer`, `project-admin`, `account-admin`
- **Project**: Linked zu Git-Repo (GitHub/GitLab/Bitbucket)
- **Application**: Eigene Ressourcen, Skalierung, Domain

## Kernkommandos

```bash
sw-paas organization create
sw-paas project create --name "shop" --repository "git@github.com:..."
sw-paas application create
sw-paas account context set   # Org+Project-ID speichern
sw-paas account whoami
```

## application.yaml (Minimal)

```yaml
app:
  php:
    version: "8.3"
    extensions: []
  environment_variables:
    - name: INSTALL_LOCALE
      value: de-DE
      scope: RUN
services:
  mysql:
    version: "8.0"
  opensearch:
    enabled: false
cronJobs: []
```

Scope: `RUN` = Laufzeit, `BUILD` = nur Build-Phase.

## Vault-Secrets (höchste Priorität)

```bash
sw-paas vault create --type buildenv --key SHOPWARE_PACKAGES_TOKEN
sw-paas vault create --type ssh  # SSH-Key generieren
sw-paas vault list / get --secret-id ID / delete --secret-id ID
```

Typen: `env` (Runtime), `buildenv` (Build), `ssh` (Git).

## k8s-meta Package

```bash
# 6.6 → ^1.0 | 6.7 → ^2.0
composer require shopware/k8s-meta --ignore-platform-reqs
```

Installiert `operator.yaml` (S3, Redis, Cluster-Mode, OpenSearch).

## Vertiefung

[FUNDAMENTALS-DETAIL.md](FUNDAMENTALS-DETAIL.md)
