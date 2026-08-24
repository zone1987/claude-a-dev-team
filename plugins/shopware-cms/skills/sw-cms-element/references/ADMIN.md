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

## The config template

A config component's fields sit inside `sw-cms-el-config-*`. Two details from the core's own
examples:

```twig
{# an inheritance-aware field: the switch is disabled while the value is inherited #}
<template #default="{ isInherited }">
    <sw-field :disabled="isInherited" />
</template>
```

```twig
{# vertical alignment, one of the general element config options #}
<sw-select-field
    field="verticalAlign"
    :label="$t('sw-cms.elements.general.config.label.verticalAlign')"
/>
```

## Source

[developer.shopware.com/docs/guides/plugins/plugins/content/cms/add-cms-element.html](https://developer.shopware.com/docs/guides/plugins/plugins/content/cms/add-cms-element.html),
Shopware 6.7, retrieved 2026-08-21.
