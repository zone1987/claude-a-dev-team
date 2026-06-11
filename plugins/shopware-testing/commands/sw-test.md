---
name: sw-test
description: Scaffold eines passenden Tests für eine Shopware-6-Klasse (Unit/Integration/Store-API/Admin-API bzw. Jest), inkl. Setup, Fixtures/Builder und Mocks.
argument-hint: <ClassOrPath> [--plugin <PluginName>] [--type unit|integration|store-api|admin-api|jest]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-test

Erzeuge einen Test für die angegebene Klasse/Datei. Delegiere an `shopware-tester`.

## Ablauf
1. Zielklasse analysieren (Abhängigkeiten, DB-Bezug) → Testebene wählen (oder `--type`).
2. Testdatei unter `tests/` spiegelnd zur Klasse anlegen:
   - Unit: ohne Kernel, Abhängigkeiten mocken (`StaticEntityRepository`/`StaticSystemConfigService`).
   - Integration: `IntegrationTestBehaviour`, echte Repos, Builder/Fixtures.
   - Store-/Admin-API: `SalesChannelApiTestBehaviour`/`AdminApiTestBehaviour`.
   - Jest (Admin/Storefront): `.spec.js` mit `@vue/test-utils` bzw. Plugin-Instanz.
3. `assertSame`, aussagekräftige Testnamen, Arrange-Act-Assert.
4. Hinweis: Tests ausführen (`vendor/bin/phpunit` / `composer admin:unit`/`storefront:unit`).

Bestehende Tests nicht überschreiben; nur ergänzen.
