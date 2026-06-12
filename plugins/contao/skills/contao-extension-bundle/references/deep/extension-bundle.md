# Contao 5 — Extension/Bundle erstellen und veröffentlichen

## Grundkonzept

Contao-Erweiterungen sind Symfony-Bundles mit Contao-spezifischen Ergänzungen.
Die Begriffe "Package", "Bundle" und "Extension" werden in der Dokumentation
synonym verwendet.

**Ziele:**
- Code-Verwaltung via Git
- Installation über `composer.json`
- Entwicklung direkt im `vendor/`-Verzeichnis möglich

---

## composer.json aufsetzen

Paketname-Konvention: `vendorname/contao-extensionname`

```json
{
    "name": "somevendor/contao-example-bundle",
    "type": "contao-bundle",
    "require": {
        "contao/core-bundle": "^4.13 || ^5.0"
    },
    "license": "LGPL-3.0-or-later",
    "autoload": {
        "psr-4": {
            "Somevendor\\ContaoExampleBundle\\": "src/"
        }
    },
    "extra": {
        "contao-manager-plugin": "Somevendor\\ContaoExampleBundle\\ContaoManager\\Plugin"
    }
}
```

---

## Entwicklungsstruktur

```
somevendor/contao-example-bundle/
├── src/
│   ├── ContaoExampleBundle.php
│   ├── ContaoManager/
│   │   └── Plugin.php
│   ├── Controller/
│   ├── DependencyInjection/
│   │   └── ContaoExampleExtension.php    # optional
│   └── EventListener/
├── contao/
│   ├── config/config.php
│   ├── dca/
│   ├── languages/
│   └── templates/
├── config/
│   ├── services.yaml
│   └── routes.yaml
├── test/
└── composer.json
```

---

## Lokale Entwicklung (Path Repository)

In der Root-`composer.json` der Contao-Installation:

```json
{
    "repositories": {
        "somevendor/contao-example-bundle": {
            "type": "path",
            "url": "/path/to/your/extension/directory"
        }
    }
}
```

Dann das Bundle requireen: `composer require somevendor/contao-example-bundle dev-main`

Composer erstellt einen Symlink ins `vendor/`-Verzeichnis — Änderungen werden sofort
wirksam.

---

## Bundle-Klasse

```php
// src/ContaoExampleBundle.php
namespace Somevendor\ContaoExampleBundle;

use Symfony\Component\HttpKernel\Bundle\AbstractBundle;

class ContaoExampleBundle extends AbstractBundle
{
}
```

### Mit Service-Konfiguration (loadExtension)

```php
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

class ContaoExampleBundle extends AbstractBundle
{
    public function loadExtension(
        array $config,
        ContainerConfigurator $containerConfigurator,
        ContainerBuilder $containerBuilder,
    ): void {
        $containerConfigurator->import('../config/services.yaml');
    }
}
```

### Alternativ: DependencyInjection Extension

```php
// src/DependencyInjection/ContaoExampleExtension.php
namespace Somevendor\ContaoExampleBundle\DependencyInjection;

use Symfony\Component\Config\FileLocator;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\DependencyInjection\Extension\Extension;
use Symfony\Component\DependencyInjection\Loader\YamlFileLoader;

class ContaoExampleExtension extends Extension
{
    public function load(array $configs, ContainerBuilder $container): void
    {
        (new YamlFileLoader($container, new FileLocator(__DIR__ . '/../../config')))
            ->load('services.yaml');
    }
}
```

---

## Manager Plugin

```php
// src/ContaoManager/Plugin.php
namespace Somevendor\ContaoExampleBundle\ContaoManager;

use Contao\CoreBundle\ContaoCoreBundle;
use Contao\ManagerPlugin\Bundle\BundlePluginInterface;
use Contao\ManagerPlugin\Bundle\Config\BundleConfig;
use Contao\ManagerPlugin\Bundle\Parser\ParserInterface;
use Somevendor\ContaoExampleBundle\ContaoExampleBundle;

class Plugin implements BundlePluginInterface
{
    public function getBundles(ParserInterface $parser): array
    {
        return [
            BundleConfig::create(ContaoExampleBundle::class)
                ->setLoadAfter([ContaoCoreBundle::class]),
        ];
    }
}
```

---

## Service-Konfiguration (`config/services.yaml`)

```yaml
services:
    _defaults:
        autowire: true
        autoconfigure: true

    Somevendor\ContaoExampleBundle\:
        resource: ../src
        exclude: ../src/{ContaoManager,DependencyInjection,ContaoExampleBundle.php}
```

---

## Routing-Konfiguration

Im Manager Plugin `RoutingPluginInterface` implementieren:

```php
use Contao\ManagerPlugin\Routing\RoutingPluginInterface;
use Symfony\Component\Config\Loader\LoaderResolverInterface;
use Symfony\Component\HttpKernel\KernelInterface;

class Plugin implements BundlePluginInterface, RoutingPluginInterface
{
    // ...

    public function getRouteCollection(LoaderResolverInterface $resolver, KernelInterface $kernel)
    {
        return $resolver
            ->resolve(__DIR__.'/../../config/routes.yaml')
            ->load(__DIR__.'/../../config/routes.yaml');
    }
}
```

```yaml
# config/routes.yaml
somevendor.contao_example_bundle.controller:
    resource: ../src/Controller
    type: attribute
```

---

## Veröffentlichung (Packagist)

1. Git-Repository initialisieren und auf GitHub/GitLab pushen:

```bash
cd vendor/somevendor/contao-example-bundle
git init
git add --all
git commit -m "initial commit"
git remote add origin git@github.com:somevendor/contao-example-bundle.git
git push origin main
```

2. Package auf [packagist.org/packages/submit](https://packagist.org/packages/submit) einreichen
3. Automatische Updates konfigurieren (Packagist Webhook)
4. Lokale Path-Repository-Konfiguration aus `composer.json` entfernen

### Voraussetzungen für Indexierung auf extensions.contao.org

- Auf packagist.org veröffentlicht
- `type: "contao-bundle"` in `composer.json`
- Versions-Tags vorhanden (Branches alleine werden ignoriert)
- Contao Manager Plugin referenziert

### Erweiterte Metadaten

Zusätzliche Beschreibungen, Übersetzungen und Logos können im Repository
`contao/package-metadata` eingereicht werden.

### Private/kommerzielle Pakete

**Artifact-Pakete:** ZIP-Archive mit allen Dateien plus `composer.json` (inkl.
Pflicht-Feld `version`). Können direkt im Contao Manager hochgeladen werden.

**contao-provider Typ:** Ermöglicht Konfiguration privater Repositories ohne manuelle
`composer.json`-Bearbeitung durch End-User.

---

*Quelle: https://docs.contao.org/5.x/dev/getting-started/extension/*  
*https://docs.contao.org/5.x/dev/guides/first-bundle/*  
*https://docs.contao.org/5.x/dev/guides/publishing-bundles/*  
*https://docs.contao.org/5.x/dev/guides/namespaces/*  
*https://docs.contao.org/5.x/dev/guides/coding-standards/*
