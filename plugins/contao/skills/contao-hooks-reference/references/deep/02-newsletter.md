# Contao Hooks – Newsletter

Hooks für Newsletter-Abonnements (An- und Abmeldung).

---

## `activateRecipient`

**Zweck:** Wird ausgelöst, wenn ein neuer Newsletter-Empfänger hinzugefügt wird (Double-Opt-In bestätigt).

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$email` | E-Mail-Adresse des Empfängers |
| 2 | `array` | `$recipientIds` | Empfänger-IDs zu dieser E-Mail-Adresse |
| 3 | `array` | `$channelIds` | Newsletter-Kanal-IDs, für die abonniert wurde |

**Rückgabe:** `void`

**Zeitpunkt:** Beim Hinzufügen eines neuen Newsletter-Empfängers.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;

#[AsHook('activateRecipient')]
class ActivateRecipientListener
{
    public function __invoke(string $email, array $recipientIds, array $channelIds): void
    {
        // z.B. Empfänger in externem Mailchimp-System anmelden
    }
}
```

---

## `removeRecipient`

**Zweck:** Wird ausgelöst, wenn ein Newsletter-Empfänger abgemeldet/entfernt wird.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$email` | E-Mail-Adresse des Empfängers |
| 2 | `array` | `$channels` | Kanäle, von denen abgemeldet wurde |

**Rückgabe:** `void`

**Zeitpunkt:** Wenn ein Newsletter-Abonnent abgemeldet wird.

```php
#[AsHook('removeRecipient')]
class RemoveRecipientListener
{
    public function __invoke(string $email, array $channels): void
    {
        // z.B. Abmeldung in externem System spiegeln
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
