# Shopware 6 — Custom entity

Declarative entities without a PHP definition — described in `src/Resources/entities.xml` (or `custom_entity.xml`).
Table and entity names carry the prefix `custom_entity_` or `ce_`. Ideal for app/plugin master data with an admin UI.

```xml
<entity name="custom_entity_ff_blog">
    <fields>
        <string name="title" required="true" translatable="true"/>
        <text name="content" allow-html="true" translatable="true"/>
        <many-to-one name="author" reference="user" />
    </fields>
</entity>
```

Shopware generates definition, entity and repository (`custom_entity_ff_blog.repository`) automatically. The `cms-aware`/
`admin-ui` attributes add CMS awareness and admin list/detail modules without code (ADR "technical-concept-custom-entities").

→ Fields, flags, admin UI/CMS options: [CUSTOM-ENTITY-CUSTOM-ENTITIES.md](CUSTOM-ENTITY-CUSTOM-ENTITIES.md)
