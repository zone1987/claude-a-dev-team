# components.json — Registries Configuration

Configure multiple resource registries to install components from various
sources including private registries.

## Basic configuration

```json
{
  "registries": {
    "@v0": "https://v0.dev/chat/b/{name}",
    "@acme": "https://registry.acme.com/{name}.json",
    "@internal": "https://internal.company.com/{name}.json"
  }
}
```

`{name}` is replaced with the resource name when installing.

## Advanced — with authentication

```json
{
  "registries": {
    "@private": {
      "url": "https://api.company.com/registry/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}",
        "X-API-Key": "${API_KEY}"
      },
      "params": {
        "version": "latest"
      }
    }
  }
}
```

Environment variables in `${VAR_NAME}` format are automatically expanded.

## Using namespaced registries

```bash
# Install from a configured registry
npx shadcn@latest add @v0/dashboard

# Install from private registry
npx shadcn@latest add @private/button

# Install multiple resources from different registries
npx shadcn@latest add @acme/header @internal/auth-utils
```

## Multi-registry example

```json
{
  "registries": {
    "@shadcn": "https://ui.shadcn.com/r/{name}.json",
    "@company-ui": {
      "url": "https://registry.company.com/ui/{name}.json",
      "headers": {
        "Authorization": "Bearer ${COMPANY_TOKEN}"
      }
    },
    "@team": {
      "url": "https://team.company.com/{name}.json",
      "params": {
        "team": "frontend",
        "version": "${REGISTRY_VERSION}"
      }
    }
  }
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/components-json.mdx`
