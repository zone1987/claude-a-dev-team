# Shopware 6 — Core Code Guidelines: Vollständige Referenz

Quellen: `resources/guidelines/code/core/` (alle .md-Dateien)

---

## 1. PHP-Sprachfeatures (ab PHP 8.1 / Shopware 6.5+)

### Promoted Properties

```php
// Statt:
class Point {
    private int $x;
    public function __construct(int $x) { $this->x = $x; }
}
// Besser:
class Point {
    public function __construct(private int $x) {}
}
```

### Readonly Properties (DTOs)

```php
class ProductReindexCommand
{
    public function __construct(
        public readonly int $productId,
        public readonly bool $includeStock
    ) {}
}
```

### match statt switch

```php
$message = match ($statusCode) {
    200, 300 => null,
    400 => 'not found',
    500 => 'server error',
    default => 'unknown status code',
};
```

Vorteile: strikte Gleichheit, kein Fall-through, exhaustiv, Expression (gibt Wert zurück).

### Enums

```php
enum IndexMethod { case PARTIAL; case FULL; }

class Indexer {
    public function product(int $id, IndexMethod $method): void {
        match ($method) {
            IndexMethod::PARTIAL => $this->partial($id),
            IndexMethod::FULL => $this->full($id)
        };
    }
}
```

Enums statt Konstanten-Arrays; typisierbar; Singleton-Semantik; `from()`/`tryFrom()` für Serialisierung.

### Native Typen

- Union Types: `int|string`
- Intersection Types: `MyService&MockObject`
- `mixed` wenn wirklich beliebig
- `never` für Methoden die nie zurückkehren (throw/exit)
- `@var/@param/@return` nur noch für Generics, Array-Shapes, Klassen-Strings, Integer-Ranges etc.

### First-Class Callable Syntax

```php
$longest = max(array_map(strlen(...), $strings)); // statt 'strlen'
$callable = $object->doCoolStuff(...);
```

### Attribute statt Annotationen

```php
// Statt Docblock-Annotation:
#[Route('/blog', name: 'blog_list')]
public function list(): Response { /* ... */ }

// Symfony DI ohne XML:
public function __construct(
    #[Autowire(service: 'email_adapter')]
    private Adapter $adapter,
    #[Autowire('%kernel.debug_mode%')]
    private bool $debugMode,
) {}
```

### Named Arguments

Nur für PHP-eigene APIs (z.B. `htmlspecialchars`), NICHT für Shopware-APIs (Parameter-Namen sind KEIN BC-Versprechen).

### Nullsafe Operator

```php
$addressLine2 = $user?->address?->addressLine2;
```

### list<T> statt array<T>

```php
/** @return list<string> */
public function getChoices(): array { return ['a', 'b']; }
```

`list<T>` für sequentielle Wert-Sammlungen ohne semantische Keys. Nach `array_merge()`/`array_unique()` mit `array_values()` normalisieren.

### Neue String-Funktionen

- `str_contains`, `str_starts_with`, `str_ends_with` statt `strpos`/`substr`

---

## 2. Extendability Guidelines

Vollständig dokumentiert in `sw-extendability`. Hier Kurzfassung:

- **Events (Mediator)** — Erste Wahl; nur Primary Keys weitergeben
- **Decorator** — AbstractClass + `getDecorated()` + `DecorationPatternException`
- **Factory/Registry** — für neue User-Input-Typen via Tagged Services
- **Visitor** — für Objekt-Verarbeitung
- **Adapter** — für Technologietausch

---

## 3. Decorator Pattern — Regeln

```php
abstract class AbstractRuleLoader
{
    abstract public function getDecorated(): AbstractRuleLoader;
    abstract public function load(Context $context): RuleCollection;
}

class CoreRuleLoader extends AbstractRuleLoader
{
    public function getDecorated(): AbstractRuleLoader
    {
        throw new DecorationPatternException(self::class);
    }
    public function load(Context $context): RuleCollection { /* ... */ }
}

class PluginDecorator extends AbstractRuleLoader
{
    public function __construct(private AbstractRuleLoader $inner) {}
    public function getDecorated(): AbstractRuleLoader { return $this->inner; }
    public function load(Context $context): RuleCollection
    {
        $rules = $this->inner->load($context);
        // Erweiterung
        return $rules;
    }
}
```

