---
title: Admin CMS Elements via SDK
impact: MEDIUM
impactDescription: Custom CMS elements are created using the Meteor Admin SDK with Vue.js iframes
tags: admin, cms, elements, meteor-sdk, vue
---

## Admin CMS Elements via SDK

Custom CMS elements use the Meteor Admin SDK loaded in iframes with Vue.js components.

### File Structure

```
Resources/app/administration/src/
├── base/mainCommands.ts      (element registration)
├── main.ts                   (entry point)
├── viewRenderer.ts           (view loading)
└── views/my-element/
    ├── my-element-config.ts  (configuration panel)
    ├── my-element-element.ts (storefront display)
    └── my-element-preview.ts (admin preview)
```

### Three Required Components

1. **Config** -- Configuration interface for shop managers
2. **Element** -- Rendered component displayed in storefront
3. **Preview** -- Preview shown in CMS element browser

### Registration

Elements are registered via the Meteor Admin SDK's CMS module with a vendor-prefix naming convention (e.g., `swag-dailymotion`). The registration generates location IDs with suffixes: `-element`, `-config`, `-preview`.

### Communication

Components communicate with the Administration through the SDK's data-binding system for real-time config synchronization between iframe and admin.

### Prerequisites

- Meteor Admin SDK concepts
- Understanding of the location system
- TypeScript recommended
