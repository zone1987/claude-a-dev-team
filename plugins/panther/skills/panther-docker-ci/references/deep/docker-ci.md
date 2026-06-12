# Panther — Docker, Interactive Mode und CI-Konfigurationen

## Docker-Integration

### Minimales Dockerfile (Chromium)

```dockerfile
FROM php:8.3-cli-alpine

# Chromium und ChromeDriver installieren
RUN apk add --no-cache chromium chromium-chromedriver

# Panther-Konfiguration fuer Container-Umgebung
ENV PANTHER_NO_SANDBOX=1
ENV PANTHER_CHROME_ARGUMENTS='--disable-dev-shm-usage'

# Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

WORKDIR /srv/app
COPY . .
RUN composer install --no-interaction --prefer-dist --optimize-autoloader

CMD ["vendor/bin/phpunit"]
```

Erklaerung der notwendigen Einstellungen:
- `PANTHER_NO_SANDBOX=1`: Chrome-Sandbox erfordert User-Namespaces; in Docker ohne
  privilegierten Modus nicht verfuegbar => `--no-sandbox` notwendig.
- `--disable-dev-shm-usage`: `/dev/shm` ist in Docker oft zu klein (Standard: 64MB);
  diese Option weist Chrome an, das regulaere `/tmp` zu nutzen.

### Dockerfile mit Chrome und Firefox

```dockerfile
FROM php:8.3-cli-alpine

ARG GECKODRIVER_VERSION=0.34.0

# Chromium und ChromeDriver
RUN apk add --no-cache chromium chromium-chromedriver

# Firefox und GeckoDriver
RUN apk add --no-cache firefox libzip-dev wget tar && \
    docker-php-ext-install zip

RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz" && \
    tar -zxf "geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz" -C /usr/local/bin && \
    rm "geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz" && \
    chmod +x /usr/local/bin/geckodriver

ENV PANTHER_NO_SANDBOX=1
ENV PANTHER_CHROME_ARGUMENTS='--disable-dev-shm-usage'

COPY --from=composer:2 /usr/bin/composer /usr/bin/composer
WORKDIR /srv/app
COPY . .
RUN composer install --no-interaction --prefer-dist
```

### Docker-Build und -Run

```bash
# Image bauen
docker build -t myproject:test .

# Tests ausfuehren (Volume-Mount fuer Code, Arbeitsverzeichnis setzen)
docker run --rm \
  -v "$PWD":/srv/app \
  -w /srv/app \
  myproject:test \
  vendor/bin/phpunit

# Mit zusaetzlichen Umgebungsvariablen
docker run --rm \
  -v "$PWD":/srv/app \
  -w /srv/app \
  -e PANTHER_ERROR_SCREENSHOT_DIR=/srv/app/var/screenshots \
  myproject:test \
  vendor/bin/phpunit
```

### Shared Memory fuer Chrome in Docker

Standard `/dev/shm` ist 64MB — kann zu Chrome-Crashes fuehren:

```yaml
# docker-compose.yml
services:
  tests:
    image: myproject:test
    environment:
      PANTHER_NO_SANDBOX: "1"
      PANTHER_CHROME_ARGUMENTS: "--disable-dev-shm-usage"
    volumes:
      - .:/srv/app
    # Alternative: /dev/shm vergroessern statt --disable-dev-shm-usage:
    shm_size: '2gb'
```

---

## Interactive Mode

Der Interactive Mode pausiert den Test nach einem Fehler, sodass man den Browserzustand
inspizieren kann. Erfordert zwei Bedingungen gleichzeitig:

1. `PANTHER_NO_HEADLESS=1` — Browser wird mit sichtbarem Fenster gestartet
2. PHPUnit wird mit `--debug` ausgefuehrt

```bash
# Interactive Mode aktivieren
PANTHER_NO_HEADLESS=1 vendor/bin/phpunit --debug tests/MyTest.php
```

Was passiert: Nach einem Test-Failure oder Test-Error gibt Panther die Meldung aus:
```
Failure: Expected selector ".success" to be visible

Press enter to continue...
```

Der Browser bleibt geoeffnet und der Test wartet auf Enter-Eingabe. Man kann dann
im Browser die DevTools oeffnen und den DOM-Zustand untersuchen.

