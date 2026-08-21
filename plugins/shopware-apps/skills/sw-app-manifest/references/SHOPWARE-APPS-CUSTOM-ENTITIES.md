---
title: Custom Entities
impact: MEDIUM
impactDescription: Custom entities create new data structures stored in the database
tags: custom-entities, entities-xml, fields, relations, store-api
---

## Custom Entities

Custom entities create entirely new database tables and are defined in `Resources/entities.xml`.

### Basic Definition

```xml
<?xml version="1.0" encoding="utf-8" ?>
<entities xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/System/CustomEntity/Xml/entity-1.0.xsd">
    <entity name="ce_my_entity" custom-fields-aware="true" label-property="name">
        <fields>
            <string name="name" required="true" translatable="true" store-api-aware="true" />
            <text name="description" translatable="true" store-api-aware="true" allow-html="true" />
            <int name="position" store-api-aware="true" />
            <float name="rating" store-api-aware="true" />
            <bool name="active" store-api-aware="true" default="true" />
            <email name="contact" store-api-aware="true" />
            <price name="price" required="true" store-api-aware="true" />
            <json name="metadata" store-api-aware="true" />
            <date name="publishDate" store-api-aware="true" />
            <many-to-one name="category" reference="category" store-api-aware="true" on-delete="set-null" />
            <many-to-many name="products" reference="product" store-api-aware="true" />
        </fields>
    </entity>
</entities>
```

### Field Types

`string`, `text`, `int`, `float`, `bool`, `json`, `date`, `email`, `price`

### Relation Types

| Relation | Description | Attributes |
|----------|-------------|------------|
| `one-to-one` | Single entity link | `reference`, `on-delete` |
| `one-to-many` | Parent to children | `reference`, `on-delete` |
| `many-to-one` | Child to parent | `reference`, `on-delete` |
| `many-to-many` | Bidirectional | `reference` |

### Key Attributes

| Attribute | Purpose |
|-----------|---------|
| `required="true"` | Mandatory field |
| `translatable="true"` | Multi-language support |
| `store-api-aware="true"` | Accessible via Store API |
| `allow-html="true"` | Allow HTML in text fields |
| `default="value"` | Default value |
| `on-delete="set-null\|cascade\|restrict"` | Referential integrity |

### Entity Attributes

| Attribute | Purpose |
|-----------|---------|
| `custom-fields-aware="true"` | Enables custom fields on entity (since 6.5.1.0) |
| `label-property="name"` | Field used as display label |

### Naming Conventions

- Standard prefix: `custom_entity_` (e.g., `custom_entity_blog`)
- Short prefix: `ce_` (since 6.4.15.0, e.g., `ce_blog`)
- Cannot rename entities after creation (causes data loss)

### API Access

```
POST /api/search/ce_my_entity
GET /api/ce_my_entity/{id}
```

### App Script Access

```twig
{% set entities = services.repository.search('ce_my_entity', criteria) %}
```

### Permissions

Apps automatically have full CRUD access to their own custom entities. Associations to core entities require explicit `<permissions>` in manifest.xml.
