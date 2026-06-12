# Contao 5.x – Hook-System: How-To

## Was sind Hooks?

Hooks sind Einstiegspunkte in den Contao-Kern (und einige Extension-Bundles), über die eigene Logik an bestimmten Stellen im Ausführungsfluss eingebettet werden kann. Technisch gesehen ist ein Hook ein benanntes Array von Callables, die der Reihe nach aufgerufen werden, wenn der Hook-Punkt erreicht wird.

> **Hinweis:** Hooks sind ein veraltetes Konzept aus Contao 2/3. Für neuen event-gesteuerten Code empfiehlt Contao, den **Symfony Event Dispatcher** zu verwenden, wo möglich. Viele Hooks bleiben jedoch die einzige Möglichkeit, bestimmte Core-Logik zu erweitern.

### Internes Ausführungsmuster

```php
// Vereinfachtes Beispiel aus dem Contao-Kern
if (isset($GLOBALS['TL_HOOKS']['activateAccount']) && \is_array($GLOBALS['TL_HOOKS']['activateAccount'])) {
    foreach ($GLOBALS['TL_HOOKS']['activateAccount'] as $callback) {
        $this->import($callback[0]);
        $this->{$callback[0]}->{$callback[1]}($objMember, $this);
    }
}
```

Listener erhalten hook-spezifische Parameter und müssen ggf. einen Wert zurückgeben, der an den nächsten Listener weitergegeben wird.

---

## Registrierungsmethoden

### 1. PHP-Attribut `#[AsHook]` (empfohlen)

Der moderne Weg. Voraussetzung: Symfony Autowiring/Autoconfigure ist aktiv (Standard in Contao-Applikationen).

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
        // Eigene Logik …
    }
}
```

Das Attribut kann auf **Klassen-** oder **Methoden-Ebene** verwendet werden:

- **Methoden-Ebene** (wie oben): Die annotierte Methode wird aufgerufen.
- **Klassen-Ebene** (invokable): Die Klasse muss `__invoke()` implementieren (siehe unten).

#### Parameter des Attributs

| Parameter  | Typ    | Bedeutung                                     |
|-----------|--------|-----------------------------------------------|
| `hook`    | string | Name des Hooks (Pflicht, erster Parameter)    |
| `priority`| int    | Ausführungsreihenfolge, Standard `0`          |
| `method`  | string | Methode, wenn nicht `__invoke` (optional)     |

---

### 2. YAML Service-Tag `contao.hook`

Konfiguration in `config/services.yaml`:

```yaml
services:
    App\EventListener\ActivateAccountListener:
        tags:
            - name: contao.hook
              hook: activateAccount
              method: onAccountActivation   # optional, sonst aus Hook-Name abgeleitet
              priority: 100                 # optional, Standard 0
```

Tag-Optionen:

| Option   | Pflicht | Beschreibung                                      |
|---------|---------|---------------------------------------------------|
| `name`  | ja      | Muss `contao.hook` sein                           |
| `hook`  | ja      | Der Hook-Name                                     |
| `method`| nein    | Methode; wird sonst automatisch aus Hook-Name abgeleitet |
| `priority`| nein | Ausführungsreihenfolge, Standard `0`              |

---

### 3. Service-Annotation `@Hook` (veraltet)

Erfordert das Service Annotation Bundle. Nicht mehr empfohlen.

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

Funktioniert weiterhin für Rückwärtskompatibilität, aber nicht mehr empfohlen:

```php
// In einer Contao-spezifischen Konfigurationsdatei oder einem Bundle
$GLOBALS['TL_HOOKS']['activateAccount'][] = ['App\MyClass', 'myMethod'];
```

---

## Invokable Services

Klassen mit `__invoke()` können ohne Methoden-Angabe als Hook-Listener registriert werden:

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
        // Eigene Logik …
    }
}
```

Oder via YAML (ohne `method`-Angabe):

```yaml
services:
    App\EventListener\ParseArticlesListener:
        tags:
            - { name: contao.hook, hook: parseArticles }
```

---

## Priorität

Die `priority` bestimmt, wann ein Listener relativ zu anderen (auch legacy) Listenern ausgeführt wird:

| Priorität       | Ausführungszeitpunkt                                                  |
|----------------|------------------------------------------------------------------------|
| `priority > 0`  | **Vor** legacy `$GLOBALS['TL_HOOKS']`-Listenern                       |
| `priority = 0`  | Gemäß Extension-Ladereihenfolge, zusammen mit legacy Listenern        |
| `priority < 0`  | **Nach** legacy `$GLOBALS['TL_HOOKS']`-Listenern                      |

Höhere Werte = frühere Ausführung (wie bei Symfony Event Listener).

---

## Typisches Listener-Muster

```php
// src/EventListener/MyHookListener.php
namespace App\EventListener;

use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;

#[AsHook('hookName', priority: 10)]
class MyHookListener
{
    public function __invoke(/* hook-spezifische Parameter */): /* Rückgabetyp */
    {
        // Logik
    }
}
```

Ablageort: `src/EventListener/` (wird durch Symfony-Autowiring automatisch als Service registriert).

---

## Hook vs. Symfony Event Dispatcher

| Aspekt          | Hook                            | Symfony Event                    |
|----------------|----------------------------------|----------------------------------|
| Stil            | Legacy Contao-Konzept           | Modern, empfohlen                |
| Typsicherheit   | Schwächer                       | Stark (Event-Klasse)             |
| Reihenfolge     | Über `priority`                 | Über `priority`                  |
| Neue Features   | Nein (Contao 6 deprecated)      | Ja                               |
| Contao-Core     | Pflicht für viele Core-Punkte   | Wo Events verfügbar              |

---

## Referenz: Alle Hook-Namen

Vollständige Referenz aller ~69 Hooks mit Parametern, Rückgabewerten und Beispielen:
→ Skill `contao-hooks-reference` / `references/deep/`

---

_Quelle: https://docs.contao.org/5.x/dev/framework/hooks/ und https://docs.contao.org/5.x/dev/getting-started/hooks/ (Stand 2025-06)_
