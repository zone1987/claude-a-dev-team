---
name: sw-translations
description: >
  Übersetzbare Felder in Shopware 6 DAL: TranslatedField + TranslationDefinition + TranslationsAssociationField,
  das translated-Array, Schreiben pro Sprache. Trigger: "TranslatedField", "TranslationDefinition", "Übersetzung",
  "mehrsprachig entity", "translations association", "translated array", "language inheritance". Shopware 6.7.
---

# Shopware 6 — Translations

Übersetzbare Werte liegen in einer separaten `*_translation`-Tabelle. Drei Teile:

1. **Haupt-Definition**: `(new TranslatedField('name'))` + `(new TranslationsAssociationField(FfExampleTranslationDefinition::class, 'ff_example_id'))->addFlags(new Required())`.
2. **Translation-Definition** erweitert `EntityTranslationDefinition`, `getParentDefinitionClass()` zeigt auf die Haupt-Definition; enthält die realen `StringField`/`LongTextField`.
3. **Schreiben**: pro `languageId` im `translations`-Payload, oder vereinfacht `['name' => 'Wert']` für die Kontext-Sprache.

Beim Lesen mappt DAL die Werte auf die Entity-Properties bzw. ins `translated`-Array (Sprach-Fallback/-Inheritance automatisch).

→ Vollständiges Beispiel (Definition + Translation): [references/example.md](references/example.md)
