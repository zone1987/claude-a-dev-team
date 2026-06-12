# Symfony Panther — Vollstandige Installations-Referenz

## 1. Composer-Installation

```bash
composer require --dev symfony/panther
```

Mindestanforderungen:
- PHP 8.1+
- Symfony 5.4 / 6.x / 7.x (Panther ist framework-agnostisch, auch ohne Symfony nutzbar)
- PHPUnit 9.5+ / 10+ / 11+

## 2. WebDriver-Installation

### Option A: BDI (empfohlen — automatische Erkennung)

```bash
composer require --dev dbrekelmans/bdi
vendor/bin/bdi detect drivers
```

BDI erkennt den installierten Browser und ladt den passenden Treiber in `./drivers/` herunter.

### Option B: Manuelle Installation

**ChromeDriver:**
1. Chrome-Version prufen: `google-chrome --version`
2. Passenden ChromeDriver von https://googlechromelabs.github.io/chrome-for-testing/ laden
3. In `./drivers/chromedriver` oder `PATH` ablegen, ausfuhrbar machen: `chmod +x drivers/chromedriver`

**GeckoDriver (Firefox):**
1. Firefox-Version prufen: `firefox --version`
2. GeckoDriver von https://github.com/mozilla/geckodriver/releases laden
3. In `./drivers/geckodriver` oder `PATH` ablegen

### Option C: System-Paketmanager

```bash
# Ubuntu/Debian
apt-get install chromium-chromedriver firefox-geckodriver

# macOS (Homebrew)
brew install chromedriver geckodriver

# Windows (Chocolatey)
choco install chromedriver selenium-gecko-driver
```

## 3. PHPUnit-Extension registrieren

Die Extension ist **Pflicht** fur:
- Automatische Screenshots bei Testfehlern
- Interaktiver Debug-Modus (`PANTHER_NO_HEADLESS=1 bin/phpunit --debug`)
- Web-Server-Persistenz zwischen Tests (Performance)
- Bessere Fehlerausgaben

### PHPUnit 10+ (`phpunit.dist.xml`)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="vendor/phpunit/phpunit/phpunit.xsd">
    <extensions>
        <bootstrap class="Symfony\Component\Panther\ServerExtension"/>
    </extensions>
    <php>
        <server name="PANTHER_WEB_SERVER_DIR" value="./public"/>
        <server name="PANTHER_WEB_SERVER_PORT" value="9080"/>
    </php>
</phpunit>
```

### PHPUnit 9.x (`phpunit.xml.dist`)

```xml
<phpunit>
    <extensions>
        <extension class="Symfony\Component\Panther\ServerExtension"/>
    </extensions>
</phpunit>
```

## 4. Vollstandige Umgebungsvariablen

### Allgemein

| Variable                          | Typ      | Default     | Beschreibung                                        |
|-----------------------------------|----------|-------------|-----------------------------------------------------|
| `PANTHER_NO_HEADLESS`             | Flag     | —           | Browser-Fenster sichtbar anzeigen (Debug)           |
| `PANTHER_WEB_SERVER_DIR`          | string   | `./public/` | Document-Root des integrierten PHP-Servers (muss mit `./` beginnen) |
| `PANTHER_WEB_SERVER_PORT`         | int      | `9080`      | Port des integrierten PHP-Built-in-Servers          |
| `PANTHER_WEB_SERVER_ROUTER`       | string   | —           | Router-Script-Pfad fur den PHP-Built-in-Server      |
| `PANTHER_EXTERNAL_BASE_URI`       | string   | —           | Externe Server-URI (kein integrierter Server)       |
| `PANTHER_APP_ENV`                 | string   | —           | Uberschreibt `APP_ENV` im Testserver                |
| `PANTHER_ERROR_SCREENSHOT_DIR`    | string   | —           | Verzeichnis fur automatische Fehler-Screenshots     |
| `PANTHER_ERROR_SCREENSHOT_ATTACH` | Flag     | —           | Screenshots an JUnit-XML-Output anhangen            |
| `PANTHER_DEVTOOLS`                | string   | `enabled`   | Browser-DevTools umschalten                         |
| `PANTHER_NO_REDUCED_MOTION`       | Flag     | —           | Nicht-essentielle Animationen aktivieren            |

### Chrome-spezifisch

| Variable                    | Beschreibung                                           |
|-----------------------------|--------------------------------------------------------|
| `PANTHER_NO_SANDBOX`        | `--no-sandbox` Flag (notwendig in Docker/CI)           |
| `PANTHER_CHROME_ARGUMENTS`  | Zusatzliche Chrome-Argumente, z. B. `'--proxy-server=http://...'` |
| `PANTHER_CHROME_BINARY`     | Pfad zur Chrome-Binary                                 |

### Firefox-spezifisch

| Variable                      | Beschreibung                          |
|-------------------------------|---------------------------------------|
| `PANTHER_FIREFOX_ARGUMENTS`   | Zusatzliche Firefox-Argumente         |
| `PANTHER_FIREFOX_BINARY`      | Pfad zur Firefox-Binary               |

## 5. Docker-Setup

### Minimales Dockerfile (Chrome + optional Firefox)

```dockerfile
FROM php:8.3-cli-alpine

