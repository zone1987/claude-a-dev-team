# Contao Security (5.x)

## Überblick

Contao nutzt Symfonys Security Component für Frontend- und Backend-Authentifizierung. Ein eigener Authenticator verarbeitet POST-Anfragen mit `username`, `password` und `FORM_SUBMIT=tl_login`. Der Request-Scope (`_scope`: `frontend` / `backend`) bestimmt, welche Firewall greift.

**Zugriffsstrategie:** „priority access decision strategy" – der erste Voter, der nicht abstain, entscheidet.

---

## Berechtigungen prüfen

### isGranted – Standard-Checks

```php
// Formular-Zugriff
$security->isGranted('contao_user.forms', 5);

// Feld-Level-Berechtigung
$security->isGranted('contao_user.alexf', 'tl_page::published');

// Ordner-Zugriff
$security->isGranted('contao_user.filemounts', '/files/foo/bar');

// Felder einer Tabelle bearbeiten
$security->isGranted('contao_user.can_edit_fields', 'tl_page');

// Seite bearbeiten
$security->isGranted('contao_user.can_edit_page', $pageModel);

// Mitgliedergruppe prüfen
$security->isGranted('contao_member.groups', $groupId);
```

### isGranted – Konstanten (empfohlen)

```php
use Contao\CoreBundle\Security\ContaoCorePermissions;
use Contao\NewsBundle\Security\ContaoNewsPermissions;

$security->isGranted(ContaoCorePermissions::USER_CAN_ACCESS_MODULE, 'news');
$security->isGranted(ContaoCorePermissions::USER_CAN_ACCESS_FIELD, 'hidden');
$security->isGranted(ContaoCorePermissions::USER_CAN_EDIT_FIELDS_OF_TABLE, 'tl_content');
$security->isGranted(ContaoNewsPermissions::USER_CAN_CREATE_ARCHIVES);
```

---

## Data Container – CRUD-Berechtigungen (ab 5.0)

### Action-Klassen

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

### AbstractDataContainerVoter (ab 5.0)

```php
// Zwei Pflichtmethoden:
protected function getTable(): string   // z.B. 'tl_example_archive'
protected function hasAccess(
    TokenInterface $token,
    CreateAction|ReadAction|UpdateAction|DeleteAction $action
): bool
```

**Tipp:** In `onload`-Listener Root-IDs setzen, damit Listenansichten keine Access-Denied-Exceptions werfen.

### Eigenen Voter – Beispiel: Admin-Einschränkung

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

### Eigenen Voter – Beispiel: Autor-Einschränkung (News)

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

## Custom Backend Access Rights (4 Schritte)

### 1. Permission registrieren

```php
// contao/config/config.php
$GLOBALS['TL_PERMISSIONS'][] = 'my_permissions';
```

### 2. User-DCA erweitern

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

### 3. User-Group-DCA erweitern (identisch, Palette: `default`)

```php
// contao/dca/tl_user_group.php
// … (wie tl_user, aber ->applyToPalette('default', 'tl_user_group'))
```

### 4. Im Controller prüfen

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

### Preview-Einstiegspunkt erkennen (`_preview`-Attribut)

```php
// PHP
if ($request->attributes->get('_preview')) { /* … */ }
```

```twig
{% if app.request.attributes._preview|default %}
    {# Im Preview-Einstiegspunkt #}
{% endif %}
```

### Aktiven Preview-Modus erkennen (`TokenChecker`)

```php
use Contao\CoreBundle\Security\Authentication\Token\TokenChecker;

if ($this->tokenChecker->isPreviewMode()) { /* … */ }
```

```twig
{# Ab Contao 5.3 #}
{% if contao.is_preview_mode %}
    {# Nur im Preview-Modus #}
{% endif %}
```

---

*Quellen:*
- *https://docs.contao.org/5.x/dev/framework/security/*
- *https://docs.contao.org/5.x/dev/framework/security/data-container/*
- *https://docs.contao.org/5.x/dev/framework/security/preview-mode/*
