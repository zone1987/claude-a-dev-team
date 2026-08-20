---
title: App Lifecycle Events
impact: HIGH
impactDescription: Understanding lifecycle events is essential for app server state management
tags: lifecycle, install, activate, deactivate, delete, events
---

## App Lifecycle Events

Shopware notifies the app server about lifecycle changes. The app server must handle these to manage shop registrations and clean up resources.

### Lifecycle Flow

1. **Install** — `app:install` triggers registration handshake (GET to registrationUrl)
2. **Activate** — `app:activate` or `--activate` flag, POST to `/app/activate`
3. **Deactivate** — `app:deactivate`, POST to `/app/deactivate`
4. **Delete** — `app:uninstall`, POST to `/app/delete`

### Handling with JS SDK (Hono)

The `configureAppServer()` helper auto-registers lifecycle endpoints:

- `POST /app/register` — Initial registration
- `POST /app/register/confirm` — Confirmation callback
- `POST /app/activate` — Shop activated
- `POST /app/deactivate` — Shop deactivated
- `POST /app/delete` — Shop deleted (clean up stored credentials)

### Handling with PHP SDK

```php
use Shopware\App\SDK\AppLifecycle;

$lifecycle = new AppLifecycle($registrationService, $shopRepository, $confirmationUrl);

// In registration endpoint
$lifecycle->register($psrRequest);

// In confirmation endpoint
$lifecycle->confirm($psrRequest);

// In activate endpoint
$lifecycle->activate($psrRequest);

// In deactivate endpoint
$lifecycle->deactivate($psrRequest);

// In delete endpoint
$lifecycle->delete($psrRequest);
```

### PHP SDK PSR-14 Events

| Event | When |
|-------|------|
| `BeforeRegistrationCompletedEvent` | Before storing shop credentials |
| `RegistrationCompletedEvent` | After successful registration |
| `BeforeShopActivateEvent` | Before activation |
| `ShopActivatedEvent` | After activation |
| `BeforeShopDeactivatedEvent` | Before deactivation |
| `ShopDeactivatedEvent` | After deactivation |
| `BeforeShopDeletionEvent` | Before deletion |
| `ShopDeletedEvent` | After deletion |

### Important Notes

- Always clean up stored shop credentials on delete
- The setup section in manifest.xml is required for lifecycle events
- All lifecycle requests are signed with HMAC
- Timeout for all requests is 5 seconds
