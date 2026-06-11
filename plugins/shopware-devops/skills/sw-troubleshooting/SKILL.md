---
name: sw-troubleshooting
description: >
  Shopware 6 Troubleshooting & Debugging: Xdebug aktivieren (compose.override.yaml),
  Blackfire/Tideways/PCOV, DB-Verbindung lokal (Port via docker compose ps), Linux-File-Permissions,
  PHPStan EntityRepository Generic-Types, Null-Safety mit first() und Assoziationen.
  Trigger: "xdebug shopware", "debugger shopware docker", "php profiling shopware",
  "phpstan entity repository", "phpstan null safety", "phpstan association",
  "debug shopware lokal", "db verbindung docker shopware", "linux permissions shopware",
  "blackfire shopware", "phpstan generic type". Shopware 6.7.
---

# Shopware 6 — Troubleshooting & Debugging

## Xdebug aktivieren (Docker)

```yaml
# compose.override.yaml im Projektroot:
services:
  web:
    environment:
      XDEBUG_MODE: debug
      XDEBUG_CONFIG: client_host=host.docker.internal
      PHP_PROFILER: xdebug
```

```bash
docker compose up -d
# IDE (PHPStorm/VSCode): Remote-Debugger auf Port 9003 anbinden
```

### Xdebug auf Linux

```yaml
# compose.override.yaml:
services:
  web:
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

## Andere Profiler

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

Weitere unterstützte Profiler: `tideways`, `pcov`.

## DB-Verbindung von Host

```bash
docker compose ps   # → exponierten DB-Port ermitteln
# Client verbinden: Host=127.0.0.1, Port=<aus ps>
```

## Linux File-Permissions

```bash
id -u   # muss 1000 sein → sonst Permission-Errors bei make up / Datei-Schreiben
```

## PHPStan: EntityRepository Generic-Type

```php
// Problem: PHPStan kennt Typ nicht
$products = $this->productRepository->search($criteria, $context)->getEntities();
foreach ($products as $product) {
    $product->getName(); // Fehler: undefined method on Entity
}

// Fix: Generic-Type im PHP-Doc
class MyService
{
    /** @param EntityRepository<ProductCollection> $productRepository */
    public function __construct(
        private readonly EntityRepository $productRepository,
    ) {}
}
```

## PHPStan: Null-Safety bei first() + Assoziationen

```php
// Problem: first() und Assoziationen können null sein
$product = $this->productRepository->search($criteria, $context)->first();
$manufacturer = $product->getManufacturer(); // null-Fehler möglich

// Fix 1: Explizite Null-Checks
$criteria->addAssociation('manufacturer');
$product = $this->productRepository->search($criteria, $context)->first();
if ($product === null) { throw new ProductNotFoundException(); }
$manufacturer = $product->getManufacturer();
if ($manufacturer === null) { throw new ManufacturerNotLoadedException(); }

// Fix 2: Null-Safe-Operator
$manufacturerName = $product?->getManufacturer()?->getName() ?? 'Unknown';
```

## PHPStan: EntityCollection Generic-Type

```php
// Fix: Generic-Type zu Custom Collection hinzufügen
/** @extends EntityCollection<FooEntity> */
class FooCollection extends EntityCollection
{
    protected function getExpectedClass(): string { return FooEntity::class; }
}
```

DAL-Filter/Aggregations-Referenz: `sw-dal-reference`.
