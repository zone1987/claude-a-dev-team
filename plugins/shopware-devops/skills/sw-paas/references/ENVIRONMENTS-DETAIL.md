# Shopware PaaS Native — Environments & Applications (Deep Reference)

Sources: `products/paas/shopware/guides/clone-application.md`,
`products/paas/shopware/guides/update-shopware.md`,
`products/paas/shopware/fundamentals/applications.md`,
`products/paas/shopware/faq.md`, `products/paas/shopware/known-issues.md`

---

## Contents

- [Application Cloning](#application-cloning)
- [Updating Shopware](#updating-shopware)
- [exec vs. command — details](#exec-vs-command-details)
- [Domain management](#domain-management)
- [Deployment status overview](#deployment-status-overview)
- [Known Issues](#known-issues)
- [FAQ](#faq)

## Application Cloning

### Use cases

- **Feature testing**: clone without affecting the original
- **Disaster recovery**: backups into other projects
- **Dev environments**: production data for realistic testing

### Prerequisites

- Source and target in the same **organization** (no cross-org cloning)
- Last deployment of the source: status `DEPLOYING_STORE_SUCCESS`
- The target application must already exist

```bash
# Check the status
sw-paas app deploy list
```

### Clone process

1. **Create a snapshot** of the source application (DB + filesystem)
2. **Restore the snapshot** onto the target application (overwrites existing data)

**Warning:** No anonymization of the data! Full DB dump.

### Interactive mode

```bash
sw-paas application clone
```

Selection:
1. Source organization → source project → source application → deployment
2. Target project → target application

### Manual mode

```bash
sw-paas application clone \
  --organization-id <org-id> \
  --project-id <source-project-id> \
  --application-id <source-application-id> \
  --target-application-id <target-application-id> \
  --target-project-id <target-project-id>
```

### Tracking progress

```bash
sw-paas app deploy list
sw-paas app deploy get
# Wait until: DEPLOYING_STORE_SUCCESS
```

### Post-clone tasks

#### Update the admin password

App B has the same password as app A.

```bash
# Open app B admin access with app A credentials
sw-paas open admin    # → select app A for the credentials

# In the shell of app B
sw-paas exec --new
bin/console user:change-password admin
```

Or via the Shopware admin UI:
1. Log in with the app A credentials
2. Profile → password section
3. New password: the app B admin password (`sw-paas open admin` for app B)

#### Reindex OpenSearch (if enabled)

```bash
sw-paas exec --new
bin/console dal:refresh:index --use-queue
```

#### Update the domain in the sales channel

1. Open the Shopware admin of the cloned application
2. Sales channel → domains
3. Change the domain to the new `shopware.shop` subdomain or a custom domain

---

## Updating Shopware

### Prerequisite

The last deployment must be `DEPLOYING_STORE_SUCCESS`:

```bash
sw-paas app deploy list
```

On `DEPLOYING_STORE_FAILED`: fix the deployment problem first!

### Step 1: create a snapshot (recommended)

```bash
sw-paas snapshot create
# Wait until the snapshot is finished
```

### Step 2: update the code

```bash
git checkout -b my-update-branch

# composer.json: adjust the shopware/core version
composer update --no-scripts
composer recipes:update
# CAUTION: review recipe updates carefully — they can contain breaking changes!

git add .
git commit -m "Update Shopware to X.Y.Z"
git push -u origin my-update-branch
```

### Step 3: prepare the system

```bash
sw-paas exec --new
# Inside the container:
bin/console system:update:prepare
```

### Step 4: deploy the application

```bash
sw-paas application update
# Progress:
sw-paas app deploy list
sw-paas app deploy get
```

### Step 5: finish the update

```bash
sw-paas exec --new
# Inside the container:
bin/console system:update:finish
```

---

## exec vs. command — details

### `exec` (interactive shell)

```bash
sw-paas exec --new
```

- Opens an interactive shell in the running container
- Working directory: `/var/www/html`
- Networking note: not compatible with NAT (VM/WSL → host/mirrored mode)

### `command` (non-interactive command)

```bash
sw-paas command create
sw-paas command logs
sw-paas command logs --command-id <id>
```

- A new, isolated container per command
- TTL: 1 hour
- Default path: `/var/www/html`
- Ideal for CI/CD and automation

---

## Domain management

### Automatic domain

On the first deployment, every application receives a `shopware.shop` subdomain.

### Custom domain

#### Non-apex domain (subdomain, e.g. `shop.example.com`)

```dns
CNAME: cdn.shopware.shop
```

#### Apex domain (e.g. `example.com`)

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
# Determine the organization ID
sw-paas org list

# Create the domain (after DNS propagation!)
sw-paas domain create

# Redeploy the application
sw-paas application deploy create
```

DNS propagation: 15-30 minutes, up to 48 hours.

---

## Deployment status overview

| Status | Meaning |
|--------|-----------|
| `PENDING` | Deployment is waiting |
| `BASE` | Base infrastructure is being deployed |
| `BASE_FAILED` | Base infrastructure failed |
| `BASE_SUCCESS` | Base infrastructure succeeded |
| `SHOP` | Shop infrastructure is being deployed |
| `SHOP_FAILED` | Shop infrastructure failed |
| `SHOP_SUCCESS` | Shop infrastructure succeeded |
| `DEPLOYING_STORE` | Shopware store is being deployed |
| `DEPLOYING_STORE_FAILED` | Store deployment failed |
| `DEPLOYING_STORE_SUCCESS` | Store deployment succeeded |
| `DEPLOYMENT_SUCCESS` | Fully successful |
| `DEPLOYMENT_FAILED` | Deployment failed |

---

## Known Issues

### Message queue size

Shopware currently does not limit the message size (this changes in 6.7).
Check local log files for critical log messages.

### Plugin S3 compatibility

Not all third-party plugins support S3 storage.
Check compatibility with the plugin vendor before use.

### Network compatibility

`exec` and `service` use mTLS tunnels — incompatible with NAT.
In a VM/WSL: set the network mode to `Host` or `Mirrored`.

---

## FAQ

**Can I roll back to an older state if I lost the Git history?**
No, with a force push without Git history no rollback is possible.

**Can I write to the local filesystem?**
No, containers are stateless. Persistence via S3 or external storage.

**Connect an application to a new branch?**
An application is bound to a commit SHA, not to a branch.
Use `sw-paas application update` with the new commit SHA.

**How often does the scheduler run?**
Every 5 minutes.

**Are there zero-downtime deployments?**
Yes, via Kubernetes rolling updates.

**Can I configure additional queues?**
No, currently not supported.
