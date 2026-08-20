---
title: Admin Custom Modules
impact: MEDIUM
impactDescription: Custom modules embed external web pages as iframes in the admin navigation
tags: admin, modules, iframe, navigation, manifest
---

## Admin Custom Modules

Custom modules load external web pages as iframes within the Shopware Administration.

### Manifest Configuration

```xml
<admin>
    <module name="myModule" parent="sw-marketing" position="50"
            source="https://my-app.com/admin/module">
        <label>My Module</label>
        <label lang="de-DE">Mein Modul</label>
    </module>
</admin>
```

### Module Attributes

| Attribute | Required | Description |
|-----------|----------|-------------|
| `name` | Yes | Technical identifier |
| `parent` | Yes | Parent navigation ID (e.g., sw-marketing, sw-catalogue, sw-order) |
| `source` | No | URL serving module content |
| `position` | No | Menu item ordering (default: 0) |

### Nested Modules (Hierarchy)

Reference other app modules as parents using `app-{appName}-{moduleName}`:

```xml
<admin>
    <module name="parentModule" parent="sw-marketing">
        <label>Parent</label>
    </module>
    <module name="childModule" parent="app-MyApp-parentModule"
            source="https://my-app.com/child">
        <label>Child Module</label>
    </module>
</admin>
```

### Authentication Parameters

Shopware sends these query parameters when loading the iframe:
- `shop-id` -- Shop identifier
- `shop-url` -- Shop URL for API calls
- `timestamp` -- Unix timestamp
- `shopware-shop-signature` -- HMAC signature for verification

### Main Module (App Store Link)

```xml
<admin>
    <main-module source="https://my-app.com/main"/>
</admin>
```

### Loading State

**Every module must signal readiness within 5 seconds:**

```javascript
window.parent.postMessage('sw-app-loaded', '*');
```
