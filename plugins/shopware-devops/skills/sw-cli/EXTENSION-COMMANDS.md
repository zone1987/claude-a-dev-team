# shopware-cli extension — Complete reference

## Contents

- [extension build](#extension-build)
- [extension admin-watch](#extension-admin-watch)
- [extension validate](#extension-validate)
- [extension zip](#extension-zip)
- [extension fix](#extension-fix)
- [extension format](#extension-format)
- [extension prepare](#extension-prepare)
- [extension get-name / get-version](#extension-get-name-get-version)
- [extension get-changelog](#extension-get-changelog)
- [extension config-schema](#extension-config-schema)
- [Typical release workflow](#typical-release-workflow)
- [Typical dev workflow](#typical-dev-workflow)

## extension build

Builds admin and storefront assets for one or more extensions.

```bash
shopware-cli extension build path/to/MyPlugin
shopware-cli extension build plugin-a/ plugin-b/ plugin-c/
SHOPWARE_PROJECT_ROOT=/var/www/shop shopware-cli extension build path/to/MyPlugin
```

- Uses ESBuild for modern extensions, Webpack for legacy ones
- `SHOPWARE_PROJECT_ROOT` sets the Shopware context for version detection
- Produces assets under `src/Resources/public/`

## extension admin-watch

ESBuild-based dev proxy for the Shopware Administration. Compiles extension assets live
and proxies the Shopware admin to the browser.

```bash
shopware-cli extension admin-watch path/to/MyPlugin http://localhost
shopware-cli extension admin-watch path/to/MyPlugin http://localhost --listen :9000
shopware-cli extension admin-watch path/to/MyPlugin http://localhost --external-url https://my-tunnel.example.com
```

| Flag | Default | Description |
|------|---------|-------------|
| `--listen string` | `:8080` | Listen address (host:port) |
| `--external-url string` | | External URL (e.g. for ngrok/reverse proxy) |

## extension validate

```bash
# Fast basic check
shopware-cli extension validate path/to/MyPlugin

# Full check (PHPStan level 8, ESLint, Stylelint, Prettier, Rector, Twig)
shopware-cli extension validate --full path/to/MyPlugin

# Store compliance (ignores custom ignore lists)
shopware-cli extension validate --full --store-compliance path/to/MyPlugin

# CI output for GitHub Actions
shopware-cli extension validate --full --reporter github path/to/MyPlugin

# Check only against the lowest supported SW version
shopware-cli extension validate --full --check-against lowest path/to/MyPlugin

# Only PHPStan and ESLint
shopware-cli extension validate --full --only phpstan,eslint path/to/MyPlugin
```

| Flag | Default | Description |
|------|---------|-------------|
| `--full` | false | PHPStan, ESLint, Stylelint, PHP-CS-Fixer, Rector, Prettier, Twig |
| `--store-compliance` | false | Force store compliance checks |
| `--reporter string` | auto | `summary` \| `json` \| `github` \| `gitlab` \| `junit` \| `markdown` |
| `--check-against string` | `highest` | SW version: `highest` \| `lowest` |
| `--only string` | | Comma-separated tool list |
| `--exclude string` | | Exclude tools |
| `--no-copy` | false | Do not copy the extension into a tmp dir |

**Reporter selection:**
- `auto`: terminal → `summary`, CI (GitHub Actions) → `github`, CI (GitLab) → `gitlab`
- `github`: annotations in GitHub Actions
- `gitlab`: code quality report for GitLab
- `junit`: JUnit XML for test reports
- `markdown`: Markdown table

## extension zip

Creates a release zip via git export (default) or directly from the source folder.

```bash
# Default: export git HEAD
shopware-cli extension zip path/to/MyPlugin

# Without git (e.g. for a dirty working tree)
shopware-cli extension zip path/to/MyPlugin --disable-git

# Release mode (removes the app backend secret)
shopware-cli extension zip path/to/MyPlugin --release

# Export a specific branch/tag
shopware-cli extension zip path/to/MyPlugin v1.2.3

# Use the git tag as the version automatically
shopware-cli extension zip path/to/MyPlugin --use-git-tag-as-version

# Write output into a specific directory
shopware-cli extension zip path/to/MyPlugin --output-directory ./dist/

# Override the app backend URL (for multi-environment setups)
shopware-cli extension zip path/to/MyPlugin --overwrite-app-backend-url https://prod.example.com

# Override the version
shopware-cli extension zip path/to/MyPlugin --overwrite-version 2.0.0
```

| Flag | Default | Description |
|------|---------|-------------|
| `--disable-git` | false | Use the source folder directly, no git export |
| `--release` | false | Remove the app backend secret from `manifest.xml` |
| `--overwrite-app-backend-url string` | | Replace the backend URL in `manifest.xml` |
| `--overwrite-app-backend-secret string` | | Replace the app secret in `manifest.xml` |
| `--overwrite-version string` | | Override the version in the zip |
| `--use-git-tag-as-version` | false | Use the detected git tag as the version (incompatible with `--disable-git` and `--overwrite-version`) |
| `--output-directory string` | | Output directory |
| `--git-commit string` | | Export a specific commit hash or tag |
| `--filename string` | | Explicit file name (default: `<Name>-<tag>.zip`) |

**Controlling zip contents:**
The files that end up in the zip are controlled by `.gitignore` and the `excluded_paths` key in `.shopware-extension.yml`.

## extension fix

```bash
shopware-cli extension fix path/to/MyPlugin
shopware-cli extension fix --only phpcs,eslint path/to/MyPlugin
shopware-cli extension fix --allow-non-git path/to/MyPlugin
```

| Flag | Default | Description |
|------|---------|-------------|
| `--only string` | | Comma-separated tool list (`phpstan`, `eslint`, `phpcs`, etc.) |
| `--allow-non-git` | false | Also run without a git repo |

Requires a git repository (checks for staged/unstaged changes for safety).

## extension format

```bash
shopware-cli extension format path/to/MyPlugin
shopware-cli extension format --dry-run path/to/MyPlugin
shopware-cli extension format --only prettier path/to/MyPlugin
```

| Flag | Default | Description |
|------|---------|-------------|
| `--only string` | | Comma-separated tool list |
| `--dry-run` | false | Only show the diff, do not apply |

## extension prepare

Pre-zip pipeline without creating the zip: install Composer deps, remove dev files.

```bash
shopware-cli extension prepare path/to/MyPlugin
```

No flags. Useful for custom zip pipelines.

## extension get-name / get-version

```bash
shopware-cli extension get-name path/to/MyPlugin    # → MyPlugin
shopware-cli extension get-version path/to/MyPlugin  # → 1.2.3
shopware-cli extension get-name MyPlugin-1.2.3.zip
shopware-cli extension get-version MyPlugin-1.2.3.zip
```

Reads from the folder name or the zip contents. No flags.

## extension get-changelog

```bash
shopware-cli extension get-changelog path/to/MyPlugin
shopware-cli extension get-changelog --language de_DE path/to/MyPlugin
shopware-cli extension get-changelog --language de_DE,en_GB path/to/MyPlugin  # Fallback
```

| Flag | Description |
|------|-------------|
| `--language string` | Language key, comma-separated fallback list |

## extension config-schema

```bash
shopware-cli extension config-schema > shopware-extension-schema.json
```

JSON schema for `.shopware-extension.yml`. No flags.

---

## Typical release workflow

```bash
# 1. Build assets
shopware-cli extension build path/to/MyPlugin

# 2. Validate (locally: without --full; CI: with --full)
shopware-cli extension validate --full path/to/MyPlugin

# 3. Create the zip
shopware-cli extension zip path/to/MyPlugin --use-git-tag-as-version --release

# 4. Upload to the store
shopware-cli account login
shopware-cli account producer extension upload MyPlugin-1.2.3.zip
```

## Typical dev workflow

```bash
# Admin dev proxy (ESBuild, hot reload)
shopware-cli extension admin-watch path/to/MyPlugin http://localhost

# Storefront: use shopware-cli project storefront-watch . instead of the extension counterpart
```
