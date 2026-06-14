# MCP: Configuring Registries

The MCP server reads registry configuration from `components.json`.
No configuration needed for the standard shadcn/ui registry.

## Basic namespace registry

```json title="components.json"
{
  "registries": {
    "@acme": "https://registry.acme.com/{name}.json"
  }
}
```

## Private (authenticated) registry

```json title="components.json"
{
  "registries": {
    "@internal": {
      "url": "https://internal.company.com/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      }
    }
  }
}
```

Set `REGISTRY_TOKEN` in `.env.local`:

```
REGISTRY_TOKEN=your_token_here
```

## Multiple registries

```json title="components.json"
{
  "registries": {
    "@acme":     "https://registry.acme.com/{name}.json",
    "@internal": {
      "url": "https://internal.company.com/{name}.json",
      "headers": { "Authorization": "Bearer ${REGISTRY_TOKEN}" }
    }
  }
}
```

## Supported registry types

- shadcn/ui (default, no config needed)
- Third-party registries following the shadcn schema
- Private / internal registries (with auth headers)
- Namespaced registries (`@namespace/item`)

## Example prompts

```
Show me all available components in the shadcn registry
Find me a login form from the shadcn registry
Add the button, dialog and card components to my project
Create a contact form using shadcn components
Show me components from the acme registry
Install @internal/auth-form
Build a landing page using hero and features sections from the acme registry
Install the Cursor rules from the acme registry
```

Source: (root)/mcp.mdx
