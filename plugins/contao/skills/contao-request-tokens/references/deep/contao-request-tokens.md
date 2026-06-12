# Contao Request Tokens / CSRF-Schutz (5.x)

## Überblick

Contao implementiert CSRF-Schutz via **Double Submit Cookie Technik**.

### Schutzumfang

| Geschützt | Nicht geschützt |
|-----------|----------------|
| Alle `POST`-Requests aus Contao-Routes (Frontend/Backend) | Ajax-Requests mit `X-Requested-With: XMLHttpRequest` |
| Nur wenn Authentifizierung per Cookies/Basic Auth persistiert | Unauthentifizierte Nutzer (kein Schutz nötig) |

---

## Schutz deaktivieren

Routen können Token-Prüfung via `_token_check => false` deaktivieren (Sicherheitsrisiko – alternative Absicherung erforderlich).

---

## Token generieren und validieren

```php
use Symfony\Component\Security\Csrf\CsrfToken;
use Symfony\Component\Security\Csrf\CsrfTokenManagerInterface;

class ExampleService
{
    public function __construct(
        private readonly CsrfTokenManagerInterface $csrfTokenManager,
        private readonly string $csrfTokenName    // Parameter: %contao.csrf_token_name%
    ) {}

    public function generateToken(): string
    {
        return $this->csrfTokenManager
            ->getToken($this->csrfTokenName)
            ->getValue();
    }

    public function checkToken(string $tokenValue): bool
    {
        $token = new CsrfToken($this->csrfTokenName, $tokenValue);
        return $this->csrfTokenManager->isTokenValid($token);
    }
}
```

### ContaoCsrfTokenManager (vereinfacht)

```php
// Default-Token-Wert direkt abrufen
$contaoCsrfTokenManager->getDefaultTokenValue();
```

---

## Token in Templates ausgeben

**PHP-Template:**
```php
<?= $this->requestToken ?>
```

**Twig-Template:**
```twig
{{ contao.request_token }}
```

---

## Symfony Forms Integration

### In Contao-Controllern (AbstractFrontendModuleController, AbstractContentElementController, AbstractController)

```php
$formBuilder = $this->createFormBuilder(
    options: $this->getCsrfFormOptions()
);
```

### In eigenen Services

```php
use Contao\CoreBundle\Csrf\ContaoCsrfTokenManager;
use Symfony\Component\DependencyInjection\Attribute\Autowire;
use Symfony\Component\Form\FormFactoryInterface;

class MyCustomService
{
    public function __construct(
        private readonly FormFactoryInterface $formFactory,
        private readonly ContaoCsrfTokenManager $csrfTokenManager,
        #[Autowire(param: 'contao.csrf_token_name')]
        private readonly string $csrfTokenName,
    ) {}

    public function getFormBuilder()
    {
        return $this->formFactory->createBuilder(options: [
            'csrf_field_name'    => 'REQUEST_TOKEN',
            'csrf_token_manager' => $this->csrfTokenManager,
            'csrf_token_id'      => $this->csrfTokenName,
        ]);
    }
}
```

---

## Sicherheitshinweise

> **XSS-Risiko:** Symfony-Forms für Backend-Records oder Legacy-Frontend-Templates kodieren Eingaben nicht automatisch. Eingaben sorgfältig behandeln um XSS zu verhindern.

---

*Quelle: https://docs.contao.org/5.x/dev/framework/request-tokens/*
