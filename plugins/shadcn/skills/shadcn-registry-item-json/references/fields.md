# registry-item.json Core Fields

Schema URL: `https://ui.shadcn.com/schema/registry-item.json`

## $schema

```json
{ "$schema": "https://ui.shadcn.com/schema/registry-item.json" }
```

## name

```json
{ "name": "hello-world" }
```

Unique identifier for the item within the registry. Used for CLI commands and
dependency references.

## title

```json
{ "title": "Hello World" }
```

Human-readable short title. Used by LLMs to understand the component.

## description

```json
{ "description": "A simple hello world component." }
```

Longer description. Shown in the CLI and used by LLMs.

## type

```json
{ "type": "registry:block" }
```

Determines item type and target install path. See [types.md](types.md).

## author

```json
{ "author": "John Doe <john@doe.com>" }
```

Optional. Author of the registry item.

## dependencies

```json
{
  "dependencies": [
    "@radix-ui/react-accordion",
    "zod",
    "lucide-react",
    "name@1.0.2"
  ]
}
```

npm packages required at runtime. Use `name@version` to pin a specific version.

## devDependencies

```json
{ "devDependencies": ["tw-animate-css", "name@1.2.0"] }
```

npm packages needed during development only.

## registryDependencies

```json
{
  "registryDependencies": [
    "button",
    "@acme/input-form",
    "acme/ui/button#v1.2.0",
    "https://example.com/r/editor.json",
    "./editor.json"
  ]
}
```

Registry items that must be installed as dependencies. Supported formats:
- `button` — built-in shadcn/ui item
- `@namespace/item` — namespaced registry item
- `owner/repo/item[#ref]` — GitHub registry item (pin with tag or full SHA)
- `https://example.com/r/item.json` — full URL
- `./item.json` — local file path

Bare names resolve to the official shadcn/ui registry, not the same GitHub
repo. For same-repo GitHub deps, use the full GitHub item address.

## docs

```json
{
  "docs": "To get an OPENAI_API_KEY, sign up at https://platform.openai.com."
}
```

Custom message shown to the user when installing via the CLI.

## categories

```json
{ "categories": ["sidebar", "dashboard"] }
```

Optional tags for organizing the registry item.

## meta

```json
{ "meta": { "foo": "bar" } }
```

Arbitrary additional metadata as key/value pairs.

Source: registry/registry-item-json.mdx
