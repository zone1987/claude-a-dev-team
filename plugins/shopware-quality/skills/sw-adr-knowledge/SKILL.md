---
name: sw-adr-knowledge
description: >
  Wissen über die Shopware-6 Architecture Decision Records (ADRs): warum bestimmte Muster gelten (Events vor Decorators,
  domain-exceptions, nested line items, payment flow, custom entities, UUIDv7, Pinia statt Vuex, Meteor, transactional
  flow actions u.v.m.). Trigger: "ADR shopware", "warum macht Shopware X so", "Architekturentscheidung", "design decision shopware",
  "welche ADR". Shopware 6.7.
---

# Shopware 6 — ADR-Wissen

Die ADRs dokumentieren bindende Architekturentscheidungen des Cores. Vor Architektur-/Pattern-Fragen hier nachschlagen
(begründet, warum etwas so gebaut wird).

## Besonders einflussreiche ADRs
- **Erweiterung**: „creating events", „decoration-pattern", „extended event system", „extract data handling to extension SDK".
- **DAL/Daten**: „when to use plain sql or dal", „dal join filter", „switch to UUIDv7", „technical-concept-custom-entities", „deprecate autoload true in dal associations".
- **Checkout**: „payment-flow", „refund-handling", „nested-line-items"/„new-nested-line-items", „tax-providers", „checkout-gateway".
- **Flow**: „transactional flow actions", „move flow execution after business process", „flow storer with scalar values".
- **Admin**: „replace Vuex with Pinia", „implementation of meteor component library", „Vue 2→3 composition api", „providing the admin extension sdk".
- **Storefront**: „add typescript support for storefront js", „refactor theme inheritance", „atomic theme compilation".
- **Qualität**: „domain-exceptions", „exception log levels", „feature flags for major versions", „follow test pyramid", „mocking repositories".

→ **Vollständiger chronologischer Index aller 149 ADRs**: [references/adr-index.md](references/adr-index.md)
Die konkreten Muster sind in den jeweiligen Fach-Skills umgesetzt (DAL, Checkout, Admin, Storefront, Framework).
