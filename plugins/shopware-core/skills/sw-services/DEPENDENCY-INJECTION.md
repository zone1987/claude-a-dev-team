# Shopware 6 — Dependency Injection

Register services in `src/Resources/config/services.xml` (Symfony DI). Shopware loads them automatically
when the plugin class uses the default `build()` convention or the path matches `getServicesFilePath()`.

```xml
<service id="FfContentPlus\Service\MyService">
    <argument type="service" id="Doctrine\DBAL\Connection"/>
    <argument type="service" id="product.repository"/>
</service>
```

DAL repositories are named `{entity}.repository` (e.g. `product.repository`). Prefer constructor property promotion.
Tagged services / service locator: `sw-service-tags`. Changing existing services: `sw-service-decoration`.

→ Autowiring, public/private, compiler pass, examples: [DEPENDENCY-INJECTION-DI.md](DEPENDENCY-INJECTION-DI.md)
→ Empty skeleton: [examples/services.xml](examples/services.xml)
