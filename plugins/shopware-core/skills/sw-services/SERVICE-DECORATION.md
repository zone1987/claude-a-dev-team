# Shopware 6 — Service Decoration

**Check events first** (`sw-events-subscriber`). Decorate only when the behaviour of an existing service
has to change and no event fits (e.g. transforming a return value).

```xml
<service id="FfContentPlus\Service\MyDecorator"
         decorates="Shopware\Core\Some\OriginalService">
    <argument type="service" id="FfContentPlus\Service\MyDecorator.inner"/>
</service>
```

The decorator implements the same interface, holds the `.inner` service and delegates. Never duplicate core
logic — only extend or transform it. Optional `decoration-priority` when several decorators apply.

ADR guidance: decoration is the exception; the event system is the default extension path. Solve ordering/timing
through event priority before reaching for a decorator.
