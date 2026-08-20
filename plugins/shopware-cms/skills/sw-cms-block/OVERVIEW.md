# Shopware 6 — CMS-Block

Ein Block ist ein Layout-Container mit benannten **Slots**, die CMS-Elemente aufnehmen. Registrierung im Admin
(`cmsService`) + Storefront-Template.

```js
Shopware.Service('cmsService').registerCmsBlock({
    name: 'ff-image-text',
    label: 'ff.cms.block.imageText',
    category: 'commerce',
    component: 'sw-cms-block-ff-image-text',          // Admin-Block-Komponente
    previewComponent: 'sw-cms-preview-ff-image-text',
    defaultConfig: { marginBottom: '20px', sizingMode: 'boxed' },
    slots: { left: 'image', right: 'text' },           // Slot-Name → Default-Element
});
```

Admin-Block-/Preview-Komponente registrieren (`sw-cms-block-admin`); Storefront-Template unter
`views/storefront/block/cms-block-ff-image-text.html.twig`. Die Slots werden mit CMS-Elementen befüllt (`sw-cms-element`).

→ CMS-Details (Block + Element + Resolver): [../sw-cms-element/`CMS.md`](../sw-cms-element/`CMS.md`)
