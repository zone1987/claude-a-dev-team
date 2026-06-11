# CMS Elements & Blocks

## Overview

Plugins can add custom CMS elements and blocks to the Shopping Experiences content management system.

## CMS Element (Backend Data Resolver)

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Core\Content\Cms\Element;

use Shopware\Core\Content\Cms\Aggregate\CmsSlot\CmsSlotEntity;
use Shopware\Core\Content\Cms\DataResolver\CriteriaCollection;
use Shopware\Core\Content\Cms\DataResolver\Element\AbstractCmsElementResolver;
use Shopware\Core\Content\Cms\DataResolver\Element\ElementDataCollection;
use Shopware\Core\Content\Cms\DataResolver\ResolverContext\ResolverContext;
use Shopware\Core\Framework\Log\Package;

#[Package('custom-plugins')]
class ContentPlusElementResolver extends AbstractCmsElementResolver
{
    public function getType(): string
    {
        return 'ff-content-plus-element';
    }

    public function collect(CmsSlotEntity $slot, ResolverContext $resolverContext): ?CriteriaCollection
    {
        // Optional: Define criteria for data to collect
        return null;
    }

    public function enrich(CmsSlotEntity $slot, ResolverContext $resolverContext, ElementDataCollection $result): void
    {
        // Enrich slot with resolved data
        $config = $slot->getFieldConfig();
        $slot->setData($myData);
    }
}
```

## Service Registration

```xml
<service id="FfContentPlus\Core\Content\Cms\Element\ContentPlusElementResolver">
    <tag name="shopware.cms.data_resolver"/>
</service>
```

## Admin Component (CMS Element)

Register the CMS element in the administration:

```javascript
// src/Resources/app/administration/src/module/sw-cms/elements/ff-content-plus-element/index.js
Shopware.Service('cmsService').registerCmsElement({
    name: 'ff-content-plus-element',
    label: 'ff-content-plus.elements.contentPlus.label',
    component: 'sw-cms-el-ff-content-plus',
    configComponent: 'sw-cms-el-config-ff-content-plus',
    previewComponent: 'sw-cms-el-preview-ff-content-plus',
    defaultConfig: {
        title: { source: 'static', value: '' },
        content: { source: 'static', value: '' },
    },
});
```

## CMS Block Registration

```javascript
Shopware.Service('cmsService').registerCmsBlock({
    name: 'ff-content-plus-block',
    label: 'ff-content-plus.blocks.contentPlus.label',
    category: 'text',
    component: 'sw-cms-block-ff-content-plus',
    previewComponent: 'sw-cms-preview-ff-content-plus',
    defaultConfig: {
        marginBottom: '20px',
        marginTop: '20px',
        marginLeft: '20px',
        marginRight: '20px',
        sizingMode: 'boxed',
    },
    slots: {
        content: 'ff-content-plus-element',
    },
});
```

## Storefront Template

```twig
{# src/Resources/views/storefront/element/cms-element-ff-content-plus.html.twig #}
{% block element_ff_content_plus %}
    <div class="cms-element-ff-content-plus">
        {% if element.config.title.value %}
            <h2>{{ element.config.title.value }}</h2>
        {% endif %}
        <div class="content">{{ element.config.content.value|raw }}</div>
    </div>
{% endblock %}
```
