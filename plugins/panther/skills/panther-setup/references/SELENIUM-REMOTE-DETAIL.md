# Panther — Selenium, remote WebDriver and advanced client configuration

## Contents

- [Selenium Grid with the built-in web server](#selenium-grid-with-the-built-in-web-server)
- [External web server](#external-web-server)
- [Multi-domain applications](#multi-domain-applications)
- [Proxy configuration](#proxy-configuration)
- [Accepting self-signed SSL certificates](#accepting-self-signed-ssl-certificates)
- [ChromeDriver arguments (not browser arguments)](#chromedriver-arguments-not-browser-arguments)
- [Configuring timeouts](#configuring-timeouts)
- [DesiredCapabilities — reference](#desiredcapabilities--reference)
- [Selenium Grid docker-compose](#selenium-grid-docker-compose)
- [Sources](#sources)

## Selenium Grid with the built-in web server

Panther can start its own PHP built-in web server and at the same time use a
remote WebDriver (Selenium Grid) as the browser.

```php
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Symfony\Component\Panther\PantherTestCase;

class SeleniumGridTest extends PantherTestCase
{
    public function testWithSeleniumGrid(): void
    {
        $client = static::createPantherClient(
            [],   // Web server options (the built-in server is started as usual)
            [],   // Kernel options
            [
                'host'         => 'http://selenium-hub:4444',
                'capabilities' => DesiredCapabilities::firefox(),
            ]
        );
        // browser => SELENIUM must be set in $options:
        // static::createPantherClient(['browser' => static::SELENIUM], [], [...])
    }
}
```

Correct example with `browser => SELENIUM`:

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

### Creating the client directly without a TestCase

```php
use Symfony\Component\Panther\Client;
use Facebook\WebDriver\Remote\DesiredCapabilities;

// Simplest form
$client = Client::createSeleniumClient('http://127.0.0.1:4444/wd/hub');

// With capabilities
$client = Client::createSeleniumClient(
    host: 'http://selenium-hub:4444/wd/hub',
    capabilities: DesiredCapabilities::firefox(),
    baseUri: 'http://myapp.test'
);

// With additional options
$client = Client::createSeleniumClient(
    host: 'http://selenium-hub:4444/wd/hub',
    capabilities: DesiredCapabilities::chrome(),
    baseUri: null,
    options: [
        // Options for SeleniumManager
    ]
);
```

---

## External web server

If the application runs on an external server (e.g. nginx, Apache, or the
Symfony CLI), the built-in server is not started.

```php
// Programmatically
$client = static::createPantherClient([
    'external_base_uri' => 'https://localhost:8000',
]);

// Via environment variable in .env.test:
// PANTHER_EXTERNAL_BASE_URI=https://localhost:8000

// Via phpunit.dist.xml:
// <server name="PANTHER_EXTERNAL_BASE_URI" value="https://localhost:8000"/>
```

Symfony CLI (development server) as the external server:

```bash
# Terminal 1: start the Symfony server
symfony serve --port=8000

# Terminal 2: run the tests
PANTHER_EXTERNAL_BASE_URI=https://localhost:8000 ./vendor/bin/phpunit
```

---

## Multi-domain applications

If a test needs a specific domain, it must run in its own process,
because Panther supports only one base URI per process.

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

## Proxy configuration

### SOCKS proxy (Chrome)

```bash
# .env.test
PANTHER_CHROME_ARGUMENTS='--proxy-server=socks://127.0.0.1:9050'
```

### HTTP/HTTPS proxy (Chrome)

```bash
PANTHER_CHROME_ARGUMENTS='--proxy-server=http://proxy.example.com:8080'
```

### Proxy bypass for local addresses

```bash
PANTHER_CHROME_ARGUMENTS='--proxy-server=http://proxy:8080 --proxy-bypass-list=localhost,127.0.0.1'
```

### Firefox proxy (programmatically)

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

## Accepting self-signed SSL certificates

### Chrome

```bash
# .env.test
PANTHER_CHROME_ARGUMENTS='--ignore-certificate-errors'
```

### Firefox (programmatically)

```php
$client = Client::createFirefoxClient(null, null, [
    'capabilities' => [
        'acceptInsecureCerts' => true,
    ],
]);
```

### Firefox inside the TestCase

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

## ChromeDriver arguments (not browser arguments)

ChromeDriver itself accepts its own command line arguments (different from
browser arguments). They are passed via `chromedriver_arguments` in
`$managerOptions`.

```php
$client = static::createPantherClient(
    [],
    [],
    [
        'chromedriver_arguments' => [
            '--log-path=/var/log/chromedriver.log',
            '--log-level=DEBUG',         // Value range: ALL, DEBUG, INFO, WARNING, SEVERE, OFF
            '--verbose',                 // Verbose output (equivalent to --log-level=ALL)
            '--silent',                  // No output (equivalent to --log-level=OFF)
            '--port=9516',               // Alternative port (normally set automatically)
            '--whitelisted-ips=',        // Empty = all IPs allowed (for Docker setups)
            '--allowed-ips=',            // Newer alias for --whitelisted-ips
        ],
    ]
);
```

---

## Configuring timeouts

### Connection and request timeouts (WebDriver level)

```php
$client = Client::createChromeClient(
    chromeDriverBinary: null,
    arguments: null,
    options: [
        'connection_timeout_in_ms' => 30000,  // 30 seconds
        'request_timeout_in_ms'    => 60000,  // 60 seconds
    ]
);

// Equivalent inside the TestCase:
$client = static::createPantherClient([], [], [
    'connection_timeout_in_ms' => 30000,
    'request_timeout_in_ms'    => 60000,
]);
```

### WebDriver wait timeouts (test level)

```php
// Script timeout for executeAsyncScript
$client->manage()->timeouts()->setScriptTimeout(10); // seconds

// Implicit wait (not recommended, can collide with an explicit waitFor())
$client->manage()->timeouts()->implicitlyWait(0);

// Page load timeout
$client->manage()->timeouts()->pageLoadTimeout(30);
```

---

## DesiredCapabilities — reference

```php
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Chrome\ChromeOptions;

// Chrome with extended capabilities
$capabilities = DesiredCapabilities::chrome();

// Disable accessibility features (for stable tests)
$chromeOptions = new ChromeOptions();
$chromeOptions->addArguments([
    '--disable-extensions',
    '--disable-infobars',
    '--disable-popup-blocking',
]);
$capabilities->setCapability(ChromeOptions::CAPABILITY, $chromeOptions);

// Enable logging
$capabilities->setCapability('goog:loggingPrefs', [
    'browser'     => 'ALL',
    'performance' => 'ALL',
]);

// Use inside the TestCase
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

Then run the tests:
```bash
docker compose -f docker-compose.selenium.yml run app vendor/bin/phpunit
```

---

## Sources

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/Client.php
- https://github.com/symfony/panther/blob/main/src/ProcessManager/ChromeManager.php
- https://github.com/symfony/panther/blob/main/src/ProcessManager/FirefoxManager.php
- https://github.com/symfony/panther/blob/main/src/PantherTestCaseTrait.php
- https://github.com/php-webdriver/php-webdriver
