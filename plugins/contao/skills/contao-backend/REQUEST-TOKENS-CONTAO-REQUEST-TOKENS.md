# Contao Request Tokens / CSRF protection (5.x)

## Contents

- [Overview](#overview)
- [Disabling protection](#disabling-protection)
- [Generating and validating tokens](#generating-and-validating-tokens)
- [Outputting tokens in templates](#outputting-tokens-in-templates)
- [Symfony Forms integration](#symfony-forms-integration)
- [Security notes](#security-notes)

## Overview

Contao implements CSRF protection via the **double submit cookie technique**.

### Scope of protection

| Protected | Not protected |
|-----------|----------------|
| All `POST` requests from Contao routes (frontend/backend) | Ajax requests with `X-Requested-With: XMLHttpRequest` |
| Only if authentication is persisted via cookies/basic auth | Unauthenticated users (no protection needed) |

---

## Disabling protection

Routes can disable the token check via `_token_check => false` (a security risk – alternative safeguards are required).

---

## Generating and validating tokens

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

### ContaoCsrfTokenManager (simplified)

```php
// Retrieve the default token value directly
$contaoCsrfTokenManager->getDefaultTokenValue();
```

---

## Outputting tokens in templates

**PHP template:**
```php
<?= $this->requestToken ?>
```

**Twig template:**
```twig
{{ contao.request_token }}
```

---

## Symfony Forms integration

### In Contao controllers (AbstractFrontendModuleController, AbstractContentElementController, AbstractController)

```php
$formBuilder = $this->createFormBuilder(
    options: $this->getCsrfFormOptions()
);
```

### In custom services

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

## Security notes

> **XSS risk:** Symfony forms for backend records or legacy frontend templates do not encode input automatically. Handle input carefully to prevent XSS.

---

*Source: https://docs.contao.org/5.x/dev/framework/request-tokens/*
