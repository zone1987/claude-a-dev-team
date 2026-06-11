---
name: sw-cms-element-admin
description: >
  Die Admin-Komponenten eines Shopware-6 CMS-Elements: Element-Komponente (sw-cms-el-*), Config-Komponente
  (sw-cms-el-config-*), Preview (sw-cms-el-preview-*), cms-element/cms-config-Mixin, defaultConfig. Trigger:
  "CMS Element Admin", "sw-cms-el-", "configComponent cms", "cms element config modal", "cms-element mixin". Shopware 6.7.
---

# Shopware 6 — CMS-Element (Admin)

Drei Komponenten je Element, registriert unter `.../module/sw-cms/elements/ff-teaser/`:

| Komponente | Rolle | Mixin |
|---|---|---|
| `sw-cms-el-ff-teaser` (`component`) | Darstellung im Editor | `cms-element` |
| `sw-cms-el-config-ff-teaser` (`configComponent`) | Config-Modal | `cms-element` |
| `sw-cms-el-preview-ff-teaser` (`previewComponent`) | Vorschaukachel | — |

```js
Shopware.Component.register('sw-cms-el-ff-teaser', {
    template,
    mixins: ['cms-element'],
    created() { this.initElementConfig('ff-teaser'); },
});
```

`cms-element`-Mixin liefert `this.element` (config + data). Config-Felder mit Meteor-Komponenten (`mt-*`) an
`element.config.<feld>.value` binden. Laufzeitdaten kommen aus dem `sw-cms-data-resolver`.
