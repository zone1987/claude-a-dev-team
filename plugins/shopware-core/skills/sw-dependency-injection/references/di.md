# Dependency Injection

## Overview

Shopware uses Symfony's DI container. Plugin services are registered in `src/Resources/config/services.xml`.

## services.xml Structure

```xml
<?xml version="1.0" ?>
<container xmlns="http://symfony.com/schema/dic/services"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://symfony.com/schema/dic/services https://symfony.com/schema/dic/services/services-1.0.xsd">

    <services>
        <!-- Enable autowiring and autoconfiguration for all services in this file -->
        <defaults autowire="true" autoconfigure="true"/>

        <!-- Register a service -->
        <service id="FfContentPlus\Service\MyService"/>

        <!-- Service with explicit arguments -->
        <service id="FfContentPlus\Subscriber\MySubscriber">
            <argument type="service" id="product.repository"/>
            <argument type="service" id="Shopware\Core\System\SystemConfig\SystemConfigService"/>
            <tag name="kernel.event_subscriber"/>
        </service>

        <!-- Service decoration -->
        <service id="FfContentPlus\Service\DecoratedService"
                 decorates="Shopware\Core\Content\Product\SalesChannel\SalesChannelProductEntity">
            <argument type="service" id=".inner"/>
        </service>
    </services>
</container>
```

## Autowiring (Recommended)

With `<defaults autowire="true" autoconfigure="true"/>`, most services only need the `<service>` tag:

```xml
<service id="FfContentPlus\Service\MyService"/>
```

Autowiring resolves constructor arguments automatically by type. Autoconfigure automatically applies tags based on implemented interfaces (e.g., `EventSubscriberInterface` → `kernel.event_subscriber`).

## When Manual Wiring is Needed

You must explicitly wire arguments when:
- Injecting **repository services** (string IDs like `product.repository`)
- Injecting **tagged services** or collections
- Injecting **parameters** (`%parameter_name%`)
- Injecting **scalar values**

```xml
<service id="FfContentPlus\Service\ProductService">
    <argument type="service" id="product.repository"/>
    <argument>%ff_content_plus.api_key%</argument>
</service>
```

## Service Decoration

Decorate existing Shopware services to extend/modify behavior:

```xml
<service id="FfContentPlus\Core\DecoratedProductRoute"
         decorates="Shopware\Core\Content\Product\SalesChannel\Detail\ProductDetailRoute">
    <argument type="service" id="FfContentPlus\Core\DecoratedProductRoute.inner"/>
</service>
```

The decorated service class:

```php
class DecoratedProductRoute extends AbstractProductDetailRoute
{
    public function __construct(
        private readonly AbstractProductDetailRoute $decorated,
    ) {}

    public function getDecorated(): AbstractProductDetailRoute
    {
        return $this->decorated;
    }

    public function load(string $productId, Request $request, SalesChannelContext $context, Criteria $criteria): ProductDetailRouteResponse
    {
        // Custom logic before/after
        return $this->decorated->load($productId, $request, $context, $criteria);
    }
}
```

## Common Service Tags

| Tag | Purpose |
|-----|---------|
| `kernel.event_subscriber` | Event subscriber (auto with `autoconfigure`) |
| `shopware.entity.definition` | DAL entity definition |
| `shopware.composite_search.definition` | Search definition |
| `shopware.scheduled.task` | Scheduled task |
| `shopware.cms.data_resolver` | CMS element data resolver |
| `shopware.payment.method.sync` | Synchronous payment handler |
| `shopware.payment.method.async` | Asynchronous payment handler |
| `shopware.payment.method.prepared` | Prepared payment handler |
| `shopware.payment.method.refund` | Refund handler |
| `shopware.payment.method.recurring` | Recurring payment handler |
| `shopware.flow.action` | Flow builder action |
| `shopware.rule.definition` | Custom rule |
| `console.command` | CLI command (auto with `autoconfigure`) |
| `shopware.entity.extension` | Entity extension |
| `shopware.cart.processor` | Cart processor |
| `shopware.cart.collector` | Cart data collector |
| `shopware.cart.validator` | Cart validator |

## Compiler Passes

Register in the plugin's `build()` method:

```php
public function build(ContainerBuilder $container): void
{
    parent::build($container);
    $container->addCompilerPass(new MyCompilerPass());
}
```

## Tagged Service Collections

Inject all services with a specific tag:

```xml
<service id="FfContentPlus\Service\HandlerRegistry">
    <argument type="tagged_iterator" tag="ff.content_plus.handler"/>
</service>
```

## Repository Services

Shopware DAL repositories follow the pattern `{entity_name}.repository`:

```xml
<argument type="service" id="product.repository"/>
<argument type="service" id="category.repository"/>
<argument type="service" id="order.repository"/>
<argument type="service" id="customer.repository"/>
<argument type="service" id="media.repository"/>
```

## Service ID Convention

Plugin service IDs use the FQCN (fully qualified class name) as the ID, which is the Symfony default with autowiring.
