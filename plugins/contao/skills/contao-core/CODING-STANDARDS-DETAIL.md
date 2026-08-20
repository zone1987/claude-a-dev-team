# Contao 5 — Coding Standards & Namenskonventionen

## Contents

- [Coding Standards](#coding-standards)
- [Automatisierte Einhaltung](#automatisierte-einhaltung)
- [Empfohlene Namespace-Struktur](#empfohlene-namespace-struktur)
- [Klassen-Suffix-Konventionen](#klassen-suffix-konventionen)
- [Bundle-Verzeichnisstruktur](#bundle-verzeichnisstruktur)
- [Namespaces für Bundles (vs. Apps)](#namespaces-für-bundles-vs-apps)
- [composer.json Konventionen](#composerjson-konventionen)
- [Publishing-Checkliste](#publishing-checkliste)

## Coding Standards

Contao folgt eng den [Symfony Coding Standards](https://symfony.com/doc/current/contributing/code/standards.html).
Maintainer öffentlicher Bundles werden ermutigt, denselben Ansatz zu verfolgen.

### Ausnahme: Service-Namen

**Contao-Regel:** Service-Namen müssen dem FQCN (Fully Qualified Class Name) der Klasse entsprechen.

**Gilt nicht für** wiederverwendbare Bundles (Symfony-Best-Practice: Bundle-Alias als Präfix).
Contao behandelt Controller jedoch als Projekt-Services — FQCN als Service-Name ist oft
für korrekte Funktionalität erforderlich.

---

## Automatisierte Einhaltung

Das Paket [`contao/easy-coding-standard`](https://github.com/contao/easy-coding-standard)
vereinfacht die Standards-Durchsetzung. Es kombiniert Sniffs und Fixers, die Code-Syntax
automatisch anpassen.

```bash
composer require --dev contao/easy-coding-standard
vendor/bin/ecs check src/
vendor/bin/ecs check src/ --fix
```

Die Contao-CI-Pipeline führt diese Prüfungen bei allen Pull Requests aus.

---

## Empfohlene Namespace-Struktur

| Namespace | Zweck |
|-----------|-------|
| `App\ContaoManager` | Contao Manager Plugin und zugehörige Klassen |
| `App\Controller\ContentElement` | Content Element Fragment-Controller |
| `App\Controller\FrontendModule` | Front-End-Modul Fragment-Controller |
| `App\Controller\Page` | Page-Controller |
| `App\Cron` | Cron-Job-Implementierungen |
| `App\EventListener` | Symfony-Event-Listener, Contao-Hooks & Callbacks |
| `App\Model` | Datenbank-Models |
| `App\Widget` | Formular-Widgets |
| `App\DependencyInjection` | DI-Extensions und Compiler-Passes |

---

## Klassen-Suffix-Konventionen

| Namespace | Suffix | Beispiel |
|-----------|--------|---------|
| `App\Controller` | `Controller` | `App\Controller\ExampleController` |
| `App\Cron` | `Cron` | `App\Cron\ExampleCron` |
| `App\EventListener` | `Listener` | `App\EventListener\ExampleListener` |
| `App\Model` | `Model` | `App\Model\ExampleModel` |

Diese Benennung entspricht Symfony-üblichen Konventionen.

---

## Bundle-Verzeichnisstruktur

```
vendor/somevendor/contao-example-bundle/
├── src/
│   ├── ContaoExampleBundle.php        # Bundle-Klasse
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

## Namespaces für Bundles (vs. Apps)

| Typ | Namespace-Pattern | Beispiel |
|-----|-------------------|---------|
| App | `App\...` | `App\Controller\HomeController` |
| Bundle | `Vendor\BundleName\...` | `Acme\NewsBundleExtras\Controller\NewsController` |

Bundle-Namespace immer aus `composer.json` PSR-4-Autoloading ableiten.

---

## composer.json Konventionen

### Paketname

```
<vendorname>/contao-<extensionname>
```

Beispiele:
- `contao/news-bundle`
- `acme/contao-blog-bundle`
- `mycompany/contao-shop-integration`

### Pflichtfelder für Contao-Bundles

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

## Publishing-Checkliste

- [ ] `type: "contao-bundle"` in `composer.json`
- [ ] Manager Plugin implementiert und referenziert
- [ ] Semantic Versioning (SemVer) für Tags
- [ ] Auf [packagist.org](https://packagist.org) veröffentlicht
- [ ] Packagist-Webhook für automatische Updates konfiguriert
- [ ] Optionale Metadaten in `contao/package-metadata` eingereicht

---

*Quelle: https://docs.contao.org/5.x/dev/guides/coding-standards/*  
*https://docs.contao.org/5.x/dev/guides/namespaces/*  
*https://docs.contao.org/5.x/dev/guides/publishing-bundles/*