Zusaetzlich mit DevTools automatisch oeffnen:
```bash
PANTHER_NO_HEADLESS=1 PANTHER_DEVTOOLS=1 vendor/bin/phpunit --debug tests/MyTest.php
```

Technischer Hintergrund (`ServerTrait::pause()`):
```php
private function pause($message): void
{
    if (in_array('--debug', $_SERVER['argv'], true)
        && filter_var($_SERVER['PANTHER_NO_HEADLESS'] ?? false, FILTER_VALIDATE_BOOLEAN)
    ) {
        echo "$message\n\nPress enter to continue...";
        fgets(STDIN);
    }
}
```

---

## CI-Konfigurationen

### GitHub Actions (vollstaendig)

```yaml
# .github/workflows/panther.yml
name: Panther E2E Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  e2e-tests:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup PHP
        uses: shivammathur/setup-php@v2
        with:
          php-version: '8.3'
          extensions: mbstring, xml, curl, zip
          coverage: none

      - name: Get composer cache directory
        id: composer-cache
        run: echo "dir=$(composer config cache-files-dir)" >> $GITHUB_OUTPUT

      - name: Cache Composer dependencies
        uses: actions/cache@v4
        with:
          path: ${{ steps.composer-cache.outputs.dir }}
          key: ${{ runner.os }}-composer-${{ hashFiles('**/composer.lock') }}
          restore-keys: ${{ runner.os }}-composer-

      - name: Install Composer dependencies
        run: composer install --no-progress --no-interaction --prefer-dist

      - name: Run Panther tests
        run: vendor/bin/phpunit tests/E2E/
        # Chrome und ChromeDriver sind auf ubuntu-latest vorinstalliert.
        # PANTHER_NO_SANDBOX wird automatisch erkannt wenn noetig.
        # Alternativ explizit:
        env:
          PANTHER_NO_SANDBOX: "1"
          PANTHER_CHROME_ARGUMENTS: "--disable-dev-shm-usage"

      - name: Upload screenshots on failure
        uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: panther-screenshots
          path: var/screenshots/
```

### Travis CI (vollstaendig)

```yaml
# .travis.yml
language: php

addons:
  chrome: stable
  firefox: latest

php:
  - '8.1'
  - '8.2'
  - '8.3'

cache:
  directories:
    - $HOME/.composer/cache

install:
  - composer install --no-interaction --prefer-dist

script:
  - vendor/bin/phpunit

# Travis setzt HAS_JOSH_K_SEAL_OF_APPROVAL=true, Panther erkennt das automatisch
# und aktiviert --no-sandbox. Keine manuelle PANTHER_NO_SANDBOX-Konfiguration noetig.
```

### GitLab CI (vollstaendig)

```yaml
# .gitlab-ci.yml
image: ubuntu:22.04

variables:
  PANTHER_NO_SANDBOX: "1"
  PANTHER_WEB_SERVER_PORT: "9080"
  PANTHER_ERROR_SCREENSHOT_DIR: "var/screenshots"
  PANTHER_ERROR_SCREENSHOT_ATTACH: "1"

before_script:
  - apt-get update -qq
  - apt-get install -y -qq software-properties-common curl wget
  - ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
  - apt-get install -y -qq \
      php8.2 php8.2-cli php8.2-common php8.2-curl php8.2-intl \
      php8.2-xml php8.2-opcache php8.2-mbstring php8.2-zip \
      chromium-chromedriver \
      libfontconfig1 fontconfig libxrender1 libfreetype6
  - curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
  - composer install --no-interaction --prefer-dist --no-scripts

panther_tests:
  script:
    - vendor/bin/phpunit tests/E2E/
  artifacts:
    when: on_failure
    paths:
      - var/screenshots/
    expire_in: 1 week
```

### AppVeyor (vollstaendig, Windows)

```yaml
# appveyor.yml
build: false
platform: x86
clone_folder: c:\projects\myproject

cache:
  - '%LOCALAPPDATA%\Composer\files'

install:
  - ps: Set-Service wuauserv -StartupType Manual
  - cinst -y php composer googlechrome chromedriver firefox selenium-gecko-driver
  - refreshenv
  - cd c:\tools\php82
  - copy php.ini-production php.ini /Y
  - echo date.timezone="UTC" >> php.ini
  - echo extension_dir=ext >> php.ini
  - echo extension=php_openssl.dll >> php.ini
  - echo extension=php_mbstring.dll >> php.ini
  - echo extension=php_curl.dll >> php.ini
  - echo extension=php_intl.dll >> php.ini
  - echo extension=php_zip.dll >> php.ini
  - echo memory_limit=512M >> php.ini
  - cd %APPVEYOR_BUILD_FOLDER%
  - composer install --no-interaction --prefer-dist

test_script:
  - cd %APPVEYOR_BUILD_FOLDER%
  - php vendor\phpunit\phpunit\phpunit tests\E2E\
```

