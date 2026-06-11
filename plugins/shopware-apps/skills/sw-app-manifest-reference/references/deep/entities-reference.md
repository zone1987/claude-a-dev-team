# Shopware 6 — App Custom Entities XML-Referenz (entities.xml)

> Quelle: `resources/references/app-reference/entities-reference.md`
> XSD-Schema: `https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/System/CustomEntity/Xml/entity-1.0.xsd`

---

## Grundstruktur

```xml
// Resources/entities.xml
<?xml version="1.0" encoding="utf-8" ?>
<entities xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/System/CustomEntity/Xml/entity-1.0.xsd">
    <entity name="custom_entity_blog">
        <fields>
            <!-- ... -->
        </fields>
    </entity>
</entities>
```

Seit Shopware v6.5.15.0 kann das `ce_`-Präfix als Kurzform verwendet werden:
```xml
<entity name="ce_blog_comment">
```

---

## Skalare Feldtypen

| Feldtyp | Beispiel | Beschreibung |
|:--------|:---------|:-------------|
| `int` | `<int name="position" store-api-aware="true" />` | Ganzzahl |
| `float` | `<float name="rating" store-api-aware="true" />` | Dezimalzahl |
| `string` | `<string name="title" required="true" translatable="true" store-api-aware="true" />` | Zeichenkette |
| `text` | `<text name="content" allow-html="true" translatable="true" store-api-aware="true" />` | Langer Text |
| `bool` | `<bool name="display" translatable="true" store-api-aware="true" />` | Boolean |
| `date` | `<date name="my_date" store-api-aware="false" />` | Datum |

---

## Spezielle Feldtypen

| Feldtyp | Beispiel | Beschreibung |
|:--------|:---------|:-------------|
| `json` | `<json name="payload" store-api-aware="false" />` | JSON-Objekt |
| `email` | `<email name="email" store-api-aware="false" />` | E-Mail-Adresse |
| `price` | `<price name="price" store-api-aware="false" />` | Preis-Feld |

---

## Feld-Attribute

| Attribut | Werte | Beschreibung |
|:---------|:------|:-------------|
| `name` | string | Technischer Feldname (Pflicht) |
| `required` | `true`/`false` | Pflichtfeld |
| `translatable` | `true`/`false` | Übersetzbar (erzeugt translations-Tabelle) |
| `store-api-aware` | `true`/`false` | Im Store-API verfügbar |
| `allow-html` | `true`/`false` | HTML erlauben (nur `text`) |
| `default` | value | Standardwert (nur skalare Typen) |
| `inherited` | `true`/`false` | Vererbung für Produkt-Relationen |

---

## Relationstypen

### many-to-many

```xml
<many-to-many name="products" reference="product" store-api-aware="true" />
<!-- Vererbte many-to-many: -->
<many-to-many name="inherited_products" reference="product" store-api-aware="true" inherited="true"/>
```

### one-to-many

```xml
<!-- Mit cascade delete auf eigene Custom Entities: -->
<one-to-many name="comments" reference="ce_blog_comment" store-api-aware="true"
             on-delete="cascade" reverse-required="true" />

<!-- Restrict: verhindert Löschen wenn verknüpft -->
<one-to-many name="links_restrict" reference="category" store-api-aware="true" on-delete="restrict" />

<!-- Set null bei Löschen: -->
<one-to-many name="links_set_null" reference="category" store-api-aware="true" on-delete="set-null" />
```

### many-to-one

```xml
<!-- Restrict: Produktlöschung verhindert wenn als top_seller_restrict gesetzt -->
<many-to-one name="top_seller_restrict" reference="product" store-api-aware="true"
             required="false" on-delete="restrict" />

<!-- Cascade: Löscht custom_entity_blog wenn Produkt gelöscht -->
<many-to-one name="top_seller_cascade" reference="product" store-api-aware="true"
             required="true" on-delete="cascade" />

<!-- Set null: Setzt Spalte auf null bei Produktlöschung -->
<many-to-one name="top_seller_set_null" reference="product" store-api-aware="true"
             on-delete="set-null" />
```

### one-to-one

```xml
<one-to-one name="link_product_restrict" reference="product" store-api-aware="false" on-delete="restrict" />
<one-to-one name="link_product_cascade" reference="product" store-api-aware="false" on-delete="cascade" />
<one-to-one name="link_product_set_null" reference="product" store-api-aware="false" on-delete="set-null" />
<!-- Vererbte one-to-one: -->
<one-to-one name="inherited_link_product" reference="product" store-api-aware="true"
            inherited="true" on-delete="set-null" />
```

---

## `on-delete`-Optionen

| Wert | Beschreibung |
|:-----|:-------------|
| `cascade` | Löscht abhängige Datensätze mit |
| `restrict` | Verhindert Löschen solange Datensatz verknüpft ist |
| `set-null` | Setzt FK-Spalte auf NULL beim Löschen |

---

## Vollständiges Beispiel

```xml
<?xml version="1.0" encoding="utf-8" ?>
<entities xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/System/CustomEntity/Xml/entity-1.0.xsd">
    <entity name="custom_entity_blog">
        <fields>
            <int name="position" store-api-aware="true" />
            <float name="rating" store-api-aware="true" />
            <string name="title" required="true" translatable="true" store-api-aware="true" />
            <text name="content" allow-html="true" translatable="true" store-api-aware="true" />
            <bool name="display" translatable="true" store-api-aware="true" />
            <date name="my_date" store-api-aware="false" />
            <json name="payload" store-api-aware="false" />
            <email name="email" store-api-aware="false" />
            <price name="price" store-api-aware="false" />
            <bool name="in_stock" store-api-aware="true" default="true" />
            <text name="internal_comment" store-api-aware="false" />
            <many-to-many name="products" reference="product" store-api-aware="true" />
            <one-to-many name="comments" reference="ce_blog_comment" store-api-aware="true"
                         on-delete="cascade" reverse-required="true" />
            <many-to-one name="top_seller_restrict" reference="product" store-api-aware="true"
                         required="false" on-delete="restrict" />
        </fields>
    </entity>

    <entity name="ce_blog_comment">
        <fields>
            <string name="title" required="true" translatable="true" store-api-aware="true" />
            <text name="content" allow-html="true" translatable="true" store-api-aware="true" />
            <email name="email" store-api-aware="false" />
            <many-to-one name="recommendation" reference="product" store-api-aware="true"
                         required="false" on-delete="set-null" />
        </fields>
    </entity>
</entities>
```
