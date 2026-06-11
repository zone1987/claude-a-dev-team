---
name: sw-cms-element
description: >
  Ein eigenes CMS-Element in Shopware 6 erstellen (Inhaltsbaustein in Block-Slots): registerCmsElement (Admin) +
  DataResolver (PHP) + Storefront-Template. Trigger: "CMS Element", "registerCmsElement", "eigenes CMS-Element",
  "cms element data resolver", "Inhaltselement Erlebniswelt". Shopware 6.7. Scaffolder: /sw-cms-element.
---

# Shopware 6 — CMS-Element

Ein Element ist ein konkreter Inhaltsbaustein (Bild, Text, eigener Baustein). Drei Teile:

1. **Admin-Registrierung** (`registerCmsElement`) + Komponenten (`sw-cms-element-admin`).
2. **DataResolver (PHP)** — lädt zur Laufzeit Daten für das Element (`sw-cms-data-resolver`).
3. **Storefront-Template** — rendert das Element (`sw-cms-element-storefront`).

```js
Shopware.Service('cmsService').registerCmsElement({
    name: 'ff-teaser',
    label: 'ff.cms.element.teaser',
    component: 'sw-cms-el-ff-teaser',
    configComponent: 'sw-cms-el-config-ff-teaser',
    previewComponent: 'sw-cms-el-preview-ff-teaser',
    defaultConfig: { product: { source: 'static', value: null } },
});
```

`defaultConfig`-Felder werden im Config-Modal editiert (`sw-cms-slot-config`) und vom DataResolver ausgewertet.

→ CMS-Architektur (Block/Element/Resolver): [references/cms.md](references/cms.md)
