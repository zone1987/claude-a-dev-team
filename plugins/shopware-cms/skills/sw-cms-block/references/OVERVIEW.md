# Shopware 6 — CMS blocks

A block is a reusable layout unit: it defines how elements are arranged in named **slots**. The block
supplies the structure, the elements supply the content — which is what lets one block display
different content in the same layout.

## Contents

- [The CMS hierarchy](#the-cms-hierarchy)
- [Where blocks live](#where-blocks-live)
- [Registering a block](#registering-a-block)
- [The block and preview components](#the-block-and-preview-components)
- [The storefront template](#the-storefront-template)
- [Rendering slots](#rendering-slots)

## The CMS hierarchy

| Level | What it is |
|---|---|
| Page | the top-level container — a category page, shop page or product page |
| Section | a horizontal segment of a page; single-column, or two-column with a sidebar |
| Block | a unit that usually spans a whole row, with its own layout and styling |
| Slot | a named container inside a block, holding exactly one element |
| Element | the content primitive itself: text, image, video, product listing |

Shopware's built-in `image-text` block, for instance, puts an image on the left and text on the
right.

## Where blocks live

In the administration: **Content → Shopping Experience**, then create or edit a layout. The designer
sidebar groups the available blocks by category, and blocks are dragged from there into a section:

| Category | What it holds |
|---|---|
| Text | text-only blocks |
| Images | image-only blocks |
| Text & Images | combined text and image blocks |
| Commerce | product sliders, listings and the like |
| Video | YouTube and Vimeo video blocks |
| Form | contact and newsletter forms |
| Sidebar | category navigation and listing filters |

The core code sits in three places:

| Layer | Path |
|---|---|
| Administration | `src/Administration/Resources/app/administration/src/module/sw-cms/blocks/` |
| Storefront | `src/Storefront/Resources/views/storefront/block/` |
| Core | `\Shopware\Core\Content\Cms\SalesChannel\SalesChannelCmsPageLoader::load` |

## Registering a block

The recommended structure inside a plugin:

```text
<plugin root>/src/Resources/app/administration/src/
├── main.js
└── module/
    └── sw-cms/
        └── blocks/
            └── text-image/                      (category)
                └── image-text-reversed/         (block name)
                    ├── index.js
                    ├── component/
                    │   ├── index.js
                    │   ├── cms-block-image-text-reversed.html.twig
                    │   └── cms-block-image-text-reversed.scss
                    └── preview/
                        ├── index.js
                        ├── cms-block-preview-image-text-reversed.html.twig
                        └── cms-block-preview-image-text-reversed.scss
```

Import it from `main.js`:

```js
// <plugin root>/src/Resources/app/administration/src/main.js
import './module/sw-cms/blocks/text-image/image-text-reversed';
```

Then register it:

```js
// .../blocks/text-image/image-text-reversed/index.js
import './component';
import './preview';

Shopware.Service('cmsService').registerCmsBlock({
    name: 'image-text-reversed',
    category: 'text-image',
    label: 'cms.blocks.imageTextReversed.label',
    component: 'cms-block-image-text-reversed',
    previewComponent: 'cms-block-preview-image-text-reversed',
    defaultConfig: {
        marginBottom: '20px',
        marginTop: '20px',
        marginLeft: '20px',
        marginRight: '20px',
        sizingMode: 'boxed',
    },
    slots: {
        left: 'text',
        right: 'image',
    },
});
```

| Property | Description |
|---|---|
| `name` | the technical name of the block |
| `category` | which category it appears under: `text`, `image`, `text-image`, `commerce`, `form`, `video`, `sidebar` |
| `label` | the display name in the UI |
| `component` | the Vue component rendering the block in the designer |
| `previewComponent` | the Vue component for the block's thumbnail preview |
| `defaultConfig` | default styling values |
| `slots` | which element type goes in which slot — the key is the slot name, the value the element type |

## The block and preview components

The **block component** must include every slot named in `slots`; those are what the administration
uses to configure the elements.

```js
// image-text-reversed/component/index.js
Shopware.Component.register('cms-block-image-text-reversed', {
    template: `...`,
});
```

The **preview component** is the thumbnail shown when picking a block from the sidebar. It may just
as well display a static image of the finished storefront block.

```js
// image-text-reversed/preview/index.js
Shopware.Component.register('cms-block-preview-image-text-reversed', {
    template: `...`,
    computed: {
        assetFilter() {
            return Shopware.Filter.getByName('asset');
        },
    },
});
```

After this the preview appears in the Shopping Experience sidebar, under the category given in
`category`.

## The storefront template

The template belongs in `src/Resources/views/storefront/block`, and its filename follows a
convention the loader depends on:

- prefix `cms-block-`
- the technical name from `name`, e.g. `image-text-reversed`
- extension `.html.twig`

Blocks are loaded by
`src/Storefront/Resources/views/storefront/section/cms-section-block-container.html.twig`, which
expects exactly that form: `cms-block-image-text-reversed.html.twig`.

```twig
{# <plugin root>/src/Resources/views/storefront/block/cms-block-image-text-reversed.html.twig #}
{% set element = block.slots.getSlot('left') %}
{% sw_include '@Storefront/storefront/element/cms-element-' ~ element.type ~ '.html.twig' with {
    'element': element
} %}

{% set element = block.slots.getSlot('right') %}
{% sw_include '@Storefront/storefront/element/cms-element-' ~ element.type ~ '.html.twig' with {
    'element': element
} %}
```

`block` is passed to the template automatically and carries the block's metadata and configuration
values; `CmsBlockDefinition.php` lists them in full. An existing block can be extended and reused
rather than written from scratch — clear the storefront cache after adding a template.

## Rendering slots

**Get a slot by name:**

```twig
{% set leftSlot = block.slots.getSlot('left') %}
```

**Render an element**, building the template path from the element's own type:

```twig
{% sw_include "@Storefront/storefront/element/cms-element-" ~ leftSlot.type ~ ".html.twig" with {
    'element': leftSlot
} %}
```

So a `leftSlot.type` of `text` renders `cms-element-text.html.twig`, and `image` renders
`cms-element-image.html.twig`.

**Loop through every slot:**

```twig
{% for slotName, slot in block.slots %}
    {% sw_include "@Storefront/storefront/element/cms-element-" ~ slot.type ~ ".html.twig" with {
        'element': slot
    } %}
{% endfor %}
```

## Related

For the elements that fill these slots, call the Skill tool with `sw-cms-element`.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/content/cms/add-cms-block.html](https://developer.shopware.com/docs/guides/plugins/plugins/content/cms/add-cms-block.html),
Shopware 6.7, retrieved 2026-08-21.
