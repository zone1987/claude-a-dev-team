---
title: Custom CMS Blocks
impact: MEDIUM
impactDescription: Custom CMS blocks define new block layouts for the Shopping Experiences editor
tags: custom, cms, blocks, cms-xml, storefront
---

## Custom CMS Blocks

Custom CMS blocks are defined in `Resources/cms.xml` and provide new block layouts for the Shopping Experiences (CMS) editor. Available since Shopware 6.4.4.0.

### Directory Structure

```
Resources/
├── cms.xml
├── cms/blocks/{block-name}/
│   ├── preview.html
│   └── styles.css
└── views/storefront/block/
    └── cms-block-{block-name}-component.html.twig
```

### cms.xml Configuration

```xml
<?xml version="1.0" encoding="utf-8" ?>
<cms xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Cms/Schema/cms-1.0.xsd">
    <blocks>
        <block>
            <name>my-image-text</name>
            <category>text-image</category>
            <label>Image with Text</label>
            <label lang="de-DE">Bild mit Text</label>
            <slots>
                <slot name="left" type="image">
                    <config>
                        <config-value name="display-mode" source="static" value="cover"/>
                    </config>
                </slot>
                <slot name="right" type="text">
                    <config>
                        <config-value name="vertical-align" source="static" value="center"/>
                    </config>
                </slot>
            </slots>
            <default-config>
                <margin-top>20px</margin-top>
                <margin-right>20px</margin-right>
                <margin-bottom>20px</margin-bottom>
                <margin-left>20px</margin-left>
                <sizing-mode>boxed</sizing-mode>
            </default-config>
        </block>
    </blocks>
</cms>
```

### Slot Types (Built-in CMS Elements)

`text`, `image`, `product-listing`, `product-slider`, `product-box`, `sidebar-filter`, `manufacturer-logo`, `buy-box`, `cross-selling`, `category-navigation`, etc.

### CSS Scoping

- `.sw-cms-preview-{block-name}` — Admin sidebar preview
- `.sw-cms-block-{block-name}-component` — CMS editor display
- `.sw-cms-slot-{slot-name}` — Individual slot styling

### Important Notes

- Only built-in CMS elements can be used in slots (no custom elements in slots yet)
- Preview HTML is sanitized — no scripts or suspicious attributes
- Cloud stores support app-based CMS blocks (not plugin-based)
