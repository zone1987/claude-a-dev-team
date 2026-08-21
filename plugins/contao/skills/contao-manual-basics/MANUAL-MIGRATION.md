# Contao 5.x — Update and migration

Sources:
- https://docs.contao.org/5.x/manual/de/migration/
- https://docs.contao.org/5.x/manual/de/installation/contao-aktualisieren/
- https://docs.contao.org/5.x/manual/de/faq/

---

## Contents

- [Semantic versioning](#semantic-versioning)
- [Updating Contao (minor/bugfix)](#updating-contao-minorbugfix)
- [Migration Contao 3.5 → 4.x](#migration-contao-35--4x)
- [Migration Contao 4.13 → 5.x](#migration-contao-413--5x)
- [Common migration problems](#common-migration-problems)
- [FAQ — frequently asked questions](#faq--frequently-asked-questions)

## Semantic versioning

Contao follows semantic versioning:

| Type | Description | Example |
|-----|-------------|---------|
| **Major** | Comprehensive new version | 4 → 5 |
| **Minor** | Milestone with new functions | 5.6 → 5.7 |
| **Bugfix** | Maintenance update | 5.7.0 → 5.7.1 |

### Long-term support (LTS)

LTS versions receive:
- 3 years of bugfix support
- 1 year of security support

---

## Updating Contao (minor/bugfix)

### Via the Contao Manager

**Bugfix update:**
1. Open the Contao Manager
2. Click "Pakete aktualisieren" (Update packages)
3. When finished: check the database tables (install tool or `contao:migrate`)

**Minor update** (e.g. 5.6 → 5.7):
1. Open the Contao Manager
2. Click the cog icon on the Contao Manager bundle
3. Enter the desired version (e.g. `5.7.*`)
4. Click "Änderungen anwenden" (Apply changes)
5. Run the database migrations

### Via the command line

```bash
# Bugfix-Update
composer update

# Minor-Update: erst composer.json anpassen
# "contao/manager-bundle": "5.7.*"
composer update

# Datenbankmigrationen ausführen
vendor/bin/contao-console contao:migrate
```

### Local updates without the cloud (in case of memory limitations at the host)

1. Carry out the update locally on your own computer
2. Synchronise `vendor/` and `composer.lock` to the server
3. Run the database migrations via CLI on the server

### After every update

Always synchronise the database tables:
```bash
php vendor/bin/contao-console contao:migrate
```

Check the template files in `templates/` — they can change with updates!

---

## Migration Contao 3.5 → 4.x

### General principle

**Major versions cannot be skipped!**

Example: from 3.2.10 you must first update to 3.5.40 before 4.13.x is possible.

### Step by step

1. **Create a database backup** (before any changes!)
2. Set up a **fresh Contao 4 installation** on the server
3. **Copy the files** (into the new installation):
   - `files/` → `files/`
   - `templates/` → `templates/`
   - `system/config/localconfig.php` → `system/config/`
4. Point the **web server** at the `public/` subfolder of the new installation
5. Run the **database migrations**:
   ```bash
   php vendor/bin/contao-console contao:migrate
   ```
6. Check the **extensions**: are there versions updated for Contao 4?

### Checking templates

Especially important with every major version migration: check the overridden templates in `templates/` for compatibility.

---

## Migration Contao 4.13 → 5.x

### Version requirements

Adjust **composer.json**:

```json
{
    "require": {
        "contao/manager-bundle": "5.0.*"
    }
}
```

Allow caret notation for minor updates:
```json
"contao/manager-bundle": "^5.0"
```

### Updating the Composer scripts

Old (Contao 4):
```json
"scripts": {
    "post-install-cmd": [
        "Contao\\ManagerBundle\\Composer\\ScriptHandler::initializeApplication"
    ]
}
```

New (Contao 5):
```json
"scripts": {
    "post-install-cmd": [
        "@php vendor/bin/contao-setup"
    ]
}
```

### Adjusting the directory structure

The `web/` folder must be renamed to `public/`:
```bash
mv web public
```

Adjust **composer.json** (if present):
```json
{
    "extra": {
        "public-dir": "public"
    }
}
```

Set the document root in the web server to `public/`.

### Folder relocations

| Old | New |
|-----|-----|
| `app/config/` | `config/` |
| `app/Resources/contao/` | `contao/` |
| `app/Resources/public/` | `public/` |
| `app/Resources/translations/` | `translations/` |

### Removed configurations

Remove the following configurations from `config.yaml` (no longer supported in Contao 5):
- `contao.prepend_locale`
- `contao.url_suffix`
- `contao.legacy_routing`
- `contao.encryption_key`

### Exporting internal stylesheets

**In Contao 5 the internal CSS editor is gone.** Existing stylesheets must be migrated:

1. Export all internal stylesheets in the backend
2. Save them as external `.css` files
3. Include them in Seitenlayouts (page layouts) as external stylesheets

### Migrating templates

**All content elements** are newly implemented in Contao 5 with **Twig templates**. Old HTML5 templates no longer take effect automatically.

**Migration steps:**
1. Identify the existing PHP templates in `templates/`
2. Create the corresponding Twig equivalents
3. Check them in the Seitenlayouts

### Starting the migration

```bash
vendor/bin/contao-console contao:migrate
```

---

## Common migration problems

### Database server not in strict mode

Contao recommends MySQL strict mode. Activation:
```sql
SET GLOBAL sql_mode = 'TRADITIONAL';
```

Or in `my.cnf`:
```ini
sql_mode = TRADITIONAL
```

### Renaming web/ to public/ (FAQ)

If you are still on a Contao version with `web/`:
1. Rename the folder: `mv web public`
2. Adjust or remove the Composer entry
3. Set the document root in the web server anew
4. Run `composer install`

### Changing the backend path

In `config/config.yaml`:
```yaml
contao:
    backend:
        route_prefix: '/admin'
```

Clear the cache:
```bash
php vendor/bin/contao-console cache:clear --env=prod --no-warmup
php vendor/bin/contao-console cache:warmup --env=prod
```

### Renewing the application cache

```bash
vendor/bin/contao-console cache:clear --no-warmup
vendor/bin/contao-console cache:warmup
```

---

## FAQ — frequently asked questions

### General

**Forgotten the administrator password?**
- Reset several admin flags in `tl_user`, then create a new admin in the install tool
- Via CLI: `php vendor/bin/contao-console contao:user:create --admin`

**Manage several websites?**
- Multi-domain operation: several Website-Startseiten (website start pages) in one installation
- Multilingual: separate start pages per language

**Commercial use?**
- Yes! The LGPL permits commercial projects

**Enable debug mode?**
- Backend: click the bug icon
- Or: `APP_ENV=dev` in `.env.local`

**White page while editing?**
- Frequently caused by browser extensions (e.g. LanguageTool)
- Solution: test in incognito mode

### Template

**Show template variables?**
- Documentation: "Template-Daten anzeigen" (Show template data)

**Configure TinyMCE?**
- Create your own `config.js` under `contao/config/tinymce.js`

**Add a CSS class to headlines?**
- Via the `_headline` Twig component (not with old PHP templates)

### Configuration

**Change the backend path?**
- `route_prefix` in `config.yaml` + clear the cache

**E-mail via forms?**
- Configure SMTP in `parameters.yaml` or `.env.local`

**URL prefix for languages?**
- In the starting point: enter the URL-Präfix (URL prefix, e.g. `de`)

**Add the HTML suffix `.html`?**
- In the starting point: enter the URL suffix

### Dateiverwaltung (File Management)

**Images not visible in the frontend?**
- Mark the image directory as "Öffentlich" (Public)
- Check old `.htaccess` files

### Theme

**SCSS changes are not applied?**
- Clear the script cache: System → Systemwartung (System maintenance) → Daten bereinigen (Purge data)

### Contao Manager

**Manager hangs/does not respond?**
- Delete the file `contao-manager/task.json`

**Update the Manager?**
- Automatically in the background; or upload a new `.phar` via FTP

**Rename the `.phar` file?**
- Possible; adjust it in `config.yaml`:
  ```yaml
  contao_manager:
      manager_path: dein-name.phar.php
  ```
  Then clear the cache.

**Install a specific Contao version?**
- In the Contao Manager: use expert mode, enter the version manually
