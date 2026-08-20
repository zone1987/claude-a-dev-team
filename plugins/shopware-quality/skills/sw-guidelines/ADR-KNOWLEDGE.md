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

→ **Vollständiger chronologischer Index aller 149 ADRs**: [ADR-KNOWLEDGE-ADR-INDEX.md](ADR-KNOWLEDGE-ADR-INDEX.md)
Die konkreten Muster sind in den jeweiligen Fach-Skills umgesetzt (DAL, Checkout, Admin, Storefront, Framework).
