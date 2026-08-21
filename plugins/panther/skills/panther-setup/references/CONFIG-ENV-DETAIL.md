# Panther — configuration and environment variables

## Contents

- [All PANTHER_* environment variables](#all-panther_-environment-variables)
- [Programmatic options for createPantherClient()](#programmatic-options-for-createpantherclient)
- [Chrome arguments set by default](#chrome-arguments-set-by-default)
- [Changing the hostname and port of the web server](#changing-the-hostname-and-port-of-the-web-server)
- [Configuration in phpunit.dist.xml](#configuration-in-phpunitdistxml)
- [Sources](#sources)

## All PANTHER_* environment variables

All variables are read from `$_SERVER` (not `$_ENV`). They can be set in
`.env.test`, `phpunit.dist.xml` (`<server name="..."/>`) or directly as a
shell export.

### Browser rendering and debugging

| Variable | Type | Default | Effect |
|---|---|---|---|
| `PANTHER_NO_HEADLESS` | bool (`FILTER_VALIDATE_BOOLEAN`) | `false` (headless) | `true`: starts Chrome/Firefox with a visible window. Chrome: `--headless` is omitted. Firefox: the `-headless` argument is not set. Prerequisite for interactive mode. |
| `PANTHER_DEVTOOLS` | bool (`FILTER_VALIDATE_BOOLEAN`) | `false` | `true`: Chrome opens DevTools automatically (`--auto-open-devtools-for-tabs`). Firefox: `--devtools` argument. Only relevant with `PANTHER_NO_HEADLESS=1`. |
| `PANTHER_NO_REDUCED_MOTION` | bool (`FILTER_VALIDATE_BOOLEAN`) | `false` (reduced motion active) | `false` (default): Chrome sets `--force-prefers-reduced-motion`, Firefox sets `ui.prefersReducedMotion=1`. `true`: `--force-prefers-no-reduced-motion` (Chrome) / `ui.prefersReducedMotion=0` (Firefox). Since Panther 2.2.0. |

### Sandbox and security

| Variable | Type | Default | Effect |
|---|---|---|---|
| `PANTHER_NO_SANDBOX` | bool (`FILTER_VALIDATE_BOOLEAN`) | `false` | `true`: adds `--no-sandbox` to the Chrome arguments. Necessary in Docker containers and CI environments without a user namespace. Insecure on desktop systems. Also enabled by `HAS_JOSH_K_SEAL_OF_APPROVAL` (legacy Travis CI flag). Chrome only. |

### Web server configuration (PHP built-in server)

| Variable | Type | Default | Effect |
|---|---|---|---|
| `PANTHER_WEB_SERVER_DIR` | string (path) | `./public` (Flex structure, relative to vendor) | Document root of the PHP built-in server. Relative paths with a `./` prefix are resolved against `getcwd()`. Absolute paths are used as-is. Overridden by `$options['webServerDir']` in `createPantherClient()` or by the static `$webServerDir`. |
| `PANTHER_WEB_SERVER_PORT` | int | `9080` | TCP port of the PHP built-in server. `createPantherClient(['port' => 8080])` takes precedence. |
| `PANTHER_WEB_SERVER_ROUTER` | string (path) | `''` (no router) | Path to the PHP router script for the built-in server. Relative to the document root or absolute. Necessary so that assets (`css`, `js`, `png` etc.) are served correctly. |
| `PANTHER_READINESS_PATH` | string (URL path) | `''` | HTTP path requested by the web server readiness probe, e.g. `/health`. Without this value the base URL is checked. |
| `PANTHER_APP_ENV` | string | not set | Sets `APP_ENV` for the started PHP built-in server (passed on as a process environment variable). Does not affect the PHPUnit process itself. |

### External server / hostname

| Variable | Type | Default | Effect |
|---|---|---|---|
| `PANTHER_EXTERNAL_BASE_URI` | string (URL) | not set | Complete base URL of an externally started web server, e.g. `https://localhost:8443`. Prevents the built-in server from starting. Alias: `SYMFONY_PROJECT_DEFAULT_ROUTE_URL` (lower priority). `$options['external_base_uri']` takes precedence. |
| `SYMFONY_PROJECT_DEFAULT_ROUTE_URL` | string (URL) | not set | Fallback for `PANTHER_EXTERNAL_BASE_URI`. Set by SymfonyCloud/Platform.sh. |

### Chrome-specific variables

| Variable | Type | Default | Effect |
|---|---|---|---|
| `PANTHER_CHROME_BINARY` | string (path) | not set | Path to the Chrome/Chromium executable, e.g. `/usr/bin/chromium-browser`. Set via `ChromeOptions::setBinary()`. |
| `PANTHER_CHROME_ARGUMENTS` | string (space-separated) | not set | Additional arguments for the Chrome browser process (not ChromeDriver). Split with `explode(' ', ...)` and appended to the arguments list. Example: `--proxy-server=socks://127.0.0.1:9050 --ignore-certificate-errors`. |

### Firefox-specific variables

| Variable | Type | Default | Effect |
|---|---|---|---|
| `PANTHER_FIREFOX_BINARY` | string (path) | not set | Path to the Firefox executable. Set as the `binary` field in `moz:firefoxOptions`. |
| `PANTHER_FIREFOX_ARGUMENTS` | string (space-separated) | not set | Additional arguments for the Firefox process. Split with `explode(' ', ...)` and added to the Firefox arguments. |

### Error screenshots

| Variable | Type | Default | Effect |
|---|---|---|---|
| `PANTHER_ERROR_SCREENSHOT_DIR` | string (directory path) | not set | When set: on a test failure or test error a screenshot is written to this directory automatically. File name format: `YYYY-MM-DD_HH-II-SS_{error|failure}_{TestClass-MethodName}-{clientIndex}.png`. Requires `ServerExtension` in `phpunit.dist.xml`. |
| `PANTHER_ERROR_SCREENSHOT_ATTACH` | bool | `false` | `true`: after each error screenshot, prints `[[ATTACHMENT|/path/to/screenshot.png]]` on stdout (GitLab CI attachment format). Only effective when `PANTHER_ERROR_SCREENSHOT_DIR` is set. |

---

## Programmatic options for createPantherClient()

```php
static::createPantherClient(
    array $options = [],        // Web server and browser options
    array $kernelOptions = [],  // Symfony kernel options (only with KernelTestCase)
    array $managerOptions = []  // ChromeManager/FirefoxManager/SeleniumManager options
): PantherClient
```

### $options (first parameter)

| Key | Type | Default | Effect |
|---|---|---|---|
| `webServerDir` | string | `./public` | Document root; overrides `PANTHER_WEB_SERVER_DIR` |
| `hostname` | string | `127.0.0.1` | Hostname of the built-in web server and base URI |
| `port` | int | `9080` | Port of the built-in web server; overrides `PANTHER_WEB_SERVER_PORT` |
| `router` | string | `''` | Router script; overrides `PANTHER_WEB_SERVER_ROUTER` |
| `readinessPath` | string | `''` | Readiness probe path; overrides `PANTHER_READINESS_PATH` |
| `external_base_uri` | string\|null | `null` | External server; overrides `PANTHER_EXTERNAL_BASE_URI` |
| `env` | array | `[]` | Additional environment variables for the web server process |
| `browser` | string | `PantherTestCase::CHROME` | `PantherTestCase::CHROME`, `::FIREFOX` or `::SELENIUM` |
| `browser_arguments` | array\|null | `null` | Browser arguments; overrides the automatically determined arguments |

### $managerOptions (third parameter) — Chrome

| Key | Type | Default | Effect |
|---|---|---|---|
| `scheme` | string | `'http'` | Protocol for the ChromeDriver connection |
| `host` | string | `'127.0.0.1'` | Host of the ChromeDriver process |
| `port` | int | `9515` | Port of the ChromeDriver process |
| `path` | string | `'/status'` | Readiness probe path of ChromeDriver |
| `chromedriver_arguments` | array | `[]` | Command line arguments for the ChromeDriver process (not the browser), e.g. `['--log-path=myfile.log', '--log-level=DEBUG']` |
| `capabilities` | array | `[]` | WebDriver capabilities as an associative array; set via `setCapability()` |
| `connection_timeout_in_ms` | int\|null | `null` (WebDriver default) | Timeout for the connection to ChromeDriver in milliseconds |
| `request_timeout_in_ms` | int\|null | `null` (WebDriver default) | Timeout for individual WebDriver requests in milliseconds |

### $managerOptions (third parameter) — Firefox

| Key | Type | Default | Effect |
|---|---|---|---|
| `scheme` | string | `'http'` | Protocol for the GeckoDriver connection |
| `host` | string | `'127.0.0.1'` | Host of the GeckoDriver process |
| `port` | int | `4444` | Port of the GeckoDriver process |
| `path` | string | `'/status'` | Readiness probe path of GeckoDriver |
| `capabilities` | array | `[]` | WebDriver capabilities as an associative array |
| `connection_timeout_in_ms` | int\|null | `null` | Connection timeout in milliseconds |
| `request_timeout_in_ms` | int\|null | `null` | Request timeout in milliseconds |

---

## Chrome arguments set by default

Panther sets these arguments automatically (unless they are completely replaced by `browser_arguments`):

| Argument | Condition |
|---|---|
| `--headless` | `PANTHER_NO_HEADLESS` is falsy |
| `--window-size=1200,1100` | `PANTHER_NO_HEADLESS` is falsy |
| `--disable-gpu` | `PANTHER_NO_HEADLESS` is falsy |
| `--auto-open-devtools-for-tabs` | `PANTHER_DEVTOOLS` is truthy |
| `--no-sandbox` | `PANTHER_NO_SANDBOX` or `HAS_JOSH_K_SEAL_OF_APPROVAL` is truthy |
| `--force-prefers-reduced-motion` | `PANTHER_NO_REDUCED_MOTION` is falsy (default) |
| `--force-prefers-no-reduced-motion` | `PANTHER_NO_REDUCED_MOTION` is truthy |
| Values from `PANTHER_CHROME_ARGUMENTS` | whenever the variable is set |

### Setting the window size manually

```php
// Chrome: via argument (overrides --window-size=1200,1100 from the headless default)
$client = Client::createChromeClient(null, ['--window-size=1920,1080']);

// Firefox: via WebDriverDimension
use Facebook\WebDriver\WebDriverDimension;
$client = Client::createFirefoxClient();
$client->manage()->window()->setSize(new WebDriverDimension(1920, 1080));
```

---

## Changing the hostname and port of the web server

```php
// In phpunit.dist.xml:
// <server name="PANTHER_WEB_SERVER_PORT" value="8080"/>

// Or programmatically:
$client = static::createPantherClient([
    'hostname' => '0.0.0.0',  // Listens on all interfaces
    'port'     => 8080,
]);
```

---

## Configuration in phpunit.dist.xml

```xml
<phpunit>
    <extensions>
        <!-- PHPUnit >= 10 -->
        <bootstrap class="Symfony\Component\Panther\ServerExtension"/>
        <!-- PHPUnit < 10 -->
        <!-- <extension class="Symfony\Component\Panther\ServerExtension"/> -->
    </extensions>

    <php>
        <server name="PANTHER_WEB_SERVER_DIR"         value="./public"/>
        <server name="PANTHER_WEB_SERVER_PORT"        value="9080"/>
        <server name="PANTHER_WEB_SERVER_ROUTER"      value="../tests/router.php"/>
        <server name="PANTHER_READINESS_PATH"         value="/health"/>
        <server name="PANTHER_APP_ENV"                value="test"/>
        <server name="PANTHER_NO_HEADLESS"            value="0"/>
        <server name="PANTHER_NO_SANDBOX"             value="0"/>
        <server name="PANTHER_NO_REDUCED_MOTION"      value="0"/>
        <server name="PANTHER_DEVTOOLS"               value="0"/>
        <server name="PANTHER_CHROME_BINARY"          value="/usr/bin/chromium"/>
        <server name="PANTHER_CHROME_ARGUMENTS"       value="--disable-dev-shm-usage"/>
        <server name="PANTHER_FIREFOX_BINARY"         value="/usr/bin/firefox"/>
        <server name="PANTHER_FIREFOX_ARGUMENTS"      value=""/>
        <server name="PANTHER_EXTERNAL_BASE_URI"      value=""/>
        <server name="PANTHER_ERROR_SCREENSHOT_DIR"   value="var/screenshots"/>
        <server name="PANTHER_ERROR_SCREENSHOT_ATTACH" value="0"/>
    </php>
</phpunit>
```

---

## Sources

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/ProcessManager/ChromeManager.php
- https://github.com/symfony/panther/blob/main/src/ProcessManager/FirefoxManager.php
- https://github.com/symfony/panther/blob/main/src/ProcessManager/WebServerManager.php
- https://github.com/symfony/panther/blob/main/src/PantherTestCaseTrait.php
- https://github.com/symfony/panther/blob/main/src/ServerExtensionLegacy.php
