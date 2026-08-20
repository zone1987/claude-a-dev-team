# Shopware PaaS Native — Get Started

## 1. Install & authenticate the CLI

```bash
curl -L https://install.sw-paas-cli.shopware.systems | sh
sw-paas version
sw-paas auth          # browser login
```

Specific version: `curl -L https://install.sw-paas-cli.shopware.systems | sh -s 0.0.30`

## 2. Prepare the codebase

```bash
# New project
composer create-project shopware/production <folder-name>
cd <folder-name>

# Existing project: install k8s-meta
# SW 6.7:
composer require shopware/k8s-meta:^2.0 --ignore-platform-reqs
# SW 6.6:
composer require shopware/k8s-meta:^1.0 --ignore-platform-reqs

# config/packages/operator.yaml must exist!
```

## 3. Create application.yaml

```yaml
# project root
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

## 4. Set up repository access

```bash
sw-paas vault create --type ssh   # generate SSH key + store it in the vault
# Public key → GitHub: Settings → Deploy Keys → Add (read-only)
# GitLab: Settings → Repository → Deploy Keys
# Bitbucket: Repository settings → Access keys
```

## 5. Create project & application

```bash
sw-paas project create --name "my-shop" --repository "git@github.com:..."
sw-paas application create
sw-paas application deploy create
sw-paas watch                      # follow the deployment live
```

Plugin management **only via Composer**. Stateless, check S3 compatibility.

## Deep dive

[GET-STARTED-DETAIL.md](GET-STARTED-DETAIL.md)
