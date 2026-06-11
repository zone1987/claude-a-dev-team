---
name: sw-custom-entity
description: >
  Custom Entities in Shopware 6 (codearm, via custom_entity.xml / Entities.xml definierte Entities ohne eigene
  PHP-Definition), inkl. cms-aware/admin-ui Flags. Trigger: "Custom Entity", "custom_entity.xml", "ce_ Entity",
  "codeless entity", "Entities.xml", "custom entity admin ui". Shopware 6.7.
---

# Shopware 6 — Custom Entity

Deklarative Entities ohne PHP-Definition — beschrieben in `src/Resources/entities.xml` (bzw. `custom_entity.xml`).
Tabellen-/Entityname mit Präfix `custom_entity_` bzw. `ce_`. Ideal für App-/Plugin-Stammdaten mit Admin-UI.

```xml
<entity name="custom_entity_ff_blog">
    <fields>
        <string name="title" required="true" translatable="true"/>
        <text name="content" allow-html="true" translatable="true"/>
        <many-to-one name="author" reference="user" />
    </fields>
</entity>
```

Shopware generiert Definition/Entity/Repository (`custom_entity_ff_blog.repository`) automatisch. Mit `cms-aware`/
`admin-ui`-Attributen entstehen CMS-Awareness und Admin-Listen/Detail-Module ohne Code (ADR „technical-concept-custom-entities").

→ Felder, Flags, Admin-UI/CMS-Optionen: [references/custom-entities.md](references/custom-entities.md)
