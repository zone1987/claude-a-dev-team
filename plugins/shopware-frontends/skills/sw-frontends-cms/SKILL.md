---
name: sw-frontends-cms
description: >
  CMS-Rendering in Shopware-Frontends mit @shopware/cms-base: Sections/Blocks/Elemente aus der Store-API rendern,
  Komponenten-Resolver (CmsGenericElement/Block), eigene CMS-Komponenten registrieren/überschreiben. Trigger:
  "@shopware/cms-base", "CMS rendern headless", "CmsGenericElement", "cms block component frontends", "resolveCmsComponent",
  "Erlebniswelt headless". Shopware Frontends.
---

# Shopware Frontends — CMS (@shopware/cms-base)

Rendert die aus der Store-API geladene CMS-Page (`useCms`) — Sections → Blocks → Elemente — über generische
Resolver-Komponenten, die anhand des Typs die passende Vue-Komponente wählen.

```vue
<script setup>
const { page } = useCms();
</script>
<template>
  <CmsPage v-if="page" :content="page.cmsPage" />
</template>
```

Komponenten-Auflösung: `CmsGenericElement`/`CmsGenericBlock` mappen `type` (z.B. `text`, `image`, `product-slider`)
auf `CmsElement<Type>`/`CmsBlock<Type>`. **Eigene/überschriebene** CMS-Komponenten registrieren (z.B. für ein
Plugin-Element aus `shopware-cms` → `sw-cms-element`), damit Custom-Elemente headless gerendert werden.
`@shopware/cms-base` liefert eine Tailwind-Default-Implementierung als Basis.

→ Vollständige Referenz: [references/deep/cms-reference.md](references/deep/cms-reference.md)
