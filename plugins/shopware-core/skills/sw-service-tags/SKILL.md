---
name: sw-service-tags
description: >
  Service-Tags in Shopware 6: getaggte Services, Service-Locator, kernel.event_subscriber, shopware.entity.definition,
  Tagged-Iterator-Argumente und Compiler-Pass-Nutzung. Trigger: "service tag", "getaggte services", "tagged iterator",
  "service locator", "kernel.event_subscriber tag", "shopware.entity.definition", "compiler pass". Shopware 6.7.
---

# Shopware 6 — Service-Tags

Tags machen Services für Shopware/Symfony auffindbar. Wichtige Tags:

| Tag | Zweck |
|---|---|
| `kernel.event_subscriber` | EventSubscriber registrieren |
| `shopware.entity.definition` | EntityDefinition registrieren |
| `console.command` | CLI-Command |
| `shopware.scheduled.task` | ScheduledTask |
| `messenger.message_handler` | Message-Handler |

Mehrere getaggte Services sammeln (Strategie-Pattern) per Tagged-Iterator:

```xml
<service id="FfContentPlus\Registry">
    <argument type="tagged_iterator" tag="ff_content_plus.handler"/>
</service>
```

→ Service-Locator, Prioritäten, Compiler-Pass, alle relevanten Tags: [references/tags.md](references/tags.md)
