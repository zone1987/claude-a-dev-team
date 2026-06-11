# JS SDK — Hooks & Lifecycle Events

## Hooks

`Hooks<Shop extends ShopInterface>` — synchronous-ordered pub/sub for lifecycle events. Supports multiple listeners per event type.

Accessed via `appServer.hooks`.

### Supported Events

| Event name | Listener signature | Fired in |
|------------|-------------------|---------|
| `onBeforeRegistrationEvent` | `(event: BeforeRegistrationEvent) => Promise<void>` | `registration.authorize()` |
| `onAuthorize` | `(event: ShopAuthorizeEvent<Shop>) => Promise<void>` | `registration.authorizeCallback()` |
| `onAppInstall` | `(event: AppInstallEvent<Shop>) => Promise<void>` | `registration.install()` |
| `onAppActivate` | `(event: AppActivateEvent<Shop>) => Promise<void>` | `registration.activate()` |
| `onAppDeactivate` | `(event: AppDeactivateEvent<Shop>) => Promise<void>` | `registration.deactivate()` |
| `onAppUpdate` | `(event: AppUpdateEvent<Shop>) => Promise<void>` | `registration.update()` |
| `onAppUninstall` | `(event: AppUninstallEvent<Shop>) => Promise<void>` | `registration.delete()` |

### Methods

```ts
hooks.on(event: keyof HookRegistry, cb: (event: ...) => Promise<void>): void
hooks.hasListeners(event: keyof HookRegistry): boolean
hooks.publish(event, ...args): Promise<void>  // calls all listeners sequentially
```

Multiple listeners per event are all called. Execution order = registration order.

## Usage Examples

### Block registrations from certain domains

```ts
appServer.hooks.on("onBeforeRegistrationEvent", async (event) => {
    if (!event.shopUrl.startsWith("https://")) {
        event.rejectRegistration("Only HTTPS shops are allowed");
    }
});
```

### Provision resources on install

```ts
appServer.hooks.on("onAppInstall", async (event) => {
    await provisionDatabase(event.shop.getShopId());
    console.log(`App installed on ${event.shop.getShopUrl()} (v${event.appVersion})`);
});
```

### Cleanup on uninstall

```ts
appServer.hooks.on("onAppUninstall", async (event) => {
    if (event.keepUserData === false) {
        await cleanupDatabase(event.shop.getShopId());
    }
    // keepUserData === true → user chose to keep data, do not purge
    // keepUserData === null → not set, treat as keep
});
```

### Reject authorization with custom check

```ts
appServer.hooks.on("onAuthorize", async (event) => {
    const shopId = event.shop.getShopId();
    const isAllowed = await checkLicense(shopId);
    if (!isAllowed) {
        event.rejectRegistration("License not valid for this shop");
    }
});
```

### In Hono via configureAppServer

```ts
configureAppServer(app, {
    appName: "MyApp",
    appSecret: "secret",
    shopRepository: repo,
    authorizeCallbackUrl: "https://app.example.com/app/register/confirm",
    setup(appServer) {
        appServer.hooks.on("onAppActivate", async (event) => {
            await sendWelcomeEmail(event.shop.getShopUrl());
        });
    },
});
```
