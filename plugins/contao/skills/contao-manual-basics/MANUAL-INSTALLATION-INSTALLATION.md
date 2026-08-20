# Contao 5.x — Installation

Sources:
- https://docs.contao.org/5.x/manual/de/installation/systemvoraussetzungen/
- https://docs.contao.org/5.x/manual/de/installation/contao-installieren/
- https://docs.contao.org/5.x/manual/de/installation/contao-aktualisieren/
- https://docs.contao.org/5.x/manual/de/installation/contao-manager/
- https://docs.contao.org/5.x/manual/de/installation/erweiterungen-installieren/
- https://docs.contao.org/5.x/manual/de/anleitungen/lokale-installation/ddev/
- https://docs.contao.org/5.x/manual/de/anleitungen/lokale-installation/devilbox/
- https://docs.contao.org/5.x/manual/de/anleitungen/lokale-installation/laragon/
- https://docs.contao.org/5.x/manual/de/anleitungen/lokale-installation/xampp/

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

![Contao Manager welcome page](../../assets/contao-manager-willkommen.png)

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

# Datenbankverbindung und Mailer setzen
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
# Erstmaliger Start (Vordergrund für Fehlererkennung)
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
