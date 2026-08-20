---
name: sw-guidelines
description: Shopware coding guidelines: code structure, domain exceptions, extendability rules, ADR knowledge, documentation guidelines. Use when reviewing Shopware code against the platform's own conventions.
---

# Shopware coding guidelines

The platform's own rules for platform-shaped code. Domain exceptions and extendability are where most plugins diverge.

## Reference map

- **[ADR-KNOWLEDGE.md](ADR-KNOWLEDGE.md)**: Die ADRs dokumentieren bindende Architekturentscheidungen des Cores. [ADR-KNOWLEDGE-ADR-INDEX](ADR-KNOWLEDGE-ADR-INDEX.md).
- **[CODE-STRUCTURE.md](CODE-STRUCTURE.md)**: Vollständige Referenz: `CODE-STRUCTURE-DETAIL.md`. [CODE-STRUCTURE-DETAIL](CODE-STRUCTURE-DETAIL.md).
- **[CODING-GUIDELINES.md](CODING-GUIDELINES.md)**: Verbindliche Leitlinien aus dem Core. [CODING-GUIDELINES-CODE-GUIDELINES-FULL](CODING-GUIDELINES-CODE-GUIDELINES-FULL.md).
- **[DOCUMENTATION-GUIDELINES.md](DOCUMENTATION-GUIDELINES.md)**: Vollständige Referenz: `DOCUMENTATION-GUIDELINES-DETAIL.md`. [DOCUMENTATION-GUIDELINES-DETAIL](DOCUMENTATION-GUIDELINES-DETAIL.md).
- **[DOMAIN-EXCEPTIONS.md](DOMAIN-EXCEPTIONS.md)**: Statt vieler einzelner Exception-Klassen: **eine Factory pro Domäne** mit statischen Methoden, die typisierte….
- **[EXTENDABILITY.md](EXTENDABILITY.md)**: Vollständige Referenz: `EXTENDABILITY-DETAIL.md`. [EXTENDABILITY-DETAIL](EXTENDABILITY-DETAIL.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20. Coding guidelines and ADRs come from the shopware/shopware repository.
