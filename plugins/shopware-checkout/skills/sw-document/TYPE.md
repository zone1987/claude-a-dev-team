# Shopware 6 — Eigener Dokumenttyp

Neuer Belegtyp = `document_type`-Entity + ein Renderer + Twig-Template.

```php
class FfPackingListRenderer extends AbstractDocumentRenderer
{
    public function supports(): string { return 'ff_packing_list'; }
    public function render(array $operations, Context $context, RendererConfig $rendererConfig): RendererResult
    { /* Order laden, Twig rendern, RenderedDocument zurückgeben */ }
}
```

Registrierung via `document.renderer`-Tag; `document_type`+`document_base_config` per Migration anlegen. Template unter
`Resources/views/documents/<type>.html.twig`. Erzeugung dann wie Standard über den `DocumentGenerator` (`sw-document`).
Nummernkreis für Belegnummern: `shopware-core` (`sw-number-range`).
