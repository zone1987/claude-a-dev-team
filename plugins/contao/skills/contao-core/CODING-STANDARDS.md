# Contao 5 — Coding Standards & Naming Conventions

## Contents

- [Coding Standards](#coding-standards)
- [Automated Compliance](#automated-compliance)
- [Recommended Namespace Structure](#recommended-namespace-structure)
- [Class Suffix Conventions](#class-suffix-conventions)
- [Bundle Directory Structure](#bundle-directory-structure)
- [Namespaces for Bundles (vs. Apps)](#namespaces-for-bundles-vs-apps)
- [composer.json Conventions](#composerjson-conventions)
- [Publishing Checklist](#publishing-checklist)

## Coding Standards

Contao closely follows the [Symfony Coding Standards](https://symfony.com/doc/current/contributing/code/standards.html).
Maintainers of public bundles are encouraged to pursue the same approach.

### Exception: Service Names

**Contao rule:** Service names must match the FQCN (Fully Qualified Class Name) of the class.

**Does not apply to** reusable bundles (Symfony best practice: bundle alias as prefix).
However, Contao treats controllers as project services — the FQCN as the service name is often
required for correct functionality.

---

## Automated Compliance

The package [`contao/easy-coding-standard`](https://github.com/contao/easy-coding-standard)
simplifies enforcing the standards. It combines sniffs and fixers that adjust code syntax
automatically.

```bash
composer require --dev contao/easy-coding-standard
vendor/bin/ecs check src/
vendor/bin/ecs check src/ --fix
```

The Contao CI pipeline runs these checks on all pull requests.

---

## Recommended Namespace Structure

| Namespace | Purpose |
|-----------|-------|
| `App\ContaoManager` | Contao Manager Plugin and related classes |
| `App\Controller\ContentElement` | Content element fragment controllers |
| `App\Controller\FrontendModule` | Front end module fragment controllers |
| `App\Controller\Page` | Page controllers |
| `App\Cron` | Cron job implementations |
| `App\EventListener` | Symfony event listeners, Contao hooks & callbacks |
| `App\Model` | Database models |
| `App\Widget` | Form widgets |
| `App\DependencyInjection` | DI extensions and compiler passes |

---

## Class Suffix Conventions

| Namespace | Suffix | Example |
|-----------|--------|---------|
| `App\Controller` | `Controller` | `App\Controller\ExampleController` |
| `App\Cron` | `Cron` | `App\Cron\ExampleCron` |
| `App\EventListener` | `Listener` | `App\EventListener\ExampleListener` |
| `App\Model` | `Model` | `App\Model\ExampleModel` |

This naming matches the conventions common in Symfony.

---

## Bundle Directory Structure

```
vendor/somevendor/contao-example-bundle/
├── src/
│   ├── ContaoExampleBundle.php        # Bundle class
│   ├── ContaoManager/
│   │   └── Plugin.php                 # Manager Plugin
│   ├── Controller/
│   │   ├── ContentElement/
│   │   │   └── ExampleController.php
│   │   └── FrontendModule/
│   │       └── NewsListController.php
│   ├── DependencyInjection/
│   │   └── ContaoExampleExtension.php # optional
│   ├── EventListener/
│   │   └── ParseArticlesListener.php
│   └── Model/
│       └── ExampleModel.php
├── contao/
│   ├── config/
│   │   └── config.php
│   ├── dca/
│   │   └── tl_example.php
│   ├── languages/
│   │   └── en/
│   │       └── tl_example.php
│   └── templates/
│       └── content_element/
│           └── example.html.twig
├── config/
│   ├── services.yaml
│   └── routes.yaml
├── test/
├── composer.json
└── README.md
```

---

## Namespaces for Bundles (vs. Apps)

| Type | Namespace pattern | Example |
|-----|-------------------|---------|
| App | `App\...` | `App\Controller\HomeController` |
| Bundle | `Vendor\BundleName\...` | `Acme\NewsBundleExtras\Controller\NewsController` |

Always derive the bundle namespace from the PSR-4 autoloading in `composer.json`.

---

## composer.json Conventions

### Package name

```
<vendorname>/contao-<extensionname>
```

Examples:
- `contao/news-bundle`
- `acme/contao-blog-bundle`
- `mycompany/contao-shop-integration`

### Required fields for Contao bundles

```json
{
    "name": "vendor/contao-example-bundle",
    "type": "contao-bundle",
    "require": {
        "contao/core-bundle": "^5.0"
    },
    "autoload": {
        "psr-4": {
            "Vendor\\ContaoExampleBundle\\": "src/"
        }
    },
    "extra": {
        "contao-manager-plugin": "Vendor\\ContaoExampleBundle\\ContaoManager\\Plugin"
    }
}
```

---

## Publishing Checklist

- [ ] `type: "contao-bundle"` in `composer.json`
- [ ] Manager Plugin implemented and referenced
- [ ] Semantic Versioning (SemVer) for tags
- [ ] Published on [packagist.org](https://packagist.org)
- [ ] Packagist webhook configured for automatic updates
- [ ] Optional metadata submitted to `contao/package-metadata`

---

*Source: https://docs.contao.org/5.x/dev/guides/coding-standards/*  
*https://docs.contao.org/5.x/dev/guides/namespaces/*  
*https://docs.contao.org/5.x/dev/guides/publishing-bundles/*
