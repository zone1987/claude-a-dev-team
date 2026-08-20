# Shopware 6 — Extension Points

In addition to events, Shopware offers **extension points**: defined places where the core dispatches an `Extension`
whose `result` a plugin can replace or enrich (more than merely "reacting afterwards").

```php
// react to an extension point (pre/post)
public static function getSubscribedEvents(): array
{
    return [ MyCoreExtension::class . '.pre' => 'beforeCompute' ];
}
```

- **Event** = notifies; the listener can cause side effects or manipulate the object passed along.
- **Extension point** = wraps a core operation; the plugin can supply or change the result (ideal for "replace behaviour").

Custom extension points for plugins: derive from `Extension` and wrap the service call via the `ExtensionDispatcher`.
If a classic event suffices, prefer it (`sw-events-subscriber`).
