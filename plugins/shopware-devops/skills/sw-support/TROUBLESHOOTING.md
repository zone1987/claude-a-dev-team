# Shopware 6 — Troubleshooting & Debugging

## Contents

- [Enabling Xdebug (Docker)](#enabling-xdebug-docker)
- [Other profilers](#other-profilers)
- [DB connection from the host](#db-connection-from-the-host)
- [Linux file permissions](#linux-file-permissions)
- [PHPStan: EntityRepository generic type](#phpstan-entityrepository-generic-type)
- [PHPStan: null safety with first() + associations](#phpstan-null-safety-with-first-associations)
- [PHPStan: EntityCollection generic type](#phpstan-entitycollection-generic-type)

## Enabling Xdebug (Docker)

```yaml
# compose.override.yaml in the project root:
services:
  web:
    environment:
      XDEBUG_MODE: debug
      XDEBUG_CONFIG: client_host=host.docker.internal
      PHP_PROFILER: xdebug
```

```bash
docker compose up -d
# IDE (PHPStorm/VSCode): attach the remote debugger on port 9003
```

### Xdebug on Linux

```yaml
# compose.override.yaml:
services:
  web:
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

## Other profilers

```yaml
# Blackfire:
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

Other supported profilers: `tideways`, `pcov`.

## DB connection from the host

```bash
docker compose ps   # → determine the exposed DB port
# Connect the client: Host=127.0.0.1, Port=<from ps>
```

## Linux file permissions

```bash
id -u   # must be 1000 → otherwise permission errors on make up / file writes
```

## PHPStan: EntityRepository generic type

```php
// Problem: PHPStan does not know the type
$products = $this->productRepository->search($criteria, $context)->getEntities();
foreach ($products as $product) {
    $product->getName(); // Error: undefined method on Entity
}

// Fix: generic type in the PHP doc
class MyService
{
    /** @param EntityRepository<ProductCollection> $productRepository */
    public function __construct(
        private readonly EntityRepository $productRepository,
    ) {}
}
```

## PHPStan: null safety with first() + associations

```php
// Problem: first() and associations can be null
$product = $this->productRepository->search($criteria, $context)->first();
$manufacturer = $product->getManufacturer(); // null error possible

// Fix 1: explicit null checks
$criteria->addAssociation('manufacturer');
$product = $this->productRepository->search($criteria, $context)->first();
if ($product === null) { throw new ProductNotFoundException(); }
$manufacturer = $product->getManufacturer();
if ($manufacturer === null) { throw new ManufacturerNotLoadedException(); }

// Fix 2: null-safe operator
$manufacturerName = $product?->getManufacturer()?->getName() ?? 'Unknown';
```

## PHPStan: EntityCollection generic type

```php
// Fix: add a generic type to the custom collection
/** @extends EntityCollection<FooEntity> */
class FooCollection extends EntityCollection
{
    protected function getExpectedClass(): string { return FooEntity::class; }
}
```

DAL filter/aggregation reference: `sw-dal-reference`.
