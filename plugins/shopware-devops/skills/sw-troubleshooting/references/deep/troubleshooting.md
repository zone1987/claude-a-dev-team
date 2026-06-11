# Shopware 6 — Troubleshooting & Debugging (vollständige Referenz)

Quellen: `guides/development/troubleshooting/index.md`, `troubleshooting/phpstan.md`

## Datenbankverbindung von Host-Maschine

Für DB-Clients (Adminer, DBeaver, lokaler MySQL-Client):

```bash
# Exponierten DB-Port ermitteln:
docker compose ps
```

Verbindungsdaten:
- Host: `127.0.0.1` oder `localhost`
- Port: Aus `docker compose ps` (exponierter Port)
- Credentials: aus `.env`/`docker-compose.yml`

## PHP Debugging mit Xdebug aktivieren

### Basis-Konfiguration

```yaml
# compose.override.yaml (im Projektroot anlegen):
services:
  web:
    environment:
      XDEBUG_MODE: debug
      XDEBUG_CONFIG: client_host=host.docker.internal
      PHP_PROFILER: xdebug
```

```bash
docker compose up -d
```

PHPStorm: Settings → PHP → Servers → Server mit lokalem Port konfigurieren.
VS Code: PHP Debug Extension installieren, launch.json konfigurieren.

Standard Xdebug-Port: `9003`

### Xdebug auf Linux

Auf Linux-Hosts muss `host.docker.internal` manuell gemappt werden:

```yaml
# compose.override.yaml:
services:
  web:
    environment:
      XDEBUG_MODE: debug
      XDEBUG_CONFIG: client_host=host.docker.internal
      PHP_PROFILER: xdebug
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

## Andere PHP-Profiler

### Blackfire

```yaml
# compose.override.yaml:
services:
  web:
    environment:
      - PHP_PROFILER=blackfire
  blackfire:
    image: blackfire/blackfire:2
    environment:
      BLACKFIRE_SERVER_ID: XXXX
      BLACKFIRE_SERVER_TOKEN: XXXX
```

### Tideways

```yaml
services:
  web:
    environment:
      - PHP_PROFILER=tideways
  tideways:
    image: tideways/daemon
    # ... Tideways-Container-Konfiguration
```

### PCOV (Code Coverage)

```yaml
services:
  web:
    environment:
      - PHP_PROFILER=pcov
```

PCOV benötigt keinen extra Container.

## Linux: File-Permissions

Auf Linux-Hosts muss die User-ID 1000 sein für korrekte Datei-Berechtigungen in Containern:

```bash
id -u
# Gibt User-ID aus — muss 1000 sein

# Falls nicht 1000: Permission-Errors bei:
# - make up
# - Schreiben in Projektdateien
# - Cache-Generierung
```

Lösung: Entweder User-ID in Docker-Konfiguration anpassen oder als User 1000 arbeiten.

## PHPStan: Häufige DAL-Fehler

### EntityRepository Generic-Type fehlt

**Problem:**
```php
class ProductService
{
    public function __construct(
        private readonly EntityRepository $productRepository,
    ) {}

    public function doSomething(): void
    {
        $products = $this->productRepository->search($criteria, $context)->getEntities();
        foreach ($products as $product) {
            // PHPStan-Fehler: "Call to an undefined method
            // Shopware\Core\Framework\DataAbstractionLayer\Entity::getName()"
            $name = $product->getName();
        }
    }
}
```

**Lösung:** Generic-Type im PHP-Doc hinzufügen:
```php
class ProductService
{
    /**
     * @param EntityRepository<ProductCollection> $productRepository
     */
    public function __construct(
        private readonly EntityRepository $productRepository,
    ) {}

    public function doSomething(): void
    {
        $products = $this->productRepository->search($criteria, $context)->getEntities();
        foreach ($products as $product) {
            $name = $product->getName(); // PHPStan identifiziert korrekt als ProductEntity
        }
    }
}
```

**Hinweis:** `EntityRepository` nimmt `EntityCollection` (nicht `Entity`) als Generic-Typ.

### Null-Safety bei first() und Assoziationen

**Problem:**
```php
$product = $this->productRepository->search($criteria, $context)->first();
$manufacturer = $product->getManufacturer();
// PHPStan: "Cannot call method getManufacturer() on
// Shopware\Core\Content\Product\ProductEntity|null"
$manufacturerName = $manufacturer->getName();
// PHPStan: "Cannot call method getName() on ...ProductManufacturerEntity|null"
```

**Lösung 1 — Explizite Null-Checks (empfohlen für Services):**
```php
$criteria = new Criteria();
$criteria->addAssociation('manufacturer');

$product = $this->productRepository->search($criteria, $context)->first();
if ($product === null) {
    throw new ProductNotFoundException();
}

$manufacturer = $product->getManufacturer();
if ($manufacturer === null) {
    throw new ManufacturerNotLoadedException();
}

$manufacturerName = $manufacturer->getName(); // Kein Fehler
```

**Lösung 2 — Null-Safe-Operator (für einfache Fälle):**
```php
$manufacturerName = $product?->getManufacturer()?->getName() ?? 'Unknown';
```

**Wichtig:** Assoziationen immer in Criteria hinzufügen, bevor auf sie zugegriffen wird.

### EntityCollection Generic-Type fehlt

**Problem:**
```php
class FooCollection extends EntityCollection
{
    protected function getExpectedClass(): string
    {
        return FooEntity::class;
    }
}

$foo = $fooCollection->first();
if ($foo === null) { throw new FooNotFoundException(); }
$foo->bar(); // PHPStan: "Cannot call method bar() on Entity"
```

**Lösung:**
```php
/**
 * @extends EntityCollection<FooEntity>
 */
class FooCollection extends EntityCollection
{
    protected function getExpectedClass(): string
    {
        return FooEntity::class;
    }
}

$foo = $fooCollection->first();
if ($foo === null) { throw new FooNotFoundException(); }
$foo->bar(); // Kein Fehler — PHPStan weiß, dass es FooEntity ist
```

## Nützliche `bin/console`-Befehle für Debugging

```bash
# System-Status
bin/console system:check

# Plugin-Informationen
bin/console plugin:list
bin/console plugin:refresh

# Cache leeren
bin/console cache:clear

# DAL Debug
bin/console debug:container --show-private | grep repository

# Schema validieren
bin/console doctrine:schema:validate

# Scheduled Tasks
bin/console scheduled-task:list
bin/console messenger:stats

# Logs (Symfony)
tail -f var/log/dev.log
```

## Umgebungsvariablen für Debugging

```dotenv
# .env.local
APP_ENV=dev              # Aktiviert Symfony Profiler, bessere Fehlerseiten
APP_DEBUG=1              # Aktiviert Debug-Modus
SHOPWARE_LOG_LEVEL=debug # Ausführliche Log-Ausgabe
```
