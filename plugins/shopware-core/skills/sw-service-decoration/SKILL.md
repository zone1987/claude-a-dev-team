---
name: sw-service-decoration
description: >
  Bestehende Shopware-6-Services per Decorator-Pattern anpassen (statt überschreiben) und WANN Decoration
  statt Event sinnvoll ist. Trigger: "Service dekorieren", "decoration pattern", "decorate service",
  "Service überschreiben", "decorates", "Core-Service anpassen", "inner service". Shopware 6.7.
---

# Shopware 6 — Service-Decoration

**Erst Events prüfen** (`sw-events-subscriber`). Decoration nur, wenn das Verhalten eines bestehenden Service
verändert werden muss und kein Event greift (z.B. Rückgabewert transformieren).

```xml
<service id="FfContentPlus\Service\MyDecorator"
         decorates="Shopware\Core\Some\OriginalService">
    <argument type="service" id="FfContentPlus\Service\MyDecorator.inner"/>
</service>
```

Der Decorator implementiert dasselbe Interface, hält den `.inner`-Service und delegiert. Niemals Core-Logik
duplizieren — nur ergänzen/transformieren. Optionale `decoration-priority` bei mehreren Decoratoren.

ADR-Leitlinie: Decoration ist die Ausnahme; das Event-System ist der Standard-Erweiterungsweg. Reihenfolge/Timing
über Event-Priorität lösen, bevor man dekoriert.
