---
name: sw-document
description: >
  Dokumente in Shopware 6 erzeugen (Rechnung, Lieferschein, Storno, Gutschrift): DocumentGenerator.generate,
  DocumentGenerateOperation, Rendering, Speicherung, ZUGFeRD/E-Rechnung. Trigger: "Dokument erzeugen", "DocumentGenerator",
  "Rechnung generieren", "Lieferschein", "DocumentGenerateOperation", "ZUGFeRD", "document api". Shopware 6.7.
---

# Shopware 6 — Dokumente erzeugen

Dokumente (Invoice, Delivery Note, Credit Note, Storno) werden über den `DocumentGenerator` aus einer Bestellung erzeugt.

```php
$operation = new DocumentGenerateOperation($orderId, FileTypes::PDF, ['documentNumber' => '1001']);
$result = $this->documentGenerator->generate('invoice', [$orderId => $operation], $context)->getSuccess()->first();
```

Typen: `invoice`, `delivery_note`, `credit_note`, `storno` (+ eigene, `sw-document-type`). Rendering über Twig-Templates
+ FileGenerator (PDF; HTML-Alternative seit ADR „offer html alternative"). **ZUGFeRD/E-Rechnung** (XML im PDF) für
gesetzeskonforme Rechnungen. Über Admin-API: `shopware-api` (`sw-admin-api-actions`). Betreibersicht: `shopware-merchant`
(`sw-merchant-orders-documents`).
