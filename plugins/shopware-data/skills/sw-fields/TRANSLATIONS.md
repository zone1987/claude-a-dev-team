# Shopware 6 — Translations

Translatable values live in a separate `*_translation` table. Three parts:

1. **Main definition**: `(new TranslatedField('name'))` + `(new TranslationsAssociationField(FfExampleTranslationDefinition::class, 'ff_example_id'))->addFlags(new Required())`.
2. **Translation definition** extends `EntityTranslationDefinition`, `getParentDefinitionClass()` points to the main definition; it contains the actual `StringField`/`LongTextField`.
3. **Writing**: one entry per `languageId` in the `translations` payload, or the simplified `['name' => 'value']` for the context language.

On read, the DAL maps the values onto the entity properties and into the `translated` array (language fallback/inheritance applied automatically).

→ Full example (definition + translation): [TRANSLATIONS-EXAMPLE.md](TRANSLATIONS-EXAMPLE.md)
