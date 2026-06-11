---
title: Cookie Consent in Apps
impact: MEDIUM
impactDescription: Apps must register cookies for GDPR compliance via manifest.xml
tags: storefront, cookies, consent, gdpr, manifest
---

## Cookie Consent in Apps

Register cookies in manifest.xml for Shopware's built-in cookie consent system.

### Single Cookie

```xml
<cookies>
    <cookie>
        <cookie>my-cookie-name</cookie>
        <snippet-name>my-app.cookie.name</snippet-name>
        <snippet-description>my-app.cookie.description</snippet-description>
        <value>1</value>
        <expiration>30</expiration>
    </cookie>
</cookies>
```

### Cookie Elements

| Element | Required | Description |
|---------|----------|-------------|
| `<cookie>` | Yes | Technical cookie name |
| `<snippet-name>` | Yes | Translation key for display name |
| `<snippet-description>` | No | Translation key for description |
| `<value>` | No | Fixed value; omit for event-triggered cookies |
| `<expiration>` | No | Lifetime in days; omit for session cookies |

### Custom Cookie Group

```xml
<cookies>
    <group>
        <snippet-name>my-app.cookie-group.name</snippet-name>
        <snippet-description>my-app.cookie-group.description</snippet-description>
        <entries>
            <cookie>
                <cookie>tracking-cookie</cookie>
                <snippet-name>my-app.cookie.tracking</snippet-name>
                <value>1</value>
                <expiration>90</expiration>
            </cookie>
        </entries>
    </group>
</cookies>
```

### Using Built-in Groups

Standard groups: `cookie.groupRequired`, `cookie.groupComfortFeatures`, `cookie.groupStatistical`, `cookie.groupMarketing`

```xml
<cookies>
    <group>
        <snippet-name>cookie.groupMarketing</snippet-name>
        <entries>
            <cookie>
                <cookie>my-marketing-cookie</cookie>
                <snippet-name>my-app.cookie.marketing</snippet-name>
                <value>1</value>
                <expiration>365</expiration>
            </cookie>
        </entries>
    </group>
</cookies>
```
