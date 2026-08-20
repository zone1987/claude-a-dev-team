# Shopware Nexus — full reference

> **Beta note:** Shopware Nexus is in its beta phase. Functionality
> is limited and may be extended in future updates.

## Contents

- [What is Shopware Nexus?](#what-is-shopware-nexus)
- [Key Capabilities](#key-capabilities)
- [Not available in beta](#not-available-in-beta)
- [Planned after beta](#planned-after-beta)
- [Getting Started](#getting-started)
- [Workflow Builder](#workflow-builder)
- [Node types](#node-types)
- [Expression syntax](#expression-syntax)
- [Business Central Integration](#business-central-integration)
- [Security & privacy](#security--privacy)
- [Troubleshooting](#troubleshooting)

## What is Shopware Nexus?

Nexus is a unified platform for **event-driven automation and
integration**. Merchants can orchestrate systems visually via low-code and create
scalable workflows that connect Shopware with ERPs, CRMs and other
business systems.

## Key Capabilities

| Feature | Description |
|---------|-------------|
| Visual Workflow Builder | Drag-and-drop interface |
| Shopware Event Triggers | Reacts to entity events |
| Schedule Triggers | Cron-based execution |
| Business Central Integration | CRUD for items, customers, sales orders |
| Shopware API Actions | Call arbitrary Shopware endpoints |
| API Requests | Generic HTTP calls |
| Slack Notifications | Send Slack messages |
| Conditional Logic | If/else and switch branching |
| S3 Storage | Store data in S3 |
| Data Transformation | Map and filter data |
| Expression Placeholders | `{{payload.field}}` for data interpolation |
| Execution Monitoring | Track runs and metrics |
| Delay Node | Delays between steps |

## Not available in beta

- SLA guarantees
- 24/7 support
- Multi-region deployment (EU only)
- On-premise/self-hosted
- Workflow marketplace

## Planned after beta

| Feature | Time frame |
|---------|-----------|
| AI-Assisted Authoring | GA |
| Advanced Analytics | GA |
| Per-Tenant Quotas | GA |
| Workflow Versioning UI | GA |
| SAP, Oracle connectors | Post-GA |
| Custom Node Development | Post-GA |

---

## Getting Started

### Prerequisites

- Shopware 6.7 or newer
- An active Shopware subscription
- Beta access granted by Shopware
- The Nexus service enabled
- Shopware Services active (T&Cs accepted, shop registered in SBP)

### Access

1. Login via Shopware SSO (Ory / OIDC)
2. After authentication: Nexus redirects to a demo workflow
3. The workflow becomes functional as soon as the shop is connected

### Connecting a shop

Shops are pulled from the Shopware Business Platform.

> **Beta limitation:** only the first company of the user account is
> used. Only shops of that company are available in Nexus.

### Creating a workflow

Instructions in the [user documentation](https://docs.shopware.com/en/shopware-6-en/shopware-services/shopware-nexus?category=shopware-6-en/insider-previews).

### Known beta limitations

| Limitation | Workaround |
|------------|------------|
| No test mode | Use staging shops |
| Limited error details | Add log nodes |
| No undo/redo | Save frequently |
| At-least-once delivery | Design idempotent workflows |

---

## Workflow Builder

### Workflow structure

A workflow consists of nodes on a canvas:

1. **Triggers** — start the workflow
2. **Actions** — do something (API calls, ERP writes, notifications)
3. **Transforms** — shape/filter data
4. **Conditions** — branching logic
5. **Outputs** — store results

### Workflow builder interface

| Element | Description |
|---------|-------------|
| Canvas | Visual working area |
| Node Palette | Available nodes |
| Node Configuration | Parameters, credentials, notes, debug |
| Toolbar | Save, Publish, Execute, Undeploy |
| Execution Tab | Run history and metrics |

### Workflow states

| State | Description | Available actions |
|---------|-------------|---------------------|
| Draft | Being edited | Save, Publish |
| Published | Ready | Execute |
| Deploying | The deployment is being created | — |
| Active | Running | Undeploy |
| Inactive | Deployed but stopped | Execute, Delete |
| Undeploying | The deployment is being removed | — |
| Failed | Deployment or execution failed | Retry, Delete |

### Execution Metrics

- Status (Success / Failed / Running)
- Execution duration
- Messages processed per node
- Error count and latency

### Monitoring limitations (beta)

- No per-node execution logs
- Limited payload inspection
- Manual refresh required

---

## Node types

### Trigger nodes

| Node | Description | Configuration |
|------|-------------|--------------|
| Shopware Event Trigger | Reacts to entity events | Shop, event |
| Schedule Trigger | Time-based execution | Cron, timezone |

### Action nodes

| Node | Description | Configuration |
|------|-------------|--------------|
| Business Central | CRUD on BC entities | Entity, operation |
| Shopware API Call | Any Shopware API call | Method, endpoint |
| Send Slack Message | Slack notification | Channel, template |
| API Request | Generic HTTP call | URL, headers |
| Send Shopware Email | Email via Shopware | Recipient, content |

### Transform nodes

| Node | Description |
|------|-------------|
| Filter | Filter array items |

### Condition nodes

| Node | Description |
|------|-------------|
| If | True/false condition |
| Switch | Complex branching logic |

### Control nodes

| Node | Description |
|------|-------------|
| Delay | Delay before continuing |

### Output nodes

| Node | Description |
|------|-------------|
| S3 Storage | Store the payload in S3 |

---

## Expression syntax

Expressions use the `{{ }}` syntax in templates and mappings.

### Examples

```text
{{payload.order.orderNumber}}
{{bc_customers_response.value[0].id}}
{{customer.firstName}} {{customer.lastName}}
```

### Common usage

- **Slack templates:** create readable notification messages
- **Data mapping:** pass values from the trigger payload to action parameters
- **Branching:** `If` conditions based on payload values

---

## Business Central Integration

### Supported entities

- Customers
- Items
- Sales Orders

### Available operations (all entities)

| Operation | Description |
|-----------|-------------|
| `getAll` | Fetch all records |
| `getOne` | Fetch a single record by identifier |
| `createOrUpdate` | Create or update a record |
| `delete` | Remove a record |
| `action` | Execute a specific action on the entity |

### OData filter examples

Business Central supports the OData filter syntax:

```text
email eq 'john@example.com'
inventory lt 10
status eq 'Open'
externalDocumentNumber eq 'SW-10001'
```

---

## Security & privacy

| Aspect | Detail |
|--------|--------|
| Authentication | Shopware SSO |
| Encryption | AES-256-GCM via AWS KMS |
| Storage | Tenant-isolated |
| Infrastructure | EU-based (eu-central-1) |

---

## Troubleshooting

| Problem | Solution |
|---------|--------|
| Workflow stuck deploying | Redeploy |
| Unauthorized errors | Re-authenticate |
| Missing event data | Inspect the payload with a log node |
| BC filter returns an empty result | Validate the OData syntax |
| Slack message is not sent | Re-authorize Slack |
