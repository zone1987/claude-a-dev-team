# Shopware 6 — Storefront-Page

Eine Page bündelt alle Daten einer vollständigen Seite. Pattern: **Page-Struct** (Daten) + **PageLoader** (befüllt).

```php
class ExamplePage extends Page
{
    protected ExampleEntity $example;
    public function getExample(): ExampleEntity { return $this->example; }
    public function setExample(ExampleEntity $e): void { $this->example = $e; }
}
```

Die Page erweitert `Page` (enthält bereits Header/Footer/Meta via `GenericPageLoader`). Der PageLoader (`sw-page-loader`)
lädt zuerst die generische Page, ergänzt eigene Daten und feuert ein `ExamplePageLoadedEvent` (Erweiterbarkeit).
Teilbereiche (z.B. AJAX-Nachladung) als **Pagelet** (`sw-storefront-pagelet`).
