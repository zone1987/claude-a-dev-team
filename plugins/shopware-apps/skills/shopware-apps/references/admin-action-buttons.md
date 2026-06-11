---
title: Admin Action Buttons
impact: MEDIUM
impactDescription: Action buttons add interactive elements to admin detail and list views
tags: admin, action-buttons, manifest, webhook
---

## Admin Action Buttons

Action buttons appear in the admin smartbar on detail or list views and trigger webhooks to your app server.

### Manifest Configuration

```xml
<admin>
    <action-button action="restockProduct" entity="product" view="list"
                   url="https://my-app.com/action/restock">
        <label>Restock Products</label>
        <label lang="de-DE">Produkte nachbestellen</label>
    </action-button>
</admin>
```

### Required Attributes

| Attribute | Values | Description |
|-----------|--------|-------------|
| `action` | string | Unique action identifier |
| `entity` | product, order, category, promotion, customer, cms_page | Target entity |
| `view` | detail, list | Where the button appears |
| `url` | URL or relative path | Endpoint receiving the request |

### Response Types (since 6.4.3.0)

**Notification:**
```json
{ "actionType": "notification", "payload": { "status": "success", "message": "Done!" } }
```
Status values: `success`, `error`, `info`, `warning`

**Open new tab:**
```json
{ "actionType": "openNewTab", "payload": { "redirectUrl": "https://example.com" } }
```

**Reload page:**
```json
{ "actionType": "reload", "payload": {} }
```

**Open modal:**
```json
{ "actionType": "openModal", "payload": { "iframeUrl": "https://example.com/modal", "size": "medium", "expand": false } }
```
Size values: `small`, `medium`, `large`, `fullscreen`

### Using App Script Endpoints (since 6.4.10.0)

Use a relative URL to handle via app scripts instead of an external server:

```xml
<action-button action="test" entity="product" view="list" url="/api/script/action-button">
    <label>Test Action</label>
</action-button>
```

### Security

Requests include `shopware-shop-signature` header (HMAC-SHA256). Responses **must** include `shopware-app-signature` header.
