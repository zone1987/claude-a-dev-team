# Shopware 6 — Dependency Injection

Services werden in `src/Resources/config/services.xml` registriert (Symfony DI). Shopware lädt sie automatisch,
wenn die Plugin-Klasse die Standard-`build()`-Konvention nutzt bzw. der Pfad in `getServicesFilePath()` liegt.

```xml
<service id="FfContentPlus\Service\MyService">
    <argument type="service" id="Doctrine\DBAL\Connection"/>
    <argument type="service" id="product.repository"/>
</service>
```

DAL-Repositories heißen `{entity}.repository` (z.B. `product.repository`). Constructor Property Promotion bevorzugen.
Tagged Services / Service-Locator: `sw-service-tags`. Bestehende Services anpassen: `sw-service-decoration`.

→ Autowiring, public/private, Compiler-Pass, Beispiele: [DEPENDENCY-INJECTION-DI.md](DEPENDENCY-INJECTION-DI.md)
→ Leeres Gerüst: [examples/services.xml](examples/services.xml)
