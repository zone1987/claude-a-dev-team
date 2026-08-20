---
name: sw-document
description: Shopware documents: document generation, custom document types, ZUGFeRD, and the customer entity in checkout. Use when the request names a Shopware document type or invoice.
---

# Shopware documents and customers

Documents are generated from templates per order. A custom type needs a renderer and a config.

## Reference map

- **[CUSTOMER.md](CUSTOMER.md)**: Customers are `customer` entities.
- **[OVERVIEW.md](OVERVIEW.md)**: Documents are generated from an order via the `DocumentGenerator`.
- **[TYPE.md](TYPE.md)**: A new document type = a `document_type` entity + a renderer + a Twig template.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
