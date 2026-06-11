---
name: sw-cms-element
description: Scaffold eines kompletten Shopware-6 CMS-Elements — Admin (component/config/preview + registerCmsElement), PHP-DataResolver und Storefront-Template.
argument-hint: <element-name> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-cms-element

Erzeuge ein vollständiges CMS-Element über alle drei Ebenen. Skills: `sw-cms-element`, `sw-cms-element-admin`,
`sw-cms-data-resolver`, `sw-cms-element-storefront`, `sw-cms-slot-config`.

## Ablauf
1. Element-Name (kebab, Owner-Präfix z.B. `ff-teaser`) + Ziel-Plugin + benötigte Config-Felder.
2. Admin (`.../module/sw-cms/elements/<name>/`): `index.js` (`registerCmsElement` + `Component.register` für
   component/configComponent/previewComponent), `.html.twig`-Templates, `defaultConfig`.
3. PHP-Resolver `src/Core/Content/Cms/.../<Name>CmsElementResolver.php` (`getType`, `collect`, `enrich`) +
   `shopware.cms.data_resolver`-Tag in services.xml.
4. Storefront-Template `views/storefront/element/cms-element-<name>.html.twig`.
5. In main.js importieren. Hinweis: Admin-Build + Lint.

Namen über alle Ebenen identisch halten. Bestehende Elemente nicht überschreiben.