# Chrome und ChromeDriver
ENV PANTHER_NO_SANDBOX=1
ENV PANTHER_CHROME_ARGUMENTS='--disable-dev-shm-usage'

RUN apk add --no-cache chromium chromium-chromedriver

# Optional: Firefox und GeckoDriver
ARG GECKODRIVER_VERSION=0.35.0
RUN apk add --no-cache firefox libzip-dev && \
    docker-php-ext-install zip && \
    wget -q "https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz" && \
    tar -zxf "geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz" -C /usr/bin && \
    rm "geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz"

COPY . /srv/app
WORKDIR /srv/app
RUN composer install --no-dev --optimize-autoloader
```

```bash
docker build . -t myproject
docker run -it -v "$PWD":/srv/app -w /srv/app myproject vendor/bin/phpunit
```

## 6. CI/CD-Integration

### GitHub Actions

```yaml
name: E2E Tests
on: [push, pull_request]

jobs:
  panther:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: shivammathur/setup-php@v2
        with:
          php-version: '8.3'
      - run: composer install --prefer-dist --no-progress
      - run: vendor/bin/phpunit --testdox
        env:
          PANTHER_NO_SANDBOX: 1
          PANTHER_CHROME_ARGUMENTS: '--disable-dev-shm-usage'
```

### GitLab CI

```yaml
image: ubuntu:22.04

before_script:
  - apt-get update -qq
  - apt-get install -y -qq chromium-chromedriver php8.2-cli php8.2-curl php8.2-mbstring php8.2-xml composer
  - export PANTHER_NO_SANDBOX=1
  - composer install -q --no-ansi --no-interaction --no-scripts --prefer-dist

test:
  script:
    - vendor/bin/phpunit
```

## 7. Asset-Loading-Probleme losen

### Problem
Assets laden nicht mit PHP-Built-in-Server (besonders AssetMapper in dev).

### Losung 1: Assets kompilieren

```bash
php bin/console asset-map:compile
```

### Losung 2: Eigenes Router-Script

`tests/router.php`:
```php
<?php
if (is_file($_SERVER['DOCUMENT_ROOT'] . \DIRECTORY_SEPARATOR . $_SERVER['SCRIPT_NAME'])) {
    return false;
}
$script = 'index.php';
$_SERVER = array_merge($_SERVER, $_ENV);
$_SERVER['SCRIPT_FILENAME'] = $_SERVER['DOCUMENT_ROOT'] . \DIRECTORY_SEPARATOR . $script;
$_SERVER['SCRIPT_NAME'] = \DIRECTORY_SEPARATOR . $script;
$_SERVER['PHP_SELF'] = \DIRECTORY_SEPARATOR . $script;
require $script;
```

`phpunit.dist.xml`:
```xml
<phpunit>
    <php>
        <server name="PANTHER_WEB_SERVER_ROUTER" value="../tests/router.php"/>
    </php>
</phpunit>
```

## 8. SSL-Zertifikat-Fehler umgehen

### Chrome

```bash
PANTHER_CHROME_ARGUMENTS='--ignore-certificate-errors' vendor/bin/phpunit
```

### Firefox

```php
$client = Client::createFirefoxClient(
    null,
    null,
    ['capabilities' => ['acceptInsecureCerts' => true]]
);
```

---

Quellen:
- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther
