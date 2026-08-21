# shadcn-vue registry.json Schema

Complete schema documentation for `registry.json`.

## References

  $schema, name, homepage, items

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/registry/registry-json.md`

## shadcn-vue registry.json — Complete Schema

JSON-Schema-URL: `https://shadcn-vue.com/schema/registry.json`

### Minimal example

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry.json",
  "name": "shadcn",
  "homepage": "https://shadcn-vue.com",
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component.",
      "files": [
        {
          "path": "registry/new-york/HelloWorld/HelloWorld.vue",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

---

### Fields

#### $schema

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry.json"
}
```

#### name

Name of the registry. Used for data attributes and metadata.

```json
{
  "name": "acme"
}
```

#### homepage

Homepage of the registry. Used for data attributes and metadata.

```json
{
  "homepage": "https://acme.com"
}
```

#### items

Array of registry items. Every item must conform to the
[registry-item schema](https://shadcn-vue.com/schema/registry-item.json).

```json
{
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component.",
      "files": [
        {
          "path": "registry/new-york/HelloWorld/HelloWorld.vue",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

Complete documentation of the item fields: see `registry-item-json.md`.