**Regeln:**
1. AbstractClass implementiert `getDecorated(): self`
2. Core wirft `DecorationPatternException` in `getDecorated()`
3. AbstractClass NICHT `@internal` oder `@final`
4. Implementierungen: KEINE zusätzlichen public Methoden
5. Implementierungen: KEIN `EventSubscriberInterface`
6. PHPStan-Regel `DecorationPatternRule` erzwingt dies

Neue Methoden BC-safe hinzufügen: als non-abstract in der AbstractClass mit Delegation:
```php
public function create(Context $context): RuleCollection
{
    return $this->getDecorated()->create($context);
}
```

---

## 4. Domain Exceptions

Pro Domäne eine Exception-Factory-Klasse, die `HttpException` extended.

```php
#[Package('customer-order')]
class CustomerException extends HttpException
{
    public const CUSTOMER_GROUP_NOT_FOUND = 'CHECKOUT__CUSTOMER_GROUP_NOT_FOUND';

    public static function customerGroupNotFound(string $id): self
    {
        return new self(
            Response::HTTP_BAD_REQUEST,
            self::CUSTOMER_GROUP_NOT_FOUND,
            'Customer group with id "{{ id }}" not found',
            ['id' => $id]
        );
    }
}
```

**Regeln:**
- `__construct` ist `private` — nur Factory-Methoden erstellen Instanzen
- Error-Codes: eindeutig innerhalb der Domäne; stabil (keine Änderung nach Release)
- Speicherort: direkt im Top-Level-Domain-Verzeichnis (`Checkout\Cart`, `Content\Product` etc.)
- Catchable Exceptions: eigene Exception-Klasse die von DomainException erbt, in `Exception/`-Unterordner

```php
class CustomerNotFoundException extends CustomerException {}
```

- HTTP Status Codes: immer passenden offiziellen Code verwenden
- ADR: https://github.com/shopware/shopware/blob/71ef1dffc97a131069cd4649f71ba35d04771e24/adr/2022-02-24-domain-exceptions.md

---

## 5. Feature Flags

Feature Flags ermöglichen unfertige Änderungen in `trunk` zu mergen, ohne sie zu aktivieren.

### .env Konfiguration
```
V6_5_0_0=1
```

### PHP
```php
use Shopware\Core\Framework\Feature;

// Bedingte Ausführung:
if (!Feature::isActive('v6.5.0.0')) {
    // altes Verhalten
    return;
}
// neues Verhalten

// Callback:
Feature::ifActive('v6.5.0.0', function() { /* ... */ });

// Deprecation:
/** @deprecated tag:v6.5.0 - Class is deprecated, use ... instead */
class OldClass {
    public function foo(): void {
        Feature::triggerDeprecationOrThrow('v6.5.0.0', 'Class is deprecated, use ... instead');
    }
}

// Tests:
Feature::skipTestIfActive('v6.5.0.0', $this);
```

### JavaScript (Admin)
```javascript
// Modul verstecken:
Module.register('sw-awesome', { flag: 'v6.5.0.0', ... });

// Inject Feature-Service:
inject: ['feature'],
featureIsActive(flag) { return this.feature.isActive(flag); }
```

### Twig (Storefront)
```twig
{% if feature('v6.5.0.0') %}
    <span>Feature is active</span>
{% endif %}
```

### Major Feature Flags

Major-Flags (`v6.5.0.0`, `v6.6.0.0`) signalisieren Breaking Changes vor dem Release. Bleiben nach dem Release erhalten → nutzbar als Versions-Switch alternativ zu `version_compare`.

### Plugin-eigene Flags

