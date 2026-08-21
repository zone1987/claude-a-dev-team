# Shopware 6 — App custom entities XML reference (entities.xml)

> Source: `resources/references/app-reference/entities-reference.md`
> XSD-Schema: `https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/System/CustomEntity/Xml/entity-1.0.xsd`

---

## Contents

- [Basic structure](#basic-structure)
- [Scalar field types](#scalar-field-types)
- [Special field types](#special-field-types)
- [Field attributes](#field-attributes)
- [Relation types](#relation-types)
- [`on-delete` options](#on-delete-options)
- [Complete example](#complete-example)

## Basic structure

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

Since Shopware v6.5.15.0 the `ce_` prefix can be used as a short form:
```xml
<entity name="ce_blog_comment">
```

---

## Scalar field types

| Field type | Example | Description |
|:--------|:---------|:-------------|
| `int` | `<int name="position" store-api-aware="true" />` | Integer |
| `float` | `<float name="rating" store-api-aware="true" />` | Decimal number |
| `string` | `<string name="title" required="true" translatable="true" store-api-aware="true" />` | String |
| `text` | `<text name="content" allow-html="true" translatable="true" store-api-aware="true" />` | Long text |
| `bool` | `<bool name="display" translatable="true" store-api-aware="true" />` | Boolean |
| `date` | `<date name="my_date" store-api-aware="false" />` | Date |

---

## Special field types

| Field type | Example | Description |
|:--------|:---------|:-------------|
| `json` | `<json name="payload" store-api-aware="false" />` | JSON object |
| `email` | `<email name="email" store-api-aware="false" />` | Email address |
| `price` | `<price name="price" store-api-aware="false" />` | Price field |

---

## Field attributes

| Attribute | Values | Description |
|:---------|:------|:-------------|
| `name` | string | Technical field name (required) |
| `required` | `true`/`false` | Mandatory field |
| `translatable` | `true`/`false` | Translatable (creates a translations table) |
| `store-api-aware` | `true`/`false` | Available in the Store API |
| `allow-html` | `true`/`false` | Allow HTML (only `text`) |
| `default` | value | Default value (scalar types only) |
| `inherited` | `true`/`false` | Inheritance for product relations |

---

## Relation types

### many-to-many

```xml
<many-to-many name="products" reference="product" store-api-aware="true" />
<!-- Inherited many-to-many: -->
<many-to-many name="inherited_products" reference="product" store-api-aware="true" inherited="true"/>
```

### one-to-many

```xml
<!-- With cascade delete on your own custom entities: -->
<one-to-many name="comments" reference="ce_blog_comment" store-api-aware="true"
             on-delete="cascade" reverse-required="true" />

<!-- Restrict: prevents deletion while linked -->
<one-to-many name="links_restrict" reference="category" store-api-aware="true" on-delete="restrict" />

<!-- Set null on deletion: -->
<one-to-many name="links_set_null" reference="category" store-api-aware="true" on-delete="set-null" />
```

### many-to-one

```xml
<!-- Restrict: product deletion prevented when set as top_seller_restrict -->
<many-to-one name="top_seller_restrict" reference="product" store-api-aware="true"
             required="false" on-delete="restrict" />

<!-- Cascade: deletes custom_entity_blog when the product is deleted -->
<many-to-one name="top_seller_cascade" reference="product" store-api-aware="true"
             required="true" on-delete="cascade" />

<!-- Set null: sets the column to null on product deletion -->
<many-to-one name="top_seller_set_null" reference="product" store-api-aware="true"
             on-delete="set-null" />
```

### one-to-one

```xml
<one-to-one name="link_product_restrict" reference="product" store-api-aware="false" on-delete="restrict" />
<one-to-one name="link_product_cascade" reference="product" store-api-aware="false" on-delete="cascade" />
<one-to-one name="link_product_set_null" reference="product" store-api-aware="false" on-delete="set-null" />
<!-- Inherited one-to-one: -->
<one-to-one name="inherited_link_product" reference="product" store-api-aware="true"
            inherited="true" on-delete="set-null" />
```

---

## `on-delete` options

| Value | Description |
|:-----|:-------------|
| `cascade` | Deletes dependent records along with it |
| `restrict` | Prevents deletion while the record is linked |
| `set-null` | Sets the FK column to NULL on deletion |

---

## Complete example

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
