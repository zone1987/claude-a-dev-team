# Contao 5 — Manager Plugin

## Übersicht

Das Manager Plugin konfiguriert die Contao Managed Edition. Bei jedem
`composer update`/`install` werden diese Plugins verarbeitet.

**Zwei Einsatzbereiche:**
1. **Paket-spezifischer Manager Plugin:** Drittanbieter-Bundle-Entwickler
2. **Anwendungs-spezifischer Manager Plugin:** Lokale Managed Edition konfigurieren

Plugins werden in definierter Reihenfolge geladen; der anwendungsspezifische Plugin
lädt zuletzt für maximale Kontrolle.

---

## composer.json Konfiguration

### Für Pakete

Korrekte Abhängigkeits-Konfiguration:

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

### Monorepo: Mehrere Plugins

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

### Anwendungs-spezifischer Plugin

Kein `extra`-Schlüssel nötig. Der Manager Plugin lädt automatisch:
- `\App\ContaoManager\Plugin` (empfohlen)
- `\ContaoManagerPlugin` (nicht empfohlen)

---

## Verfügbare Interfaces

| Interface | Zweck |
|-----------|-------|
| `BundlePluginInterface` | Bundles im Kernel registrieren |
| `ConfigPluginInterface` | Bundle-Konfiguration laden |
| `ExtensionPluginInterface` | Andere Bundle-Konfigurationen modifizieren |
| `DependentPluginInterface` | Plugin-Ladereihenfolge sicherstellen |
| `RoutingPluginInterface` | Anwendungsrouten hinzufügen |
| `HttpCacheSubscriberPluginInterface` | HttpCache-Verhalten modifizieren |

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

### setLoadAfter — Abhängigkeiten definieren

```php
BundleConfig::create(MyBundle::class)
    ->setLoadAfter([ContaoCoreBundle::class]),
```

### Legacy-Module unterstützen

```php
BundleConfig::create(SomeBundle::class)
    ->setLoadAfter([ContaoCoreBundle::class, 'notification_center'])
    ->setReplace(['old_module_name']),
```

---

## ConfigPluginInterface

Bundles über den Container-Konfigurations-Loader konfigurieren:

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

Für komplexe Konfigurationsszenarien, bei denen Merge-Reihenfolge entscheidend ist
(z.B. `security.firewalls`, `monolog.handlers`):

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

### Monolog Handler hinzufügen

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

Sicherstellen, dass andere Package-Plugins zuerst geladen werden:

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

### Attributbasierte Routen

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

Ermöglicht: Request-Modifikation (z.B. Cookies entfernen) oder Response-Manipulation
(z.B. Header hinzufügen) vor Cache- oder Contao-Verarbeitung.

---

## Container zur Compile-Zeit modifizieren

Compiler Passes in der Managed Edition (ohne Kernel/Bundle-Klasse) via
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

*Quelle: https://docs.contao.org/5.x/dev/framework/manager-plugin/*  
*https://docs.contao.org/5.x/dev/guides/modify-container-at-compile-time/*
