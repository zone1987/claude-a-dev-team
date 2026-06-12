---
name: sw-extendability
description: >
  Shopware-6 Erweiterbarkeits-Prinzipien: wann Events vs. Decorator vs. Extension-Pattern einsetzen,
  was zur stabilen Public API gehört, wie @internal/@final Klassen korrekt eingesetzt werden,
  Decoration-Pattern-Regeln (AbstractClass + getDecorated()), Hooks für Apps. Trigger:
  "erweiterbarkeit shopware", "extension pattern", "events oder decorator", "public api shopware",
  "internal final annotation", "wie erweitere ich shopware", "decoration pattern rules",
  "getDecorated", "abstract class shopware", "hooks apps". Shopware 6.7.
---

# Shopware 6 — Erweiterbarkeits-Prinzipien

Vollständige Referenz: `references/deep/extendability.md`

## Kurzfassung

- **Events (Mediator)** — erste Wahl für Erweiterbarkeit; Listener via `EventSubscriberInterface`; nur Primary Keys weitergeben, keine Entities
- **Decorator (Decoration Pattern)** — wenn Events nicht ausreichen; AbstractClass zwingend erforderlich; `getDecorated()` + `DecorationPatternException` im Core
- **Factory** — für neuen User-Input-Typen; Registry-Pattern mit Tagged Services
- **Visitor** — für Objekte, die während der Verarbeitung besucht/erweitert werden sollen
- **Adapter** — für Functional Exchange Market (kompletter Technologietausch)
- **Hooks** — App-Script-Einstiegspunkte (Äquivalent zu Events für Apps)

## @internal / @final Regeln

- `@final`: Klasse ist Public API (konsumierbar), aber nicht erweiterbar; Änderungen an public methods verboten
- `@internal`: Private API; kann ohne Deprecation geändert/entfernt werden; kein Einsatz in Dritt-Plugins
- Alle DTOs, Event-Subscriber → `final`
- Alle dekorier­baren Services → AbstractClass (KEIN `@internal`, KEIN `@final`)

## Decoration-Pattern-Pflicht­regeln

1. AbstractClass mit `getDecorated(): self` definieren
2. Core-Implementierung: `getDecorated()` wirft `DecorationPatternException`
3. AbstractClass darf NICHT `@internal` oder `@final` sein
4. Implementierungen dürfen KEINE zusätzlichen public Methoden hinzufügen
5. Implementierungen dürfen NICHT als EventSubscriber dienen

Abgrenzung zu `sw-coding-guidelines`: Dieser Skill fokussiert auf die Architektur-Konzepte; Coding-Guidelines behandelt Coding-Stil, Migrationen und Static Analysis.
