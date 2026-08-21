---
title: Shipping Methods
impact: LOW-MEDIUM
impactDescription: Apps can define shipping methods with delivery times via manifest
tags: shipping, methods, delivery-time, manifest
---

## Shipping Methods

Since Shopware 6.5.7.0 (experimental), apps can define shipping methods in manifest.xml.

### Manifest Configuration

```xml
<shipping-methods>
    <shipping-method>
        <identifier>myShipping</identifier>
        <name>Express Delivery</name>
        <name lang="de-DE">Expressversand</name>
        <description>Next-day delivery service</description>
        <icon>Resources/icons/express.png</icon>
        <active>true</active>
        <position>1</position>
        <tracking-url>https://tracking.example.com</tracking-url>
        <delivery-time>
            <id>a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4</id>
            <name>1-2 business days</name>
            <name lang="de-DE">1-2 Werktage</name>
            <min>1</min>
            <max>2</max>
            <unit>day</unit>
        </delivery-time>
    </shipping-method>
</shipping-methods>
```

### Delivery Time Units

`hour`, `day`, `week`, `month`, `year`

### Important Notes

- The `identifier` must remain unchanged — shipping methods not in manifest are deactivated/deleted on app update
- The `delivery-time` `id` should be a UUID (generated once, never changed)
- After installation, `description`, `icon`, and `active` can be overridden by merchants
- This feature is **experimental** and subject to change
