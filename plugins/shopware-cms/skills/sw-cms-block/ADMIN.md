# Shopware 6 — CMS block (admin)

Every block needs two admin components: the **block component** (renders the slots in the editor) and the
**preview component** (the preview image in the block picker).

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

The `<slot name="...">` entries correspond to the `slots` from `registerCmsBlock` (`sw-cms-block`). Directory:
`.../module/sw-cms/blocks/<category>/ff-image-text/`. Elements that appear in the slots: `sw-cms-element-admin`.
