# Service Tags Reference

## Overview

Shopware uses Symfony service tags to register plugin extensions. This is a comprehensive reference of all important service tags.

## Core Tags

| Tag | Purpose |
|-----|---------|
| `shopware.event_subscriber` | Register event subscribers (auto with `autoconfigure`) |
| `shopware.entity.definition` | Register DAL entity definitions |
| `shopware.entity.extension` | Register entity extensions |
| `shopware.composite_search.definition` | Register entity for global search |

## Cart & Checkout

| Tag | Purpose | Priority |
|-----|---------|----------|
| `shopware.cart.processor` | Cart line item processor | Higher = earlier |
| `shopware.cart.collector` | Cart data collector | - |
| `shopware.cart.validator` | Cart validator | - |
| `shopware.tax.provider` | Tax calculation provider | - |

## CMS

| Tag | Purpose |
|-----|---------|
| `shopware.cms.data_resolver` | CMS element data resolver |

## DAL

| Tag | Purpose |
|-----|---------|
| `shopware.entity.definition` | Entity definition registration |
| `shopware.entity.extension` | Entity extension |

## Flow Builder

| Tag | Purpose |
|-----|---------|
| `shopware.flow.action` | Flow builder action |

## Payment

| Tag | Purpose |
|-----|---------|
| `shopware.payment.handler` | Payment handler |

## Rules

| Tag | Purpose |
|-----|---------|
| `shopware.rule.definition` | Custom rule definition |

## SEO

| Tag | Purpose |
|-----|---------|
| `shopware.seo_url.route` | SEO URL route template |

## Scheduled Tasks

| Tag | Purpose |
|-----|---------|
| `shopware.scheduled.task` | Scheduled task registration |

## Elasticsearch

| Tag | Purpose |
|-----|---------|
| `shopware.es.definition` | Elasticsearch entity definition |

## Storefront

| Tag | Purpose |
|-----|---------|
| `shopware.storefront.controller` | Storefront controller (auto) |

## Store API

| Tag | Purpose |
|-----|---------|
| `shopware.store_api.route` | Store API route (auto with `#[Route]`) |

## Twig

| Tag | Purpose |
|-----|---------|
| `twig.extension` | Twig extension |
| `twig.runtime` | Twig runtime extension |

## Console Commands

| Tag | Purpose |
|-----|---------|
| `console.command` | CLI command (auto with `AsCommand`) |

## Message Queue

| Tag | Purpose |
|-----|---------|
| `messenger.message_handler` | Message handler (auto with `AsMessageHandler`) |

## Symfony Standard Tags

These Symfony tags also work in Shopware:

| Tag | Purpose |
|-----|---------|
| `kernel.event_subscriber` | Event subscriber |
| `kernel.event_listener` | Event listener |
| `controller.service_arguments` | Controller argument injection |
| `validator.constraint_validator` | Custom validation constraint |
| `serializer.normalizer` | Custom serializer normalizer |

## Example: Multiple Tags

A service can have multiple tags:

```xml
<service id="FfContentPlus\Core\Content\FfContentPlusItemDefinition">
    <tag name="shopware.entity.definition" entity="ff_content_plus_item"/>
</service>

<service id="FfContentPlus\Core\Checkout\Cart\DiscountProcessor">
    <tag name="shopware.cart.processor" priority="4000"/>
</service>

<service id="FfContentPlus\Core\Content\Seo\FfContentPlusSeoUrlRoute">
    <tag name="shopware.seo_url.route"/>
</service>
```

## Autoconfigure

With `autoconfigure="true"` in services.xml, many tags are applied automatically based on implemented interfaces:

- `EventSubscriberInterface` → `kernel.event_subscriber`
- `#[AsCommand]` → `console.command`
- `#[AsMessageHandler]` → `messenger.message_handler`
- `CartProcessorInterface` → `shopware.cart.processor`
- `CartDataCollectorInterface` → `shopware.cart.collector`
- `CartValidatorInterface` → `shopware.cart.validator`
- `Rule` subclass → `shopware.rule.definition`
