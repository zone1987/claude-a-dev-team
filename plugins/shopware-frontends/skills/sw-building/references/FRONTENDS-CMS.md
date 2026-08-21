# Shopware Frontends — CMS (@shopware/cms-base)

Renders the CMS page loaded from the Store API (`useCms`) — sections → blocks → elements — through generic
resolver components that pick the matching Vue component based on the type.

```vue
<script setup>
const { page } = useCms();
</script>
<template>
  <CmsPage v-if="page" :content="page.cmsPage" />
</template>
```

Component resolution: `CmsGenericElement`/`CmsGenericBlock` map `type` (e.g. `text`, `image`, `product-slider`)
onto `CmsElement<Type>`/`CmsBlock<Type>`. Register **custom/overridden** CMS components (e.g. for a
plugin element from `shopware-cms` → `sw-cms-element`) so custom elements are rendered headlessly.
`@shopware/cms-base` ships a Tailwind default implementation as a base.

→ Full reference: [FRONTENDS-CMS-CMS-REFERENCE.md](FRONTENDS-CMS-CMS-REFERENCE.md)
