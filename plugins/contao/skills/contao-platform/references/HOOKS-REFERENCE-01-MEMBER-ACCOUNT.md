# Contao Hooks – Member / Account

Hooks around front end member registration, activation, passwords and data maintenance.

---

## Contents

- [`activateAccount`](#activateaccount)
- [`closeAccount`](#closeaccount)
- [`createNewUser`](#createnewuser)
- [`setNewPassword`](#setnewpassword)
- [`updatePersonalData`](#updatepersonaldata)

## `activateAccount`

**Purpose:** Triggered when a new front end member account is activated.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\MemberModel` | `$member` | The activated member |
| 2 | `\Contao\Module` | `$module` | The registration module |

**Returns:** `void`

**Timing:** After a successful account activation through a registration module.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\MemberModel;
use Contao\Module;

#[AsHook('activateAccount')]
class ActivateAccountListener
{
    public function __invoke(MemberModel $member, Module $module): void
    {
        // e.g. send a welcome e-mail, notify an external system
    }
}
```

---

## `closeAccount`

**Purpose:** Triggered when a member closes their account (deactivates or deletes it).

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `int` | `$userId` | ID of the member |
| 2 | `string` | `$mode` | `close_deactivate` or `close_delete` |
| 3 | `\Contao\Module` | `$module` | The front end module |

**Returns:** `void`

**Timing:** When a member initiates the account closure from the front end.

```php
#[AsHook('closeAccount')]
class CloseAccountListener
{
    public function __invoke(int $userId, string $mode, Module $module): void
    {
        if ('close_delete' === $mode) {
            // Clean up the member's external data
        }
    }
}
```

---

## `createNewUser`

**Purpose:** Triggered when a new front end member registers.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `int` | `$userId` | ID of the new member |
| 2 | `array` | `$userData` | Submitted registration form data (without the ID) |
| 3 | `\Contao\Module` | `$module` | The front end module |

**Returns:** `void`

**Timing:** After a successful registration.

```php
#[AsHook('createNewUser')]
class CreateNewUserListener
{
    public function __invoke(int $userId, array $userData, Module $module): void
    {
        // e.g. create the user in an external database
    }
}
```

---

## `setNewPassword`

**Purpose:** Triggered after a member has set a new password (via the change password or password reset module).

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `object` | `$member` | Front end member (`\Contao\Database\Result` or `\Contao\MemberModel`) |
| 2 | `string` | `$password` | The new encrypted password |
| 3 | `\Contao\Module\|null` | `$module` | The calling module (null in a back end context) |

**Returns:** `void`

**Timing:** After the password has been set successfully.

```php
#[AsHook('setNewPassword')]
class SetNewPasswordListener
{
    public function __invoke($member, string $password, ?Module $module): void
    {
        // e.g. write a password change log entry
    }
}
```

---

## `updatePersonalData`

**Purpose:** Triggered after a member has updated their personal data through the personal data module. The member object and the database are already updated.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\FrontendUser` | `$member` | The logged-in front end member |
| 2 | `array` | `$data` | The submitted form data |
| 3 | `\Contao\Module` | `$module` | The `ModulePersonalData` module |

**Returns:** `void`

**Timing:** After the updated member data has been persisted to the database.

```php
#[AsHook('updatePersonalData')]
class UpdatePersonalDataListener
{
    public function __invoke(FrontendUser $member, array $data, Module $module): void
    {
        // e.g. synchronise the data with an external CRM
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
