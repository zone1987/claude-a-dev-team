# Contao Hooks – Newsletter

Hooks for newsletter subscriptions (subscribe and unsubscribe).

---

## `activateRecipient`

**Purpose:** Triggered when a new newsletter recipient is added (double opt-in confirmed).

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$email` | E-mail address of the recipient |
| 2 | `array` | `$recipientIds` | Recipient IDs for this e-mail address |
| 3 | `array` | `$channelIds` | Newsletter channel IDs that were subscribed to |

**Returns:** `void`

**Timing:** When a new newsletter recipient is added.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;

#[AsHook('activateRecipient')]
class ActivateRecipientListener
{
    public function __invoke(string $email, array $recipientIds, array $channelIds): void
    {
        // e.g. subscribe the recipient in an external Mailchimp system
    }
}
```

---

## `removeRecipient`

**Purpose:** Triggered when a newsletter recipient unsubscribes or is removed.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$email` | E-mail address of the recipient |
| 2 | `array` | `$channels` | Channels that were unsubscribed from |

**Returns:** `void`

**Timing:** When a newsletter subscriber is unsubscribed.

```php
#[AsHook('removeRecipient')]
class RemoveRecipientListener
{
    public function __invoke(string $email, array $channels): void
    {
        // e.g. mirror the unsubscribe in an external system
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
