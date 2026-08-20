# Sales Agent — Installation & Setup

Full reference: [AGENT-SETUP-SETUP.md](AGENT-SETUP-SETUP.md)

## Quick start

```bash
git clone https://github.com/shopware/swagsalesagent.git
cd swagsalesagent
cp .env.template .env
# fill in .env (MySQL, Redis, APP_NAME, APP_SECRET, ...)
pnpm install --frozen-lockfile --prefer-offline
pnpm db:migration:deploy   # migrate the database
pnpm dev                    # development
# or:
pnpm build                  # production
```

## Connect to Shopware

```bash
pnpm app:build  # create the ZIP
# upload the ZIP at bundle/swagsalesagent.zip in Shopware Extensions
```
