# shadcn-vue registry.json — Vollstaendiges Schema

JSON-Schema-URL: `https://shadcn-vue.com/schema/registry.json`

## Minimales Beispiel

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

## Felder

### $schema

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry.json"
}
```

### name

Name der Registry. Wird fuer Data-Attribute und Metadaten verwendet.

```json
{
  "name": "acme"
}
```

### homepage

Homepage der Registry. Wird fuer Data-Attribute und Metadaten verwendet.

```json
{
  "homepage": "https://acme.com"
}
```

### items

Array von Registry-Items. Jedes Item muss dem
[registry-item Schema](https://shadcn-vue.com/schema/registry-item.json) entsprechen.

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

Vollstaendige Dokumentation der Item-Felder: siehe `registry-item-json.md`.
