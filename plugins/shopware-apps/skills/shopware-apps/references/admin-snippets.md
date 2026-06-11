---
title: Admin Translation Snippets
impact: MEDIUM
impactDescription: Apps add admin translations via JSON files but cannot override existing keys
tags: admin, snippets, translations, i18n, json
---

## Admin Translation Snippets

Apps add translation snippets to the Administration via JSON files.

### File Structure

```
Resources/app/administration/snippet/
├── de.json
├── en.json
└── en-US.json
```

### JSON Format

```json
{
    "my-app": {
        "module": {
            "title": "My Module",
            "description": "Module description"
        },
        "actions": {
            "save": "Save changes",
            "cancel": "Cancel"
        }
    }
}
```

### Critical Limitation

**Apps cannot override existing snippet keys.** This is a key distinction from plugins. Plan snippet keys carefully with unique vendor prefixes.

**Incorrect:**
```json
{
    "sw-product": { "title": "My Custom Title" }
}
```

**Correct (vendor-prefixed):**
```json
{
    "my-app-product": { "title": "My Custom Title" }
}
```
