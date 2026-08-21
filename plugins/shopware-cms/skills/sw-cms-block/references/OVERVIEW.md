# Shopware 6 — CMS block

A block is a layout container with named **slots** that take CMS elements. Registered in the admin
(`cmsService`) + a storefront template.

```js
Shopware.Service('cmsService').registerCmsBlock({
    name: 'ff-image-text',
    label: 'ff.cms.block.imageText',
    category: 'commerce',
    component: 'sw-cms-block-ff-image-text',          // admin block component
    previewComponent: 'sw-cms-preview-ff-image-text',
    defaultConfig: { marginBottom: '20px', sizingMode: 'boxed' },
    slots: { left: 'image', right: 'text' },           // slot name → default element
});
```

Register the admin block and preview components (`sw-cms-block-admin`); the storefront template goes under
`views/storefront/block/cms-block-ff-image-text.html.twig`. The slots are filled with CMS elements (`sw-cms-element`).

→ CMS details (block + element + resolver): call the Skill tool with `sw-cms-element`, then see `CMS.md`
