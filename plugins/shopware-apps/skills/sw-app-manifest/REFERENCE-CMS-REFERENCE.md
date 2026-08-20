# Shopware 6 — App CMS blocks XML reference (cms.xml)

> Source: `resources/references/app-reference/cms-reference.md`
> XSD-Schema: `https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Cms/Schema/cms-1.0.xsd`

---

## Contents

- [Basic structure](#basic-structure)
- [`<block>` elements](#block-elements)
- [`<slots>` and `<slot>`](#slots-and-slot)
- [`<default-config>`](#default-config)
- [Available CMS element types (slot `type`)](#available-cms-element-types-slot-type)
- [Complete example](#complete-example)

## Basic structure

```xml
// Resources/cms.xml
<?xml version="1.0" encoding="utf-8" ?>
<cms xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Cms/Schema/cms-1.0.xsd">
    <blocks>
        <block>
            <!-- ... -->
        </block>
    </blocks>
</cms>
```

---

## `<block>` elements

| Element | Required | Description |
|:--------|:--------|:-------------|
| `<name>` | yes | Unique technical name (recommended: company abbreviation as a prefix, e.g. `swag-my-block`) |
| `<category>` | yes | Category assignment (values from the XSD) |
| `<label>` | yes | Display name in the Administration (translatable with `lang="de-DE"`) |
| `<slots>` | yes | Slot definitions of the block |
| `<default-config>` | no | Default configuration when the block is added |

---

## `<slots>` and `<slot>`

Every slot needs a unique `name` and a `type` that references a CMS element.

```xml
<slots>
    <slot name="left" type="manufacturer-logo">
        <config>
            <config-value name="display-mode" source="static" value="cover"/>
        </config>
    </slot>
    <slot name="middle" type="image-gallery">
        <config>
            <config-value name="display-mode" source="static" value="auto"/>
            <config-value name="min-height" source="static" value="300px"/>
        </config>
    </slot>
    <slot name="right" type="buy-box">
        <config>
            <config-value name="display-mode" source="static" value="contain"/>
        </config>
    </slot>
</slots>
```

### `<config-value>` attributes

| Attribute | Description |
|:---------|:-------------|
| `name` | Configuration key |
| `source` | Source type (e.g. `static`) |
| `value` | Value |

Interpreted in JavaScript as: `{ displayMode: { source: "static", value: "cover" } }`

---

## `<default-config>`

Default layout configuration of the block:

```xml
<default-config>
    <margin-bottom>20px</margin-bottom>
    <margin-top>20px</margin-top>
    <margin-left>20px</margin-left>
    <margin-right>20px</margin-right>
    <!-- Allowed values: "boxed" or "full_width" -->
    <sizing-mode>boxed</sizing-mode>
    <background-color>#000</background-color>
</default-config>
```

---

## Available CMS element types (slot `type`)

Currently only the CMS elements provided by Shopware can be used:

| Type | Description |
|:----|:-------------|
| `manufacturer-logo` | Manufacturer logo |
| `image-gallery` | Image gallery |
| `buy-box` | Buy box |
| `form` | Form |
| `image` | Single image |
| `youtube-video` | YouTube video |
| `text` | Text element |
| `product-listing` | Product listing |
| `product-box` | Product box |
| `cross-selling` | Cross-selling |
| `category-navigation` | Category navigation |

---

## Complete example

```xml
<?xml version="1.0" encoding="utf-8" ?>
<cms xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Cms/Schema/cms-1.0.xsd">
    <blocks>
        <block>
            <name>my-first-block</name>
            <category>text-image</category>
            <label>First block from app</label>
            <label lang="de-DE">Erster Block einer App</label>
            <slots>
                <slot name="left" type="manufacturer-logo">
                    <config>
                        <config-value name="display-mode" source="static" value="cover"/>
                    </config>
                </slot>
                <slot name="middle" type="image-gallery">
                    <config>
                        <config-value name="display-mode" source="static" value="auto"/>
                        <config-value name="min-height" source="static" value="300px"/>
                    </config>
                </slot>
                <slot name="right" type="buy-box">
                    <config>
                        <config-value name="display-mode" source="static" value="contain"/>
                    </config>
                </slot>
            </slots>
            <default-config>
                <margin-bottom>20px</margin-bottom>
                <margin-top>20px</margin-top>
                <margin-left>20px</margin-left>
                <margin-right>20px</margin-right>
                <sizing-mode>boxed</sizing-mode>
                <background-color>#000</background-color>
            </default-config>
        </block>
    </blocks>
</cms>
```
