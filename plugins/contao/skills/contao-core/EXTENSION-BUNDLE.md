# Contao 5 — Creating and publishing an extension/bundle

## Contents

- [Basic concept](#basic-concept)
- [Setting up composer.json](#setting-up-composerjson)
- [Development structure](#development-structure)
- [Local development (path repository)](#local-development-path-repository)
- [Bundle class](#bundle-class)
- [Manager Plugin](#manager-plugin)
- [Service configuration (`config/services.yaml`)](#service-configuration-configservicesyaml)
- [Routing configuration](#routing-configuration)
- [Publishing (Packagist)](#publishing-packagist)

## Basic concept

Contao extensions are Symfony bundles with Contao-specific additions.
The terms "package", "bundle" and "extension" are used synonymously in the
documentation.

**Goals:**
- Code management via Git
- Installation through `composer.json`
- Development directly in the `vendor/` directory possible

---

## Setting up composer.json

Package name convention: `vendorname/contao-extensionname`

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

## Development structure

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

## Local development (path repository)

In the root `composer.json` of the Contao installation:

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

Then require the bundle: `composer require somevendor/contao-example-bundle dev-main`

Composer creates a symlink into the `vendor/` directory — changes take effect
immediately.

---

## Bundle class

```php
// src/ContaoExampleBundle.php
namespace Somevendor\ContaoExampleBundle;

use Symfony\Component\HttpKernel\Bundle\AbstractBundle;

class ContaoExampleBundle extends AbstractBundle
{
}
```

### With service configuration (loadExtension)

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

### Alternative: DependencyInjection extension

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

## Service configuration (`config/services.yaml`)

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

## Routing configuration

Implement `RoutingPluginInterface` in the Manager Plugin:

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

## Publishing (Packagist)

1. Initialise the Git repository and push it to GitHub/GitLab:

```bash
cd vendor/somevendor/contao-example-bundle
git init
git add --all
git commit -m "initial commit"
git remote add origin git@github.com:somevendor/contao-example-bundle.git
git push origin main
```

2. Submit the package at [packagist.org/packages/submit](https://packagist.org/packages/submit)
3. Configure automatic updates (Packagist webhook)
4. Remove the local path repository configuration from `composer.json`

### Requirements for indexing on extensions.contao.org

- Published on packagist.org
- `type: "contao-bundle"` in `composer.json`
- Version tags present (branches alone are ignored)
- Contao Manager Plugin referenced

### Extended metadata

Additional descriptions, translations and logos can be submitted in the
`contao/package-metadata` repository.

### Private/commercial packages

**Artifact packages:** ZIP archives with all files plus a `composer.json` (including
the mandatory `version` field). They can be uploaded directly in the Contao Manager.

**contao-provider type:** allows configuring private repositories without manual
`composer.json` editing by end users.

---

*Source: https://docs.contao.org/5.x/dev/getting-started/extension/*  
*https://docs.contao.org/5.x/dev/guides/first-bundle/*  
*https://docs.contao.org/5.x/dev/guides/publishing-bundles/*  
*https://docs.contao.org/5.x/dev/guides/namespaces/*  
*https://docs.contao.org/5.x/dev/guides/coding-standards/*
