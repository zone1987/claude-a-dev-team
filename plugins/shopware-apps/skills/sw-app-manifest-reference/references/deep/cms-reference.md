# Shopware 6 — App CMS-Blocks XML-Referenz (cms.xml)

> Quelle: `resources/references/app-reference/cms-reference.md`
> XSD-Schema: `https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Cms/Schema/cms-1.0.xsd`

---

## Grundstruktur

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

## `<block>`-Elemente

| Element | Pflicht | Beschreibung |
|:--------|:--------|:-------------|
| `<name>` | ja | Eindeutiger technischer Name (empfohlen: Firmen-Kürzel als Präfix, z.B. `swag-my-block`) |
| `<category>` | ja | Kategorie-Zuordnung (Werte aus XSD) |
| `<label>` | ja | Anzeigebezeichnung in der Administration (übersetzbar mit `lang="de-DE"`) |
| `<slots>` | ja | Slot-Definitionen des Blocks |
| `<default-config>` | nein | Standard-Konfiguration beim Hinzufügen des Blocks |

---

## `<slots>` und `<slot>`

Jeder Slot benötigt einen eindeutigen `name` und einen `type`, der auf ein CMS-Element verweist.

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

### `<config-value>`-Attribute

| Attribut | Beschreibung |
|:---------|:-------------|
| `name` | Konfigurationsschlüssel |
| `source` | Quelltyp (z.B. `static`) |
| `value` | Wert |

Wird in JavaScript interpretiert als: `{ displayMode: { source: "static", value: "cover" } }`

---

## `<default-config>`

Standard-Layout-Konfiguration des Blocks:

```xml
<default-config>
    <margin-bottom>20px</margin-bottom>
    <margin-top>20px</margin-top>
    <margin-left>20px</margin-left>
    <margin-right>20px</margin-right>
    <!-- Erlaubte Werte: "boxed" oder "full_width" -->
    <sizing-mode>boxed</sizing-mode>
    <background-color>#000</background-color>
</default-config>
```

---

## Verfügbare CMS-Element-Typen (Slot `type`)

Aktuell nur die von Shopware bereitgestellten CMS-Elemente nutzbar:

| Typ | Beschreibung |
|:----|:-------------|
| `manufacturer-logo` | Herstellerlogo |
| `image-gallery` | Bildergalerie |
| `buy-box` | Kauf-Box |
| `form` | Formular |
| `image` | Einzelbild |
| `youtube-video` | YouTube-Video |
| `text` | Text-Element |
| `product-listing` | Produktauflistung |
| `product-box` | Produktbox |
| `cross-selling` | Crossselling |
| `category-navigation` | Kategorienavigation |

---

## Vollständiges Beispiel

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
