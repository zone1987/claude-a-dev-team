# Contao Content Security Policy (5.3+)

## Überblick

Contao 5.3 führte CSP-Support für das Frontend ein. Die `CspHandler`-Klasse integriert sich in den Response Context.

---

## CspHandler zugreifen

```php
use Contao\CoreBundle\Routing\ResponseContext\Csp\CspHandler;
use Contao\CoreBundle\Routing\ResponseContext\ResponseContextAccessor;

class ExampleService
{
    public function __construct(
        private readonly ResponseContextAccessor $responseContextAccessor
    ) {}

    public function __invoke(): void
    {
        $responseContext = $this->responseContextAccessor->getResponseContext();

        if ($responseContext?->has(CspHandler::class)) {
            $cspHandler = $responseContext->get(CspHandler::class);
        }
    }
}
```

---

## Quellen hinzufügen (`addSource`)

Erlaubt externe Ressourcen für eine CSP-Direktive:

**PHP:**
```php
$cspHandler->addSource('frame-src', 'https://www.youtube.com/embed/foobar123');
```

**Twig:**
```twig
{% do csp_source('frame-src', 'https://www.youtube.com/embed/foobar123') %}
```

**PHP-Template:**
```php
<?php $this->addCspSource('frame-src', 'https://...') ?>
```

---

## Nonces abrufen (`getNonce`)

Nonces ermöglichen sichere Inline-Skripte/-Styles ohne `'unsafe-inline'`:

**PHP:**
```php
$nonce = $cspHandler->getNonce('script-src');
```

**Twig:**
```twig
<script{{ attrs().setIfExists('nonce', csp_nonce('script-src')) }}>
```

**PHP-Template:**
```php
<script<?= $this->attr()->setIfExists('nonce', $this->nonce('script-src')) ?>>
```

---

## Hashes hinzufügen (`addHash`)

Erlaubt spezifische Inline-Styles/-Scripts per Hash:

**PHP:**
```php
$cspHandler->addHash('style-src', 'display:none');
```

**Twig:**
```twig
{% do csp_hash('style-src', 'display:none') %}
```

**PHP-Template:**
```php
<div style="<?= $this->cspInlineStyle('display:none') ?>">
```

> **Hinweis:** Für Browser mit CSP Level 3 muss zusätzlich `'unsafe-hashes'` in der Direktiv-Quellenliste stehen.

---

## WysiwygStyleProcessor

Verarbeitet automatisch Inline-Styles aus dem TinyMCE WYSIWYG-Editor.

**Konfiguration erlaubter Styles:**
```yaml
# config/config.yaml (oder Bundle-Config)
contao:
    csp:
        allowed_inline_styles: ['color', 'font-size', 'text-align']
```

**Nutzung im Service:**
```php
use Contao\CoreBundle\Csp\WysiwygStyleProcessor;

class ExampleService
{
    public function __construct(
        private readonly WysiwygStyleProcessor $wysiwygProcessor,
    ) {}

    public function processInlineStyles(string $html, CspHandler $csp): void
    {
        if (!$styles = $this->wysiwygProcessor->extractStyles($html)) {
            return;
        }
        foreach ($styles as $style) {
            $csp->addHash('style-src', $style);
        }
    }
}
```

**Twig-Template:**
```twig
{{ text|csp_inline_styles|insert_tag|encode_email|raw }}
```

**PHP-Template:**
```php
<?= $this->cspInlineStyles($this->text) ?>
```

---

*Quelle: https://docs.contao.org/5.x/dev/framework/csp/*
