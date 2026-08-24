# Shopware 6 — Generating Documents

Documents (invoice, delivery note, credit note, cancellation) are generated from an order via the `DocumentGenerator`.

```php
$operation = new DocumentGenerateOperation($orderId, FileTypes::PDF, ['documentNumber' => '1001']);
$result = $this->documentGenerator->generate('invoice', [$orderId => $operation], $context)->getSuccess()->first();
```

Types: `invoice`, `delivery_note`, `credit_note`, `storno` (plus custom ones — see `TYPE.md`). Rendering via Twig templates
plus a file generator (PDF; HTML alternative since the ADR "offer html alternative"). **ZUGFeRD/e-invoicing** (XML inside the PDF) for
legally compliant invoices. Through the Admin API: call the Skill tool with `sw-admin`. For the merchant view, `sw-merchant-orders`.

## Contents

- [Configuring a document (legacy)](#configuring-a-document-legacy)
- [The config keys](#the-config-keys)

## Configuring a document (legacy)

A *document* in the sense of configuration lives in **`document_base_config`**. Do not confuse it
with the `document` table, which holds the generated documents of an order rather than their
configuration.

Adding one takes two kinds of row, written by a migration:

| Table | Purpose |
|---|---|
| `document_base_config` | the whole configuration and the document's name |
| `document_base_config_sales_channel` | one row per sales channel the document should be available in |

```php
// <plugin root>/src/Migration/Migration1616668698AddDocument.php
$documentTypeId = $this->getDocumentTypeId($connection);

$connection->insert('document_base_config', [
    'id' => $documentConfigId,
    'name' => 'custom',
    'filename_prefix' => 'custom_',
    'global' => 0,
    'document_type_id' => $documentTypeId,
    'config' => $this->getConfig(),
    'created_at' => (new \DateTime())->format(Defaults::STORAGE_DATE_TIME_FORMAT),
]);

$storefrontSalesChannelId = $this->getStorefrontSalesChannelId($connection);
if (!$storefrontSalesChannelId) {
    return;
}

$connection->insert('document_base_config_sales_channel', [
    'id' => Uuid::randomBytes(),
    'document_base_config_id' => $documentConfigId,
    'sales_channel_id' => $storefrontSalesChannelId,
    'document_type_id' => $documentTypeId,
    'created_at' => (new \DateTime())->format(Defaults::STORAGE_DATE_TIME_FORMAT),
]);
```

The migration fetches the storefront sales channel — through
`Uuid::fromHexToBytes(Defaults::SALES_CHANNEL_TYPE_STOREFRONT)`, returning `null` when there is none
— and the id of the document type it configures, in the guide's case the delivery note.

`name` and `filename_prefix` are required. **Set `global` to `1` to make the configuration a
fallback**, which is what a configuration for an entirely new document type usually wants.

## The config keys

`getConfig()` returns the JSON stored in the `config` column:

```php
$config = [
    'displayPrices' => false,
    'displayFooter' => true,
    'displayHeader' => true,
    'displayLineItems' => true,
    'displayLineItemPosition' => true,
    'displayPageCount' => true,
    'displayCompanyAddress' => true,
    'pageOrientation' => 'portrait',
    'pageSize' => 'a4',
    'itemsPerPage' => 10,
    'companyName' => 'Example company',
    'companyAddress' => 'Example company address',
    'companyEmail' => 'custom@example.org',
];

return json_encode($config);
```

Note the spelling here: this page writes `displayLineItemPosition`, while the document *type* guide's
default set writes `diplayLineItemPosition`. Both appear in the upstream documentation; check which
one the core reads for your version before relying on it.

Custom templates for a custom document are a matter of adding a document type — see `TYPE.md`.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/documents/legacy/add-custom-document.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/documents/legacy/add-custom-document.html),
Shopware 6.7, retrieved 2026-08-21.
