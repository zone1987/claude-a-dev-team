# Shopware 6 — Generating Documents

Documents (invoice, delivery note, credit note, cancellation) are generated from an order via the `DocumentGenerator`.

```php
$operation = new DocumentGenerateOperation($orderId, FileTypes::PDF, ['documentNumber' => '1001']);
$result = $this->documentGenerator->generate('invoice', [$orderId => $operation], $context)->getSuccess()->first();
```

Types: `invoice`, `delivery_note`, `credit_note`, `storno` (plus custom ones, `sw-document-type`). Rendering via Twig templates
plus a file generator (PDF; HTML alternative since the ADR "offer html alternative"). **ZUGFeRD/e-invoicing** (XML inside the PDF) for
legally compliant invoices. Through the Admin API: `shopware-api` (`sw-admin-api-actions`). Merchant view: `shopware-merchant`
(`sw-merchant-orders-documents`).
