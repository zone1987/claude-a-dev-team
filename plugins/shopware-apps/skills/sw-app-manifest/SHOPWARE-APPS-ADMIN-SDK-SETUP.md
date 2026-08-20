---
title: Meteor Admin SDK Setup
impact: MEDIUM
impactDescription: The Meteor Admin SDK is required for extending the Shopware Administration
tags: admin, sdk, meteor, setup, iframe, administration
---

## Meteor Admin SDK Setup

The Meteor Admin SDK is an NPM library for building admin extensions. It works via iframes and provides a standardized API.

### Key Features

- TypeScript support with autocompletion
- Tree-shakable, zero dependencies
- Works identically for apps and plugins
- Strong backwards compatibility

### Installation

```bash
npm install @shopware-ag/meteor-admin-sdk
```

### Loading State (Critical)

Every admin module iframe must signal readiness:

```javascript
function sendReadyState() {
    window.parent.postMessage('sw-app-loaded', '*');
}
```

If not sent within **5 seconds**, the loading state aborts.

### Base App URL

Set a base URL in manifest.xml for SDK communication:

```xml
<admin>
    <base-app-url>https://my-app.com</base-app-url>
</admin>
```

### Important Constraints

- The Shopware Administration **cannot** be extended by freely overriding components
- JavaScript in `Resources/administration` is **ignored** for apps
- All extensions must use documented extension points (Meteor SDK, manifest XML)
