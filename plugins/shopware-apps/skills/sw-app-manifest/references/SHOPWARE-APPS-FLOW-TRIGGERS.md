---
title: Flow Triggers
impact: LOW-MEDIUM
impactDescription: Custom flow triggers dispatch events into the Flow Builder
tags: flow, triggers, events, flow-xml, custom-events
---

## Flow Triggers

Custom flow triggers allow apps to dispatch events into the Flow Builder. Available since Shopware 6.5.3.0.

### flow.xml Definition

```xml
<flow-extensions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Flow/Schema/flow-1.0.xsd">
    <flow-events>
        <flow-event>
            <name>swag.before.open_the_doors</name>
            <aware>orderAware</aware>
            <aware>customerAware</aware>
        </flow-event>
    </flow-events>
</flow-extensions>
```

### Dispatching via API

```
POST /api/_action/trigger-event/swag.before.open_the_doors
Content-Type: application/json

{
    "customerId": "uuid-of-customer",
    "salesChannelId": "uuid-of-sales-channel",
    "shopName": "My Shop",
    "url": "https://myshop.com"
}
```

### Awareness Types

`orderAware`, `customerAware`, `customerGroupAware`, `mailAware`, `salesChannelAware`, `userAware`, `delayAware`

### Important Notes

- Event names must be globally unique (pattern: `[a-z][a-z._]*[a-z]`)
- Data passed to the API becomes available as template variables in flow actions
- `aware` determines which flow actions become available for this trigger
