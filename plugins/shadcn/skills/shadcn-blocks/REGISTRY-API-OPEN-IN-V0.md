# Open in v0

Open any registry item directly in v0 using the API endpoint.

## URL pattern

```
https://v0.dev/chat/api/open?url=[ITEM_URL]
```

Example:

```
https://v0.dev/chat/api/open?url=https://ui.shadcn.com/r/styles/new-york/login-01.json
```

## Limitations

Open in v0 does NOT support:
- `cssVars`
- `css`
- `envVars`
- Namespaced registries
- Bearer tokens or header-based authentication

Only query parameter authentication is supported.

## Button component

```tsx
import { Button } from "@/components/ui/button"

export function OpenInV0Button({ url }: { url: string }) {
  return (
    <Button
      aria-label="Open in v0"
      className="h-8 gap-1 rounded-[6px] bg-black px-3 text-xs text-white hover:bg-black hover:text-white dark:bg-white dark:text-black"
      asChild
    >
      <a
        href={`https://v0.dev/chat/api/open?url=${url}`}
        target="_blank"
        rel="noreferrer"
      >
        Open in v0
      </a>
    </Button>
  )
}
```

```jsx
<OpenInV0Button url="https://example.com/r/hello-world.json" />
```

## Query parameter authentication

Add a `token` query parameter to the item URL:

```
https://registry.company.com/r/hello-world.json?token=your_secure_token
```

Server-side validation (Next.js):

```typescript
export async function GET(request: NextRequest) {
  const token = request.nextUrl.searchParams.get("token")

  if (!isValidToken(token)) {
    return NextResponse.json(
      { error: "Unauthorized", message: "Invalid or missing token" },
      { status: 401 }
    )
  }

  return NextResponse.json(registryItem)
}
```

Tokens should be encrypted and time-limited. Never expose production tokens.

Source: registry/open-in-v0.mdx
