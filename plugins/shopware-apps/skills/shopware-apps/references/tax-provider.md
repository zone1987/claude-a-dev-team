---
title: Tax Provider
impact: LOW-MEDIUM
impactDescription: Apps can provide custom tax calculations for complex tax scenarios
tags: tax, provider, calculation, checkout
---

## Tax Provider

Since Shopware 6.5.0.0, apps can provide custom tax calculations — essential for regions with complex tax rules (e.g., US state/locality rates).

### Manifest Configuration

```xml
<tax>
    <tax-provider>
        <identifier>myTaxProvider</identifier>
        <name>My Tax Provider</name>
        <priority>1</priority>
        <process-url>https://tax.app/calculate</process-url>
    </tax-provider>
</tax>
```

### Elements

| Element | Purpose |
|---------|---------|
| `identifier` | Unique ID (immutable after creation) |
| `name` | Display name in administration |
| `priority` | Execution order (adjustable in admin) |
| `process-url` | Endpoint called during checkout |

### Execution Flow

During checkout, Shopware queries active tax providers sorted by priority, calling them sequentially until one responds successfully.

### Response Capabilities

The response can adjust taxes at three levels:
- **Entire cart** via `cartPriceTaxes`
- **Entire delivery**
- **Individual line items**

When `cartPriceTaxes` is provided, Shopware uses those values directly instead of recalculating.

### Important Notes

- **5-second timeout** on responses
- Activates automatically upon app installation (visible under Settings > Tax)
- All requests/responses are signed
- The `identifier` cannot be changed after creation
