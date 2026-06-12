# Panther — Konfiguration und Umgebungsvariablen

## Alle PANTHER_*-Umgebungsvariablen

Alle Variablen werden aus `$_SERVER` gelesen (nicht `$_ENV`). Sie koennen in
`.env.test`, `phpunit.dist.xml` (`<server name="..."/>`) oder direkt als
Shell-Export gesetzt werden.

### Browser-Darstellung und Debugging

| Variable | Typ | Default | Wirkung |
|---|---|---|---|
| `PANTHER_NO_HEADLESS` | bool (`FILTER_VALIDATE_BOOLEAN`) | `false` (Headless) | `true`: startet Chrome/Firefox mit sichtbarem Fenster. Chrome: `--headless` wird weggelassen. Firefox: `-headless`-Argument wird nicht gesetzt. Voraussetzung fuer Interactive Mode. |
| `PANTHER_DEVTOOLS` | bool (`FILTER_VALIDATE_BOOLEAN`) | `false` | `true`: Chrome oeffnet DevTools automatisch (`--auto-open-devtools-for-tabs`). Firefox: `--devtools`-Argument. Nur relevant mit `PANTHER_NO_HEADLESS=1`. |
| `PANTHER_NO_REDUCED_MOTION` | bool (`FILTER_VALIDATE_BOOLEAN`) | `false` (reduced motion aktiv) | `false` (Default): Chrome setzt `--force-prefers-reduced-motion`, Firefox setzt `ui.prefersReducedMotion=1`. `true`: `--force-prefers-no-reduced-motion` (Chrome) / `ui.prefersReducedMotion=0` (Firefox). Seit Panther 2.2.0. |

### Sandbox und Sicherheit

| Variable | Typ | Default | Wirkung |
|---|---|---|---|
| `PANTHER_NO_SANDBOX` | bool (`FILTER_VALIDATE_BOOLEAN`) | `false` | `true`: fuegt `--no-sandbox` zu Chrome-Argumenten hinzu. Notwendig in Docker-Containern und CI-Umgebungen ohne User-Namespace. Unsicher auf Desktop-Systemen. Wird auch aktiviert durch `HAS_JOSH_K_SEAL_OF_APPROVAL` (Travis-CI-Legacy-Flag). Nur Chrome. |

### Webserver-Konfiguration (PHP Built-In Server)

| Variable | Typ | Default | Wirkung |
|---|---|---|---|
| `PANTHER_WEB_SERVER_DIR` | string (Pfad) | `./public` (Flex-Struktur, relativ zu Vendor) | Document-Root des PHP Built-In-Servers. Relative Pfade mit `./`-Praefix werden zu `getcwd()` aufgeloest. Absolute Pfade direkt uebernommen. Ueberschrieben durch `$options['webServerDir']` in `createPantherClient()` oder statisches `$webServerDir`. |
| `PANTHER_WEB_SERVER_PORT` | int | `9080` | TCP-Port des PHP Built-In-Servers. `createPantherClient(['port' => 8080])` hat Vorrang. |
| `PANTHER_WEB_SERVER_ROUTER` | string (Pfad) | `''` (kein Router) | Pfad zum PHP-Router-Skript fuer den Built-In-Server. Relativ zum Document-Root oder absolut. Notwendig damit Assets (`css`, `js`, `png` etc.) korrekt ausgeliefert werden. |
| `PANTHER_READINESS_PATH` | string (URL-Pfad) | `''` | HTTP-Pfad der vom Webserver-Readiness-Probe angefragt wird, z.B. `/health`. Ohne diesen Wert wird der Basis-URL geprueft. |
| `PANTHER_APP_ENV` | string | nicht gesetzt | Setzt `APP_ENV` fuer den gestarteten PHP Built-In-Server (wird als Prozess-Umgebungsvariable weitergegeben). Beeinflusst nicht den PHPUnit-Prozess selbst. |

### Externer Server / Hostname

| Variable | Typ | Default | Wirkung |
|---|---|---|---|
| `PANTHER_EXTERNAL_BASE_URI` | string (URL) | nicht gesetzt | Vollstaendige Basis-URL eines extern gestarteten Webservers, z.B. `https://localhost:8443`. Verhindert den Start des Built-In-Servers. Alias: `SYMFONY_PROJECT_DEFAULT_ROUTE_URL` (niedrigere Prioritaet). `$options['external_base_uri']` hat Vorrang. |
| `SYMFONY_PROJECT_DEFAULT_ROUTE_URL` | string (URL) | nicht gesetzt | Fallback fuer `PANTHER_EXTERNAL_BASE_URI`. Wird von SymfonyCloud/Platform.sh gesetzt. |

### Chrome-spezifische Variablen

| Variable | Typ | Default | Wirkung |
|---|---|---|---|
| `PANTHER_CHROME_BINARY` | string (Pfad) | nicht gesetzt | Pfad zur Chrome/Chromium-Executable, z.B. `/usr/bin/chromium-browser`. Wird via `ChromeOptions::setBinary()` gesetzt. |
| `PANTHER_CHROME_ARGUMENTS` | string (Leerzeichen-getrennt) | nicht gesetzt | Zusaetzliche Argumente fuer den Chrome-Browser-Prozess (nicht ChromeDriver). Wird per `explode(' ', ...)` aufgeteilt und an die Arguments-Liste angehaengt. Beispiel: `--proxy-server=socks://127.0.0.1:9050 --ignore-certificate-errors`. |

### Firefox-spezifische Variablen

| Variable | Typ | Default | Wirkung |
|---|---|---|---|
| `PANTHER_FIREFOX_BINARY` | string (Pfad) | nicht gesetzt | Pfad zur Firefox-Executable. Wird als `binary`-Feld in `moz:firefoxOptions` gesetzt. |
| `PANTHER_FIREFOX_ARGUMENTS` | string (Leerzeichen-getrennt) | nicht gesetzt | Zusaetzliche Argumente fuer den Firefox-Prozess. Wird per `explode(' ', ...)` aufgeteilt und zu den Firefox-Argumenten hinzugefuegt. |

### Error-Screenshots

| Variable | Typ | Default | Wirkung |
|---|---|---|---|
| `PANTHER_ERROR_SCREENSHOT_DIR` | string (Verzeichnispfad) | nicht gesetzt | Wenn gesetzt: Bei Test-Fehler oder Test-Error wird automatisch ein Screenshot in dieses Verzeichnis geschrieben. Dateiname-Format: `YYYY-MM-DD_HH-II-SS_{error|failure}_{TestClass-MethodName}-{clientIndex}.png`. Erfordert `ServerExtension` in `phpunit.dist.xml`. |
| `PANTHER_ERROR_SCREENSHOT_ATTACH` | bool | `false` | `true`: Gibt nach jedem Fehler-Screenshot `[[ATTACHMENT|/pfad/zum/screenshot.png]]` auf stdout aus (GitLab-CI-Attachment-Format). Nur wirksam wenn `PANTHER_ERROR_SCREENSHOT_DIR` gesetzt ist. |

---

## Programmatische Optionen fuer createPantherClient()

```php
static::createPantherClient(
    array $options = [],        // Web-Server- und Browser-Optionen
    array $kernelOptions = [],  // Symfony-Kernel-Optionen (nur bei KernelTestCase)
    array $managerOptions = []  // ChromeManager/FirefoxManager/SeleniumManager-Optionen
): PantherClient
```

### $options (erster Parameter)

| Schluessel | Typ | Default | Wirkung |
|---|---|---|---|
| `webServerDir` | string | `./public` | Document-Root; ueberschreibt `PANTHER_WEB_SERVER_DIR` |
| `hostname` | string | `127.0.0.1` | Hostname des Built-In-Webservers und Basis-URI |
| `port` | int | `9080` | Port des Built-In-Webservers; ueberschreibt `PANTHER_WEB_SERVER_PORT` |
| `router` | string | `''` | Router-Skript; ueberschreibt `PANTHER_WEB_SERVER_ROUTER` |
| `readinessPath` | string | `''` | Readiness-Probe-Pfad; ueberschreibt `PANTHER_READINESS_PATH` |
| `external_base_uri` | string\|null | `null` | Externer Server; ueberschreibt `PANTHER_EXTERNAL_BASE_URI` |
| `env` | array | `[]` | Zusaetzliche Umgebungsvariablen fuer den Webserver-Prozess |
| `browser` | string | `PantherTestCase::CHROME` | `PantherTestCase::CHROME`, `::FIREFOX` oder `::SELENIUM` |
| `browser_arguments` | array\|null | `null` | Browser-Argumente; ueberschreibt automatisch ermittelte Argumente |

