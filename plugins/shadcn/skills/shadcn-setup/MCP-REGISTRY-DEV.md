# MCP for Registry Developers

The shadcn MCP server works out of the box with any shadcn-compatible registry.
No special configuration is needed on the registry side.

## Prerequisite: registry.json at root

The MCP server fetches the registry index by requesting
`{base-url}/registry.json` (or `{base-url}/registry` without extension).

Example: if items are served at `https://acme.com/r/{name}.json`, the index
must be at `https://acme.com/r/registry.json`.

The index must conform to the registry.json schema.

## Tell users how to configure the MCP

Ask consumers to:

1. Add your namespace to their `components.json`:

```json title="components.json"
{
  "registries": {
    "@acme": "https://acme.com/r/{name}.json"
  }
}
```

2. Init the MCP server:

```bash
npx shadcn@latest mcp init --client claude
```

3. Restart their MCP client and use prompts like:
   - "Show me components from the acme registry"
   - "Create a landing page using items from the acme registry"

## Best practices for MCP-compatible registries

1. **Clear descriptions**: Write concise, informative `description` and `title`
   fields — AI assistants use them to match user intent.
2. **Complete dependencies**: List all `dependencies` accurately so MCP can
   install them automatically.
3. **Registry dependencies**: Use `registryDependencies` to capture
   relationships between items.
4. **Consistent naming**: Use kebab-case for all item names.

Source: registry/mcp.mdx
