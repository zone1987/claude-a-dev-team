# Shopware 6 — Service Tags

Tags make services discoverable for Shopware/Symfony. Important tags:

**Without `autoconfigure`, every one of these is set by hand.** The standard registers
services explicitly (→ [DEPENDENCY-INJECTION.md](DEPENDENCY-INJECTION.md)), so Symfony
infers nothing from an implemented interface. Forgetting a tag is silent: the class exists,
the service is registered, and nothing ever calls it.

| Tag | Purpose |
|---|---|
| `kernel.event_subscriber` | register an event subscriber |
| `shopware.entity.definition` | register an EntityDefinition |
| `console.command` | CLI command |
| `shopware.scheduled.task` | ScheduledTask |
| `messenger.message_handler` | message handler |
| `kernel.reset` | reset per-request state — see [SERVICE-RESET.md](SERVICE-RESET.md) |
| `controller.service_arguments` | a storefront or API controller, so its actions get their arguments injected |
| `shopware.entity.extension` | an `EntityExtension` adding fields to a core entity |
| `shopware.cms.data_resolver` | a CMS element's `DataResolver` |
| `shopware.cart.processor` / `shopware.cart.collector` | cart calculation |
| `shopware.cart.line_item_factory_handler` | a line-item factory for a custom item type |
| `shopware.payment.method` | a payment handler |
| `document.renderer` | a document type's renderer |
| `shopware.rule.definition` | a rule for the rule builder |
| `shopware.mcp.tool` | a tool exposed to the Shopware MCP server |

Collect several tagged services (strategy pattern) with a tagged iterator:

```php
$services->set(Registry::class)
    ->args([tagged_iterator('ff_content_plus.handler')]);
```

→ Service locator, priorities, compiler pass, all relevant tags: [SERVICE-TAGS-TAGS.md](SERVICE-TAGS-TAGS.md)
