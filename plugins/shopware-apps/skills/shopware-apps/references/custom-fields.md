---
title: Custom Fields
impact: MEDIUM
impactDescription: Custom fields extend existing entities with additional data
tags: custom-fields, entities, manifest, field-types
---

## Custom Fields

Custom fields add additional data to existing Shopware entities (products, orders, customers, etc.). They are organized into custom field sets defined in manifest.xml.

### Manifest Definition

```xml
<custom-fields>
    <custom-field-set>
        <name>swag_example_set</name>
        <label>Example Set</label>
        <label lang="de-DE">Beispiel-Set</label>
        <related-entities>
            <product/>
            <order/>
        </related-entities>
        <fields>
            <text name="swag_example_text">
                <label>Text field</label>
                <position>1</position>
                <required>true</required>
            </text>
            <int name="swag_example_count">
                <label>Count</label>
                <position>2</position>
                <min>0</min>
                <max>100</max>
                <steps>1</steps>
            </int>
            <float name="swag_example_price">
                <label>Price modifier</label>
                <position>3</position>
                <min>0.0</min>
                <max>999.99</max>
                <steps>0.01</steps>
            </float>
            <bool name="swag_example_active">
                <label>Active</label>
                <position>4</position>
            </bool>
            <datetime name="swag_example_date">
                <label>Valid until</label>
                <position>5</position>
            </datetime>
            <single-select name="swag_example_type">
                <label>Type</label>
                <position>6</position>
                <options>
                    <option value="standard">
                        <name>Standard</name>
                    </option>
                    <option value="premium">
                        <name>Premium</name>
                    </option>
                </options>
            </single-select>
            <single-entity-select name="swag_example_product">
                <label>Related Product</label>
                <position>7</position>
                <entity>product</entity>
                <label-property>name</label-property>
            </single-entity-select>
            <media-selection name="swag_example_image">
                <label>Image</label>
                <position>8</position>
            </media-selection>
            <color-picker name="swag_example_color">
                <label>Color</label>
                <position>9</position>
            </color-picker>
        </fields>
    </custom-field-set>
</custom-fields>
```

### Available Field Types

`int`, `float`, `text`, `text-area`, `bool`, `datetime`, `single-select`, `multi-select`, `single-entity-select`, `multi-entity-select`, `color-picker`, `media-selection`, `price`

### Common Properties

All fields support: `label`, `help-text`, `required`, `position`, `allow-customer-write`, `allow-cart-expose`

### Available Related Entities

`product`, `order`, `category`, `customer`, `customer_address`, `media`, `product_manufacturer`, `sales_channel`, `landing_page`, `promotion`, etc.

**Important:** Field names must use a vendor prefix (e.g., `swag_`) to ensure global uniqueness.
