# shopware-cli project

Commands for managing the entire Shopware project.

```bash
shopware-cli project create my-shop --version latest --deployment shopware-paas
shopware-cli project ci .                    # CI build pipeline
shopware-cli project admin-build .           # Build admin assets
shopware-cli project storefront-build .      # Storefront + theme:compile
shopware-cli project worker 2                # Start 2 messenger consumers
shopware-cli project dump --clean --anonymize
```

## Command overview

| Command | Summary |
|---------|---------|
| `create` | Create a new Shopware project (interactively or with flags) |
| `ci` | Complete CI pipeline (composer + assets + cache + checksums) |
| `admin-build` | Build admin JS/CSS for all extensions |
| `storefront-build` | Storefront assets + `theme:compile` |
| `admin-watch` | Start the admin webpack dev server |
| `storefront-watch` | Start the storefront webpack hot proxy |
| `console` | `bin/console` passthrough with tab completion |
| `dump` | MySQL dump (parallel, anonymize, gzip/zstd) |
| `worker` | Messenger consumer (restart on failure, SIGTERM-safe) |
| `doctor` | Check the project for problems |
| `validate` | Validate the entire project |
| `fix` | Run code fixers on the project |
| `format` | Run formatters on the project |
| `generate-jwt` | Generate an RSA key pair for JWT |
| `image-proxy` | Local image proxy with upstream fallback |
| `admin-api` | Authenticated Admin REST API wrapper |
| `clear-cache` | Clear the cache (API or local) |
| `upgrade-check` | Check extension compatibility with a new SW version |
| `config init` | Create `.shopware-project.yml` interactively |
| `config-schema` | JSON schema for `.shopware-project.yml` |
| `extension *` | Extension lifecycle via Admin API (list/install/activate/...) |
| `autofix composer-plugins` | Migrate plugins to Composer |
| `autofix flex` | Migrate to Symfony Flex |

## Deep dive

- [PROJECT-COMMANDS.md](PROJECT-COMMANDS.md) — All flags, examples, edge cases
