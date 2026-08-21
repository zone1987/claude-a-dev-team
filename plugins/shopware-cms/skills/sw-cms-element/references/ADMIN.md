# Shopware 6 — CMS element (admin)

Three components per element, registered under `.../module/sw-cms/elements/ff-teaser/`:

| Component | Role | Mixin |
|---|---|---|
| `sw-cms-el-ff-teaser` (`component`) | Rendering in the editor | `cms-element` |
| `sw-cms-el-config-ff-teaser` (`configComponent`) | Config modal | `cms-element` |
| `sw-cms-el-preview-ff-teaser` (`previewComponent`) | Preview tile | — |

```js
Shopware.Component.register('sw-cms-el-ff-teaser', {
    template,
    mixins: ['cms-element'],
    created() { this.initElementConfig('ff-teaser'); },
});
```

The `cms-element` mixin supplies `this.element` (config + data). Bind config fields with Meteor components (`mt-*`) to
`element.config.<field>.value`. Runtime data comes from the `sw-cms-data-resolver`.
