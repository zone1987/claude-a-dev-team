# Contao Content Security Policy (5.3+)

## Contents

- [Overview](#overview)
- [Accessing the CspHandler](#accessing-the-csphandler)
- [Adding sources (`addSource`)](#adding-sources-addsource)
- [Retrieving nonces (`getNonce`)](#retrieving-nonces-getnonce)
- [Adding hashes (`addHash`)](#adding-hashes-addhash)
- [WysiwygStyleProcessor](#wysiwygstyleprocessor)

## Overview

Contao 5.3 introduced CSP support for the front end. The `CspHandler` class integrates into the response context.

---

## Accessing the CspHandler

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

## Adding sources (`addSource`)

Allows external resources for a CSP directive:

**PHP:**
```php
$cspHandler->addSource('frame-src', 'https://www.youtube.com/embed/foobar123');
```

**Twig:**
```twig
{% do csp_source('frame-src', 'https://www.youtube.com/embed/foobar123') %}
```

**PHP template:**
```php
<?php $this->addCspSource('frame-src', 'https://...') ?>
```

---

## Retrieving nonces (`getNonce`)

Nonces enable secure inline scripts/styles without `'unsafe-inline'`:

**PHP:**
```php
$nonce = $cspHandler->getNonce('script-src');
```

**Twig:**
```twig
<script{{ attrs().setIfExists('nonce', csp_nonce('script-src')) }}>
```

**PHP template:**
```php
<script<?= $this->attr()->setIfExists('nonce', $this->nonce('script-src')) ?>>
```

---

## Adding hashes (`addHash`)

Allows specific inline styles/scripts by hash:

**PHP:**
```php
$cspHandler->addHash('style-src', 'display:none');
```

**Twig:**
```twig
{% do csp_hash('style-src', 'display:none') %}
```

**PHP template:**
```php
<div style="<?= $this->cspInlineStyle('display:none') ?>">
```

> **Note:** For browsers with CSP Level 3, `'unsafe-hashes'` must additionally be present in the directive's source list.

---

## WysiwygStyleProcessor

Automatically processes inline styles coming from the TinyMCE WYSIWYG editor.

**Configuring allowed styles:**
```yaml
# config/config.yaml (or bundle config)
contao:
    csp:
        allowed_inline_styles: ['color', 'font-size', 'text-align']
```

**Usage in a service:**
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

**Twig template:**
```twig
{{ text|csp_inline_styles|insert_tag|encode_email|raw }}
```

**PHP template:**
```php
<?= $this->cspInlineStyles($this->text) ?>
```

---

*Source: https://docs.contao.org/5.x/dev/framework/csp/*
