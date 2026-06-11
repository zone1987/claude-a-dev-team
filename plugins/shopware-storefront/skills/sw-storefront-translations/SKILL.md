---
name: sw-storefront-translations
description: >
  Storefront-Snippets (Übersetzungen) in Shopware 6: snippet/<locale>.json unter Resources, |trans, Platzhalter,
  Snippet-Set/Namespacing. Trigger: "Storefront Snippet", "Übersetzung storefront", "trans filter", "snippet json",
  "de-DE.json storefront", "Platzhalter Snippet", "i18n storefront". Shopware 6.7.
---

# Shopware 6 — Storefront-Snippets

Übersetzungen liegen als JSON unter `src/Resources/snippet/<locale>/<name>.<locale>.json` (z.B.
`storefront.de-DE.json`) und werden automatisch geladen. Verschachtelte Keys per Punktnotation.

```json
{ "ff": { "hint": "Hinweis", "greeting": "Hallo {{ name }}" } }
```
```twig
{{ "ff.hint"|trans }}
{{ "ff.greeting"|trans({'%name%': customer.firstName}) }}  {# bzw. {{ name }}-Platzhalter je Konvention #}
```

Pro Sprache eine Datei; Keys mit Owner-Präfix (`ff.*`) gegen Kollisionen. Admin-Snippets sind getrennt
(`shopware-admin` → `sw-admin-snippets`). Umlaute korrekt als UTF-8.
