---
name: sw-document
description: Shopware documents: document generation, custom document types, ZUGFeRD, and the customer entity in checkout. Use when the request names a Shopware document type or invoice.
---

# Shopware documents and customers

Documents are generated from templates per order. A custom type needs a renderer and a config.

## Reference map

- **[CUSTOMER.md](CUSTOMER.md)**: Kunden sind `customer`-Entities.
- **[OVERVIEW.md](OVERVIEW.md)**: Dokumente werden über den `DocumentGenerator` aus einer Bestellung erzeugt.
- **[TYPE.md](TYPE.md)**: Neuer Belegtyp = `document_type`-Entity + ein Renderer + Twig-Template.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
