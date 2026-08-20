# Shopware MCP Server — Complete Reference

The Model Context Protocol (MCP) server has been part of the core platform since Shopware 6.7.
It lets AI clients (Claude Desktop, Claude Code, Cursor, Codex) communicate directly and in a
structured way with the shop through a tool-based interface.

> **Experimental:** Behind the feature flag `MCP_SERVER`. APIs and tool names may still
> change up to Shopware 6.8.

---

## Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [Security Layers](#security-layers)
- [Built-in Tools](#built-in-tools)
- [Built-in Resources](#built-in-resources)
- [Built-in Prompts](#built-in-prompts)
- [Configuration](#configuration)
- [MCP Concepts: Tools vs. Resources vs. Prompts](#mcp-concepts-tools-vs-resources-vs-prompts)
- [Shopware MCP Extensions](#shopware-mcp-extensions)
- [Extending the MCP Server](#extending-the-mcp-server)
- [Typical Example Workflows](#typical-example-workflows)
- [Troubleshooting](#troubleshooting)
- [Known Limitations (Spec Coverage)](#known-limitations-spec-coverage)

## Overview

| Property | Details |
|----------|---------|
| Endpoint | `POST /api/_mcp` (streamable HTTP transport) |
| Authentication | Integration credentials or OAuth bearer token |
| Authorization | Full Admin API ACL check per tool call |
| Tool allowlist | Per integration and per user; intersection with `sw-app-user-id` |
| Rate limiting | Per integration |
| Discovery | `bin/console debug:mcp` lists all registered capabilities |
| Extensibility | Plugins, bundles and apps can contribute their own tools/prompts/resources |

---

## Quick Start

### 1. Enable the feature flag

```bash
# .env
MCP_SERVER=1
```

### 2. Create an integration

```bash
bin/console integration:create "My MCP Client" --admin
# Output:
# SHOPWARE_ACCESS_KEY_ID=SWIA...
# SHOPWARE_SECRET_ACCESS_KEY=...
```

> For production: omit `--admin`, create a dedicated ACL role with minimal privileges.

### 3. Configure the AI client

**Claude Desktop / Cursor** (`~/Library/Application Support/Claude/claude_desktop_config.json` or `.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "shopware": {
      "type": "streamable-http",
      "url": "https://your-shop.example.com/api/_mcp",
      "headers": {
        "sw-access-key": "SWIA...",
        "sw-secret-access-key": "..."
      }
    }
  }
}
```

**Claude Code** (`.mcp.json` in the project root — `type` must be `http`, not `streamable-http`):
```json
{
  "mcpServers": {
    "shopware": {
      "type": "http",
      "url": "http://localhost:8000/api/_mcp",
      "headers": {
        "sw-access-key": "SWIA...",
        "sw-secret-access-key": "..."
      }
    }
  }
}
```

Or via CLI:
```bash
claude mcp add --transport http shopware http://localhost:8000/api/_mcp \
  --header "sw-access-key: SWIA..." \
  --header "sw-secret-access-key: ..."
```

**Codex** (`~/.codex/config.toml`):
```toml
[mcp_servers.shopware]
url = "https://your-shop.example.com/api/_mcp"
env_http_headers = { "sw-access-key" = "SHOPWARE_MCP_ACCESS_KEY", "sw-secret-access-key" = "SHOPWARE_MCP_SECRET_KEY" }
enabled = true
```
```bash
export SHOPWARE_MCP_ACCESS_KEY='SWIA...'
export SHOPWARE_MCP_SECRET_KEY='...'
```

### 4. Test the connection

```bash
bin/console debug:mcp
```

---

## Authentication

### Integration credentials (recommended)

HTTP headers `sw-access-key` and `sw-secret-access-key`. No token expiry, no manual renewal.

### Bearer token

Standard Admin API OAuth bearer token. Expires (default: 10 minutes) — unsuitable for persistent clients. Uses the per-user allowlist.

---

## Security Layers

Every request passes through three independent layers:

```
Request → [1. Authentication] → [2. MCP allowlist] → [3. ACL] → execute capability
```

**Layer 1 — Authentication:** `sw-access-key` + `sw-secret-access-key`.

**Layer 2 — MCP allowlist:** Per principal. `null` = all capabilities; `[]` = none.

| Auth method | Allowlist source |
|-------------|------------------|
| Integration key (`SWIA...`) | Per integration under Settings → Integrations → Edit MCP Allowlist |
| User key (`SWUA...`) | Per user under Settings → Users & Permissions → MCP Tool Allowlist |
| Bearer JWT (password/refresh) | Per-user allowlist |
| Bearer JWT (client credentials) | Per-integration allowlist |
| Integration + `sw-app-user-id` (Copilot) | Intersection of integration and user |

Admin users (`admin = true`) bypass the allowlist entirely.
`--admin` on an integration bypasses only the ACL (layer 3), not the allowlist (layer 2).

**Layer 3 — ACL:** The integration role must have the required entity permissions.

---

## Built-in Tools

### Response format

All core tools respond with a consistent envelope:

```json
// Success:
{"success": true, "data": [], "_meta": {"total": 42, "page": 1, "limit": 25}}

// Error:
{"success": false, "error": "Actionable error message"}
```

### Dry-run behavior

All write tools default to `dryRun=true`:
- Validation and preview, no persistence
- Open transaction → execute → rollback
- Flow Builder actions suppressed
- Pass `dryRun=false` explicitly to commit

### Tool dependency graph

| Tool | Depends On |
|------|-----------|
| `shopware-entity-read` | `shopware-entity-schema` |
| `shopware-entity-search` | `shopware-entity-schema` |
| `shopware-entity-aggregate` | `shopware-entity-schema` |
| `shopware-entity-upsert` | `shopware-entity-schema` |
| `shopware-entity-delete` | `shopware-entity-search` |
| `shopware-system-config-write` | `shopware-system-config-read` |

---

### Read tools

#### `shopware-entity-schema`

Retrieve the schema (fields + associations) of an entity. Always call this first, before search/upsert.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `entity` | string | yes | Entity name (e.g. `product`, `order`, `customer`) |

```json
{"entity": "product"}
```

ACL: none (schema introspection only).

---

#### `shopware-entity-search`

Search entity records. Supports `filter`, `sort`, `limit`, `page`, `associations`, `includes`, `fields`, `ids`, `term`, `query`, `post-filter`, `grouping`, `total-count-mode`.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `entity` | string | yes | — | Entity name |
| `criteria` | string | no | `{}` | JSON criteria object |
| `limit` | int | no | `25` | Results per page |
| `page` | int | no | `1` | Page |
| `term` | string | no | — | Full-text search |

```json
{"entity": "product", "term": "shirt", "limit": 5}
```

```json
{
  "entity": "product",
  "criteria": "{\"filter\": [{\"type\": \"range\", \"field\": \"stock\", \"parameters\": {\"lte\": 5}}], \"sort\": [{\"field\": \"stock\", \"order\": \"ASC\"}]}"
}
```

Pagination: `page * limit >= _meta.total` → last page reached.

Without `includes`: the response is automatically trimmed to scalar fields (no thumbnails, no translation duplicates).

ACL: `{entity}:read`

---

#### `shopware-entity-aggregate`

Run aggregations without loading records. For counts, averages, sums.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `entity` | string | yes | Entity name |
| `aggregations` | string | yes | JSON array of aggregation definitions |
| `filters` | string | no | JSON array of filters |

Aggregation types: `avg`, `sum`, `min`, `max`, `count`, `terms`, `date-histogram`, `range`, `filter`, `entity`

```json
{
  "entity": "order",
  "aggregations": "[{\"type\": \"avg\", \"name\": \"avgOrderValue\", \"field\": \"amountTotal\"}]"
}
```

ACL: `{entity}:read`

---

#### `shopware-entity-read`

Read a single entity by UUID.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `entity` | string | yes | Entity name |
| `id` | string | yes | UUID |
| `criteria` | string | no | JSON criteria for associations |

ACL: `{entity}:read`

---

#### `shopware-system-config-read`

Read system configuration values. A domain prefix returns all keys under that domain.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | string | yes | Config key or domain prefix (e.g. `core.listing`) |
| `salesChannelId` | string | no | Scope to a sales channel |

ACL: `system_config:read`

---

### Write tools

#### `shopware-entity-upsert`

Create or update an entity. Without `id` → create; with `id` → update.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `entity` | string | yes | — | Entity name |
| `payload` | string | yes | — | JSON object or array |
| `dryRun` | bool | no | `true` | Preview without persistence |

ACL: `{entity}:create` and/or `{entity}:update`

---

#### `shopware-entity-delete`

Delete entities by UUID. Cascade impact preview in dry run.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `entity` | string | yes | — | Entity name |
| `ids` | string | yes | — | JSON array of UUIDs |
| `dryRun` | bool | no | `true` | Cascade preview |

ACL: `{entity}:delete`

---

#### `shopware-system-config-write`

Update system configuration. Shows a before/after diff in dry run.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `key` | string | yes | — | Full config key |
| `value` | string | yes | — | New value (JSON-encoded for complex types) |
| `salesChannelId` | string | no | — | Scope to a sales channel |
| `dryRun` | bool | no | `true` | Diff preview |

ACL: `system_config:update`

---

#### `shopware-order-state`

Change the order, transaction and/or delivery state in a single call.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `orderNumber` | string | one of | — | Order number (e.g. `10001`) |
| `orderId` | string | one of | — | Order UUID |
| `orderAction` | string | no | — | `cancel`, `process`, `complete`, `reopen` |
| `transactionAction` | string | no | — | `cancel`, `paid`, `refund` |
| `deliveryAction` | string | no | — | `cancel`, `ship`, `retour`, `reopen` |
| `dryRun` | bool | no | `true` | Preview without execution |

```json
{"orderNumber": "10001", "deliveryAction": "ship", "dryRun": true}
```

```json
{"orderNumber": "10001", "orderAction": "cancel", "transactionAction": "refund", "deliveryAction": "cancel", "dryRun": false}
```

ACL: `order:read` always; `order:update`, `order_transaction:update`, `order_delivery:update` depending on the action when committing.

---

#### `shopware-media-upload`

Upload a media file from a public URL. No dry run.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | yes | Public URL |
| `fileName` | string | no | File name (default: URL basename) |
| `mediaFolderId` | string | no | UUID of the media folder |
| `productId` | string | no | Product UUID — sets the image as cover |

ACL: `media:create`; additionally `product:update` when `productId` is given.

---

### Storefront bundle tools

#### `shopware-theme-config`

Read or update the theme configuration for a sales channel.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `salesChannelId` | string | yes* | `""` | Sales channel UUID |
| `action` | string | no | `"get"` | `"get"` or `"update"` |
| `config` | string | no | `"{}"` | JSON key-value (for update) |
| `dryRun` | bool | no | `true` | Preview (for update) |

```json
{
  "salesChannelId": "<uuid>",
  "action": "update",
  "config": "{\"sw-color-brand-primary\": {\"value\": \"#0000ff\"}}",
  "dryRun": false
}
```

ACL: `theme:read` (get), `theme:update` (update).

---

## Built-in Resources

Resources are read-only reference data without a tool call budget.

| URI | Description |
|-----|-------------|
| `shopware://entities` | All registered entity names |
| `shopware://sales-channels` | All sales channels with IDs, names, types, domains |
| `shopware://currencies` | All currencies with ISO codes, symbols, factors |
| `shopware://languages` | All languages with locale codes |
| `shopware://state-machines` | All state machines with states and valid transitions |
| `shopware://business-events` | All events that can trigger flows |
| `shopware://flow-actions` | All Flow Builder actions |
| `shopware://extensions` | Active plugins/bundles with additional MCP tools |

---

## Built-in Prompts

### `shopware-context`

System prompt with Shopware domain knowledge:
- Core entity relationships (product, order, customer, category)
- DAL criteria format
- Tools grouped by purpose
- Common multi-step workflows as recipes
- Error recovery guidance
- Best practices (schema first, dryRun, includes)

---

## Configuration

### Feature flag

```bash
# .env
MCP_SERVER=1
```

### Shopware MCP settings

```yaml
# config/packages/shopware.yaml
shopware:
  mcp:
    allowed_tools: []    # Empty = all tools. A list = global restriction.
    app_tool_timeout: 10 # Timeout in seconds for app webhook calls
```

### Global tool allowlist

```yaml
shopware:
  mcp:
    allowed_tools:
      - shopware-entity-schema
      - shopware-entity-search
      - shopware-system-config-read
```

### Session store

Default: file-based in `%kernel.cache_dir%/mcp-sessions/` (single server only).

**Redis for multi-server/Kubernetes:**

```yaml
# config/services.yaml
services:
  mcp.session.cache_psr16:
    class: Symfony\Component\Cache\Psr16Cache
    arguments: ['@cache.mcp_sessions']
  mcp.session.store:
    class: Mcp\Server\Session\Psr16SessionStore
    arguments:
      - '@mcp.session.cache_psr16'
      - 3600
```

```yaml
# config/packages/framework.yaml
framework:
  cache:
    pools:
      cache.mcp_sessions:
        adapter: cache.adapter.redis_tag_aware
        provider: 'redis://your-redis-host:6379'
        default_lifetime: 3600
```

### Delegated user calls (`sw-app-user-id`)

Apps can act on behalf of a logged-in user:

```
sw-access-key: SWIA...
sw-secret-access-key: ...
sw-app-user-id: <user-uuid>
```

User UUID from JavaScript: `Shopware.Store.get('session').currentUser.id`
Or via API: `GET /api/_info/me` → `data.id`

Shopware applies the **intersection** of the integration allowlist and the user allowlist.

### CLI: `debug:mcp`

```bash
bin/console debug:mcp                         # All capabilities
bin/console debug:mcp --tools                 # Tools only
bin/console debug:mcp --prompts               # Prompts only
bin/console debug:mcp --resources             # Resources only
bin/console debug:mcp shopware-entity-search  # A single capability
bin/console debug:mcp --integration=SWIA...   # From the perspective of an integration
```

### Configuring the ACL

1. Create an ACL role in Settings → Users & Permissions → Roles
2. Create the integration without `--admin` and assign the role
3. Settings → Integrations → Edit MCP Allowlist → enable only the required tools

**Privilege overview in the admin:** The role detail page shows a banner for MCP-enabled integrations.
Clicking **Show MCP tool requirements** opens the modal with the missing privileges per tool/entity:

![MCP permissions privilege hint](../../assets/mcp-permissions-privilege-hint.png)

**Allowlist with privilege gaps:** The Edit MCP Allowlist modal shows coverage warnings for missing permissions:

![MCP allowlist collapsed with warnings](../../assets/mcp-allowlist-collapsed.png)

**Configuring the allowlist** (integration + capability selection):

![MCP allowlist clean selection](../../assets/mcp-allowlist-clean.png)

**Integration list with the Edit Allowlist action:**

![MCP integrations edit allowlist](../../assets/mcp-integrations-edit-mcp-allowlist.png)

---

## MCP Concepts: Tools vs. Resources vs. Prompts

| | Tool | Resource | Prompt |
|---|------|----------|--------|
| Invocation | Agent decides | Client/agent fetches | User selects |
| Parameters | Yes, typed | URI only | Optional |
| Writes | Yes | No | No |
| Has description | Yes (agent routing) | No | Yes |
| Counts as a tool call | Yes | No | No |
| Best for | Actions, queries | Reference data | System instructions |

---

## Shopware MCP Extensions

### Shopware Copilot

AI assistant directly in the Shopware Administration. Primary consumer of the MCP server. Enabled automatically when the MCP server is running.

### SwagMcpMerchantAssistant

**Prefix:** `merchant-*` | **Distribution:** Shopware Marketplace

Higher-level merchant workflow tools:

| Tool | Purpose |
|------|---------|
| `merchant-order-summary` | Order overview with customer, line items, totals, status |
| `merchant-customer-lookup` | Find a customer by email, customer number or UUID |
| `merchant-product-create` | Create a product with natural parameters (gross price, tax rate) |
| `merchant-revenue-report` | Revenue breakdown by day/week/month |
| `merchant-bestseller-report` | Top products by quantity sold |
| `merchant-storefront-search` | Customer-facing product search with prices |
| `merchant-cart-manage` | Create, inspect and modify a cart |
| `merchant-cart-checkout` | Complete the checkout |
| `merchant-checkout-methods` | List payment and shipping methods |

### SwagMcpDevTools

**Prefix:** `swag-dev-tools-*` | **Distribution:** Symfony bundle (not a plugin)

Developer diagnostic tools:

| Tool | Purpose |
|------|---------|
| `swag-dev-tools-log-stream` | Read recent Monolog entries from disk |
| `swag-dev-tools-log-search` | Search log files for a substring |

Sensitive fields (passwords, tokens) are redacted automatically.

### ai-coding-tools

Developer-facing local MCP tools (experimental): code generation, testing, linting, cache clearing. Separate from `/api/_mcp`.

---

## Extending the MCP Server

### Via plugin

```php
#[McpTool(name: 'swag-my-plugin-orders', title: 'Order List', description: 'List recent orders.')]
#[McpToolRequires('order:read')]
class OrdersTool extends McpToolResponse
{
    public function __invoke(int $limit = 10): string
    {
        $context = $this->contextProvider->getContext();
        if ($error = $this->requirePrivilege($context, 'order:read')) {
            return $error;
        }
        return $this->success([/* ... */]);
    }
}
```

Service tag in `services.xml`: `<tag name="shopware.mcp.tool"/>`.

### Via app (remote webhook)

```xml
<!-- Resources/mcp.xml -->
<mcp-tools>
  <mcp-tool name="sync-orders" url="https://app.example.com/mcp/sync-orders">
    <description>Synchronize orders with the ERP</description>
    <input-schema>
      <property name="since" type="string" description="ISO 8601 date" required="true"/>
    </input-schema>
    <required-privileges>
      <privilege>order:read</privilege>
    </required-privileges>
  </mcp-tool>
</mcp-tools>
```

### Via bundle

Identical to a plugin. Load services in `build()`. The MCP feature flag only blocks the HTTP endpoint, not the DI registration.

---

## Typical Example Workflows

### Ship an order

```json
// 1. Check the valid delivery actions
// Resource: shopware://state-machines

// 2. Preview
{"tool": "shopware-order-state", "orderNumber": "10001", "deliveryAction": "ship", "dryRun": true}

// 3. Execute
{"tool": "shopware-order-state", "orderNumber": "10001", "deliveryAction": "ship", "dryRun": false}
```

### Create a product

```json
// 1. Check the schema
{"tool": "shopware-entity-schema", "entity": "product"}

// 2. Get currency + tax ID
// Resource: shopware://currencies
{"tool": "shopware-entity-search", "entity": "tax", "limit": 10}

// 3. Create (preview)
{
  "tool": "shopware-entity-upsert",
  "entity": "product",
  "payload": "{\"name\": \"New Product\", \"productNumber\": \"SW-NEW-001\", \"stock\": 100, \"taxId\": \"<tax-uuid>\", \"price\": [{\"currencyId\": \"<currency-uuid>\", \"gross\": 29.99, \"net\": 25.20, \"linked\": true}]}",
  "dryRun": true
}
```

### Analytics

```json
// Average order value
{
  "tool": "shopware-entity-aggregate",
  "entity": "order",
  "aggregations": "[{\"type\": \"avg\", \"name\": \"avgOrderValue\", \"field\": \"amountTotal\"}]"
}

// Orders per month
{
  "tool": "shopware-entity-aggregate",
  "entity": "order",
  "aggregations": "[{\"type\": \"date-histogram\", \"name\": \"ordersByMonth\", \"field\": \"orderDateTime\", \"interval\": \"month\"}]"
}
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Authentication failed` | Wrong credentials | Check `sw-access-key`/`sw-secret-access-key` |
| `Tool "X" is not in the allowlist` | Tool not enabled | Settings → Integrations → Edit MCP Allowlist |
| `Missing privilege: {entity}:read` | Missing ACL permission | Assign an ACL role with the privilege |
| Tool missing from `tools/list` | Allowlist block | Enable the tool under Edit MCP Allowlist |
| No tools in `tools/list` | Allowlist empty | Set the "All tools" toggle to ON |
| `ECONNREFUSED` | Server not running | Start Shopware, check the URL |
| Claude Code: "Does not adhere to schema" | `type: streamable-http` instead of `type: http` | Change to `"type": "http"` in `.mcp.json` |
| Tool missing from `debug:mcp` | Plugin inactive, tag missing, attribute wrong | Activate the plugin, `bin/console cache:clear` |

**Debugging the connection:**
```bash
bin/console debug:mcp
bin/console debug:mcp --integration=SWIA...
```

---

## Known Limitations (Spec Coverage)

| Area | Status |
|------|--------|
| `listChanged` notifications | Not implemented |
| Resource templates + subscriptions | Not implemented |
| Protocol-level pagination | Not implemented (Shopware uses `limit`/`page`) |
| Completion for prompt/URI template arguments | Not implemented |
| `structuredContent` and `isError` | Not used (custom `{"success": bool}` envelope) |
| ACL checks on resources | Not implemented |
