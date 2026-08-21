# Shopware 6 — CMS element

An element is a concrete content building block (image, text, your own block). Three parts:

1. **Admin registration** (`registerCmsElement`) + components (`sw-cms-element-admin`).
2. **DataResolver (PHP)** — loads the element's data at runtime (`sw-cms-data-resolver`).
3. **Storefront template** — renders the element (`sw-cms-element-storefront`).

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

`defaultConfig` fields are edited in the config modal (`sw-cms-slot-config`) and evaluated by the DataResolver.

→ CMS architecture (block/element/resolver): [CMS.md](CMS.md)