Interne Verwendung; Verhalten kann sich jederzeit ändern:
```php
private const FEATURE_FLAGS = ['paypal:v1.0.0.0'];

public function boot(): void
{
    Feature::setRegisteredFeatures(
        array_merge(array_keys(Feature::getAll()), self::FEATURE_FLAGS),
        $this->container->getParameter('kernel.cache_dir') . '/shopware_features.php'
    );
}
```

---

## 6. @final und @internal Annotation

→ Vollständig dokumentiert in `sw-extendability`.

Kurzfassung:
- `@final`: Public API, nicht erweiterbar
- `@internal`: Private API, keine Garantien, kein Einsatz in Plugins

---

## 7. Datenbank-Migrationen

### Struktur

```php
// Namespace pro Major-Version:
namespace Shopware\Core\Migration\V6_7;

class Migration1234567890MyFeature extends MigrationStep
{
    public function update(Connection $connection): void
    {
        // Non-destructive, backward-compatible
        $connection->executeStatement('
            ALTER TABLE product ADD COLUMN new_field VARCHAR(255) NULL
        ');
    }

    public function updateDestructive(Connection $connection): void
    {
        // Irreversible (z.B. Spalte löschen) — nur in separatem Schritt
        $connection->executeStatement('
            ALTER TABLE product DROP COLUMN old_field
        ');
    }
}
```

### Mandatory Rules

1. **NEVER eine bereits released Migration ändern** — neue Migration schreiben statt editieren
2. **Idempotent** — Migration muss mehrfach ausführbar sein; `IF [NOT] EXISTS` nutzen
3. **Keine Identifier vertrauen** — immer Identifier via Query ermitteln, nie hart coden
4. **Keine Kundendaten überschreiben** — `updated_at IS NULL` prüfen vor Updates
5. **Performance** — max. 10 Sekunden auf lokalem System; mit Produktionsdatenmengen testen
6. **Keine Default-Sprache annehmen** — `ImportTranslationsTrait` nutzen
7. **Table Naming** — snake_case, kein `swag_`-Präfix, beschreibende Namen

### Expand-and-Contract Pattern

```
1. Expand:    Neue Spalte hinzufügen (non-destructive, update())
2. Migrate:   Daten von alter in neue Spalte kopieren (update())
3. Contract:  Alte Spalte löschen (updateDestructive())
```

### Migration-Modes für Destructive Changes

| Mode | Führt Destructive aus bis |
|------|--------------------------|
| `mode=all` | Aktuelle Major-Version |
| `mode=blue-green` | Vorherige Major-Version |
| `mode=safe` (default) | Zwei Majors vor aktueller |

### Migration erstellen

```bash
bin/console database:create-migration
# Ausführen:
bin/console database:migrate --all core.V6_7
```

### Migration Tests

- Tests in `tests/Migration/V6_*/`
- KEIN `IntegrationTestBehaviour` / `KernelTestBehaviour` — Connection via `KernelLifecycleManager::getConnection()`
- `update()` zweimal ausführen um Idempotenz zu verifizieren
- DDL-Commands (CREATE/ALTER/DROP TABLE) laufen außerhalb von Transactions (Implicit Commit)
- DDL-Tests müssen DDL-Änderungen manuell rückgängig machen (kein Rollback via `MigrationTestTrait`)
- `MigrationTestTrait` für reine DML-Migrations nutzen
- `MultiInsertQueryQueue` für Bulk-Fixture-Daten

---

## 8. Unit Tests

### Prinzipien

- **100% Coverage** bedeutet: alle Use Cases getestet, nicht nur hohe Zeilenzahl
- **Performance**: Tests schnell halten; mocks für DB-Zugriffe
- **Behavior over Implementation**: Was tut der Code, nicht wie
- **Modularity**: Tests dürfen keine Artefakte anderer Tests voraussetzen
- **Cleanup**: EventListener in `teardown()` entfernen; DB rollbacken
- **Failure Cases**: Nicht nur Happy-Path; auch Fehlerfälle testen
- **Expected Exceptions**: `expectExceptionObject()` statt try/catch

