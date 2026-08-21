# Contao Security (5.x)

## Contents

- [Overview](#overview)
- [Checking permissions](#checking-permissions)
- [Data Container – CRUD permissions (5.0 and later)](#data-container-crud-permissions-50-and-later)
- [Custom Backend Access Rights (4 steps)](#custom-backend-access-rights-4-steps)
- [Preview Mode](#preview-mode)

## Overview

Contao uses Symfony's Security component for front end and back end authentication. A dedicated authenticator processes POST requests carrying `username`, `password` and `FORM_SUBMIT=tl_login`. The request scope (`_scope`: `frontend` / `backend`) determines which firewall applies.

**Access strategy:** "priority access decision strategy" – the first voter that does not abstain decides.

---

## Checking permissions

### isGranted – standard checks

```php
// Form access
$security->isGranted('contao_user.forms', 5);

// Field-level permission
$security->isGranted('contao_user.alexf', 'tl_page::published');

// Folder access
$security->isGranted('contao_user.filemounts', '/files/foo/bar');

// Editing the fields of a table
$security->isGranted('contao_user.can_edit_fields', 'tl_page');

// Editing a page
$security->isGranted('contao_user.can_edit_page', $pageModel);

// Checking a member group
$security->isGranted('contao_member.groups', $groupId);
```

### isGranted – constants (recommended)

```php
use Contao\CoreBundle\Security\ContaoCorePermissions;
use Contao\NewsBundle\Security\ContaoNewsPermissions;

$security->isGranted(ContaoCorePermissions::USER_CAN_ACCESS_MODULE, 'news');
$security->isGranted(ContaoCorePermissions::USER_CAN_ACCESS_FIELD, 'hidden');
$security->isGranted(ContaoCorePermissions::USER_CAN_EDIT_FIELDS_OF_TABLE, 'tl_content');
$security->isGranted(ContaoNewsPermissions::USER_CAN_CREATE_ARCHIVES);
```

---

## Data Container – CRUD permissions (5.0 and later)

### Action classes

```php
use Contao\CoreBundle\Security\DataContainer\CreateAction;
use Contao\CoreBundle\Security\DataContainer\DeleteAction;
use Contao\CoreBundle\Security\DataContainer\ReadAction;
use Contao\CoreBundle\Security\DataContainer\UpdateAction;

$security->isGranted('contao_dc.tl_foobar', new CreateAction('tl_foobar', $record));
$security->isGranted('contao_dc.tl_foobar', new DeleteAction('tl_foobar', $record));
$security->isGranted('contao_dc.tl_foobar', new ReadAction('tl_foobar', $record));
$security->isGranted('contao_dc.tl_foobar', new UpdateAction('tl_foobar', $record));
```

### AbstractDataContainerVoter (5.0 and later)

```php
// Two mandatory methods:
protected function getTable(): string   // e.g. 'tl_example_archive'
protected function hasAccess(
    TokenInterface $token,
    CreateAction|ReadAction|UpdateAction|DeleteAction $action
): bool
```

**Tip:** Set root IDs in an `onload` listener so that list views do not throw access-denied exceptions.

### A custom voter – example: admin restriction

```php
namespace App\Security\Voter;

use Contao\BackendUser;
use Contao\CoreBundle\Security\ContaoCorePermissions;
use Symfony\Component\Security\Core\Authentication\Token\TokenInterface;
use Symfony\Component\Security\Core\Authorization\Voter\Voter;

class AdminMaintenanceAccessVoter extends Voter
{
    protected function supports(string $attribute, $subject): bool
    {
        return 'maintenance' === $subject
            && $attribute === ContaoCorePermissions::USER_CAN_ACCESS_MODULE;
    }

    public function vote(TokenInterface $token, mixed $subject, array $attributes): int
    {
        if (!($user = $token->getUser()) instanceof BackendUser || !$user->isAdmin) {
            return Voter::ACCESS_ABSTAIN;
        }
        return parent::vote($token, $subject, $attributes);
    }

    protected function voteOnAttribute(string $attribute, mixed $subject, TokenInterface $token): bool
    {
        return 1 === (int) $token->getUser()->id;
    }
}
```

### A custom voter – example: author restriction (news)

```php
namespace App\Security\Voter;

use Contao\BackendUser;
use Contao\CoreBundle\Security\ContaoCorePermissions;
use Contao\CoreBundle\Security\DataContainer\DeleteAction;
use Contao\CoreBundle\Security\DataContainer\UpdateAction;
use Contao\NewsModel;
use Symfony\Component\Security\Core\Authentication\Token\TokenInterface;
use Symfony\Component\Security\Core\Authorization\Voter\Voter;

class NewsAccessVoter extends Voter
{
    protected function supports(string $attribute, $subject): bool
    {
        if (!$subject instanceof DeleteAction && !$subject instanceof UpdateAction) {
            return false;
        }
        if (ContaoCorePermissions::DC_PREFIX.'tl_news' === $attribute) return true;
        if (ContaoCorePermissions::DC_PREFIX.'tl_content' === $attribute) {
            return 'tl_news' === $subject->getCurrent()['ptable'];
        }
        return false;
    }

    protected function voteOnAttribute(string $attribute, mixed $subject, TokenInterface $token): bool
    {
        $user = $token->getUser();
        if ($user->isAdmin) return true;

        $record   = $subject->getCurrent();
        $authorId = 'tl_news' === $subject->getDataSource()
            ? $record['author']
            : NewsModel::findById($record['pid'])->author;

        return (int) $user->id === (int) $authorId;
    }
}
```

---

## Custom Backend Access Rights (4 steps)

### 1. Register the permission

```php
// contao/config/config.php
$GLOBALS['TL_PERMISSIONS'][] = 'my_permissions';
```

### 2. Extend the user DCA

```php
// contao/dca/tl_user.php
use Contao\CoreBundle\DataContainer\PaletteManipulator;

$GLOBALS['TL_DCA']['tl_user']['fields']['my_permissions'] = [
    'exclude'   => true,
    'inputType' => 'checkbox',
    'eval'      => ['multiple' => true],
    'options'   => [
        'first_permission'  => 'First permission',
        'second_permission' => 'Second permission',
    ],
    'sql' => ['type' => 'blob', 'notnull' => false],
];

PaletteManipulator::create()
    ->addLegend('my_legend', null)
    ->addField('my_permissions', 'my_legend', PaletteManipulator::POSITION_APPEND)
    ->applyToPalette('extend', 'tl_user')
    ->applyToPalette('custom', 'tl_user');
```

### 3. Extend the user group DCA (identical, palette: `default`)

```php
// contao/dca/tl_user_group.php
// … (same as tl_user, but ->applyToPalette('default', 'tl_user_group'))
```

### 4. Check in the controller

```php
#[Route('/contao/my-backend-route', defaults: ['_scope' => 'backend'])]
class BackendController
{
    public function __invoke(): Response
    {
        if (!$this->auth->isGranted('ROLE_ADMIN')
            && !$this->auth->isGranted('contao_user.my_permissions', 'first_permission')) {
            throw new AccessDeniedException('...');
        }
        return new Response($this->twig->render('my_backend_route.html.twig', []));
    }
}
```

---

## Preview Mode

### Detecting the preview entry point (the `_preview` attribute)

```php
// PHP
if ($request->attributes->get('_preview')) { /* … */ }
```

```twig
{% if app.request.attributes._preview|default %}
    {# Inside the preview entry point #}
{% endif %}
```

### Detecting active preview mode (`TokenChecker`)

```php
use Contao\CoreBundle\Security\Authentication\Token\TokenChecker;

if ($this->tokenChecker->isPreviewMode()) { /* … */ }
```

```twig
{# Contao 5.3 and later #}
{% if contao.is_preview_mode %}
    {# Only in preview mode #}
{% endif %}
```

---

*Sources:*
- *https://docs.contao.org/5.x/dev/framework/security/*
- *https://docs.contao.org/5.x/dev/framework/security/data-container/*
- *https://docs.contao.org/5.x/dev/framework/security/preview-mode/*
