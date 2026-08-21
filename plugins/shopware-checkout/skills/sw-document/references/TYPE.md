# Shopware 6 — Custom Document Type

A new document type = a `document_type` entity + a renderer + a Twig template.

```php
class FfPackingListRenderer extends AbstractDocumentRenderer
{
    public function supports(): string { return 'ff_packing_list'; }
    public function render(array $operations, Context $context, RendererConfig $rendererConfig): RendererResult
    { /* load order, render Twig, return RenderedDocument */ }
}
```

Register via the `document.renderer` tag; create `document_type` and `document_base_config` in a migration. Place the template at
`Resources/views/documents/<type>.html.twig`. Generation then works like the standard types through the `DocumentGenerator` (`sw-document`).
Number range for document numbers: `shopware-core` (`sw-number-range`).
