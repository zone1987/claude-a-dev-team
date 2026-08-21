# Shopware 6 — Staging & test environment: complete reference

## Contents

- [Terms and differences](#terms-and-differences)
- [4-step process: setting up a staging instance](#4-step-process-setting-up-a-staging-instance)
- [What staging mode does NOT do](#what-staging-mode-does-not-do)
- [App management after activating staging](#app-management-after-activating-staging)
- [Protecting the staging environment](#protecting-the-staging-environment)
- [Test environment for updates: best practices](#test-environment-for-updates-best-practices)

## Terms and differences

### Staging environment
A completely separate, non-production copy of the live shop with:
- **Its own hosting** (a separate server or container)
- **Its own domain** (e.g. staging.meinshop.de)
- **Its own database** (a clone of the live DB)
- **Its own Redis instance** (separate from live!)
- **Its own Elasticsearch/OpenSearch index prefix**
- **Its own .env configuration**

### Staging mode (since Shopware 6.6.1.0)
A Shopware mechanism activated via `bin/console system:setup:staging` which:
- Severs app connections to production
- Disables e-mail sending
- Rewrites URLs to the staging domain
- Shows a banner in the admin and the storefront

> **Critical:** `system:setup:staging` duplicates NO database and NO files — that has to be done separately.

---

## 4-step process: setting up a staging instance

### Step 1: set up a separate installation

**Recommended:** deploy into the new environment from the Git repository.

```bash
# Neue Domain/Subdomain einrichten
# z.B.: staging.meinshop.de

# .env anpassen
APP_URL=https://staging.meinshop.de
APP_ENV=prod
APP_SECRET=<neues-geheimes-secret>
```

> **Licence note:** in the Shopware Account licence, keep using the **live domain** to avoid licence problems. Shopware tolerates staging instances under other domains.

### Step 2: clone the database

#### Option A: shopware-cli (recommended)

```bash
# Standard-Dump (ohne Cart-Daten, "clean")
shopware-cli project dump \
  --clean \
  --host localhost \
  --username db_user \
  --password db_pass \
  --output shop.sql \
  shopware_datenbankname

# Dump mit anonymisierten Kundendaten (DSGVO-konform)
shopware-cli project dump \
  --clean \
  --anonymize \
  --host localhost \
  --username db_user \
  --password db_pass \
  --output shop-anon.sql \
  shopware_datenbankname
```

**What --anonymize anonymises:**
- Customer names → random names
- E-mail addresses → example.com addresses
- Phone numbers → random numbers
- Addresses → generic addresses

#### Option B: mysqldump (the classic way)

```bash
# Vollständiger Dump
mysqldump -u user -p --single-transaction shopware_db > backup.sql

# Dump ohne Session/Log-Tabellen (schneller)
mysqldump -u user -p --single-transaction \
  --ignore-table=shopware_db.messenger_messages \
  --ignore-table=shopware_db.dead_message \
  shopware_db > backup.sql
```

> **Warning:** `mysqldump` and `mysql` must have the same major version and the same vendor (MySQL/MariaDB).

#### Importing the dump into the staging database

```bash
# Staging-Datenbank vorbereiten
mysql -u staging_user -p -e "CREATE DATABASE IF NOT EXISTS staging_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Dump einspielen
mysql -u staging_user -p staging_db < shop-anon.sql

# Mit Fortschrittsanzeige (pv muss installiert sein)
pv shop-anon.sql | mysql -u staging_user -p staging_db
```

### Step 3: configure staging

#### Adjusting .env for staging

```bash
# Staging .env (config/packages/.env oder .env.local)
APP_URL=https://staging.meinshop.de
DATABASE_URL=mysql://staging_user:password@localhost:3306/staging_db

# Redis (GETRENNT von Live!)
REDIS_URL=redis://localhost:6380

# Elasticsearch/OpenSearch (GETRENNT von Live!)
SHOPWARE_ES_INDEX_PREFIX=staging_
SHOPWARE_ES_HOSTS=localhost:9200

# Oder Elasticsearch komplett deaktivieren für Staging
SHOPWARE_ES_ENABLED=0
```

> **CRITICAL:** NEVER share Redis and Elasticsearch between live and staging. Different data → data loss and inconsistencies.

#### staging.yaml configuration

Create the file: `config/packages/staging.yaml`

```yaml
shopware:
    staging:
        mailing:
            disable_delivery: true      # Keine Mails an echte Kunden!
        storefront:
            show_banner: true           # Staging-Banner in Storefront
        administration:
            show_banner: true           # Staging-Banner in Admin
        sales_channel:
            domain_rewrite: []          # URL-Umschreibung konfigurieren
        elasticsearch:
            check_for_existence: true   # Prüft ob ES-Index bereits existiert
```

#### URL rewriting (three methods)

**Method 1: direct exchange (equal)**
```yaml
shopware:
    staging:
        sales_channel:
            domain_rewrite:
                - type: equal
                  match: https://www.meinshop.de
                  replace: https://staging.meinshop.de
```

**Method 2: prefix replacement (prefix)**
```yaml
shopware:
    staging:
        sales_channel:
            domain_rewrite:
                - type: prefix
                  match: https://www.meinshop.de
                  replace: https://staging.meinshop.de
```

**Method 3: regex replacement (regex)**
```yaml
shopware:
    staging:
        sales_channel:
            domain_rewrite:
                - type: regex
                  match: '/https?:\/\/(\w+)\.(\w+)$/m'
                  replace: 'http://$1-$2.local'
```

### Step 4: activate staging mode

```bash
# Interaktiv (Bestätigung erforderlich)
bin/console system:setup:staging

# Nicht-interaktiv (für Scripts/CI)
bin/console system:setup:staging --no-interaction --force
```

**What the command carries out:**
1. Deletes all apps with active external connections
2. Resets the instance ID (prevents app conflicts with live)
3. Disables e-mail sending
4. Rewrites the sales channel URLs (from the domain_rewrite configuration)
5. Verifies the Elasticsearch indexes (checking for existence)
6. Activates the staging banner in the admin and the storefront

---

## What staging mode does NOT do

| Not included | Has to be done separately |
|---|---|
| Duplicating the database | mysqldump / shopware-cli project dump |
| Copying files | rsync / hosting tools |
| Modifying the live environment | — |
| Setting up hosting | Hosting provider / DevOps |

---

## App management after activating staging

The staging command **deletes all apps** with external connections (Shopware App Server, external APIs).

After activating staging:
```bash
# Apps neu installieren (generiert neue Instanz-IDs)
bin/console app:install <app-name>
# oder über Admin: Erweiterungen > Apps > Installieren
```

For plugin developers: subscribing to the staging event
```php
use Shopware\Core\Maintenance\Staging\Event\SetupStagingEvent;

public static function getSubscribedEvents(): array
{
    return [SetupStagingEvent::class => 'onSetupStaging'];
}

public function onSetupStaging(SetupStagingEvent $event): void
{
    // Eigene Staging-Initialisierung
    // z.B. Test-API-Keys setzen, Webhooks deaktivieren
}
```

---

## Protecting the staging environment

The staging environment should be protected against public access:

### Apache: basic auth
```apache
# .htaccess im Web-Root
AuthType Basic
AuthName "Staging"
AuthUserFile /pfad/zu/.htpasswd
Require valid-user
```

```bash
# .htpasswd erstellen
htpasswd -c /pfad/zu/.htpasswd staging_user
```

### Nginx: basic auth
```nginx
server {
    auth_basic "Staging";
    auth_basic_user_file /pfad/zu/.htpasswd;
}
```

### IP restriction (Apache)
```apache
Order Deny,Allow
Deny from all
Allow from 192.168.1.0/24
Allow from 10.0.0.100
```

### IP restriction (Nginx)
```nginx
allow 192.168.1.0/24;
allow 10.0.0.100;
deny all;
```

### Cloudflare Access / Azure Application Gateway
- An OAuth2 proxy solution
- Staff login via SSO
- No separate password management needed

---

## Test environment for updates: best practices

### Workflow for update tests

1. **Create a database snapshot** (live → staging)
2. **Synchronise the files** (`rsync` from live → staging)
3. **Activate staging mode** (`system:setup:staging`)
4. **Run the update on staging** (admin or Composer)
5. **Test:** storefront, admin, ordering process, extensions
6. **If everything is fine:** run the update on live
7. **If there are errors:** use staging for debugging; live stays untouched

### Checklist after the update on staging

- [ ] The home page loads correctly
- [ ] The admin login works
- [ ] Products are displayed
- [ ] Placing an order is possible (test order)
- [ ] All activated extensions work
- [ ] The theme is rendered correctly
- [ ] E-mails are NOT sent (staging mode active)
- [ ] No PHP errors in the logs (`var/log/`)

---

*Source: https://developer.shopware.com/docs/guides/hosting/installation-updates/creating-a-staging-instance.html*
*Additionally: https://docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten*
