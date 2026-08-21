# Contao 5.x – Hook system: How-to

## Contents

- [What are hooks?](#what-are-hooks)
- [Registration methods](#registration-methods)
- [Invokable services](#invokable-services)
- [Priority](#priority)
- [Typical listener pattern](#typical-listener-pattern)
- [Hook vs. Symfony Event Dispatcher](#hook-vs-symfony-event-dispatcher)
- [Reference: all hook names](#reference-all-hook-names)

## What are hooks?

Hooks are entry points into the Contao core (and some extension bundles) that let you embed your own logic at specific places in the execution flow. Technically, a hook is a named array of callables that are invoked one after another when the hook point is reached.

> **Note:** Hooks are a legacy concept from Contao 2/3. For new event-driven code, Contao recommends using the **Symfony Event Dispatcher** where possible. Many hooks, however, remain the only way to extend certain core logic.

### Internal execution pattern

```php
// Simplified example from the Contao core
if (isset($GLOBALS['TL_HOOKS']['activateAccount']) && \is_array($GLOBALS['TL_HOOKS']['activateAccount'])) {
    foreach ($GLOBALS['TL_HOOKS']['activateAccount'] as $callback) {
        $this->import($callback[0]);
        $this->{$callback[0]}->{$callback[1]}($objMember, $this);
    }
}
```

Listeners receive hook-specific parameters and may have to return a value that is passed on to the next listener.

---

## Registration methods

### 1. PHP attribute `#[AsHook]` (recommended)

The modern approach. Prerequisite: Symfony autowiring/autoconfigure is enabled (the default in Contao applications).

```php
namespace App\EventListener;

use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\FrontendTemplate;
use Contao\Module;

#[AsHook('parseArticles', priority: 100)]
class ParseArticlesListener
{
    public function onParseArticles(FrontendTemplate $template, array $newsEntry, Module $module): void
    {
        // Your own logic …
    }
}
```

The attribute can be used at **class** or **method level**:

- **Method level** (as above): the annotated method is called.
- **Class level** (invokable): the class must implement `__invoke()` (see below).

#### Attribute parameters

| Parameter  | Type   | Meaning                                       |
|-----------|--------|-----------------------------------------------|
| `hook`    | string | Name of the hook (required, first parameter)  |
| `priority`| int    | Execution order, default `0`                  |
| `method`  | string | Method, if not `__invoke` (optional)          |

---

### 2. YAML service tag `contao.hook`

Configuration in `config/services.yaml`:

```yaml
services:
    App\EventListener\ActivateAccountListener:
        tags:
            - name: contao.hook
              hook: activateAccount
              method: onAccountActivation   # optional, otherwise derived from the hook name
              priority: 100                 # optional, default 0
```

Tag options:

| Option   | Required | Description                                      |
|---------|---------|---------------------------------------------------|
| `name`  | yes     | Must be `contao.hook`                             |
| `hook`  | yes     | The hook name                                     |
| `method`| no      | Method; otherwise derived automatically from the hook name |
| `priority`| no    | Execution order, default `0`                      |

---

### 3. Service annotation `@Hook` (deprecated)

Requires the Service Annotation Bundle. No longer recommended.

```php
use Contao\CoreBundle\ServiceAnnotation\Hook;

/**
 * @Hook("parseArticles", priority=100)
 */
public function onParseArticles(FrontendTemplate $template, array $newsEntry, Module $module): void
{
    // …
}
```

---

### 4. Legacy `$GLOBALS['TL_HOOKS']`

Still works for backwards compatibility, but is no longer recommended:

```php
// In a Contao-specific configuration file or in a bundle
$GLOBALS['TL_HOOKS']['activateAccount'][] = ['App\MyClass', 'myMethod'];
```

---

## Invokable services

Classes with `__invoke()` can be registered as hook listeners without specifying a method:

```php
namespace App\EventListener;

use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\FrontendTemplate;
use Contao\Module;

#[AsHook('parseArticles')]
class ParseArticlesListener
{
    public function __invoke(FrontendTemplate $template, array $newsEntry, Module $module): void
    {
        // Your own logic …
    }
}
```

Or via YAML (without a `method` entry):

```yaml
services:
    App\EventListener\ParseArticlesListener:
        tags:
            - { name: contao.hook, hook: parseArticles }
```

---

## Priority

The `priority` determines when a listener runs relative to other (including legacy) listeners:

| Priority        | Execution time                                                        |
|----------------|------------------------------------------------------------------------|
| `priority > 0`  | **Before** legacy `$GLOBALS['TL_HOOKS']` listeners                    |
| `priority = 0`  | According to extension load order, together with legacy listeners     |
| `priority < 0`  | **After** legacy `$GLOBALS['TL_HOOKS']` listeners                     |

Higher values = earlier execution (as with Symfony event listeners).

---

## Typical listener pattern

```php
// src/EventListener/MyHookListener.php
namespace App\EventListener;

use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;

#[AsHook('hookName', priority: 10)]
class MyHookListener
{
    public function __invoke(/* hook-specific parameters */): /* return type */
    {
        // Logic
    }
}
```

Location: `src/EventListener/` (registered automatically as a service through Symfony autowiring).

---

## Hook vs. Symfony Event Dispatcher

| Aspect          | Hook                            | Symfony event                    |
|----------------|----------------------------------|----------------------------------|
| Style           | Legacy Contao concept           | Modern, recommended              |
| Type safety     | Weaker                          | Strong (event class)             |
| Order           | Via `priority`                  | Via `priority`                   |
| New features    | No (deprecated in Contao 6)     | Yes                              |
| Contao core     | Required for many core points   | Where events are available       |

---

## Reference: all hook names

Full reference of all ~69 hooks with parameters, return values and examples:
→ Skill `contao-hooks-reference` / `references/deep/`

---

_Source: https://docs.contao.org/5.x/dev/framework/hooks/ and https://docs.contao.org/5.x/dev/getting-started/hooks/ (as of 2025-06)_
