---
name: sw-guidelines
description: Shopware coding guidelines: code structure, domain exceptions, extendability rules, ADR knowledge, documentation guidelines. Use when reviewing Shopware code against the platform's own conventions.
---

# Shopware coding guidelines

The platform's own rules for platform-shaped code. Domain exceptions and extendability are where most plugins diverge.

## Reference map

- **[ADR-KNOWLEDGE.md](ADR-KNOWLEDGE.md)**: The ADRs document binding architecture decisions of the core. [ADR-KNOWLEDGE-ADR-INDEX](ADR-KNOWLEDGE-ADR-INDEX.md).
- **[CODE-STRUCTURE.md](CODE-STRUCTURE.md)**: Complete reference: `CODE-STRUCTURE-DETAIL.md`. [CODE-STRUCTURE-DETAIL](CODE-STRUCTURE-DETAIL.md).
- **[CODING-GUIDELINES.md](CODING-GUIDELINES.md)**: Binding guidelines from the core. [CODING-GUIDELINES-CODE-GUIDELINES-FULL](CODING-GUIDELINES-CODE-GUIDELINES-FULL.md).
- **[DOCUMENTATION-GUIDELINES.md](DOCUMENTATION-GUIDELINES.md)**: Complete reference: `DOCUMENTATION-GUIDELINES-DETAIL.md`. [DOCUMENTATION-GUIDELINES-DETAIL](DOCUMENTATION-GUIDELINES-DETAIL.md).
- **[DOMAIN-EXCEPTIONS.md](DOMAIN-EXCEPTIONS.md)**: Instead of many individual exception classes: **one factory per domain** with static methods that return typed….
- **[EXTENDABILITY.md](EXTENDABILITY.md)**: Complete reference: `EXTENDABILITY-DETAIL.md`. [EXTENDABILITY-DETAIL](EXTENDABILITY-DETAIL.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20. Coding guidelines and ADRs come from the shopware/shopware repository.
