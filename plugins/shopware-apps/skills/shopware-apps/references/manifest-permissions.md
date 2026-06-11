---
title: Manifest Permissions
impact: CRITICAL
impactDescription: Permissions control which entities the app can access via API
tags: manifest, permissions, read, create, update, delete, crud, allowed-hosts
---

## Manifest Permissions

The `<permissions>` section declares which Shopware entities your app can access. Without proper permissions, API requests will be rejected.

### Permission Types

| Element | Description |
|---------|-------------|
| `<read>` | Read access to an entity |
| `<create>` | Create new records |
| `<update>` | Modify existing records |
| `<delete>` | Remove records |
| `<crud>` | Shortcut for all four (since 6.7.3.0) |
| `<permission>` | Non-entity permissions (e.g., `system:cache:info`) |

**Incorrect (overly broad, requesting all permissions when only read is needed):**

```xml
<permissions>
    <crud>product</crud>    <!-- Only need to read products -->
    <crud>category</crud>   <!-- Only need to read categories -->
</permissions>
```

**Correct (minimal permissions — principle of least privilege):**

```xml
<permissions>
    <read>product</read>
    <read>category</read>
</permissions>
```

**Correct (when full CRUD is genuinely needed, since 6.7.3.0):**

```xml
<permissions>
    <crud>product</crud>
    <read>category</read>
    <permission>system:cache:info</permission>
</permissions>
```

**Equivalent without CRUD shortcut:**

```xml
<permissions>
    <read>product</read>
    <create>product</create>
    <update>product</update>
    <delete>product</delete>
    <read>category</read>
    <permission>system:cache:info</permission>
</permissions>
```

### Allowed Hosts

The `<allowed-hosts>` section declares external hosts the app communicates with:

```xml
<allowed-hosts>
    <host>api.example.com</host>
    <host>cdn.example.com</host>
</allowed-hosts>
```

### Important Notes

- Permissions are displayed to the shop owner during app installation
- Request only the permissions your app actually needs
- Custom entities created by the app are automatically accessible without explicit permissions
- Associations to core entities from custom entities require explicit `<read>` permissions
