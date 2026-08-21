# shopware-cli account — Complete reference

## Contents

- [account login](#account-login)
- [account logout](#account-logout)
- [account producer extension list](#account-producer-extension-list)
- [account producer extension info pull](#account-producer-extension-info-pull)
- [account producer extension info push](#account-producer-extension-info-push)
- [account producer extension upload](#account-producer-extension-upload)
- [`.shopware-extension.yml` — Complete format](#shopware-extensionyml-complete-format)
- [Typical store publishing workflow](#typical-store-publishing-workflow)
- [CI pipeline for automatic store upload](#ci-pipeline-for-automatic-store-upload)

## account login

OIDC/OAuth2 browser-based login against the Shopware Account.

```bash
shopware-cli account login
# → Opens the browser for the OIDC flow
# → Token is cached locally (~/.config/shopware-cli/ or XDG_CONFIG_HOME)
```

No additional flags beyond the global ones (`--no-interaction`, `--verbose`).

With `--no-interaction`: login fails (it requires the browser flow).
For CI: set the `ACCOUNT_EMAIL` and `ACCOUNT_PASSWORD` environment variables.

```bash
# CI login via environment variables
ACCOUNT_EMAIL=user@example.com ACCOUNT_PASSWORD=secret shopware-cli account login
```

## account logout

Invalidate the local token cache.

```bash
shopware-cli account logout
```

No flags.

## account producer extension list

List all of your own store extensions.

```bash
shopware-cli account producer extension list
shopware-cli account producer extension list --search "My"
```

| Flag | Description |
|------|-------------|
| `--search string` | Filter results by name |

**Output:**
- Extension name (technical)
- Display name
- Status (active/inactive)
- Current version in the store

## account producer extension info pull

Pull store information from the Shopware Account into local files.

```bash
shopware-cli account producer extension info pull path/to/MyPlugin
```

**Downloads into:**
- `.shopware-extension.yml` — metadata (name, descriptions, categories, settings)
- `src/Resources/store/` — store assets:
  - `icon.png` — extension icon (256x256px)
  - `images/` — store screenshots
  - `description_de.html`, `description_en.html` — descriptions
  - `installation_manual_de.html`, `installation_manual_en.html` — installation manuals

No additional flags.

## account producer extension info push

Upload local store info from `.shopware-extension.yml` and `src/Resources/store/` to the Shopware Account.

```bash
shopware-cli account producer extension info push path/to/MyPlugin
# or a zip file
shopware-cli account producer extension info push MyPlugin-1.2.3.zip
```

**Updates:**
- Descriptions (all languages)
- Installation manual
- Store screenshots
- Icon
- Categories
- Compatibility flags

No additional flags.

## account producer extension upload

Upload an extension zip to the Shopware Store and trigger the code review.

```bash
shopware-cli account producer extension upload MyPlugin-1.2.3.zip

# Without waiting for the code review
shopware-cli account producer extension upload MyPlugin-1.2.3.zip --skip-for-review-result
```

| Flag | Default | Description |
|------|---------|-------------|
| `--skip-for-review-result` | false | Do not wait for the automatic code review (faster CI) |

**Upload sequence:**
1. Upload the zip via the Shopware Account API
2. Trigger the automatic code review
3. (Default) Wait for the review result and print it
4. Exit code != 0 if the code review reports errors

**The code review checks, among other things:**
- PHP syntax
- Forbidden functions (`eval`, `exec`, etc.)
- Shopware API usage
- Performance problems
- Security problems

---

## `.shopware-extension.yml` — Complete format

```yaml
store:
  # Store icon (256x256px PNG)
  icon: src/Resources/store/icon.png

  # Supported Shopware language regions
  localizations:
    - de_DE
    - en_GB

  # Store categories
  categories:
    - Storefront
    - Administration

  # Automatic bugfix version compatibility
  automatic_bugfix_version_compatibility: true

  # Store texts per language
  info:
    de:
      name: "My Plugin"
      summary: "Short description (max. 150 characters)"
      description: "Long description in Markdown/HTML"
      installation_manual: "Installation instructions"
      highlights:
        - "Feature 1"
        - "Feature 2"
      features:
        - "Feature A"
      faq:
        - question: "How do I install the plugin?"
          answer: "Via the Plugin Manager"
      tags:
        - "Shopware 6"
        - "Extension"
    en:
      name: "My Plugin"
      summary: "Short description"
      description: "Long description"
      installation_manual: "Installation instructions"

# Build configuration
build:
  # Exclude files/folders from the zip
  zip:
    assets:
      enable: true
    pack:
      excludes:
        # Patterns to exclude
        - "node_modules"
        - "src/Resources/app/*/node_modules"
        - ".git"
        - "*.test.*"
        - "phpunit.xml*"
        - "tests/"
```

---

## Typical store publishing workflow

```bash
# 1. Build and validate the extension
shopware-cli extension build path/to/MyPlugin
shopware-cli extension validate --full --store-compliance path/to/MyPlugin

# 2. Create the release zip
shopware-cli extension zip path/to/MyPlugin --use-git-tag-as-version --release

# 3. Keep store info up to date
shopware-cli account login
shopware-cli account producer extension info push path/to/MyPlugin

# 4. Upload the extension
shopware-cli account producer extension upload MyPlugin-1.2.3.zip

# 5. After the upload: check the status
shopware-cli account producer extension list --search MyPlugin
```

---

## CI pipeline for automatic store upload

```yaml
# GitHub Actions example
- name: Build and upload extension
  env:
    ACCOUNT_EMAIL: ${{ secrets.SHOPWARE_ACCOUNT_EMAIL }}
    ACCOUNT_PASSWORD: ${{ secrets.SHOPWARE_ACCOUNT_PASSWORD }}
  run: |
    shopware-cli account login
    shopware-cli extension build .
    shopware-cli extension validate --full --reporter github .
    shopware-cli extension zip . --use-git-tag-as-version --release
    ZIP=$(ls *.zip | head -1)
    shopware-cli account producer extension upload "$ZIP"
```
