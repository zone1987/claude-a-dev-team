# Contao 5.x — Installation

Sources:
- https://docs.contao.org/5.x/manual/en/installation/system-requirements/
- https://docs.contao.org/5.x/manual/en/installation/install-contao/
- https://docs.contao.org/5.x/manual/en/installation/update-contao/
- https://docs.contao.org/5.x/manual/en/installation/contao-manager/
- https://docs.contao.org/5.x/manual/en/installation/install-extensions/
- https://docs.contao.org/5.x/manual/en/guides/local-installation/ddev/
- https://docs.contao.org/5.x/manual/en/guides/local-installation/devilbox/
- https://docs.contao.org/5.x/manual/en/guides/local-installation/laragon/
- https://docs.contao.org/5.x/manual/en/guides/local-installation/xampp/

---

## Contents

- [System requirements](#system-requirements)
- [Installation](#installation)
- [Updating Contao](#updating-contao)
- [The Contao Manager](#the-contao-manager)
- [Extensions](#extensions)
- [Local development environments](#local-development-environments)

## System requirements

### Recommended versions

| Software | Minimum version | Recommended |
|----------|---------------|-----------|
| PHP | 8.1 | 8.4+ (latest patch version) |
| MySQL | 5.7.6 / MariaDB 10.4.3 | 8.0+ |

### Required PHP extensions

DOM, PCRE, Intl, PDO, ZLIB, JSON, Curl, Mbstring, GD, File Information.
As of PHP 8.3: additionally **Sodium**.

### Image processing

Contao automatically chooses an image processing library:
- GD: required (default)
- ImageMagick or GraphicsMagick: better performance

### MySQL requirements

- Table format: **InnoDB**
- Character set: **UTF8mb4**
- Minimum version as of Contao 5.6: MySQL 5.7.6 or MariaDB 10.4.3

### Web server configuration

- The **document root** must point to the `public/` subfolder
- URL rewriting must be enabled (all requests through `index.php`)
- Each Contao installation requires its own (sub)domain

---

## Installation

### Route 1: Contao Manager (recommended for beginners)

#### Step 1 — install the Contao Manager

1. Download `contao-manager.phar` from contao.org
2. Rename the file in `public/` to `contao-manager.phar.php`
3. Upload it to the server via FTP/SFTP

#### Step 2 — call up and configure the Manager

URL: `https://www.example.com/contao-manager.phar.php`

![Contao Manager welcome page](assets/contao-manager-willkommen.png)

Basic configuration:
- Create a new Manager user (independent of the later Contao user)
- The PHP binary path is detected automatically
- Enable the **Composer Resolver Cloud** (if the server has little RAM): dependencies are resolved in the Contao Association's cloud

#### Step 3 — install Contao

In the Manager: choose the desired version → initial configuration → click "Installieren" (Install).
The installation takes several minutes. The console output can be viewed via the icon.

#### Step 4 — update the database

Open the Contao install tool → check and apply the database changes.

---

### Route 2: command line (Composer)

#### Prerequisites

SSH access to the server, Composer installed.

#### Installation

```bash
# SSH verbinden
ssh benutzername@example.com
cd www

# Contao installieren (example = Zielverzeichnis, 5.7 = Version)
php composer.phar create-project contao/managed-edition example 5.7
```

#### Configure the hosting

Point the document root to `/www/example/public`.

#### Update the database

```bash
php vendor/bin/contao-console contao:migrate

# Optional: Datenbank anlegen
php vendor/bin/contao-console doctrine:database:create
```

Database connection in `config/parameters.yaml` or `.env`:
```yaml
parameters:
    database_host: localhost
    database_port: 3306
    database_user: root
    database_password: null
    database_name: contao
```

#### Create a backend user

```bash
php vendor/bin/contao-console contao:user:create
```

---

## Updating Contao

### Update cycle (semantic versioning)

| Type | Example | Meaning |
|-----|---------|-----------|
| **Major release** | 5.x | Completely new version, breaking changes possible |
| **Minor release** | 5.7 | New functions, minor adjustments necessary |
| **Bugfix release** | 5.7.1 | Bug fixing, unproblematic |
| **LTS** | 4.13, 5.3 | 3 years of bugfixes + 1 year of security updates |

**Before every update:** create backups of `composer.json`, `composer.lock` and the database!

### Update via the Contao Manager

**Bugfix update**: click "Pakete aktualisieren" (Update packages) in the Manager.

**Minor update**: cog icon next to "Contao Open Source CMS" → enter the desired version → "Pakete aktualisieren" → "Änderungen anwenden" (Apply changes).

Then open the install tool and apply the database changes.

### Update via the command line

**Bugfix update**:
```bash
composer update
```

**Minor update** — first adjust `composer.json`:
```json
{
    "require": {
        "contao/manager-bundle": "5.7.*"
    }
}
```
Then:
```bash
composer update
vendor/bin/contao-console contao:migrate
```

### Local update (without the Composer Resolver Cloud)

Useful when the hosting server has too little RAM for `composer update`:

1. Copy `composer.json` and `composer.lock` from the server locally
2. Run `composer update` locally (saves server resources)
3. Copy the updated `composer.lock` back to the server
4. On the server: `composer install` (install only, do not resolve)
5. Update the database

For differing PHP versions in `composer.json`:
```json
"config": {
    "platform": {
        "php": "8.2.99"
    }
}
```

---

## The Contao Manager

### Functions

- Install and update Contao
- Search for, install and remove extensions
- Clear the cache (Systemwartung / system maintenance)
- Invite users (as of Manager 1.9)

### Common problems

#### Forgotten password

1. Delete `contao-manager/users.json` via FTP
2. Call up the Manager URL → create a new admin user
3. If the login screen still appears: delete the cookies or use incognito mode

#### The Manager hangs

Delete the file `contao-manager/task.json` → the Manager should work again.

#### Renaming the Manager (`.phar` file)

Any file name is possible. Enter it in `config/config.yaml`:
```yaml
contao_manager:
    manager_path: dein-name.phar.php
```
Then clear the app cache.

### Manager user roles (as of version 1.9)

| Role | Permissions |
|-------|---------------|
| READ | View packages, read logs |
| UPDATE | Update packages, maintenance tasks |
| INSTALL | Install packages, system settings |
| ADMIN | Full access including user management |

---

## Extensions

### Searching

- Website: extensions.contao.org
- In the Contao Manager: search field in an existing installation
- Command line: `php composer.phar search <suchbegriff>`

### Installation via the Contao Manager

1. Log in to the Manager
2. Search for the extension (e.g. "EasyThemes")
3. Click "Hinzufügen" (Add) (repeat for further extensions)
4. "Pakete" (Packages) tab → "Änderungen anwenden" (Apply changes)
5. When finished: install tool for the database update

### Installation via the command line

```bash
# Einzelne Erweiterung
php composer.phar require terminal42/contao-easy_themes

# Mehrere Erweiterungen
php composer.phar require terminal42/notification_center terminal42/contao-leads

# Datenbank aktualisieren
php vendor/bin/contao-console contao:migrate
```

---

## Local development environments

### DDEV (recommended, cross-platform)

**Prerequisite**: Docker installed.

#### Setup via Composer

```bash
mkdir contao && cd contao

# DDEV konfigurieren
ddev config --project-type=php --docroot=public --webserver-type=apache-fpm --php-version=8.2

# Contao 5.7 installieren
ddev composer create-project contao/managed-edition:5.7

# Set the database connection and the mailer
ddev dotenv set .env.local --database-url=mysql://db:db@db:3306/db --mailer-dsn=smtp://localhost:1025

# Datenbank migrieren
ddev exec contao-console contao:migrate --no-interaction

# Admin-Benutzer anlegen
ddev exec contao-console contao:user:create \
    --username=admin --name=Administrator \
    --email=admin@example.com --language=de \
    --password=Password123 --admin

# Backend öffnen
ddev launch contao
```

#### Useful DDEV commands

| Command | Function |
|--------|---------|
| `ddev start` / `ddev stop` | Start/stop the project |
| `ddev poweroff` | Stop all containers |
| `ddev ssh` | Open the container shell |
| `ddev describe` | Show services and credentials |
| `ddev xdebug on` | Enable XDebug |

#### Setting up a DDEV cronjob (as of Contao 5.5)

```bash
ddev add-on get ddev/ddev-cron
```

Create the file `/.ddev/web-build/contao.cron`:
```
* * * * * php /var/www/html/vendor/bin/contao-console contao:cron
```

Then: `ddev restart`

#### Database tools

```bash
# Adminer
ddev add-on get ddev/ddev-adminer && ddev restart

# phpMyAdmin
ddev add-on get ddev/ddev-phpmyadmin && ddev restart
```

---

### Docker Devilbox

**Prerequisite**: Docker and Docker Compose installed.

#### Configuration (`.env` file)

```
HTTPD_DOCROOT_DIR=public
HTTPD_SERVER=apache-2.4
PHP_SERVER=8.2
MYSQL_SERVER=mariadb-10.3
```

**Important**: do not delete the entries, only comment/uncomment them.

#### Starting Devilbox

```bash
# First run, in the foreground so errors are visible
docker-compose up httpd php mysql

# Folgestarts im Hintergrund
docker-compose up -d httpd php mysql
```

#### Stopping Devilbox

```bash
docker-compose stop
docker-compose rm -f
```

#### Installing Contao

1. Create a directory in `data/www/contao4/`
2. Create the subfolder `public/`
3. Copy the Contao Manager (`contao-manager.phar.php`) into it
4. In `/etc/hosts`: enter `127.0.0.1 contao4.loc`
5. In the browser: `http://contao4.loc/contao-manager.phar.php`

#### Database credentials (Devilbox)

| Entry | Value |
|---------|------|
| Host | mysql |
| User name | root |
| Password | (empty) |

---

### Laragon (Windows)

#### Prerequisites

Windows 7–10, set up symlink permission for a normal user (via Polsedit: policy "Create symbolic links").

#### Installation

1. Download `laragon-wamp.exe` from github.com/leokhoa/laragon
2. Install it, start the services
3. Install Composer globally
4. Adjust `laragon\usr\laragon.ini`: extend `QuickSettings` with `sys_temp_dir`
5. Set the PHP memory limit to `-1`

#### Installing Contao via Laragon

Menu → new website → "Contao 4.9 Website…" (or the corresponding version) → enter the project name.

Laragon automatically creates:
- A database with the project name
- A virtual host `projektname.local`

#### URLs after the installation

| Target | URL |
|------|-----|
| Frontend | http://mycompany.local/ |
| Backend | http://mycompany.local/contao |
| Install tool | http://mycompany.local/contao/install |
| Manager | http://mycompany.local/contao-manager.phar.php |

---

### XAMPP (Windows)

#### Configuration

1. Unpack XAMPP Portable, run `setup_xampp.bat`
2. Start `xampp-control.exe` as administrator
3. In `apache\php.ini`: enable `memory_limit = -1` and `extension=intl`
4. Add at the end of `httpd.conf` (increase the ThreadStackSize):

```apache
<IfModule mpm_winnt_module>
    ThreadStackSize 8388608
</IfModule>
```

#### Installing Composer

In the XAMPP shell:
```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```

#### Installing Contao

```bash
php ../composer.phar create-project contao/managed-edition demo 5.7
```

#### Configuring a vHost (recommended)

In `\apache\conf\extra\httpd-vhosts.conf`:
```apache
<VirtualHost *:80>
  DocumentRoot "D:\vhost\demo\public"
  ServerName demo.local
  <Directory D:\vhost\demo>
    Options +FollowSymlinks
    AllowOverride All
    Require all granted
  </Directory>
</VirtualHost>
```

In `C:\Windows\System32\drivers\etc\hosts`:
```
127.0.0.1 demo.local
```

## Moving an installation

**Source:** https://docs.contao.org/5.x/manual/en/installation/move-contao/

This page describes moving a Contao installation from one location to another (for example from a local installation to a live server). It is almost the same as a new installation but also includes transferring the existing database and application related files.

The overall order is: 1. Transferring the database, 2. Setting up web space, 3. Transferring the files, 4. Installing Contao.

**Warning (prerequisite):** to reduce the risk of conflicts, the source and target server must both run the **same PHP version**.

### Transferring the database: export the database (source)

A SQL dump can be created either with the graphical database administration tool phpMyAdmin or with the `mysqldump` program from the command line.

phpMyAdmin variant:

1. Log into "phpMyAdmin", select the database to export, select the "Export" tab in the upper menu and click "Ok".
2. A `sql` file is returned that is imported in the next step.

Command line variant:

1. Make sure `mysqldump` and `gzip` are installed, then run the following command (replacing "my_user" and "my_db_name" with the database user and database name):

```bash
mysqldump --host=localhost --user=my_user --password --hex-blob --opt my_db_name | gzip -c > my_dump.sql.gz
```

2. Enter the database password if asked for.
3. A `my_dump.sql.gz` file containing the dumps is saved in the current directory and is used in the next step.

### Transferring the database: import the database (target)

phpMyAdmin variant:

1. Open "phpMyAdmin" and select a new (empty) database.
2. Click on the "Import" button in the upper menu, upload the previously created SQL dump and start the import.

Command line variant:

1. Copy the previously created dump file to the target machine and navigate to it.
2. Make sure `mysql` and `gunzip` are installed, then run the following command (replacing "my_user" and "my_db_name" with the database user and database name as well as "my_dump.sql.gz" with the appropriate file name of the copied dump):

```bash
gunzip < my_dump.sql.gz | mysql --host=localhost --user=my_user --password my_db_name
```

3. Enter the database password if asked for.

### Preparing your web space

1. Create a folder called `public` in the **empty** web space.
2. Copy the latest version of the file `contao-manager.phar.php` (available on the Contao website) into **the public folder that was created**.

### Transferring the files

The following files and folders must be transferred from the source server to the **main folder** (**not** `public`) on the destination server:

- **`files`**: the site's files.
- **`templates`**: the site's templates.
- **`composer.json`**: wished dependencies.
- **`composer.lock`**: actually installed dependencies.
- **`system/config/localconfig.php`**: the site's preferences.

The following files and folders need to be transferred from the source to the target machine, if applicable:

- **`config`**: or, **before Contao 4.8**, `app/config/`.
- **`contao`**: or, **before Contao 4.8**, `app/Resources/contao/`.
- **`src`**: not further described upstream.
- **`.env*`**: not further described upstream.

If old extensions still exist within `system/modules/`, or if there are old configurations in the directory `system/config/`, then they have to be transferred as well.

An FTP client can be used for this task, or `scp` from the command line:

```bash
cd /path/to/project

scp -r files/ templates/ composer.json composer.lock your_server:/www/project/
```

### Installing Contao

1. Make sure the hosting configuration is correctly set up (the public root points to `public`).
2. Then let *Composer* do its work. As the `composer.lock` file containing all package version details from the original server was also transferred, Composer will replicate the identical state as before. To do so, either use the Contao Manager or the command line like with a regular installation.
3. If the command line is not to be used, open this URL in the browser: `https://example.com/contao-manager.phar.php`. The Contao Manager launches and asks for a username and password for the Contao Manager. The Contao installation then begins. Finally, a connection to the database is established. In Contao 5, there is no longer an installation tool; step 4 is not possible or required.
4. Run the install tool to configure the new database connection.

**Info note:** if the installation has not been moved to another server and a 1:1 copy has simply been created on the same server, delete and recreate the application cache via the Contao Manager after adjusting the database connection, to ensure that the changes are applied correctly and that the correct database is in use.

## Updating extensions

**Source:** https://docs.contao.org/5.x/manual/en/installation/update-extensions/

This page describes updating Contao extensions either with the Contao Manager or via the command line with Composer.

### Updating with the Contao Manager

1. Log in to Contao Manager by calling up the domain with the addition `/contao-manager.phar.php` and entering the access data.
2. To update the extension "terminal42/contao-easy_themes", switch to the "Packages" tab and click the "Update" button next to the extension. Other extensions can also be reserved for update at the same time.
3. Click on "Apply changes" to start the update. The update can take several minutes. Details of the update process can be displayed by clicking on the console output icon.
4. Once the Contao Manager has updated the extension(s), run the Contao-Installtool to update the database if necessary.

### Update via the command line

Prerequisite: SSH access to the server with username and domain.

1. Log in to the server:

```bash
ssh username@example.com
```

2. Go to the directory of the Contao installation:

```bash
cd www/example/
```

3. To get the latest version of an extension and update the `composer.lock`, the command `update` is executed.

Update a single extension:

```bash
php composer.phar update terminal42/contao-easy_themes
```

Update multiple extensions:

```bash
php composer.phar update terminal42/notification_center terminal42/contao-leads
```

4. To display a list of installed extensions for which updates are available, including their current and latest versions, the command `outdated` can also be used:

```bash
php composer.phar outdated
```

Result of the query:

```bash
doctrine/dbal               v2.8.1 v2.9.2  Database Abstraction Layer
knplabs/knp-menu            2.6.0  v3.0.1  An object oriented menu library
monolog/monolog             1.25.1 2.0.0   Sends your logs to files, sockets, inboxes, databases …
php-http/client-common      1.9.1  2.0.0   Common HTTP Client implementations and tools for HTTPlug
php-http/guzzle6-adapter    v1.1.1 v2.0.1  Guzzle 6 HTTP Adapter
php-http/httplug            v1.1.0 v2.0.0  HTTPlug, the HTTP client abstraction for PHP
sensiolabs/security-checker v5.0.3 v6.0.2  A security checker for your composer.lock
```

5. Once the update of the extension(s) is complete, run the Contao-Installtool to update the database if necessary.

**Caveat:** on some hosters the `update` command causes the process to fail because the system requirements are too high, and the update fails. In this case the Contao Manager should be used instead.

## Uninstalling extensions

**Source:** https://docs.contao.org/5.x/manual/en/installation/uninstalling-extensions/

This page describes uninstalling Contao extensions either with the Contao Manager or via the command line with Composer.

### Uninstalling with Contao Manager

1. Log in to Contao Manager by calling up the domain with the addition `/contao-manager.phar.php` and entering the access data.
2. To uninstall the extension "terminal42/contao-easy_themes", go to the "Packages" tab and click on the "Remove" button next to the extension. Other extensions can also be reserved for uninstallation at the same time.
3. Click on "Apply changes" to start the uninstallation. The uninstallation can take several minutes. Details of the uninstallation process can be displayed by clicking on the console output icon.
4. Once the Contao Manager has uninstalled the extension(s), run the Contao-Installtool to update the database if necessary.

### Uninstalling using the command line

Prerequisite: SSH access to the server with username and domain.

1. Log on to the server:

```bash
ssh username@example.com
```

2. Then go to the directory of the Contao installation:

```bash
cd www/example/
```

3. The command `remove` removes the extension from the `composer.json` and deletes the code from the project. To remove an extension and update the `composer.lock`, the command `remove` is executed.

Uninstall a single extension:

```bash
php composer.phar remove terminal42/contao-easy_themes
```

Uninstall multiple extensions:

```bash
php composer.phar remove terminal42/notification_center terminal42/contao-leads
```

4. Once the uninstallation of the extension(s) is complete, run the Contao-Installtool to update the database if necessary.

**Caveat:** this will cause some hosters to not be able to finish the process because of the high system load and the update will fail. In this case the Contao Manager should be used instead.

## The Contao Install Tool

**Source:** https://docs.contao.org/5.x/manual/en/installation/contao-installtool/

This page describes the Contao Install Tool, with which a database connection is created, tables are updated, templates are imported and an administrator account is created.

**Info note:** the Contao Install Tool no longer exists as of Contao 5, as the database can be updated directly via the Contao Manager or the console.

### Access

1. In the browser, open the URL of the Contao installation and add the `/contao/install` path to access the Install Tool, for example `www.example.com/contao/install`.
2. Accept the license and create a password with which the Install Tool can be accessed again later.

### Create database connection

The Contao Install Tool cannot create new databases itself because most shared hosting packages only allow this with the management software (for example Confixx, Plesk or cPanel).

1. Go to the management interface of the server and create a new database there.
2. Then enter the credentials for the database in the Contao Install Tool.

- **Host**: the domain or IP address of the database server.
- **Port number**: the port number of the database server, which can be changed here.
- **Username**: the username for the database.
- **Password**: the password.
- **Database**: the name of the database.

### Update tables

1. After the database access data has been saved, the Install Tool connects to the database and compares the tables with the current version of Contao.
2. If an update is necessary, the Install Tool automatically presents a list of changes that can be confirmed or rejected.

Usually the offered changes should be accepted so that the tables are always up to date and Contao does not try to access missing fields later. For a new installation, the list of changes is usually very long since all tables have to be created first.

If multiple applications share a database on the server, the Install Tool offers the possibility to "clean up" the tables of the other applications that are not needed.

**Warning:** although it is technically possible to run multiple applications in one database, a separate database should be used for each application.

### Importing a Template

At this point a `.sql` file from the `/templates` directory can be imported. This will delete all existing data. To import a theme instead, the theme manager in the Contao back end should be used.

**Warning:** when a template is imported, existing data is overwritten.

### Create an administrator account

If no template was imported, for example when creating a new website with Contao, an administrator user must be created that can be used to log in to the Contao back end later.

- **Username**: the username of the administrator.
- **Name**: the first and last name of the administrator.
- **e-mail address**: the email address of the administrator.
- **Password**: the password of the administrator, set and confirmed here.

After the administrator user has been created, the installation of Contao is complete and the link at the bottom right redirects to the back end.

## When the Contao Manager fails

**Source:** https://docs.contao.org/5.x/manual/en/installation/contao-manager-error/

This page covers the single failure case in which the Contao Manager cannot be accessed after uploading it, and the workaround for it.

### The Contao Manager cannot be accessed

Situation: the Contao Manager, consisting of a single file, has been downloaded from contao.org and the file `contao-manager.phar.php` has been transferred to the `public` directory on the web server.

The download file `contao-manager.phar.php` is a PHP script that downloads the required file in the background and then overwrites itself.

However, when the URL `www.example.com/contao-manager.phar.php` is called up, the welcome page of the Contao Manager does not appear.

1. In this case, try uploading the `.phar` file directly, from `https://download.contao.org/contao-manager.phar`.

**Note:** `.phar` files are not executed by all hosting providers. For best compatibility, add the file extension `.php` (final file name: `contao-manager.phar.php`).

**Warning:** `.php` files are transferred by most FTP programs in text mode instead of binary mode, which destroys the manager file. Therefore, add the file extension `.php` only after the upload.

## Backend search requirements

**Source:** https://docs.contao.org/5.x/manual/en/installation/system-requirements/backend-search/

This page documents the requirements and configuration of the Contao back end search, which is based on the PHP-CMSIG "SEAL" (Search Engine Abstraction Layer) project. Available as of version 5.5.0.

SEAL has the same goal as Doctrine DBAL: while Doctrine DBAL focuses on abstracting various database servers, PHP-CMSIG SEAL abstracts different search engines. The advantage in both cases is that, ideally, Contao can be used with different databases and search engines and benefit from their respective advantages.

### Basic Requirements

Every search engine works in a relatively similar way. Content (usually called a "document") is provided to it, which is then processed so that it can be efficiently searched. There are various techniques to meet different requirements. Examples given upstream: searching for "systems" also finding "system" (Stemming); searching for "Markdwon" also finding "Markdown" (Typo Tolerance); searching for "warm clothing" also finding "gloves" (AI Embeddings). Not all search engines support all functions. Some are faster but less accurate. Others have specific system requirements.

### Basic Requirement 1: The Cronjob Framework

All search engines have one thing in common: processing documents can take a long time. Making an entire Contao back end searchable, including all its content, can take several minutes depending on the system's size. The exact duration depends on the amount of content and the search engine used.

For this reason, Contao requires the ability to index the content in the background via the command line, where typical 30-second limits, as with a web server, do not exist.

1. The simplest way to meet this requirement is to set up the Contao Cronjob Framework.

### Basic Requirement 2: A Search Engine

SEAL supports a variety of search engines. To use a specific search engine, the appropriate adapter is needed, which can be installed via Composer.

- **Elasticsearch**: required Composer package `cmsig/seal-elasticsearch-adapter`. Example DSN: `elasticsearch://127.0.0.1:9200`. Notes: not stated upstream.
- **Opensearch**: required Composer package `cmsig/seal-opensearch-adapter`. Example DSN: `opensearch://127.0.0.1:9200`. Notes: not stated upstream.
- **Meilisearch**: required Composer package `cmsig/seal-meilisearch-adapter`. Example DSN: `meilisearch://apiKey@127.0.0.1:7700`. Notes: not stated upstream.
- **Algolia**: required Composer package `cmsig/seal-algolia-adapter`. Example DSN: `algolia://YourApplicationID:YourAdminAPIKey`. Notes: not stated upstream.
- **Solr**: required Composer package `cmsig/seal-solr-adapter`. Example DSN: `solr://solr:SolrRocks@127.0.0.1:8983`. Notes: not stated upstream.
- **Redisearch**: required Composer package `cmsig/seal-redisearch-adapter`. Example DSN: `redis://phpredis:phpredis@127.0.0.1:6379`. Notes: not stated upstream.
- **Typesense**: required Composer package `cmsig/seal-typesense-adapter`. Example DSN: `typesense://S3CR3T@127.0.0.1:8108`. Notes: not stated upstream.
- **Loupe**: required Composer package `cmsig/seal-loupe-adapter`. Example DSN: `loupe://var/indexes/`. Note: Loupe runs on the local filesystem and only requires PHP and an SQLite database. The minimal requirement is that either `sqlite3` or `pdo_sqlite` is available in the PHP setup.

The back end search is configured via DSN in `config.yaml`:

```yaml
# config/config.yaml
contao:
    backend_search:
        enabled: true # Can be omitted if DSN is set. But can be disabled with "false".
        dsn: '...' # See table above
        index_name: 'my_index' # Optional, "contao_backend" is the default
```

- **`enabled`**: can be omitted if the DSN is set, but can be disabled with `false`. Values: `true`, `false`.
- **`dsn`**: the search engine DSN, per the adapter table above.
- **`index_name`**: optional index name. Default: `contao_backend`.

### Integration in the Contao Managed Edition

When using the Contao Managed Edition, the package `contao/loupe-bridge` can be installed, which requires the `cmsig/seal-loupe-adapter` and configures it at `var/loupe` automatically. The local search engine is preconfigured and no additional search engine server is needed. Only the Cronjob Framework needs to be configured to fulfill Basic Requirement 1.

**Note:** at least version `3.35.0` of the `sqlite` library is needed within the hosting environment.

### Build search index

The search index can be created manually via System Maintenance in the "Back end search" section using the "Rebuild index" button. In addition, similar to the frontend, the index is generated automatically as soon as an entry is called up or changed in the back end.

## Source

Distilled from the [Contao 5 user manual](https://docs.contao.org/5.x/manual/en/installation/), retrieved 2026-08-21.
