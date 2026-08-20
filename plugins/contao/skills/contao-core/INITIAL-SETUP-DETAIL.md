# Contao 5 — Initial Setup

## Installation: Managed Edition

```bash
composer create-project contao/managed-edition
# Specific version:
composer create-project contao/managed-edition . 5.7
```

The **Managed Edition** is intended for projects in which Contao is the central
component of the application. It enables automatic configuration through
third-party bundles.

---

## Managed Edition internals

### Core components

1. **Manager Bundle** (`contao/manager-bundle`)  
   Provides the application skeleton: entry points and configuration files.
   
2. **Manager Plugin** (`contao/manager-plugin`)  
   A Composer plugin that automatically runs the `contao-setup` script after every
   `composer install`/`composer update`.

### What `contao-setup` does

- Creates the application structure and the required directories
- Rebuilds the cache
- Generates the required symlinks

**composer.json (Managed Edition):**

```json
{
    "scripts": {
        "post-install-cmd": ["@php vendor/bin/contao-setup"],
        "post-update-cmd": ["@php vendor/bin/contao-setup"]
    }
}
```

The specialised kernel of the Managed Edition queries installed packages for
configuration data through interfaces of the Manager Plugin — full
auto-configuration is the result.

---

## Integration into an existing Symfony application

Contao can be integrated into existing Symfony applications as a standalone Symfony
bundle. This option makes sense when Contao only provides supplementary CMS features
while the Symfony app is the core.

### Contao 5.3 in a Symfony application

The installation instructions for Contao 5.3 LTS as a Symfony bundle are
documented at
`https://docs.contao.org/5.x/dev/getting-started/initial-setup/symfony-application/contao-5.3/`.

**Principle:** since Contao is a Symfony bundle, all standard Symfony bundle
conventions apply. The integration requires:
- Bundle registration in the kernel
- Routing configuration
- Database migrations

---

## Which variant when?

| Criterion | Managed Edition | Symfony Application |
|-----------|----------------|---------------------|
| Contao is the main component | ✅ | ❌ |
| Automatic bundle configuration | ✅ | Manual |
| Existing Symfony app | ❌ | ✅ |
| Simplest updates | ✅ | ❌ |

---

## Starting development

After installing with the Managed Edition:

1. `composer install` (without `--optimize-autoloader` during development)
2. New classes are available immediately without a cache rebuild
3. Your own code in `src/`, Contao-specific things in `contao/`

**Recommendation:** use `.env` files instead of `parameters.yaml` for sensitive data.

---

*Source: https://docs.contao.org/5.x/dev/getting-started/initial-setup/*  
*https://docs.contao.org/5.x/dev/getting-started/initial-setup/managed-edition/*  
*https://docs.contao.org/5.x/dev/getting-started/initial-setup/symfony-application/*
