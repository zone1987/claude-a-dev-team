# Testing and Publishing a Registry

## Testing by URL

### List items (catalog discovery)

```bash
npx shadcn@latest list http://localhost:3000/r/registry.json
```

### Search items

```bash
npx shadcn@latest search http://localhost:3000/r/registry.json --query button
```

### View one item

```bash
npx shadcn@latest view http://localhost:3000/r/button.json
```

### Install one item

```bash
npx shadcn@latest add http://localhost:3000/r/button.json
```

## Testing by namespace

### Register the namespace locally

```bash
npx shadcn@latest registry add @acme=http://localhost:3000/r/{name}.json
```

The `{name}` placeholder is replaced by the item name. The catalog must still
be served separately at `.../r/registry.json`.

### List / search / view / add by namespace

```bash
npx shadcn@latest list @acme
npx shadcn@latest search @acme --query button
npx shadcn@latest view @acme/button
npx shadcn@latest add @acme/button
```

## Publishing

Deploy your project to a public URL. Users can then:

- Install items by full URL: `npx shadcn@latest add https://acme.com/r/button.json`
- Add your namespace to their `components.json`:
  ```bash
  npx shadcn@latest registry add @acme=https://acme.com/r/{name}.json
  ```
  Or manually:
  ```json title="components.json"
  {
    "registries": {
      "@acme": "https://acme.com/r/{name}.json"
    }
  }
  ```
- Then install by namespace: `npx shadcn@latest add @acme/button`

## Listing in the Registry Index

To allow `@acme` to work without users pasting the URL template, submit your
namespace to the official registry index. See
[registry/registry-index.mdx](registry-index.mdx) for requirements.

Source: registry/getting-started.mdx
