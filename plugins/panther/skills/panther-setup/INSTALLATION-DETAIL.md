# Symfony Panther — complete installation reference

## Contents

- [1. Composer installation](#1-composer-installation)
- [2. WebDriver installation](#2-webdriver-installation)
- [3. Registering the PHPUnit extension](#3-registering-the-phpunit-extension)
- [4. Complete environment variables](#4-complete-environment-variables)
- [5. Docker setup](#5-docker-setup)
- [6. CI/CD integration](#6-cicd-integration)
- [7. Solving asset loading problems](#7-solving-asset-loading-problems)
- [8. Working around SSL certificate errors](#8-working-around-ssl-certificate-errors)

## 1. Composer installation

```bash
composer require --dev symfony/panther
```

Minimum requirements:
- PHP 8.1+
- Symfony 5.4 / 6.x / 7.x (Panther is framework-agnostic and can also be used without Symfony)
- PHPUnit 9.5+ / 10+ / 11+

## 2. WebDriver installation

### Option A: BDI (recommended — automatic detection)

```bash
composer require --dev dbrekelmans/bdi
vendor/bin/bdi detect drivers
```

BDI detects the installed browser and downloads the matching driver into `./drivers/`.

### Option B: Manual installation

**ChromeDriver:**
1. Check the Chrome version: `google-chrome --version`
2. Download the matching ChromeDriver from https://googlechromelabs.github.io/chrome-for-testing/
3. Place it in `./drivers/chromedriver` or in `PATH` and make it executable: `chmod +x drivers/chromedriver`

**GeckoDriver (Firefox):**
1. Check the Firefox version: `firefox --version`
2. Download GeckoDriver from https://github.com/mozilla/geckodriver/releases
3. Place it in `./drivers/geckodriver` or in `PATH`

### Option C: System package manager

```bash
# Ubuntu/Debian
apt-get install chromium-chromedriver firefox-geckodriver

# macOS (Homebrew)
brew install chromedriver geckodriver

# Windows (Chocolatey)
choco install chromedriver selenium-gecko-driver
```

## 3. Registering the PHPUnit extension

The extension is **mandatory** for:
- Automatic screenshots on test failures
- Interactive debug mode (`PANTHER_NO_HEADLESS=1 bin/phpunit --debug`)
- Web server persistence between tests (performance)
- Better error output

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

## 4. Complete environment variables

### General

| Variable                          | Type     | Default     | Description                                         |
|-----------------------------------|----------|-------------|-----------------------------------------------------|
| `PANTHER_NO_HEADLESS`             | Flag     | —           | Show the browser window (debugging)                 |
| `PANTHER_WEB_SERVER_DIR`          | string   | `./public/` | Document root of the integrated PHP server (must start with `./`) |
| `PANTHER_WEB_SERVER_PORT`         | int      | `9080`      | Port of the integrated PHP built-in server          |
| `PANTHER_WEB_SERVER_ROUTER`       | string   | —           | Router script path for the PHP built-in server      |
| `PANTHER_EXTERNAL_BASE_URI`       | string   | —           | External server URI (no integrated server)          |
| `PANTHER_APP_ENV`                 | string   | —           | Overrides `APP_ENV` in the test server              |
| `PANTHER_ERROR_SCREENSHOT_DIR`    | string   | —           | Directory for automatic error screenshots           |
| `PANTHER_ERROR_SCREENSHOT_ATTACH` | Flag     | —           | Attach screenshots to the JUnit XML output          |
| `PANTHER_DEVTOOLS`                | string   | `enabled`   | Toggle the browser DevTools                         |
| `PANTHER_NO_REDUCED_MOTION`       | Flag     | —           | Enable non-essential animations                     |

### Chrome-specific

| Variable                    | Description                                            |
|-----------------------------|--------------------------------------------------------|
| `PANTHER_NO_SANDBOX`        | `--no-sandbox` flag (necessary in Docker/CI)           |
| `PANTHER_CHROME_ARGUMENTS`  | Additional Chrome arguments, e.g. `'--proxy-server=http://...'` |
| `PANTHER_CHROME_BINARY`     | Path to the Chrome binary                              |

### Firefox-specific

| Variable                      | Description                           |
|-------------------------------|---------------------------------------|
| `PANTHER_FIREFOX_ARGUMENTS`   | Additional Firefox arguments          |
| `PANTHER_FIREFOX_BINARY`      | Path to the Firefox binary            |

## 5. Docker setup

### Minimal Dockerfile (Chrome + optionally Firefox)

```dockerfile
FROM php:8.3-cli-alpine

# Chrome and ChromeDriver
ENV PANTHER_NO_SANDBOX=1
ENV PANTHER_CHROME_ARGUMENTS='--disable-dev-shm-usage'

RUN apk add --no-cache chromium chromium-chromedriver

# Optional: Firefox and GeckoDriver
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

## 6. CI/CD integration

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

## 7. Solving asset loading problems

### Problem
Assets do not load with the PHP built-in server (especially AssetMapper in dev).

### Solution 1: Compile the assets

```bash
php bin/console asset-map:compile
```

### Solution 2: A custom router script

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

## 8. Working around SSL certificate errors

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

Sources:
- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther
