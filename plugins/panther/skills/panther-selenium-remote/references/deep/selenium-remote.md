# Panther — Selenium, Remote WebDriver und fortgeschrittene Client-Konfiguration

## Selenium Grid mit Built-In-Webserver

Panther kann seinen eigenen PHP Built-In-Webserver starten und gleichzeitig einen
Remote-WebDriver (Selenium Grid) als Browser verwenden.

```php
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Symfony\Component\Panther\PantherTestCase;

class SeleniumGridTest extends PantherTestCase
{
    public function testWithSeleniumGrid(): void
    {
        $client = static::createPantherClient(
            [],   // Web-Server-Optionen (Built-In-Server wird normal gestartet)
            [],   // Kernel-Optionen
            [
                'host'         => 'http://selenium-hub:4444',
                'capabilities' => DesiredCapabilities::firefox(),
            ]
        );
        // browser => SELENIUM muss in $options gesetzt werden:
        // static::createPantherClient(['browser' => static::SELENIUM], [], [...])
    }
}
```

Korrektes Beispiel mit `browser => SELENIUM`:

```php
$client = static::createPantherClient(
    [
        'browser' => static::SELENIUM,
    ],
    [],
    [
        'host'         => 'http://selenium-hub:4444/wd/hub',
        'capabilities' => DesiredCapabilities::chrome(),
    ]
);
```

### Direkte Client-Erstellung ohne TestCase

```php
use Symfony\Component\Panther\Client;
use Facebook\WebDriver\Remote\DesiredCapabilities;

// Einfachste Form
$client = Client::createSeleniumClient('http://127.0.0.1:4444/wd/hub');

// Mit Capabilities
$client = Client::createSeleniumClient(
    host: 'http://selenium-hub:4444/wd/hub',
    capabilities: DesiredCapabilities::firefox(),
    baseUri: 'http://myapp.test'
);

// Mit zusaetzlichen Optionen
$client = Client::createSeleniumClient(
    host: 'http://selenium-hub:4444/wd/hub',
    capabilities: DesiredCapabilities::chrome(),
    baseUri: null,
    options: [
        // Optionen fuer SeleniumManager
    ]
);
```

---

## Externer Webserver

Wenn die Applikation auf einem externen Server laeuft (z.B. nginx, Apache, oder
Symfony CLI), wird der Built-In-Server nicht gestartet.

```php
// Programmatisch
$client = static::createPantherClient([
    'external_base_uri' => 'https://localhost:8000',
]);

// Via Umgebungsvariable in .env.test:
// PANTHER_EXTERNAL_BASE_URI=https://localhost:8000

// Via phpunit.dist.xml:
// <server name="PANTHER_EXTERNAL_BASE_URI" value="https://localhost:8000"/>
```

Symfony CLI (Development-Server) als externer Server:

```bash
# Terminal 1: Symfony-Server starten
symfony serve --port=8000

# Terminal 2: Tests laufen lassen
PANTHER_EXTERNAL_BASE_URI=https://localhost:8000 ./vendor/bin/phpunit
```

---

## Multi-Domain-Applikationen

Wenn der Test eine bestimmte Domain braucht, muss er im eigenen Prozess laufen,
da Panther nur eine Basis-URI pro Prozess unterstuetzt.

```php
use PHPUnit\Framework\Attributes\RunInSeparateProcess;
use Symfony\Component\Panther\PantherTestCase;

class TenantATest extends PantherTestCase
{
    #[RunInSeparateProcess]
    public function testTenantALogin(): void
    {
        $client = static::createPantherClient([
            'external_base_uri' => 'http://tenant-a.localhost:8000',
        ]);
        $client->request('GET', '/login');
        $this->assertSelectorExists('form[action="/login_check"]');
    }
}

class TenantBTest extends PantherTestCase
{
    #[RunInSeparateProcess]
    public function testTenantBLogin(): void
    {
        $client = static::createPantherClient([
            'external_base_uri' => 'http://tenant-b.localhost:8000',
        ]);
        $client->request('GET', '/login');
        $this->assertPageTitleContains('Tenant B Login');
    }
}
```

---

## Proxy-Konfiguration

### SOCKS-Proxy (Chrome)

```bash
# .env.test
PANTHER_CHROME_ARGUMENTS='--proxy-server=socks://127.0.0.1:9050'
```

### HTTP/HTTPS-Proxy (Chrome)

```bash
PANTHER_CHROME_ARGUMENTS='--proxy-server=http://proxy.example.com:8080'
```

### Proxy-Bypass fuer lokale Adressen

```bash
PANTHER_CHROME_ARGUMENTS='--proxy-server=http://proxy:8080 --proxy-bypass-list=localhost,127.0.0.1'
```

### Firefox-Proxy (programmatisch)

```php
use Facebook\WebDriver\Remote\DesiredCapabilities;

$capabilities = DesiredCapabilities::firefox();
$capabilities->setCapability('proxy', [
    'proxyType' => 'manual',
    'httpProxy' => 'proxy.example.com:8080',
    'sslProxy'  => 'proxy.example.com:8080',
]);

$client = Client::createFirefoxClient(null, null, [
    'capabilities' => $capabilities->toArray(),
]);
```

---

## Self-Signed-SSL-Zertifikate akzeptieren

### Chrome

```bash
# .env.test
PANTHER_CHROME_ARGUMENTS='--ignore-certificate-errors'
```

### Firefox (programmatisch)

```php
$client = Client::createFirefoxClient(null, null, [
    'capabilities' => [
        'acceptInsecureCerts' => true,
    ],
]);
```

### Firefox im TestCase

```php
$client = static::createPantherClient(
    ['browser' => static::FIREFOX],
    [],
    [
        'capabilities' => [
            'acceptInsecureCerts' => true,
        ],
    ]
);
```

---

## ChromeDriver-Argumente (nicht Browser-Argumente)

ChromeDriver selbst akzeptiert eigene Kommandozeilen-Argumente (verschieden von
Browser-Argumenten). Diese werden ueber `chromedriver_arguments` in `$managerOptions`
uebergeben.

```php
$client = static::createPantherClient(
    [],
    [],
    [
        'chromedriver_arguments' => [
            '--log-path=/var/log/chromedriver.log',
            '--log-level=DEBUG',         // Wertebereich: ALL, DEBUG, INFO, WARNING, SEVERE, OFF
            '--verbose',                 // Ausfuehrliche Ausgabe (entspricht --log-level=ALL)
            '--silent',                  // Keine Ausgaben (entspricht --log-level=OFF)
            '--port=9516',               // Alternativer Port (normalerweise automatisch gesetzt)
            '--whitelisted-ips=',        // Leer = alle IPs erlaubt (fuer Docker-Setups)
            '--allowed-ips=',            // Neueres Alias fuer --whitelisted-ips
        ],
    ]
);
```

---

## Timeouts konfigurieren

### Verbindungs- und Request-Timeouts (WebDriver-Ebene)

```php
$client = Client::createChromeClient(
    chromeDriverBinary: null,
    arguments: null,
    options: [
        'connection_timeout_in_ms' => 30000,  // 30 Sekunden
        'request_timeout_in_ms'    => 60000,  // 60 Sekunden
    ]
);

// Entsprechend im TestCase:
$client = static::createPantherClient([], [], [
    'connection_timeout_in_ms' => 30000,
    'request_timeout_in_ms'    => 60000,
]);
```

### WebDriver-Wait-Timeouts (Test-Ebene)

```php
// Script-Timeout fuer executeAsyncScript
$client->manage()->timeouts()->setScriptTimeout(10); // Sekunden

// Impliziter Wait (nicht empfohlen, kann mit explizitem waitFor() kollidieren)
$client->manage()->timeouts()->implicitlyWait(0);

// Seiten-Lade-Timeout
$client->manage()->timeouts()->pageLoadTimeout(30);
```

---

## DesiredCapabilities — Referenz

```php
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Chrome\ChromeOptions;

// Chrome mit erweiterten Capabilities
$capabilities = DesiredCapabilities::chrome();

// Accessibility-Features deaktivieren (fuer stabile Tests)
$chromeOptions = new ChromeOptions();
$chromeOptions->addArguments([
    '--disable-extensions',
    '--disable-infobars',
    '--disable-popup-blocking',
]);
$capabilities->setCapability(ChromeOptions::CAPABILITY, $chromeOptions);

// Logging aktivieren
$capabilities->setCapability('goog:loggingPrefs', [
    'browser'     => 'ALL',
    'performance' => 'ALL',
]);

// Im TestCase verwenden
$client = static::createPantherClient([], [], [
    'capabilities' => $capabilities->toArray(),
]);
```

---

## Selenium Grid docker-compose

```yaml
# docker-compose.selenium.yml
version: '3.8'
services:
  selenium-hub:
    image: selenium/hub:4
    ports:
      - "4442:4442"
      - "4443:4443"
      - "4444:4444"

  chrome:
    image: selenium/node-chrome:4
    depends_on:
      - selenium-hub
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub
      - SE_EVENT_BUS_PUBLISH_PORT=4442
      - SE_EVENT_BUS_SUBSCRIBE_PORT=4443
    volumes:
      - /dev/shm:/dev/shm

  firefox:
    image: selenium/node-firefox:4
    depends_on:
      - selenium-hub
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub
      - SE_EVENT_BUS_PUBLISH_PORT=4442
      - SE_EVENT_BUS_SUBSCRIBE_PORT=4443
    volumes:
      - /dev/shm:/dev/shm

  app:
    image: myapp:latest
    environment:
      PANTHER_EXTERNAL_BASE_URI: http://app:80
    depends_on:
      - selenium-hub
```

Tests dann ausfuehren:
```bash
docker compose -f docker-compose.selenium.yml run app vendor/bin/phpunit
```

---

## Quellen

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/Client.php
- https://github.com/symfony/panther/blob/main/src/ProcessManager/ChromeManager.php
- https://github.com/symfony/panther/blob/main/src/ProcessManager/FirefoxManager.php
- https://github.com/symfony/panther/blob/main/src/PantherTestCaseTrait.php
- https://github.com/php-webdriver/php-webdriver