### $managerOptions (dritter Parameter) — Chrome

| Schluessel | Typ | Default | Wirkung |
|---|---|---|---|
| `scheme` | string | `'http'` | Protokoll fuer ChromeDriver-Verbindung |
| `host` | string | `'127.0.0.1'` | Host des ChromeDriver-Prozesses |
| `port` | int | `9515` | Port des ChromeDriver-Prozesses |
| `path` | string | `'/status'` | Readiness-Probe-Pfad des ChromeDrivers |
| `chromedriver_arguments` | array | `[]` | Kommandozeilen-Argumente fuer den ChromeDriver-Prozess (nicht Browser), z.B. `['--log-path=myfile.log', '--log-level=DEBUG']` |
| `capabilities` | array | `[]` | WebDriver-Capabilities als assoziatives Array; werden via `setCapability()` gesetzt |
| `connection_timeout_in_ms` | int\|null | `null` (WebDriver-Default) | Timeout fuer die Verbindung zum ChromeDriver in Millisekunden |
| `request_timeout_in_ms` | int\|null | `null` (WebDriver-Default) | Timeout fuer einzelne WebDriver-Anfragen in Millisekunden |

### $managerOptions (dritter Parameter) — Firefox

| Schluessel | Typ | Default | Wirkung |
|---|---|---|---|
| `scheme` | string | `'http'` | Protokoll fuer GeckoDriver-Verbindung |
| `host` | string | `'127.0.0.1'` | Host des GeckoDriver-Prozesses |
| `port` | int | `4444` | Port des GeckoDriver-Prozesses |
| `path` | string | `'/status'` | Readiness-Probe-Pfad des GeckoDrivers |
| `capabilities` | array | `[]` | WebDriver-Capabilities als assoziatives Array |
| `connection_timeout_in_ms` | int\|null | `null` | Verbindungs-Timeout in Millisekunden |
| `request_timeout_in_ms` | int\|null | `null` | Request-Timeout in Millisekunden |

---

## Standardmaessig gesetzte Chrome-Argumente

Diese Argumente setzt Panther automatisch (sofern nicht durch `browser_arguments` vollstaendig ersetzt):

| Argument | Bedingung |
|---|---|
| `--headless` | `PANTHER_NO_HEADLESS` ist falsy |
| `--window-size=1200,1100` | `PANTHER_NO_HEADLESS` ist falsy |
| `--disable-gpu` | `PANTHER_NO_HEADLESS` ist falsy |
| `--auto-open-devtools-for-tabs` | `PANTHER_DEVTOOLS` ist truthy |
| `--no-sandbox` | `PANTHER_NO_SANDBOX` oder `HAS_JOSH_K_SEAL_OF_APPROVAL` ist truthy |
| `--force-prefers-reduced-motion` | `PANTHER_NO_REDUCED_MOTION` ist falsy (Default) |
| `--force-prefers-no-reduced-motion` | `PANTHER_NO_REDUCED_MOTION` ist truthy |
| Werte aus `PANTHER_CHROME_ARGUMENTS` | immer wenn Variable gesetzt |

### Fenstergrösse manuell setzen

```php
// Chrome: via Argument (ueberschreibt --window-size=1200,1100 aus Headless-Default)
$client = Client::createChromeClient(null, ['--window-size=1920,1080']);

// Firefox: via WebDriverDimension
use Facebook\WebDriver\WebDriverDimension;
$client = Client::createFirefoxClient();
$client->manage()->window()->setSize(new WebDriverDimension(1920, 1080));
```

---

## Hostname und Port des Webservers aendern

```php
// In phpunit.dist.xml:
// <server name="PANTHER_WEB_SERVER_PORT" value="8080"/>

// Oder programmatisch:
$client = static::createPantherClient([
    'hostname' => '0.0.0.0',  // Lauscht auf allen Interfaces
    'port'     => 8080,
]);
```

---

## Konfiguration in phpunit.dist.xml

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

## Quellen

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/ProcessManager/ChromeManager.php
- https://github.com/symfony/panther/blob/main/src/ProcessManager/FirefoxManager.php
- https://github.com/symfony/panther/blob/main/src/ProcessManager/WebServerManager.php
- https://github.com/symfony/panther/blob/main/src/PantherTestCaseTrait.php
- https://github.com/symfony/panther/blob/main/src/ServerExtensionLegacy.php