---

## Known Limitations

Panther unterstuetzt folgende BrowserKit/DomCrawler-Features **nicht**:

| Einschraenkung | Details |
|---|---|
| XML-Dokumente crawlen | Nur HTML wird unterstuetzt |
| Bestehende Dokumente aktualisieren | `request()` laedt immer neu |
| Multidimensionale PHP-Array-Syntax fuer Formulare | `foo[bar][baz]` unterstuetzt |
| Methoden die `\DOMElement` zurueckgeben | Panther gibt `WebDriverElement` zurueck |
| Ungueltige `<select>`-Optionen auswaehlen | Nur existierende Optionen waehlbar |
| Redirects nicht folgen | WebDriver folgt immer Redirects |

---

## Troubleshooting

### Assets werden nicht geladen (CSS, JS, Bilder)

Der PHP Built-In-Server liefert nur `index.php` aus, keine statischen Dateien.
Loesung: Router-Skript erstellen.

```php
// tests/router.php
<?php

if (is_file($_SERVER['DOCUMENT_ROOT'] . DIRECTORY_SEPARATOR . $_SERVER['SCRIPT_NAME'])) {
    // Statische Datei direkt ausliefern
    return false;
}

$script = 'index.php';

$_SERVER = array_merge($_SERVER, $_ENV);
$_SERVER['SCRIPT_FILENAME'] = $_SERVER['DOCUMENT_ROOT'] . DIRECTORY_SEPARATOR . $script;
$_SERVER['SCRIPT_NAME']     = DIRECTORY_SEPARATOR . $script;
$_SERVER['PHP_SELF']        = DIRECTORY_SEPARATOR . $script;

require $script;
```

Router in `phpunit.dist.xml` registrieren:

```xml
<phpunit>
    <php>
        <server name="PANTHER_WEB_SERVER_ROUTER" value="../tests/router.php"/>
    </php>
</phpunit>
```

### Bootstrap 5 Smooth-Scroll-Probleme

Bootstrap 5 aktiviert standardmaessig Smooth-Scrolling, das Tests verlangsamt
oder Elemente ausserhalb des Viewports laesst. Deaktivieren:

```scss
// assets/styles/app.scss
$enable-smooth-scroll: false;
@import "bootstrap/scss/bootstrap";
```

Oder via PANTHER_NO_REDUCED_MOTION (Panther 2.2.0+):
```
# .env.test
PANTHER_NO_REDUCED_MOTION=0   # (default) setzt --force-prefers-reduced-motion
```

### Port bereits belegt

```bash
# Port pruefen
lsof -i :9080
# Anderen Port verwenden
PANTHER_WEB_SERVER_PORT=9090 vendor/bin/phpunit
```

### ChromeDriver nicht gefunden

```bash
# Via dbrekelmans/bdi installieren
composer require --dev dbrekelmans/bdi
vendor/bin/bdi detect drivers
# Legt chromedriver in ./drivers/ ab, das Panther automatisch durchsucht

# Oder manuell: $PATH, ./drivers/ oder ./vendor/bin/ werden durchsucht
```

### "DevToolsActivePort file doesn't exist" in Docker

```bash
# Loesung 1: /dev/shm vergroessern
docker run --shm-size=2g ...

# Loesung 2: --disable-dev-shm-usage
PANTHER_CHROME_ARGUMENTS='--disable-dev-shm-usage'

# Loesung 3: Kein Sandbox
PANTHER_NO_SANDBOX=1
```

### Tests laufen im Headless-Modus, aber nicht in GUI-Umgebung

```bash
# Wenn kein Display verfuegbar: Xvfb verwenden
Xvfb :99 -screen 0 1280x1024x24 &
export DISPLAY=:99
PANTHER_NO_HEADLESS=1 vendor/bin/phpunit
```

---

## Quellen

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/ServerTrait.php
- https://github.com/symfony/panther/blob/main/src/ServerExtensionLegacy.php
