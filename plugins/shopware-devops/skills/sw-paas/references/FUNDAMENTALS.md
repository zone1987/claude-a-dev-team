# Shopware PaaS Native — Fundamentals

PaaS Native = Kubernetes/AWS-managed hosting exclusively for Shopware, fully managed infra.

## Hierarchy

```
Organization → Project → Application(s)
```

- **Organization**: top level, roles: `read-only`, `developer`, `project-admin`, `account-admin`
- **Project**: linked to a Git repo (GitHub/GitLab/Bitbucket)
- **Application**: own resources, scaling, domain

## Core commands

```bash
sw-paas organization create
sw-paas project create --name "shop" --repository "git@github.com:..."
sw-paas application create
sw-paas account context set   # store org+project ID
sw-paas account whoami
```

## application.yaml (minimal)

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

Scope: `RUN` = runtime, `BUILD` = build phase only.

## Vault secrets (highest priority)

```bash
sw-paas vault create --type buildenv --key SHOPWARE_PACKAGES_TOKEN
sw-paas vault create --type ssh  # generate SSH key
sw-paas vault list / get --secret-id ID / delete --secret-id ID
```

Types: `env` (runtime), `buildenv` (build), `ssh` (Git).

## k8s-meta package

```bash
# 6.6 → ^1.0 | 6.7 → ^2.0
composer require shopware/k8s-meta --ignore-platform-reqs
```

Installs `operator.yaml` (S3, Redis, cluster mode, OpenSearch).

## Deep dive

[FUNDAMENTALS-DETAIL.md](FUNDAMENTALS-DETAIL.md)
