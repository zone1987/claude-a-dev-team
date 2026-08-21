# shopware-cli — Overview

`shopware-cli` is a CLI written in Go for all Shopware DevOps tasks:
extension build, project management, account upload, CI pipelines.

```bash
# Installation
curl -1sLf https://dl.cloudsmith.io/public/friendsofshopware/stable/setup.deb.sh | sudo bash
sudo apt install shopware-cli          # Debian/Ubuntu

brew install shopware/homebrew-tap/shopware-cli  # macOS

go install github.com/shopware/shopware-cli@latest  # Go
npm install -g @shopware-ag/shopware-cli            # npm
# Docker: shopware/shopware-cli:latest
```

## Global flags

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--verbose` | | false | Debug output |
| `--no-interaction` | `-n` | false | No interactive input (CI-safe) |
| `--version` | | | Print version |

## Command groups

| Group | Description |
|-------|-------------|
| `account` | Shopware Account: login, logout, producer/store actions |
| `extension` | Extension build, validate, zip, watch, fix, format |
| `project` | Project management: create, CI build, DB dump, worker, Admin API |

## Deep dive

- [ALL-COMMANDS.md](ALL-COMMANDS.md) — All commands with flags and purpose (exhaustive)
- [INTERNAL-PACKAGES.md](INTERNAL-PACKAGES.md) — Important internal Go packages
