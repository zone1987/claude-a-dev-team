# Shopware 6 — ADR knowledge

The ADRs document binding architecture decisions of the core. Consult them before answering architecture or pattern
questions (they explain why something is built the way it is).

## Particularly influential ADRs
- **Extension**: "creating events", "decoration-pattern", "extended event system", "extract data handling to extension SDK".
- **DAL/data**: "when to use plain sql or dal", "dal join filter", "switch to UUIDv7", "technical-concept-custom-entities", "deprecate autoload true in dal associations".
- **Checkout**: "payment-flow", "refund-handling", "nested-line-items"/"new-nested-line-items", "tax-providers", "checkout-gateway".
- **Flow**: "transactional flow actions", "move flow execution after business process", "flow storer with scalar values".
- **Admin**: "replace Vuex with Pinia", "implementation of meteor component library", "Vue 2→3 composition api", "providing the admin extension sdk".
- **Storefront**: "add typescript support for storefront js", "refactor theme inheritance", "atomic theme compilation".
- **Quality**: "domain-exceptions", "exception log levels", "feature flags for major versions", "follow test pyramid", "mocking repositories".

→ **Complete chronological index of all 149 ADRs**: [ADR-KNOWLEDGE-ADR-INDEX.md](ADR-KNOWLEDGE-ADR-INDEX.md)
The concrete patterns are implemented in the respective domain skills (DAL, Checkout, Admin, Storefront, Framework).
