# Shopware PaaS Native — Environments & Applications

## Application Cloning

```bash
sw-paas application clone            # Interactive

# Manual
sw-paas application clone \
  --organization-id <org-id> \
  --project-id <source-project-id> \
  --application-id <source-app-id> \
  --target-application-id <target-app-id> \
  --target-project-id <target-project-id>
```

**Prerequisite:** The last deployment must be `DEPLOYING_STORE_SUCCESS`.

After the clone:
1. Change the admin password (`sw-paas open admin`)
2. Reindex OpenSearch: `bin/console dal:refresh:index --use-queue`
3. Update the domain in the sales channel

## Updating the Shopware version

```bash
# 1. Create a snapshot
sw-paas snapshot create

# 2. New branch, update composer.json
git checkout -b update-shopware
# adjust the shopware/core version
composer update --no-scripts
composer recipes:update
git add . && git commit -m "Update Shopware X.Y.Z"
git push

# 3. Preparation in the running system
sw-paas exec --new
bin/console system:update:prepare

# 4. Deployment
sw-paas application update

# 5. Completion
sw-paas exec --new
bin/console system:update:finish
```

## exec vs. command

| | `exec` | `command` |
|---|---|---|
| Container | Existing | New |
| Mode | Interactive | Non-interactive |
| Use case | Debugging, maintenance | CI/CD, automation |
| TTL | Session | 1 hour |

```bash
sw-paas exec --new           # Interactive shell
sw-paas command create       # Run a one-off command
```

## Deep dive

[ENVIRONMENTS-DETAIL.md](ENVIRONMENTS-DETAIL.md)
