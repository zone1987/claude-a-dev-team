# Contao Hooks – Member / Account

Hooks rund um Frontend-Benutzer-Registrierung, -Aktivierung, Passwort und Datenpflege.

---

## `activateAccount`

**Zweck:** Wird ausgelöst, wenn ein neues Frontend-Benutzerkonto aktiviert wird.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\MemberModel` | `$member` | Das aktivierte Mitglied |
| 2 | `\Contao\Module` | `$module` | Das Registrierungs-Modul |

**Rückgabe:** `void`

**Zeitpunkt:** Nach erfolgreicher Konto-Aktivierung über ein Registrierungs-Modul.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\MemberModel;
use Contao\Module;

#[AsHook('activateAccount')]
class ActivateAccountListener
{
    public function __invoke(MemberModel $member, Module $module): void
    {
        // z.B. Willkommens-E-Mail senden, externes System benachrichtigen
    }
}
```

---

## `closeAccount`

**Zweck:** Wird ausgelöst, wenn ein Benutzer sein Konto schließt (deaktiviert oder löscht).

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `int` | `$userId` | ID des Benutzers |
| 2 | `string` | `$mode` | `close_deactivate` oder `close_delete` |
| 3 | `\Contao\Module` | `$module` | Das Frontend-Modul |

**Rückgabe:** `void`

**Zeitpunkt:** Wenn ein Benutzer die Konto-Schließung über das Frontend initiiert.

```php
#[AsHook('closeAccount')]
class CloseAccountListener
{
    public function __invoke(int $userId, string $mode, Module $module): void
    {
        if ('close_delete' === $mode) {
            // Externe Daten des Nutzers bereinigen
        }
    }
}
```

---

## `createNewUser`

**Zweck:** Wird ausgelöst, wenn sich ein neuer Frontend-Benutzer registriert.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `int` | `$userId` | ID des neuen Benutzers |
| 2 | `array` | `$userData` | Übermittelte Registrierungsformulardaten (ohne ID) |
| 3 | `\Contao\Module` | `$module` | Das Frontend-Modul |

**Rückgabe:** `void`

**Zeitpunkt:** Nach erfolgreicher Registrierung.

```php
#[AsHook('createNewUser')]
class CreateNewUserListener
{
    public function __invoke(int $userId, array $userData, Module $module): void
    {
        // z.B. Benutzer in externer Datenbank anlegen
    }
}
```

---

## `setNewPassword`

**Zweck:** Wird ausgelöst, nachdem ein Benutzer ein neues Passwort gesetzt hat (über Passwort-Ändern- oder Passwort-Reset-Modul).

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `object` | `$member` | Frontend-Benutzer (`\Contao\Database\Result` oder `\Contao\MemberModel`) |
| 2 | `string` | `$password` | Das neue verschlüsselte Passwort |
| 3 | `\Contao\Module\|null` | `$module` | Das aufrufende Modul (null im Backend-Kontext) |

**Rückgabe:** `void`

**Zeitpunkt:** Nach erfolgreichem Passwort-Setzen.

```php
#[AsHook('setNewPassword')]
class SetNewPasswordListener
{
    public function __invoke($member, string $password, ?Module $module): void
    {
        // z.B. Passwort-Änderungs-Log schreiben
    }
}
```

---

## `updatePersonalData`

**Zweck:** Wird ausgelöst, nachdem ein Mitglied seine persönlichen Daten über das Personal-Data-Modul aktualisiert hat. Benutzer-Objekt und Datenbank sind bereits aktualisiert.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\FrontendUser` | `$member` | Der angemeldete Frontend-Benutzer |
| 2 | `array` | `$data` | Die übermittelten Formulardaten |
| 3 | `\Contao\Module` | `$module` | Das `ModulePersonalData`-Modul |

**Rückgabe:** `void`

**Zeitpunkt:** Nach der Datenbankpersistenz der aktualisierten Benutzerdaten.

```php
#[AsHook('updatePersonalData')]
class UpdatePersonalDataListener
{
    public function __invoke(FrontendUser $member, array $data, Module $module): void
    {
        // z.B. Daten mit externem CRM synchronisieren
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
