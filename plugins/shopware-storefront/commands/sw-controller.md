---
name: sw-controller
description: Scaffolds a storefront controller in Shopware 6 including its Page, PageLoader, template and route registration.
argument-hint: <Name> [--plugin <PluginName>] [--route /path]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-controller

Produce a storefront controller with its page, page loader and template. Skills: `sw-controller`,
`sw-twig`.

## Steps
1. Settle the name, target plugin and route path; the route name is `frontend.<owner>.<name>`.
2. Create:
   - `src/Storefront/Controller/<Name>Controller.php` (extends `StorefrontController`,
     `_routeScope storefront`).
   - `src/Storefront/Page/<Name>/<Name>Page.php` and `<Name>PageLoader.php`, plus
     `<Name>PageLoadedEvent`.
   - The template `src/Resources/views/storefront/page/<name>/index.html.twig` (`sw_extends` the base
     layout).
   - Route registration (`routes.xml` or `#[Route]`), and `src/Resources/config/services/storefront.php`
     for the controller and loader — PHP, not XML (`XmlFileLoader` is `@deprecated tag:v6.8.0`),
     explicitly and without autowiring. A `StorefrontController` needs the controller service locator:

     ```php
     $services->set(MyController::class)
         ->args([service(MyPageLoader::class)])
         ->call('setContainer', [service('service_container')])
         ->tag('controller.service_arguments');
     ```

     → `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`
3. Note the follow-up: set `_httpCache` where it applies (`sw-features`), and add the snippets.

Load data in the page loader, not the controller. Never overwrite existing files.
