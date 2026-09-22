# Shopware 6 — Dependency Injection

**Services are registered in PHP, not XML. And without autowiring.**

`src/Resources/config/services.php` plus one file per area under
`src/Resources/config/services/`.

## Why PHP and not XML

**Shopware is removing XML.** `Framework/Bundle.php` carries this on its `XmlFileLoader`:

```
@deprecated tag:v6.8.0 - XML service definitions are deprecated, remove the
XmlFileLoader together with the deprecation
```

Two further reasons, independent of the deprecation:

- **PHPStan reads PHP.** A typo in a class name fails the gate. In XML it fails on the
  first page view.
- **The IDE follows the reference.** `MyService::class` is clickable; a string in XML is
  not.

## The structure

`services.php` imports only:

```php
<?php declare(strict_types=1);

namespace {PluginNamespace}\Resources\config;

use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $containerConfigurator): void {
    $containerConfigurator->import('services/definitions.php');
    $containerConfigurator->import('services/logging.php');
    $containerConfigurator->import('services/subscribers.php');
    $containerConfigurator->import('services/commands.php');
};
```

**One file per area.** A single `services.php` holding everything becomes unreadable, and
every merge conflict lands in the same file.

## One service file

```php
<?php declare(strict_types=1);

namespace {PluginNamespace}\Resources\config\services;

use {PluginNamespace}\Service\MyService;
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

use function Symfony\Component\DependencyInjection\Loader\Configurator\service;

return static function (ContainerConfigurator $containerConfigurator): void {
    $services = $containerConfigurator->services();

    $services->set(MyService::class)
        ->args([
            service('product.repository'),
            service('Doctrine\DBAL\Connection'),
        ]);
};
```

## No autowiring, no autoconfigure

There is **no** `->autowire()` and **no** `->autoconfigure()`. Every dependency is written
out in `->args([...])`.

| Reason | Detail |
|---|---|
| **Visibility** | A class's dependencies are in one place, readable without opening the constructor |
| **No surprises on update** | Autowiring resolves by type. When Shopware changes a type declaration, a different service is injected — silently |
| **Legible failures** | A missing explicit dependency fails the container build and names the service. A failed autowire says "cannot autowire" and names a type |
| **The consequence** | Without `autoconfigure` you set tags yourself — see below |

## Tags you now have to set yourself

This is the cost of dropping `autoconfigure`, and the place it bites hardest:

```php
$services->set(MyCachingService::class)
    ->args([service('product.repository')])
    // Symfony wires ResetInterface through registerForAutoconfiguration, which this
    // plugin does not use: services are registered explicitly, so the tag is too.
    ->tag('kernel.reset', ['method' => 'reset']);
```

**Implementing `ResetInterface` alone does nothing here.** The interface is there, the
method exists, the code looks complete — and `reset()` is never called. The same applies
to `kernel.event_subscriber`, `console.command` and every other tag Symfony would
otherwise infer.

→ Which services need `ResetInterface`: [SERVICE-RESET.md](SERVICE-RESET.md)

## Repositories

Shopware generates a repository service per DAL entity, named `<entity_name>.repository`:

```php
service('product.repository')
service('{table-prefix}my_entity.repository')
```

## Decorators

```php
$services->set(MyPagingProcessor::class)
    ->decorate('Shopware\Core\Content\Product\SalesChannel\Listing\Processor\PagingListingProcessor')
    ->args([
        service(MyPagingProcessor::class . '.inner'),
        service(MyLoader::class),
    ]);
```

**`.inner` is the decorated service**, passed as the first argument so the decorator can
delegate to the original.

→ In depth: [SERVICE-DECORATION.md](SERVICE-DECORATION.md)
→ Tags: [SERVICE-TAGS.md](SERVICE-TAGS.md)
→ Skeleton: [examples/dependency-injection-services.php](../examples/dependency-injection-services.php)

## Migrating an existing plugin from XML

The five XML files under `src/Resources/config/` are replaced by `services.php` plus one
file per area. **Do it in one commit**, not file by file: a half-migrated plugin has its
services in two places, and which one wins depends on load order.
