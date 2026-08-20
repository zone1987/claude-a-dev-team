---
name: sw-cms-element
description: Scaffold a complete Shopware 6 CMS element — admin (component/config/preview + registerCmsElement), the PHP DataResolver and the storefront template.
argument-hint: <element-name> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-cms-element

Create a complete CMS element across all three layers. Skills: `sw-cms-element`,
`sw-cms-block`.

## Steps
1. Element name (kebab-case, owner prefix e.g. `ff-teaser`) + target plugin + the config fields you need.
2. Admin (`.../module/sw-cms/elements/<name>/`): `index.js` (`registerCmsElement` + `Component.register` for
   component/configComponent/previewComponent), the `.html.twig` templates, `defaultConfig`.
3. PHP resolver `src/Core/Content/Cms/.../<Name>CmsElementResolver.php` (`getType`, `collect`, `enrich`) +
   the `shopware.cms.data_resolver` tag in services.xml.
4. Storefront template `views/storefront/element/cms-element-<name>.html.twig`.
5. Import it in main.js. Note: admin build + lint.

Keep the name identical across all layers. Do not overwrite existing elements.
