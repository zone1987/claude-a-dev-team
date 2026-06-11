# Storefront

## Overview

The storefront covers Twig templates, controllers, JavaScript plugins, SCSS styling, and snippet translations for the customer-facing shop.

## Storefront Controller

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Storefront\Controller;

use Shopware\Core\Framework\Log\Package;
use Shopware\Core\PlatformRequest;
use Shopware\Core\System\SalesChannel\SalesChannelContext;
use Shopware\Storefront\Controller\StorefrontController;
use Shopware\Storefront\Framework\Routing\StorefrontRouteScope;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

/**
 * @class ContentController
 * @package FfContentPlus\Storefront\Controller
 */
#[Route(defaults: [PlatformRequest::ATTRIBUTE_ROUTE_SCOPE => [StorefrontRouteScope::ID]])]
#[Package('custom-plugins')]
class ContentController extends StorefrontController
{
    /**
     * @param Request $request
     * @param SalesChannelContext $context
     * @return Response
     */
    #[Route(
        path: '/content-plus/items',
        name: 'frontend.content-plus.items',
        methods: ['GET'],
    )]
    public function listItems(Request $request, SalesChannelContext $context): Response
    {
        // Load data...
        return $this->renderStorefront(
            '@FfContentPlus/storefront/page/content-plus/index.html.twig',
            ['items' => $items]
        );
    }
}
```

## Route Registration (routes.xml)

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<routes xmlns="http://symfony.com/schema/routing"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://symfony.com/schema/routing https://symfony.com/schema/routing/routing-1.0.xsd">

    <import resource="../../Storefront/Controller/" type="attribute"/>
</routes>
```

Place at: `src/Resources/config/routes.xml`

## Twig Templates

### Extending Existing Templates

```twig
{# src/Resources/views/storefront/page/product-detail/index.html.twig #}
{% sw_extends '@Storefront/storefront/page/product-detail/index.html.twig' %}

{% block page_product_detail_buy %}
    {# Add content before the block #}
    {% if page.product.customFields.ff_content_plus_badge_text %}
        <div class="ff-content-plus-badge">
            {{ page.product.translated.customFields.ff_content_plus_badge_text }}
        </div>
    {% endif %}

    {# Render original block content #}
    {{ parent() }}
{% endblock %}
```

### Custom Template

```twig
{# src/Resources/views/storefront/page/content-plus/index.html.twig #}
{% sw_extends '@Storefront/storefront/base.html.twig' %}

{% block base_content %}
    <div class="content-plus-page">
        <h1>{{ "ContentPlus.page.title"|trans }}</h1>

        {% for item in items %}
            <div class="content-plus-item">
                <h2>{{ item.translated.name }}</h2>
                <p>{{ item.translated.description|raw }}</p>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

### Key Rules

- Use `{% sw_extends %}` (not `{% extends %}`) for Shopware template inheritance
- Use `{{ parent() }}` to include the original block content
- Access translated fields via `entity.translated.fieldName`
- Template path convention: `@PluginName/storefront/...`

## JavaScript Plugins

### Plugin Class

```javascript
// src/Resources/app/storefront/src/js/content-plus-plugin.js
import Plugin from 'src/plugin-system/plugin.class';

export default class ContentPlusPlugin extends Plugin {
    static options = {
        animationSpeed: 300,
        activeClass: 'is-active',
    };

    init() {
        this._registerEvents();
    }

    _registerEvents() {
        this.el.addEventListener('click', this._onClick.bind(this));
    }

    _onClick(event) {
        event.preventDefault();
        this.el.classList.toggle(this.options.activeClass);
    }
}
```

### Registration (main.js)

```javascript
// src/Resources/app/storefront/src/main.js
import ContentPlusPlugin from './js/content-plus-plugin';

const PluginManager = window.PluginManager;
PluginManager.register('ContentPlusPlugin', ContentPlusPlugin, '[data-content-plus]');
```

### Usage in Twig

```twig
<div data-content-plus="true" data-content-plus-options='{"animationSpeed": 500}'>
    Click me
</div>
```

## SCSS Styling

```scss
// src/Resources/app/storefront/src/scss/base.scss
.ff-content-plus-badge {
    display: inline-block;
    padding: 4px 8px;
    background-color: var(--bs-primary);
    color: #fff;
    font-size: 0.75rem;
    border-radius: 3px;
}

.content-plus-item {
    margin-bottom: 1.5rem;
    padding: 1rem;
    border: 1px solid var(--bs-border-color);
    border-radius: var(--bs-border-radius);
}
```

## Snippet Translations

See the main SKILL.md for snippet file structure. Snippets are used in Twig:

```twig
{{ "ContentPlus.page.title"|trans }}
{{ "ContentPlus.button.submit"|trans({'%name%': item.name}) }}
```

## Page/Pagelet Subscribers

Extend existing pages with additional data:

```php
use Shopware\Storefront\Page\Product\ProductPageLoadedEvent;

class ProductPageSubscriber implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [
            ProductPageLoadedEvent::class => 'onProductPageLoaded',
        ];
    }

    public function onProductPageLoaded(ProductPageLoadedEvent $event): void
    {
        $page = $event->getPage();
        $product = $page->getProduct();

        // Add custom data via extensions
        $page->addExtension('ffContentPlus', new ArrayStruct([
            'relatedItems' => $this->loadRelatedItems($product->getId()),
        ]));
    }
}
```

Access in Twig:
```twig
{% set ffData = page.extensions.ffContentPlus %}
{% for item in ffData.relatedItems %}
    ...
{% endfor %}
```

## Cookie Consent

Register cookies for GDPR compliance:

```php
use Shopware\Storefront\Framework\Cookie\CookieProviderInterface;

class CookieProvider implements CookieProviderInterface
{
    public function __construct(
        private readonly CookieProviderInterface $original,
    ) {}

    public function getCookieGroups(): array
    {
        $cookies = $this->original->getCookieGroups();

        foreach ($cookies as &$group) {
            if ($group['snippet_name'] === 'cookie.groupStatistical') {
                $group['entries'][] = [
                    'snippet_name' => 'ContentPlus.cookie.name',
                    'cookie' => 'ff-content-plus-tracking',
                ];
            }
        }

        return $cookies;
    }
}
```

## Building Assets

```bash
# With Shopware CLI
ddev exec shopware-cli project storefront-build --only-extensions FfContentPlus
ddev exec shopware-cli project storefront-watch --only-extensions FfContentPlus

# Without Shopware CLI
ddev exec bin/build-storefront.sh
ddev exec bin/watch-storefront.sh
```
