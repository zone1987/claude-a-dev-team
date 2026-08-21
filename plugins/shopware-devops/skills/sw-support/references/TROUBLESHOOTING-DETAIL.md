# Shopware 6 — Troubleshooting & Debugging (complete reference)

Sources: `guides/development/troubleshooting/index.md`, `troubleshooting/phpstan.md`

## Contents

- [Database connection from the host machine](#database-connection-from-the-host-machine)
- [Enabling PHP debugging with Xdebug](#enabling-php-debugging-with-xdebug)
- [Other PHP profilers](#other-php-profilers)
- [Linux: file permissions](#linux-file-permissions)
- [PHPStan: common DAL errors](#phpstan-common-dal-errors)
- [Useful `bin/console` commands for debugging](#useful-binconsole-commands-for-debugging)
- [Environment variables for debugging](#environment-variables-for-debugging)

## Database connection from the host machine

For DB clients (Adminer, DBeaver, local MySQL client):

```bash
# Determine the exposed DB port:
docker compose ps
```

Connection details:
- Host: `127.0.0.1` or `localhost`
- Port: from `docker compose ps` (exposed port)
- Credentials: from `.env`/`docker-compose.yml`

## Enabling PHP debugging with Xdebug

### Base configuration

```yaml
# compose.override.yaml (create it in the project root):
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

PHPStorm: Settings → PHP → Servers → configure a server with the local port.
VS Code: install the PHP Debug extension, configure launch.json.

Default Xdebug port: `9003`

### Xdebug on Linux

On Linux hosts, `host.docker.internal` has to be mapped manually:

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

## Other PHP profilers

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
    # ... Tideways container configuration
```

### PCOV (code coverage)

```yaml
services:
  web:
    environment:
      - PHP_PROFILER=pcov
```

PCOV needs no extra container.

## Linux: file permissions

On Linux hosts the user ID must be 1000 for correct file permissions inside containers:

```bash
id -u
# Prints the user ID — must be 1000

# If not 1000: permission errors on:
# - make up
# - writing to project files
# - cache generation
```

Solution: either adjust the user ID in the Docker configuration or work as user 1000.

## PHPStan: common DAL errors

### Missing EntityRepository generic type

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
            // PHPStan error: "Call to an undefined method
            // Shopware\Core\Framework\DataAbstractionLayer\Entity::getName()"
            $name = $product->getName();
        }
    }
}
```

**Solution:** add the generic type in the PHP doc:
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
            $name = $product->getName(); // PHPStan correctly identifies it as ProductEntity
        }
    }
}
```

**Note:** `EntityRepository` takes `EntityCollection` (not `Entity`) as its generic type.

### Null safety with first() and associations

**Problem:**
```php
$product = $this->productRepository->search($criteria, $context)->first();
$manufacturer = $product->getManufacturer();
// PHPStan: "Cannot call method getManufacturer() on
// Shopware\Core\Content\Product\ProductEntity|null"
$manufacturerName = $manufacturer->getName();
// PHPStan: "Cannot call method getName() on ...ProductManufacturerEntity|null"
```

**Solution 1 — explicit null checks (recommended for services):**
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

$manufacturerName = $manufacturer->getName(); // No error
```

**Solution 2 — null-safe operator (for simple cases):**
```php
$manufacturerName = $product?->getManufacturer()?->getName() ?? 'Unknown';
```

**Important:** always add associations to the Criteria before accessing them.

### Missing EntityCollection generic type

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

**Solution:**
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
$foo->bar(); // No error — PHPStan knows it is a FooEntity
```

## Useful `bin/console` commands for debugging

```bash
# System status
bin/console system:check

# Plugin information
bin/console plugin:list
bin/console plugin:refresh

# Clear the cache
bin/console cache:clear

# DAL debug
bin/console debug:container --show-private | grep repository

# Validate the schema
bin/console doctrine:schema:validate

# Scheduled tasks
bin/console scheduled-task:list
bin/console messenger:stats

# Logs (Symfony)
tail -f var/log/dev.log
```

## Environment variables for debugging

```dotenv
# .env.local
APP_ENV=dev              # Enables the Symfony profiler and better error pages
APP_DEBUG=1              # Enables debug mode
SHOPWARE_LOG_LEVEL=debug # Verbose log output
```
