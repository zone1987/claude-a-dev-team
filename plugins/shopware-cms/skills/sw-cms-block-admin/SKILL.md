---
name: sw-cms-block-admin
description: >
  Die Admin-Seite eines Shopware-6 CMS-Blocks: Block-Komponente (sw-cms-block-*) + Preview-Komponente
  (sw-cms-preview-*), Slot-Markup, Registrierung. Trigger: "CMS Block Admin Komponente", "sw-cms-block-", "cms preview component",
  "Block component administration", "block slot template admin". Shopware 6.7.
---

# Shopware 6 — CMS-Block (Admin)

Jeder Block braucht zwei Admin-Komponenten: die **Block-Komponente** (rendert die Slots im Editor) und die
**Preview-Komponente** (Vorschaubild in der Block-Auswahl).

```js
Shopware.Component.register('sw-cms-block-ff-image-text', { template });
Shopware.Component.register('sw-cms-preview-ff-image-text', { template: previewTemplate });
```
```twig
{# sw-cms-block-ff-image-text.html.twig #}
{% block sw_cms_block_ff_image_text %}
<div class="sw-cms-block-ff-image-text">
    <slot name="left"></slot>
    <slot name="right"></slot>
</div>
{% endblock %}
```

Die `<slot name="...">` entsprechen den `slots` aus `registerCmsBlock` (`sw-cms-block`). Verzeichnis:
`.../module/sw-cms/blocks/<category>/ff-image-text/`. Elemente, die in den Slots erscheinen: `sw-cms-element-admin`.
