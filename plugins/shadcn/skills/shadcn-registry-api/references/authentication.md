# Registry Authentication

Configure authentication in `components.json` under `registries`.
Environment variables (`${VAR_NAME}`) are expanded at runtime from
`process.env` and never logged or stored.

## Token (Bearer)

```json title="components.json"
{
  "registries": {
    "@private": {
      "url": "https://registry.company.com/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      }
    }
  }
}
```

`.env.local`:

```
REGISTRY_TOKEN=your_secret_token_here
```

## API Key in header

```json
{
  "@company": {
    "url": "https://api.company.com/registry/{name}.json",
    "headers": {
      "X-API-Key": "${API_KEY}",
      "X-Workspace-Id": "${WORKSPACE_ID}"
    }
  }
}
```

## Basic authentication

```json
{
  "@internal": {
    "url": "https://registry.company.com/{name}.json",
    "headers": {
      "Authorization": "Basic ${BASE64_CREDENTIALS}"
    }
  }
}
```

## Query parameter authentication

```json
{
  "@secure": {
    "url": "https://registry.example.com/{name}.json",
    "params": {
      "api_key": "${API_KEY}",
      "client_id": "${CLIENT_ID}"
    }
  }
}
```

## Multiple authentication methods

```json
{
  "@enterprise": {
    "url": "https://api.enterprise.com/v2/registry/{name}",
    "headers": {
      "Authorization": "Bearer ${ACCESS_TOKEN}",
      "X-API-Key": "${API_KEY}",
      "X-Workspace-Id": "${WORKSPACE_ID}"
    },
    "params": { "version": "latest" }
  }
}
```

## Server-side: Next.js route handler

```typescript title="app/api/registry/[name]/route.ts"
import { NextRequest, NextResponse } from "next/server"

export async function GET(
  request: NextRequest,
  { params }: { params: { name: string } }
) {
  const authHeader = request.headers.get("authorization")
  const token = authHeader?.replace("Bearer ", "")

  if (!isValidToken(token)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  if (!hasAccessToComponent(token, params.name)) {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 })
  }

  const component = await getComponent(params.name)
  return NextResponse.json(component)
}
```

## Custom error messages (shown to CLI users)

```typescript
return NextResponse.json(
  {
    error: "Unauthorized",
    message: "Set REGISTRY_TOKEN in your .env.local file",
  },
  { status: 401 }
)
```

## Testing locally

```bash
curl -H "Authorization: Bearer your_token" https://registry.company.com/button.json

REGISTRY_TOKEN=your_token npx shadcn@latest add @private/button
```

## HTTP status codes

| Status | Meaning                                   |
|--------|-------------------------------------------|
| 401    | Invalid or missing token                  |
| 403    | Token valid but insufficient permissions  |
| 429    | Rate limit exceeded                       |

## Security checklist

- Always use HTTPS URLs
- Never commit tokens — use `.env.local`
- Implement rate limiting on your server
- Rotate tokens regularly (e.g. 30-day expiration)
- Log access for auditing
- All resources are validated against schema before install — no exec

Source: registry/authentication.mdx