### Mock-Strategie

Mocks sparsam einsetzen:
1. Echte Implementierung nutzen wenn möglich (kein DB-Zugriff, keine Side-Effects)
2. Hand-crafted Stub/Dummy (z.B. `StaticEntityRepository`, `StaticSystemConfigService`)
3. PHPUnit Mock Framework als letztes Mittel

**Mocks sind problematisch weil:**
- Schlecht refactorierbar (IDEs erkennen Mock-Referenzen nicht)
- Implementierungsdetails testen statt Verhalten
- Können stale werden wenn sich Implementierung ändert

### Gute Test-Beispiele

- `CriteriaTest` — simple DTO-Tests
- `CashRoundingTest` — Test-Matrix für Single-Service
- `AddCustomerTagActionTest` — Mocks für Repositories
- `ProductCartTest` — Integration-Test mit Helper-Functions
- `CachedProductListingRouteTest` — Komplexe Test-Matrix

### Para-Test-Kompatibilität

Tests müssen mit Parallel-Test-Setup kompatibel sein.

---

## 9. Writing Code for Static Analysis

PHPStan wird intensiv genutzt — Code muss statisch analysierbar sein.

### Typ-Sicherheit Prioritäten

1. **Runtime-Checks** (bevorzugt):
```php
$foo = $bar->getFoo(); // Foo|null
if ($foo === null) {
    throw new \InvalidArgumentException('Foo must not be null');
}
// PHPStan weiß jetzt: $foo ist Foo
```

2. **assert()** (Development/Test only):
```php
assert($foo !== null);         // Für Entwicklung/Test
assert(is_string($foo));
assert($foo instanceof Foo);
```

3. **@var Annotations** (letztes Mittel):
```php
/** @var Foo $foo */
$foo = $bar->getFoo();
```

### Type Casts vermeiden

Casts (`(string)`, `(int)`) verbergen Typ-Fehler; PHPStan erkennt unerwartete Cast-Effekte nicht.

### @var/@param/@return nur für:

- Generics: `@return Collection<int, Product>`
- Array-Shapes: `@param array{id: string, name: string} $data`
- Spezielle PHPStan-Typen: `class-string`, `positive-int`

### list<T> vs array<T>

```php
/** @return list<string> */
public function getTags(): array
{
    return array_values(array_unique($tags)); // array_values() normalisiert zu list
}
```

---

## 10. ADR-Format

Erwartungen an Architecture Decision Records:

- Vollständige Anforderungsbeschreibung
- Alle betroffenen technischen Domänen auflisten
- Alle betroffenen Logik-Bereiche auflisten
- Pseudo-Code zur Visualisierung
- Alle zu erstellenden/ändernden Public APIs definieren
- Erweiterbarkeit und Business-Cases beschreiben
- Begründung der Entscheidung
- Alle Konsequenzen für Drittentwickler

### Empfohlener Ablauf

1. Liste der zu berührenden Domains erstellen
2. Für jede Domain: Warum betroffen (2 Sätze)
3. Pro Domain: "Problems" (Was muss geändert werden — noch nicht wie)
4. Pro Domain: "Solution" (Wie die Problems gelöst werden)
5. Section "Extendability": Wie können Entwickler das neue System erweitern
6. Pseudo-Code am Ende

---

## Referenzen

- `resources/guidelines/code/core/6.5-new-php-language-features.md`
- `resources/guidelines/code/core/extendability.md`
- `resources/guidelines/code/core/decorator-pattern.md`
- `resources/guidelines/code/core/domain-exceptions.md`
- `resources/guidelines/code/core/feature-flags.md`
- `resources/guidelines/code/core/final-and-internal.md`
- `resources/guidelines/code/core/internal.md`
- `resources/guidelines/code/core/database-migations.md`
- `resources/guidelines/code/core/unit-tests.md`
- `resources/guidelines/code/core/writing-code-for-static-analysis.md`
- `resources/guidelines/code/core/adr.md`
