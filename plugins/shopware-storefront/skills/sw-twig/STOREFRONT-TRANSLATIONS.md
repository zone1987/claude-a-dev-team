# Shopware 6 — Storefront snippets

Translations live as JSON in `src/Resources/snippet/<locale>/<name>.<locale>.json` (e.g.
`storefront.de-DE.json`) and are loaded automatically. Nested keys use dot notation.

```json
{ "ff": { "hint": "Hinweis", "greeting": "Hallo {{ name }}" } }
```
```twig
{{ "ff.hint"|trans }}
{{ "ff.greeting"|trans({'%name%': customer.firstName}) }}  {# or {{ name }} placeholders, depending on convention #}
```

One file per language; prefix keys with an owner namespace (`ff.*`) to avoid collisions. Admin snippets are separate
(`shopware-admin` → `sw-admin-snippets`). Encode special characters correctly as UTF-8.
