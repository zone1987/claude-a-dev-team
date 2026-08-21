# Panther — Docker, interactive mode and CI configurations

## Contents

- [Docker integration](#docker-integration)
- [Interactive Mode](#interactive-mode)
- [CI configurations](#ci-configurations)
- [Known Limitations](#known-limitations)
- [Troubleshooting](#troubleshooting)
- [Sources](#sources)

## Docker integration

### Minimal Dockerfile (Chromium)

```dockerfile
FROM php:8.3-cli-alpine

# Install Chromium and ChromeDriver
RUN apk add --no-cache chromium chromium-chromedriver

# Panther configuration for the container environment
ENV PANTHER_NO_SANDBOX=1
ENV PANTHER_CHROME_ARGUMENTS='--disable-dev-shm-usage'

# Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

WORKDIR /srv/app
COPY . .
RUN composer install --no-interaction --prefer-dist --optimize-autoloader

CMD ["vendor/bin/phpunit"]
```

Explanation of the necessary settings:
- `PANTHER_NO_SANDBOX=1`: the Chrome sandbox requires user namespaces; in Docker without
  privileged mode these are not available => `--no-sandbox` is necessary.
- `--disable-dev-shm-usage`: `/dev/shm` is often too small in Docker (default: 64MB);
  this option tells Chrome to use the regular `/tmp` instead.

### Dockerfile with Chrome and Firefox

```dockerfile
FROM php:8.3-cli-alpine

ARG GECKODRIVER_VERSION=0.34.0

# Chromium and ChromeDriver
RUN apk add --no-cache chromium chromium-chromedriver

# Firefox and GeckoDriver
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

### Docker build and run

```bash
# Build the image
docker build -t myproject:test .

# Run the tests (volume mount for the code, set the working directory)
docker run --rm \
  -v "$PWD":/srv/app \
  -w /srv/app \
  myproject:test \
  vendor/bin/phpunit

# With additional environment variables
docker run --rm \
  -v "$PWD":/srv/app \
  -w /srv/app \
  -e PANTHER_ERROR_SCREENSHOT_DIR=/srv/app/var/screenshots \
  myproject:test \
  vendor/bin/phpunit
```

### Shared memory for Chrome in Docker

The default `/dev/shm` is 64MB — this can lead to Chrome crashes:

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
    # Alternative: enlarge /dev/shm instead of --disable-dev-shm-usage:
    shm_size: '2gb'
```

---

## Interactive Mode

Interactive mode pauses the test after a failure so that the browser state can be
inspected. It requires two conditions at the same time:

1. `PANTHER_NO_HEADLESS=1` — the browser is started with a visible window
2. PHPUnit is run with `--debug`

```bash
# Enable interactive mode
PANTHER_NO_HEADLESS=1 vendor/bin/phpunit --debug tests/MyTest.php
```

What happens: after a test failure or test error, Panther prints the message:
```
Failure: Expected selector ".success" to be visible

Press enter to continue...
```

The browser stays open and the test waits for the Enter key. You can then
open the DevTools in the browser and examine the DOM state.

Additionally, with DevTools opened automatically:
```bash
PANTHER_NO_HEADLESS=1 PANTHER_DEVTOOLS=1 vendor/bin/phpunit --debug tests/MyTest.php
```

Technical background (`ServerTrait::pause()`):
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

## CI configurations

### GitHub Actions (complete)

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
        # Chrome and ChromeDriver are preinstalled on ubuntu-latest.
        # PANTHER_NO_SANDBOX is detected automatically when needed.
        # Alternatively, explicitly:
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

### Travis CI (complete)

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

# Travis sets HAS_JOSH_K_SEAL_OF_APPROVAL=true, which Panther detects automatically
# and enables --no-sandbox. No manual PANTHER_NO_SANDBOX configuration needed.
```

### GitLab CI (complete)

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

### AppVeyor (complete, Windows)

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

Panther does **not** support the following BrowserKit/DomCrawler features:

| Limitation | Details |
|---|---|
| Crawling XML documents | Only HTML is supported |
| Updating existing documents | `request()` always reloads |
| Multidimensional PHP array syntax for forms | `foo[bar][baz]` supported |
| Methods returning `\DOMElement` | Panther returns `WebDriverElement` |
| Selecting invalid `<select>` options | Only existing options can be selected |
| Not following redirects | WebDriver always follows redirects |

---

## Troubleshooting

### Assets are not loaded (CSS, JS, images)

The PHP built-in server only serves `index.php`, no static files.
Solution: create a router script.

```php
// tests/router.php
<?php

if (is_file($_SERVER['DOCUMENT_ROOT'] . DIRECTORY_SEPARATOR . $_SERVER['SCRIPT_NAME'])) {
    // Serve the static file directly
    return false;
}

$script = 'index.php';

$_SERVER = array_merge($_SERVER, $_ENV);
$_SERVER['SCRIPT_FILENAME'] = $_SERVER['DOCUMENT_ROOT'] . DIRECTORY_SEPARATOR . $script;
$_SERVER['SCRIPT_NAME']     = DIRECTORY_SEPARATOR . $script;
$_SERVER['PHP_SELF']        = DIRECTORY_SEPARATOR . $script;

require $script;
```

Register the router in `phpunit.dist.xml`:

```xml
<phpunit>
    <php>
        <server name="PANTHER_WEB_SERVER_ROUTER" value="../tests/router.php"/>
    </php>
</phpunit>
```

### Bootstrap 5 smooth-scroll problems

Bootstrap 5 enables smooth scrolling by default, which slows tests down
or leaves elements outside the viewport. Disable it:

```scss
// assets/styles/app.scss
$enable-smooth-scroll: false;
@import "bootstrap/scss/bootstrap";
```

Or via PANTHER_NO_REDUCED_MOTION (Panther 2.2.0+):
```
# .env.test
PANTHER_NO_REDUCED_MOTION=0   # (default) sets --force-prefers-reduced-motion
```

### Port already in use

```bash
# Check the port
lsof -i :9080
# Use a different port
PANTHER_WEB_SERVER_PORT=9090 vendor/bin/phpunit
```

### ChromeDriver not found

```bash
# Install via dbrekelmans/bdi
composer require --dev dbrekelmans/bdi
vendor/bin/bdi detect drivers
# Places chromedriver in ./drivers/, which Panther searches automatically

# Or manually: $PATH, ./drivers/ or ./vendor/bin/ are searched
```

### "DevToolsActivePort file doesn't exist" in Docker

```bash
# Solution 1: enlarge /dev/shm
docker run --shm-size=2g ...

# Solution 2: --disable-dev-shm-usage
PANTHER_CHROME_ARGUMENTS='--disable-dev-shm-usage'

# Solution 3: no sandbox
PANTHER_NO_SANDBOX=1
```

### Tests run in headless mode, but not in a GUI environment

```bash
# If no display is available: use Xvfb
Xvfb :99 -screen 0 1280x1024x24 &
export DISPLAY=:99
PANTHER_NO_HEADLESS=1 vendor/bin/phpunit
```

---

## Sources

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/ServerTrait.php
- https://github.com/symfony/panther/blob/main/src/ServerExtensionLegacy.php
