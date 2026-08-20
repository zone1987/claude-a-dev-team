# Symfony Flex recipes for Shopware

Recipes automate configuration during `composer require`. The official Shopware Flex
repository extends the Symfony standard server with Shopware-specific
packages.

```json
// composer.json
"extra": {
    "symfony": {
        "endpoint": ["https://raw.githubusercontent.com/shopware/recipes/flex/main/index.json"]
    }
}
```

```bash
composer require shopware/core          # installs + applies the recipe
composer recipes                        # show all applied recipes
composer recipes:update shopware/core   # re-apply a recipe (after an update)
```

## Manifest keys (quick overview)

| Key | Purpose |
|-----|-------|
| `copy-from-recipe` | Copy files from the recipe dir into the project |
| `bundles` | Register bundles in `config/bundles.php` |
| `env` | Add `.env` entries (`%generate(secret)%`) |
| `gitignore` | Append `.gitignore` lines |
| `container` | Set container parameters / `env(...)` defaults |
| `docker-compose` | Inject services into `docker-compose.yml` |
| `makefile` | Insert Makefile targets |
| `aliases` | `composer require` short aliases (`paas`, `fastly`) |
| `conflict` | Declare incompatible package versions |
| `composer-scripts` | Register `composer.json` scripts |

## Deep dive

- [RECIPES-MANIFEST.md](RECIPES-MANIFEST.md) — all keys with full examples and Shopware specifics
- [RECIPES-PACKAGES.md](RECIPES-PACKAGES.md) — all available recipe packages with versions
