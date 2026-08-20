# Shopware PaaS Native — Get Started (Deep Reference)

Sources: `products/paas/shopware/get-started/` (index.md, quickstart.md, cli.md,
prepare-codebase.md) + `products/paas/shopware/guides/setting-up-repository-access.md`

---

## Contents

- [CLI installation](#cli-installation)
- [Preparing the codebase](#preparing-the-codebase)
- [Setting up repository access](#setting-up-repository-access)
- [Quickstart — complete](#quickstart-complete)
- [Permissions & roles](#permissions-roles)
- [Common questions when starting out](#common-questions-when-starting-out)

## CLI installation

```bash
# Standard
curl -L https://install.sw-paas-cli.shopware.systems | sh

# Specific version
curl -L https://install.sw-paas-cli.shopware.systems | sh -s 0.0.30
```

Installs to `~/.sw-paas/bin/sw-paas`. The directory can be changed via `SW_PAAS_DIR`.
PATH is extended automatically.

```bash
sw-paas version     # verify the installation
sw-paas auth        # browser login, the token is stored
sw-paas             # show all available commands
```

Bugs/feedback: https://github.com/shopware/sw-paas/issues

---

## Preparing the codebase

### Requirements

- macOS or Linux recommended for local development
- Windows: use Docker or WSL2
- Plugin management **ONLY via Composer** (HA/cluster setup = stateless)
- Check the S3 compatibility of every plugin!

### New project

```bash
composer create-project shopware/production <folder-name>
cd <folder-name>
```

### Existing project

```bash
cd <your-project-folder>

# Shopware 6.7
composer require shopware/k8s-meta:^2.0 --ignore-platform-reqs

# Shopware 6.6
composer require shopware/k8s-meta:^1.0 --ignore-platform-reqs
```

### What k8s-meta configures

`config/packages/operator.yaml` must exist after the installation.
It contains: S3 storage, Redis cache+session, cluster mode, admin worker disabled.

### Creating application.yaml

Create it at the project root:

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

### Uninstalling plugins

Through the Deployment Helper with `.shopware-project.yml`:
1. Set the extension to `remove` → deploy (uninstallation)
2. Remove the extension from the source code → deploy again

---

## Setting up repository access

### Option 1: automatically via the CLI (recommended)

```bash
# At organization level (all projects)
sw-paas vault create --type ssh

# At project level (a single project only)
sw-paas vault create --type ssh --project <project-id>
```

Copy the public key from the CLI output and add it to the Git provider.

### Option 2: manually

```bash
# RSA 4096 (PEM format, passwordless)
ssh-keygen -t rsa -b 4096 -m PEM -f ./sw-paas
# Alternatively: ED25519 or ECDSA (also PEM, passwordless)

# Add the public key (sw-paas.pub) to the Git provider (read-only)
# GitHub: Settings → Deploy Keys
# GitLab/Bitbucket: Deploy Keys

# Store the private key in the vault
cat sw-paas | sw-paas vault create --type ssh --password-stdin
```

**Important:** Only one SSH key per level (org/project) is possible.
The project level overrides the org level.

---

## Quickstart — complete

### Step 1: install the CLI

```bash
curl -L https://install.sw-paas-cli.shopware.systems | sh
sw-paas version
```

### Step 2: SSH key for the Git repo

```bash
sw-paas vault create --type ssh
# Public key → repository deploy keys
```

### Step 3: create the project

```bash
sw-paas project create --name "my-shopware-app" --repository "git@github.com:username/repo.git"
```

### Step 4: create & deploy the application

```bash
sw-paas application create
sw-paas application deploy create
sw-paas watch          # live monitoring
```

---

## Permissions & roles

| Role | Description |
|-------|-------------|
| `read-only` | Only `get` and `list` |
| `developer` | All actions on projects/applications |
| `project-admin` | All actions on projects/applications |
| `account-admin` | User management |

Adding a new user (as account-admin):
```bash
# The user reports their sub ID:
sw-paas account whoami --output json | jq ".sub"

# The admin adds the user:
sw-paas account user add --sub "<sub-id>"
```

---

## Common questions when starting out

**Q: Can I run other kinds of applications (e.g. Node.js)?**
No, PaaS Native supports Shopware projects only.

**Q: Can I protect an application with basic auth?**
Not recommended — unexpected behavior in the platform setup.
Use the Shopware maintenance mode instead.

**Q: Which cloud providers are supported?**
Currently AWS only.
