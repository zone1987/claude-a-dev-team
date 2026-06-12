# ClassHelper (`src/Helper/ClassHelper.php`)

## Zweck
Reflection-Hilfsfunktion, die die Argumente der **aufrufenden** Methode als assoziatives `['paramName' => value]`-Array zurückgibt (für generisches Caching/Logging à la „Methodenargumente automatisch erfassen").

## Typ & Vererbung
- Namespace: `FfOctoApi\Helper`
- `abstract class ClassHelper`, `declare(strict_types=1)`

## Methoden
### `static getMethodArgs(): array`
Liest `debug_backtrace()[1]` (Aufrufer), ermittelt Klasse/Methode/Args, mappt via `ReflectionMethod::getParameters()` Parameternamen auf Werte. Leeres Array bei fehlender Klasse/Methode oder `ReflectionException`.

## Besonderheiten / Fallstricke
- Hängt fest an Backtrace-Index `[1]` → nur direkt aus der Zielmethode aufrufen (nicht über Wrapper).

## Bezüge
ggf. `CachedOctoApiClient`/`getCachedItem`-Umfeld.
