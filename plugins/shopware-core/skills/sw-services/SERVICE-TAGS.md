# Shopware 6 — Service Tags

Tags make services discoverable for Shopware/Symfony. Important tags:

| Tag | Purpose |
|---|---|
| `kernel.event_subscriber` | register an event subscriber |
| `shopware.entity.definition` | register an EntityDefinition |
| `console.command` | CLI command |
| `shopware.scheduled.task` | ScheduledTask |
| `messenger.message_handler` | message handler |

Collect several tagged services (strategy pattern) with a tagged iterator:

```xml
<service id="FfContentPlus\Registry">
    <argument type="tagged_iterator" tag="ff_content_plus.handler"/>
</service>
```

→ Service locator, priorities, compiler pass, all relevant tags: [SERVICE-TAGS-TAGS.md](SERVICE-TAGS-TAGS.md)
