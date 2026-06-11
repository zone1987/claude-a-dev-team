---
name: sw-coding-guidelines
description: >
  Shopware-6 Core-Coding-Guidelines: final & internal, Extendability (Events vor Decorators), Decorator-Pattern,
  Domain-Exceptions, Feature-Flags, DB-Migrationen, Code für Static Analysis, Deprecation-Strategie. Trigger:
  "Coding Guidelines shopware", "final internal", "extendability", "deprecation strategy", "wie schreibt man shopware code",
  "Konventionen Core". Shopware 6.7.
---

# Shopware 6 — Coding-Guidelines

Verbindliche Leitlinien aus dem Core (`coding-guidelines/`). Kernpunkte:

- **Extendability**: Erweiterung primär über **Events** (`EventSubscriberInterface`); Decorator nur wenn Event-Timing
  nicht passt. Eigene Klassen `final` machen, wo möglich.
- **final & internal**: `@internal`/`final` markieren Nicht-API; darauf NICHT verlassen (kann ohne BC-Bruch ändern).
- **Decorator-Pattern**: gleiches Interface, `.inner` delegieren, keine Core-Logik duplizieren.
- **Domain-Exceptions**: pro Domäne eine Exception-Factory mit stabilen `code`s (`sw-domain-exceptions`).
- **Deprecation**: Änderungen hinter Feature-Flags/Major-Flags; konsistente Deprecation-Notices; Rector-Codemods.
- **DB-Migrationen**: non-destructive `update()` + getrennt `updateDestructive()`; idempotent.
- **Static Analysis**: Code so schreiben, dass PHPStan Level (hoch) + Deptrac grün sind; strikte Typen.

Lint/Analyse-Befehle: `composer ecs[-fix]`, `composer phpstan`, `composer eslint:admin|storefront`, `stylelint`, `ludtwig`.
Architektur-Entscheidungen: `sw-adr-knowledge`. Static-Analysis-Tools: `sw-static-analysis`.
