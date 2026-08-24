# Shopware — from the Language Pack plugin to integrated translations

| Version | State |
|---|---|
| **6.7.3.0** | translations are managed by Shopware itself; the Language Pack plugin still works but is no longer recommended |
| **6.8.0.0** | the Language Pack plugin is **not compatible** |

The CLI command that replaces it:

```bash
bin/console translation:install --locales it-IT
```

## Contents

- [What changes in 6.7.3.0](#what-changes-in-6730)
- [If you do not use the Language Pack](#if-you-do-not-use-the-language-pack)
- [If you do use the Language Pack](#if-you-do-use-the-language-pack)
- [New installations](#new-installations)

## What changes in 6.7.3.0

- Translations install through Shopware; the plugin is not needed to fetch the newest ones.
- Languages gain an **active flag**, toggled under **Settings → Languages**.
- Languages managed from other sources no longer have to register their locales in the admin.
- **Other translation plugins and theme snippets are unaffected** and keep working alongside the
  integrated handling — in both 6.7 and 6.8.

## If you do not use the Language Pack

Nothing changes. Install further languages with the command, which takes a comma-separated list:

```bash
bin/console translation:install --locales it-IT,fr-FR
```

## If you do use the Language Pack

1. **Install every language your shop uses:**

   ```bash
   bin/console translation:install --locales en-GB,de-DE
   ```

   It draws on the same source as the plugin — translate.shopware.com — but is updated more often, so
   the result is identical or newer.

2. **Activate the languages** under **Settings → Languages**.

3. **Create base snippet sets** for the languages in use:
   - **6.7.7.0 or later**: done automatically.
   - **6.7.6.0 or earlier**: create one per language by hand, e.g. `BASE en-US` for English (US).

4. **Point the sales channel domains at the base snippet sets:**
   - **Language Pack 5.37.1 or later**: done automatically.
   - **Language Pack 5.37.0 or earlier**: open each sales channel, scroll to its domains and change
     the snippet set from `LanguagePack` to `BASE` — `LanguagePack en-US` becomes `BASE en-US`.

5. **Uninstall and remove the plugin** once `translation:install` has succeeded for every locale.
   **Custom snippets survive**, because the snippet module stores them in the database.

## New installations

The installer offers the languages directly; they are downloaded and installed with the shop. No
language plugin is involved.

## Source

[developer.shopware.com/docs/guides/upgrades-migrations/language-pack-migration.html](https://developer.shopware.com/docs/guides/upgrades-migrations/language-pack-migration.html),
Shopware 6.7, retrieved 2026-08-21.
