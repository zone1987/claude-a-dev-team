# Custom Entities (XML-Based)

## Overview

Custom entities are defined in XML and automatically get admin UI, API endpoints, and DAL integration. They are simpler than class-based entity definitions but less flexible.

## Entity Definition XML

Place at: `src/Resources/entities.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<entities xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/System/CustomEntity/Xml/entity-1.0.xsd">

    <entity name="ff_content_plus_faq">
        <fields>
            <string name="question" required="true" translatable="true" store-api-aware="true"/>
            <text name="answer" required="true" translatable="true" allow-html="true" store-api-aware="true"/>
            <int name="position" store-api-aware="true"/>
            <bool name="active" store-api-aware="true"/>
            <many-to-one name="media" reference="media" store-api-aware="true"/>
        </fields>
    </entity>
</entities>
```

## Available Field Types

| Type | XML Element | Description |
|------|------------|-------------|
| String | `<string>` | VARCHAR(255) |
| Text | `<text>` | LONGTEXT |
| Int | `<int>` | INT |
| Float | `<float>` | DOUBLE |
| Bool | `<bool>` | TINYINT(1) |
| Date | `<date>` | DATE |
| Email | `<email>` | VARCHAR(255) with validation |
| Price | `<price>` | Price JSON |
| JSON | `<json>` | JSON |

## Field Attributes

| Attribute | Description |
|-----------|-------------|
| `name` | Field name (required) |
| `required` | Field is required |
| `translatable` | Field is translatable |
| `store-api-aware` | Available in Store API |
| `allow-html` | Allow HTML (text fields) |

## Association Types

```xml
<!-- Many-to-One -->
<many-to-one name="category" reference="category" store-api-aware="true"/>

<!-- One-to-Many -->
<one-to-many name="items" reference="ff_content_plus_faq_item" store-api-aware="true"/>

<!-- Many-to-Many -->
<many-to-many name="products" reference="product" store-api-aware="true"/>
```

## Admin UI Config

Add `admin-ui` section for automatic admin listing:

```xml
<entity name="ff_content_plus_faq">
    <fields>
        <string name="question" required="true" translatable="true" store-api-aware="true"/>
        <text name="answer" required="true" translatable="true" allow-html="true" store-api-aware="true"/>
        <bool name="active" store-api-aware="true"/>
    </fields>

    <admin-ui>
        <listing-columns>
            <column ref="question"/>
            <column ref="active"/>
        </listing-columns>
        <detail>
            <tab name="main">
                <card name="general">
                    <field ref="question"/>
                    <field ref="answer"/>
                    <field ref="active"/>
                </card>
            </tab>
        </detail>
    </admin-ui>
</entity>
```

## API Access

Custom entities are automatically accessible via Admin API:

```
GET  /api/ff-content-plus-faq
POST /api/ff-content-plus-faq
GET  /api/ff-content-plus-faq/{id}
PATCH /api/ff-content-plus-faq/{id}
DELETE /api/ff-content-plus-faq/{id}
```

With `store-api-aware`, also via Store API:
```
GET /store-api/ff-content-plus-faq
```
