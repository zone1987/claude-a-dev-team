# Contao 5 — Manager Plugin

## Contents

- [Overview](#overview)
- [composer.json configuration](#composerjson-configuration)
- [Available interfaces](#available-interfaces)
- [BundlePluginInterface](#bundleplugininterface)
- [ConfigPluginInterface](#configplugininterface)
- [ExtensionPluginInterface](#extensionplugininterface)
- [DependentPluginInterface](#dependentplugininterface)
- [RoutingPluginInterface](#routingplugininterface)
- [HttpCacheSubscriberPluginInterface](#httpcachesubscriberplugininterface)
- [Modifying the container at compile time](#modifying-the-container-at-compile-time)

## Overview

The Manager Plugin configures the Contao Managed Edition. These plugins are processed
on every `composer update`/`install`.

**Two areas of use:**
1. **Package-specific Manager Plugin:** third-party bundle developers
2. **Application-specific Manager Plugin:** configure the local Managed Edition

Plugins are loaded in a defined order; the application-specific plugin
loads last for maximum control.

---

## composer.json configuration

### For packages

Correct dependency configuration:

```json
{
    "conflict": {
        "contao/manager-plugin": "<2.0 || >=3.0"
    },
    "require-dev": {
        "contao/manager-plugin": "^2.0"
    },
    "extra": {
        "contao-manager-plugin": "YourVendor\\YourPackageName\\ContaoManager\\Plugin"
    }
}
```

### Monorepo: multiple plugins

```json
{
    "extra": {
        "contao-manager-plugin": {
            "your-vendor/feature1-bundle": "YourVendor\\Feature1Bundle\\ContaoManager\\Plugin",
            "your-vendor/feature2-bundle": "YourVendor\\Feature2Bundle\\ContaoManager\\Plugin"
        }
    }
}
```

### Application-specific plugin

No `extra` key needed. The Manager Plugin loads automatically:
- `\App\ContaoManager\Plugin` (recommended)
- `\ContaoManagerPlugin` (not recommended)

---

## Available interfaces

| Interface | Purpose |
|-----------|-------|
| `BundlePluginInterface` | Register bundles in the kernel |
| `ConfigPluginInterface` | Load bundle configuration |
| `ExtensionPluginInterface` | Modify other bundle configurations |
| `DependentPluginInterface` | Ensure the plugin load order |
| `RoutingPluginInterface` | Add application routes |
| `HttpCacheSubscriberPluginInterface` | Modify HttpCache behaviour |

---

## BundlePluginInterface

```php
namespace Vendor\SomeBundle\ContaoManager;

use Contao\ManagerPlugin\Bundle\BundlePluginInterface;
use Contao\ManagerPlugin\Bundle\Config\BundleConfig;
use Contao\ManagerPlugin\Bundle\Parser\ParserInterface;
use Contao\CoreBundle\ContaoCoreBundle;
use Knp\Bundle\MenuBundle\KnpMenuBundle;

class Plugin implements BundlePluginInterface
{
    public function getBundles(ParserInterface $parser)
    {
        return [
            BundleConfig::create(KnpMenuBundle::class),
        ];
    }
}
```

### setLoadAfter — defining dependencies

```php
BundleConfig::create(MyBundle::class)
    ->setLoadAfter([ContaoCoreBundle::class]),
```

### Supporting legacy modules

```php
BundleConfig::create(SomeBundle::class)
    ->setLoadAfter([ContaoCoreBundle::class, 'notification_center'])
    ->setReplace(['old_module_name']),
```

---

## ConfigPluginInterface

Configure bundles through the container configuration loader:

```php
namespace Vendor\SomeBundle\ContaoManager;

use Contao\ManagerPlugin\Config\ConfigPluginInterface;
use Symfony\Component\Config\Loader\LoaderInterface;

class Plugin implements ConfigPluginInterface
{
    public function registerContainerConfiguration(LoaderInterface $loader, array $config)
    {
        $loader->load(__DIR__.'/../../config/config.yaml');
    }
}
```

---

## ExtensionPluginInterface

For complex configuration scenarios in which the merge order is decisive
(e.g. `security.firewalls`, `monolog.handlers`):

```php
namespace Vendor\MyBundle\ContaoManager;

use Contao\ManagerPlugin\Config\ContainerBuilder;
use Contao\ManagerPlugin\Config\ExtensionPluginInterface;

class Plugin implements ExtensionPluginInterface
{
    public function getExtensionConfig($extensionName, array $extensionConfigs, ContainerBuilder $container)
    {
        if ('security' !== $extensionName) {
            return $extensionConfigs;
        }

        foreach ($extensionConfigs as &$extensionConfig) {
            if (isset($extensionConfig['firewalls'])) {
                $extensionConfig['providers']['app.api_user_provider'] = [
                    'id' => 'app.security.api_user_provider',
                ];

                $offset = (int) array_search('frontend', array_keys($extensionConfig['firewalls']));

                $extensionConfig['firewalls'] = array_merge(
                    array_slice($extensionConfig['firewalls'], 0, $offset, true),
                    [
                        'api' => [
                            'pattern' => '/api/*',
                            'anonymous' => true,
                            'guard' => [
                                'authenticators' => ['app.security.api_guard_authenticator'],
                            ],
                        ],
                    ],
                    array_slice($extensionConfig['firewalls'], $offset, null, true)
                );

                break;
            }
        }

        return $extensionConfigs;
    }
}
```

### Adding a Monolog handler

```php
public function getExtensionConfig($extensionName, array $extensionConfigs, ContainerBuilder $container)
{
    if ('monolog' !== $extensionName) {
        return $extensionConfigs;
    }

    foreach ($extensionConfigs as &$extensionConfig) {
        if (isset($extensionConfig['channels'])) {
            $extensionConfig['channels'][] = 'api';
        }

        if (isset($extensionConfig['handlers'])) {
            $offset = (int) array_search('contao', array_keys($extensionConfig['handlers']));

            $extensionConfig['handlers'] = array_merge(
                array_slice($extensionConfig['handlers'], 0, $offset, true),
                [
                    'api' => [
                        'type' => 'rotating_file',
                        'max_files' => 10,
                        'path' => '%kernel.logs_dir%/%kernel.environment%_api.log',
                        'level' => 'info',
                        'channels' => ['api'],
                    ],
                ],
                array_slice($extensionConfig['handlers'], $offset, null, true)
            );
        }
    }

    return $extensionConfigs;
}
```

---

## DependentPluginInterface

Ensure that other package plugins are loaded first:

```php
namespace Vendor\SomeBundle\ContaoManager;

use Contao\ManagerPlugin\Dependency\DependentPluginInterface;

class Plugin implements DependentPluginInterface
{
    public function getPackageDependencies()
    {
        return ['contao/news-bundle'];
    }
}
```

---

## RoutingPluginInterface

```php
namespace Vendor\SomeBundle\ContaoManager;

use Contao\ManagerPlugin\Routing\RoutingPluginInterface;
use Symfony\Component\Config\Loader\LoaderResolverInterface;
use Symfony\Component\HttpKernel\KernelInterface;

class Plugin implements RoutingPluginInterface
{
    public function getRouteCollection(LoaderResolverInterface $resolver, KernelInterface $kernel)
    {
        return $resolver
            ->resolve(__DIR__.'/../../config/routes.yaml')
            ->load(__DIR__.'/../../config/routes.yaml');
    }
}
```

### Attribute-based routes

```php
public function getRouteCollection(LoaderResolverInterface $resolver, KernelInterface $kernel)
{
    return $resolver
        ->resolve(__DIR__.'/../Controller', 'attribute')
        ->load(__DIR__.'/../Controller');
}
```

---

## HttpCacheSubscriberPluginInterface

```php
namespace Vendor\SomeBundle\ContaoManager;

use Contao\ManagerPlugin\Routing\HttpCacheSubscriberPluginInterface;

class Plugin implements HttpCacheSubscriberPluginInterface
{
    public function getHttpCacheSubscribers(): array
    {
        return [
            new CustomCacheSubscriber(),
        ];
    }
}
```

Enables: request modification (e.g. removing cookies) or response manipulation
(e.g. adding headers) before cache or Contao processing.

---

## Modifying the container at compile time

Compiler passes in the Managed Edition (without a kernel/bundle class) via
`ConfigPluginInterface`:

```php
namespace App\ContaoManager;

use App\DependencyInjection\Compiler\MyCompilerPass;
use Contao\ManagerPlugin\Config\ConfigPluginInterface;
use Symfony\Component\Config\Loader\LoaderInterface;
use Symfony\Component\DependencyInjection\ContainerBuilder;

class Plugin implements ConfigPluginInterface
{
    public function registerContainerConfiguration(
        LoaderInterface $loader,
        array $managerConfig
    ) {
        $loader->load(static function (ContainerBuilder $container) {
            $container->addCompilerPass(new MyCompilerPass());
        });
    }
}
```

---

*Source: https://docs.contao.org/5.x/dev/framework/manager-plugin/*  
*https://docs.contao.org/5.x/dev/guides/modify-container-at-compile-time/*
