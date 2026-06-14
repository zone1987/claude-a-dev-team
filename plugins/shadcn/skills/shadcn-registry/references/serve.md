# Serving a Registry

## Option A: Static JSON files (shadcn build)

```bash
npx shadcn@latest build
# generates public/r/registry.json + public/r/[name].json
```

Override output directory:

```bash
npx shadcn@latest build --output dist/r
```

`shadcn build` resolves `include`, reads file contents from disk, and writes
flattened registry JSON. The generated `registry.json` does NOT contain
`include`.

For Next.js, the dev server then serves files at `http://localhost:3000/r/`.

## Option B: Dynamic route handlers (shadcn/registry)

Install `shadcn` as a runtime dependency:

```bash
npm install shadcn
```

### Serve the catalog

```ts title="app/r/registry.json/route.ts"
import { loadRegistry } from "shadcn/registry"

export async function GET() {
  try {
    const registry = await loadRegistry()
    return Response.json(registry)
  } catch (error) {
    console.error(error)
    return Response.json({ error: "Failed to load registry." }, { status: 500 })
  }
}
```

### Serve individual items

```ts title="app/r/[name].json/route.ts"
import { loadRegistryItem, RegistryItemNotFoundError } from "shadcn/registry"

export async function GET(
  _request: Request,
  context: { params: Promise<{ name: string }> }
) {
  const { name } = await context.params
  try {
    const item = await loadRegistryItem(name)
    return Response.json(item)
  } catch (error) {
    if (error instanceof RegistryItemNotFoundError) {
      return Response.json(
        { error: `Registry item "${name}" was not found.` },
        { status: 404 }
      )
    }
    console.error(error)
    return Response.json(
      { error: "Failed to load registry item." },
      { status: 500 }
    )
  }
}
```

Both loaders resolve `include` at request time — no `shadcn build` required.

## Content negotiation (root hosting)

The CLI sends:
- `User-Agent: shadcn`
- `Accept: application/vnd.shadcn.v1+json, application/json;q=0.9`

Use this to serve HTML to browsers and JSON to the CLI from the same URL.

### Next.js rewrite example

```ts title="next.config.ts"
import type { NextConfig } from "next"

const nextConfig: NextConfig = {
  async rewrites() {
    return {
      beforeFiles: [
        {
          source: "/",
          has: [
            {
              type: "header",
              key: "accept",
              value: "(.*)application/vnd\\.shadcn\\.v1\\+json(.*)",
            },
          ],
          destination: "/r/index.json",
        },
        {
          source: "/",
          has: [{ type: "header", key: "user-agent", value: "shadcn" }],
          destination: "/r/index.json",
        },
      ],
    }
  },
  async headers() {
    return [
      {
        source: "/",
        headers: [{ key: "Vary", value: "Accept, User-Agent" }],
      },
    ]
  },
}

export default nextConfig
```

### Express example

```js title="server.js"
app.get("/", (req, res) => {
  res.vary("Accept")
  res.vary("User-Agent")
  if (req.accepts("application/vnd.shadcn.v1+json")) {
    return res.json(registryData)
  }
  if (req.get("User-Agent") === "shadcn") {
    return res.json(registryData)
  }
  res.send(htmlContent)
})
```

Source: registry/getting-started.mdx
