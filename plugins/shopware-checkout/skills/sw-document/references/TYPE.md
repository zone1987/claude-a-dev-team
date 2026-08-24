# Shopware 6 — custom document types

Two document systems exist in 6.7, and which one applies decides everything else:

| System | State in 6.7 | Use it when |
|---|---|---|
| **legacy** | the working default; deprecated, removed in 6.9 | building for 6.7 today |
| **v2** | experimental, behind the `DOCUMENT_GENERATION_REWORK` feature flag; becomes the default in 6.8 | preparing for 6.8, accepting API churn |

## Contents

- [Legacy: the database entries](#legacy-the-database-entries)
- [Legacy: the renderer](#legacy-the-renderer)
- [Legacy: the number range](#legacy-the-number-range)
- [Legacy: service registration and template](#legacy-service-registration-and-template)
- [v2: type, render data and provider](#v2-type-render-data-and-provider)
- [v2: registration, template and database](#v2-registration-template-and-database)
- [v2: format renderers](#v2-format-renderers)
- [v2: adding data to an existing document](#v2-adding-data-to-an-existing-document)
- [v2: overriding a document template](#v2-overriding-a-document-template)

## Legacy: the database entries

A type needs rows in three tables, added by a plugin migration: `document_type`,
`document_type_translation` (one per language) and `document_base_config`.

The migration splits into three private methods — `addTranslations()` and
`addDocumentBaseConfig()` are called from `update()` after the type row itself is inserted, and
`$documentBaseConfigId` is generated with `Uuid::randomBytes()`:

```php
// <plugin root>/src/Migration/Migration1616677952AddDocumentType.php
$connection->insert('document_type', [
    'id' => $documentTypeId,
    'technical_name' => self::TYPE,
    'created_at' => (new \DateTime())->format(Defaults::STORAGE_DATE_TIME_FORMAT),
]);
```

**Translations** go through `Shopware\Core\Migration\Traits\ImportTranslationsTrait`, which supplies
`importTranslation()`. It takes the translation table plus a
`Shopware\Core\Migration\Traits\Translations` instance, whose two constructor arguments are the
German array and the English array, each with its id column:

```php
$documentTypeTranslations = new Translations(
    ['document_type_id' => $documentTypeId, 'name' => $germanName],
    ['document_type_id' => $documentTypeId, 'name' => $englishName],
);
$this->importTranslation('document_type_translation', $documentTypeTranslations, $connection);
```

**The base configuration** holds the defaults an editor later overrides in the administration. The
full set the guide uses:

```php
$defaultConfig = [
    'displayPrices' => true,
    'displayFooter' => true,
    'displayHeader' => true,
    'displayLineItems' => true,
    'diplayLineItemPosition' => true,     // spelled this way in the core
    'displayPageCount' => true,
    'displayCompanyAddress' => true,
    'pageOrientation' => 'portrait',
    'pageSize' => 'a4',
    'itemsPerPage' => 10,
    'companyName' => 'Example Company',
    'taxNumber' => '',
    'vatId' => '',
    'taxOffice' => '',
    'bankName' => '',
    'bankIban' => '',
    'bankBic' => '',
    'placeOfJurisdiction' => '',
    'placeOfFulfillment' => '',
    'executiveDirector' => '',
    'companyAddress' => '',
    'referencedDocumentType' => self::TYPE,
];
```

It is inserted into `document_base_config` with `global => 1` and a `filename_prefix`, then linked to
the sales channels through `document_base_config_sales_channel`.

After installing the plugin the type appears in the administration — but it does not work yet, since
every type needs an `AbstractDocumentRenderer`.

## Legacy: the renderer

Implement `Shopware\Core\Checkout\Document\Renderer\AbstractDocumentRenderer`, conventionally under
`<plugin root>/src/Core/Checkout/Document/Renderer`. It forces three methods:

| Method | Contract |
|---|---|
| `getDecorated` | returns the decorated service, or throws `DecorationPatternException` |
| `supports` | returns the type's technical name — `'example'` for a type named example |
| `render` | returns a `RendererResult` holding a `RenderedDocument` per `orderId` |

`render()` takes three parameters: `$operations`, an array of `DocumentGenerateOperation` objects
carrying the order ids; `$context`; and `$rendererConfig`, a `DocumentRendererConfig` for additional
configuration.

```php
public function render(array $operations, Context $context, DocumentRendererConfig $rendererConfig): RendererResult
{
    $ids = \array_map(fn (DocumentGenerateOperation $operation) => $operation->getOrderId(), $operations);
    if (empty($ids)) {
        return new RendererResult();
    }

    $result = new RendererResult();
    $criteria = new Criteria($ids);
    $criteria->addAssociation('language');
    $criteria->addAssociation('language.locale');

    $orders = $this->orderRepository->search($criteria, $context)->getEntities();
    foreach ($orders as $order) {
        $orderId = $order->getId();
        try {
            $operation = $operations[$orderId] ?? null;
            if ($operation === null) {
                continue;
            }

            $config = clone $this->documentConfigLoader->load(self::TYPE, $order->getSalesChannelId(), $context);
            $config->merge($operation->getConfig());

            $number = $config->getDocumentNumber() ?: $this->getNumber($context, $order, $operation);
            $now = (new \DateTime())->format(Defaults::STORAGE_DATE_TIME_FORMAT);

            $config->merge([
                'documentDate' => $operation->getConfig()['documentDate'] ?? $now,
                'documentNumber' => $number,
                'custom' => ['invoiceNumber' => $number],
            ]);

            // a document uploaded manually
            if ($operation->isStatic()) {
                $doc = new RenderedDocument($number, $config->buildName(), $operation->getFileType(), $config->jsonSerialize());
                $result->addSuccess($orderId, $doc);
                continue;
            }

            $doc = new RenderedDocument($number, $config->buildName(), $operation->getFileType(), $config->jsonSerialize());

            // the recommended path: let the registry produce the content
            $doc->setTemplate(self::DEFAULT_TEMPLATE);
            $doc->setOrder($order);
            $doc->setContext($context);
            $doc->setContent($this->fileRendererRegistry->render($doc));

            // alternatively set the content by hand, e.g. XML or CSV:
            // $doc->setContent('Id;Name;…');

            $result->addSuccess($orderId, $doc);
        } catch (\Throwable $exception) {
            $result->addError($orderId, $exception);
        }
    }

    return $result;
}
```

The document number comes from the number range named `'document_' . self::TYPE`:

```php
private function getNumber(Context $context, OrderEntity $order, DocumentGenerateOperation $operation): string
{
    return $this->numberRangeValueGenerator->getValue(
        'document_' . self::TYPE, $context, $order->getSalesChannelId(), $operation->isPreview(),
    );
}
```

**`DocumentFileRendererRegistry`** is the central registry of file renderers keyed by extension
(`.pdf`, `.html`), delegating to the implementation for that type. Use it rather than producing PDF
bytes yourself; set the content by hand only for a format it does not cover.

An error is caught per order and added with `addError()`, so one failing order does not abort the
batch.

## Legacy: the number range

Without a number range no number is generated, so the document cannot be produced. It takes four
kinds of row, again in a plugin migration:

| Table | What it holds |
|---|---|
| `number_range_type` | the type itself, with a technical name |
| `number_range` | the configured range, referencing that type |
| `number_range_sales_channel` | assigns a sales channel to the range |
| `number_range_translation`, `number_range_type_translation` | one row per language |

The number range migration splits the same way: `insertNumberRange()` writes the three rows and
`insertTranslations()` the language rows, both called from `update()`.

```php
// <plugin root>/src/Migration/Migration1616974646AddDocumentNumberRange.php
$connection->insert('number_range_type', [
    'id' => $numberRangeTypeId,
    'global' => 0,
    'technical_name' => 'document_example',
    'created_at' => (new \DateTime())->format(Defaults::STORAGE_DATE_TIME_FORMAT),
]);

$connection->insert('number_range', [
    'id' => $numberRangeId,
    'type_id' => $numberRangeTypeId,
    'global' => 0,
    'pattern' => '{n}',
    'start' => 10000,
    'created_at' => (new \DateTime())->format(Defaults::STORAGE_DATE_TIME_FORMAT),
]);
```

The technical name must match what the renderer asks for — `'document_' . self::TYPE`.

The sales channel assignment needs the storefront channel's id. A private
`getStorefrontSalesChannelId()` finds it by channel type and returns `null` when there is none:

```php
private function getStorefrontSalesChannelId(Connection $connection): ?string
{
    $salesChannelId = $connection->fetchOne($sql, [
        'typeId' => Uuid::fromHexToBytes(Defaults::SALES_CHANNEL_TYPE_STOREFRONT),
    ]);

    return $salesChannelId ?: null;
}
```

Where `$storefrontSalesChannelId` is null, return early rather than failing the migration. Otherwise
insert `number_range_sales_channel` with `Uuid::randomBytes()` as its id, plus the range id, the
channel id and the type id.

Both translation tables take the same `Translations` shape as the document type —
`$numberRangeTranslations` keyed by `number_range_id`, `$numberRangeTypeTranslations` by
`number_range_type_id`. **The type's label column is `type_name`, not `name`.**

## Legacy: service registration and template

```php
// <plugin root>/src/Resources/config/services.php
$services->set(ExampleDocumentRenderer::class)
    ->args([
        service('order.repository'),
        service(DocumentConfigLoader::class),
        service(NumberRangeValueGeneratorInterface::class),
        service(DocumentFileRendererRegistry::class),
    ])
    ->tag('document.renderer');
```

The tag `document.renderer` is what makes the renderer discoverable. The template goes to
`<plugin root>/src/Resources/views/documents/example_document.html.twig` and extends the base:

```twig
{% sw_extends '@Framework/documents/base.html.twig' %}
```

## v2: type, render data and provider

Experimental in 6.7, the default in 6.8. Four parts: the type, a render-data DTO, a data provider,
and a template.

A **document type** declares its technical name and the formats it can be rendered in
(`<plugin root>/src/Core/Checkout/Document/ExampleDocumentType.php`).

A **render data DTO** carries the values the template uses. **Public properties on the DTO end up on
the template's `config` variable** — a `noteText` property renders as `config.noteText`.

A **data provider** builds that DTO for an order. `enrichOrderCriteria()` adds the associations the
provider needs, so they are loaded before `provideRenderingData()` runs:

```php
public function enrichOrderCriteria(Criteria $criteria): void
{
    $criteria->addAssociation('lineItems');
}

public function provideRenderingData(ProviderInput $input, Context $context): AbstractRenderData
{
    return new ExampleRenderData(
        noteText: 'Thank you for your order!',
    );
}
```

## v2: registration, template and database

```php
// <plugin root>/src/Resources/config/services.php
$services->set(ExampleDocumentType::class)->tag('shopware.document_v2.type');
$services->set(ExampleDocumentDataProvider::class)->tag('shopware.document_v2.provider');
```

The HTML renderer resolves `@Framework/documents/<technical_name>.html.twig`:

```twig
{% sw_extends '@Framework/documents/base.html.twig' %}

{% block document_headline %}
    <h1>Example document {{ documentNumber }}</h1>
    <p>{{ config.noteText }}</p>
{% endblock %}
```

A type offering the `zugferd_xml` format additionally needs an XML template at
`<plugin root>/src/Resources/views/documents/zugferd/example_document.xml.twig`, resolved the same
way.

**Two database rows are still required**, exactly as in the legacy system: a `document_type` row
whose `technical_name` matches the type — the `document` table has a foreign key on it — and a number
range of type `document_<technical_name>`. The migration code is identical to the legacy one above.

## v2: format renderers

A renderer produces exactly **one** format. `getDependencies()` names the formats that must render
first, so their results are in `RenderState` when yours runs.

```php
// <plugin root>/src/Core/Checkout/Document/TextRenderer.php
// depends on 'html' and derives plain text from the rendered HTML
$html = $state->require('html');

return new RenderResult(
    $this->getFormat(),
    strip_tags($html->content),
    sprintf('%s_txt', $input->documentNumber),
    $this->getFileExtension(),
    'text/plain',
);
```

```php
$container->services()
    ->set(TextRenderer::class)
    ->tag('shopware.document_v2.renderer');
```

**A format only becomes selectable once a document type lists it in `getSupportedFormats()`.**

### Overriding a built-in renderer

The registry keeps the **first** renderer registered per format, ordered by tag priority. Register
for the same format string with a higher priority to replace a built-in one:

```php
$container->services()
    ->set(CustomPdfRenderer::class)
    ->tag('shopware.document_v2.renderer', ['priority' => 100]);
```

This replaces the legacy system's `getDecorated()` decoration chains.

## v2: adding data to an existing document

**Any number of providers can support the same document type.** Each stores its render data DTO under
its own key, and the DTO's public fields are flattened onto the template's `config` variable.

**A key already used by another provider for the same type makes generation throw.**

```php
// <plugin root>/src/Core/Checkout/Document/InvoiceNoteDataProvider.php
$order = $input->order;

return new InvoiceNoteRenderData(
    invoiceNote: sprintf('Please quote order %s in all correspondence.', $order->getOrderNumber()),
);
```

```php
$container->services()
    ->set(InvoiceNoteDataProvider::class)
    ->tag('shopware.document_v2.provider');
```

## v2: overriding a document template

Templates live under `@Framework/documents/` and are overridden with `sw_extends`, the same mechanism
as everywhere else in Shopware. The invoice template exposes the blocks of `base.html.twig` and the
`includes/` partials, so overriding `invoice.html.twig` reaches all of them.

```twig
{# <plugin root>/src/Resources/views/documents/invoice.html.twig #}
{% sw_extends '@Framework/documents/invoice.html.twig' %}

{% block document_footer %}
    {{ parent() }}
    {{ config.invoiceNote }}
{% endblock %}
```

**The same templates render for every format that needs HTML**, so a change to `invoice.html.twig`
reaches the HTML, the PDF and the ZUGFeRD-embedded PDF alike.

## Related

Generation itself runs through `DocumentGenerator`; see `OVERVIEW.md`. For number ranges, call the
Skill tool with `sw-platform`.

## Source

- [legacy/add-custom-document-type.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/documents/legacy/add-custom-document-type.html) — the legacy system
- [v2/add-a-document-type.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/documents/v2/add-a-document-type.html) — Document System v2
- [v2/add-a-format-renderer.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/documents/v2/add-a-format-renderer.html) — format renderers
- [v2/customize-document-data-and-templates.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/documents/v2/customize-document-data-and-templates.html) — providers and templates

Shopware 6.7, retrieved 2026-08-21.
