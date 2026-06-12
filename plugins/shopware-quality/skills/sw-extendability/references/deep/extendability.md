# Shopware 6 — Erweiterbarkeit: Vollständige Referenz

Quellen: `guides/development/extensions/architecture/{extendability,final-and-internal,internal,index}.md` +
`resources/guidelines/code/core/{extendability,final-and-internal,internal,decorator-pattern}.md`

---

## Überblick: Warum Erweiterbarkeit?

Shopware muss von Drittanbietern und intern angepasst werden können, ohne dass jede Änderung die Stabilität des Core bricht. Deshalb gibt es ein klares Erweiterungsmodell mit definierten Mustern und API-Grenzen.

Erweiterungstypen: **Plugins** (voller Server-Zugriff, Self-hosted only), **Apps** (API-basiert, Cloud-kompatibel), **Project Bundles** (projektspezifisch).

---

## Technische Anforderungen

| Kategorie | Beschreibung | Beispiel |
|-----------|-------------|---------|
| Functional extensibility | Feature mit zusätzlichen Features erweitern | Enterprise Search um Suggestion-Feature ergänzen |
| Functional modifiability | Teile eines Features überschreiben | Steuerberechnung für USA via Tax Provider |
| Functional differentiation | Teile kostenpflichtig machen | Feature hinter Version-Flag |
| Functional exchange market | Feature komplett ersetzen | Externes Newsletter-System anbinden |

---

## Erweiterungsmuster (Patterns)

### 1. Decoration (Decorator Pattern)

**Einsatz:** Kompletters Ersetzen oder Erweitern von Services; Store API Routes; Functional Exchange Market.

**Pflicht-Regeln:**

1. AbstractClass (kein Interface!) mit `getDecorated(): static` definieren.
2. Core-Klasse: `getDecorated()` wirft `DecorationPatternException(self::class)`.
3. Die AbstractClass darf NICHT `@internal` oder `@final` sein.
4. Implementierungen dürfen KEINE zusätzlichen public Methoden über die AbstractClass hinaus hinzufügen.
5. Implementierungen dürfen NICHT als `EventSubscriberInterface` dienen (Symfony-Event-System-Limitation).
6. PHPStan-Regel `DecorationPatternRule` erzwingt diese Regeln automatisch.

```php
abstract class AbstractRuleLoader
{
    abstract public function getDecorated(): AbstractRuleLoader;
    abstract public function load(Context $context): RuleCollection;

    // Neue Methoden: als non-abstract mit Delegation hinzufügen (BC-safe):
    public function create(Context $context): RuleCollection
    {
        return $this->getDecorated()->create($context);
    }
}

class CoreRuleLoader extends AbstractRuleLoader
{
    public function getDecorated(): AbstractRuleLoader
    {
        throw new DecorationPatternException(self::class);
    }
    public function load(Context $context): RuleCollection { /* ... */ }
}

class PluginRuleLoader extends AbstractRuleLoader
{
    public function __construct(private AbstractRuleLoader $inner) {}

    public function getDecorated(): AbstractRuleLoader { return $this->inner; }

    public function load(Context $context): RuleCollection
    {
        $rules = $this->inner->load($context);
        // Erweiterung / Modifikation
        return $rules;
    }
}
```

**Interne Decoration (ohne externe Erweiterbarkeit):** Wenn nur intern dekoriert werden soll (z.B. Cache- oder Log-Layer), AbstractClass verwenden, aber alle Klassen als `@internal` oder `@final` markieren.

```php
/**
 * @final
 */
class CachedLoader extends AbstractRuleLoader
{
    public function __construct(
        private readonly AbstractRuleLoader $decorated,
        private readonly CacheInterface $cache
    ) {}

    public function load(Context $context): RuleCollection
    {
        return $this->cache->get(self::CACHE_KEY, fn () => $this->decorated->load($context));
    }
}
```

ADR: [2020-11-25-decoration-pattern](https://github.com/shopware/shopware/blob/trunk/adr/2020-11-25-decoration-pattern.md)

---

### 2. Factory Pattern

**Einsatz:** User-Input interpretieren und validieren; Functional extensibility; neue Typen hinzufügen.

**Beispiel:** `LineItemFactoryRegistry` — Registry mit Tagged Services; Drittanbieter können eigene Handler registrieren.

```xml
<!-- services.xml -->
<service id="MyPlugin\LineItemFactory\CustomLineItemFactory">
    <tag name="shopware.cart.line_item_factory_handler"/>
</service>
```

---

### 3. Visitor Pattern

**Einsatz:** Verarbeitung von Objekt-Mengen; Functional extensibility + modifiability.

**Beispiel:** `Processor` (Cart) ruft alle `LineItemProcessor`-Implementierungen auf; Drittanbieter-Visitor werden vor/nach Core-Visitor ausgeführt.

---

### 4. Mediator Pattern — Events

**Einsatz:** Einstiegspunkte für Listener; asynchrone Verarbeitung.

**Best Practices:**
- Nur Primary Keys im Event weitergeben, keine Entities oder Objekte — ermöglicht asynchrone Verarbeitung.
- Listener registrieren via `EventSubscriberInterface`.

```php
// Gut: Nur ID weitergeben
class CheckoutOrderPlacedEvent
{
    public function __construct(private readonly string $orderId) {}
    public function getOrderId(): string { return $this->orderId; }
}

// Schlecht: Ganzes Entity weitergeben
class CheckoutOrderPlacedEvent
{
    public function __construct(private readonly OrderEntity $order) {}
}
```

#### Hooks (für Apps)

Hooks sind App-Script-Einstiegspunkte — äquivalent zu Events für Plugins. Da Apps keinen direkten Server-Zugriff haben, erlauben Hooks komplexere Businesslogik ohne HTTP-Roundtrip zum App-Server.

Beispiel: `ProductPageLoadedHook` — wird im Controller dispatcht; jedes registrierte App-Script wird ausgeführt.

---

### 5. Adapter Pattern

**Einsatz:** Functional Exchange Market; Technologietausch (z.B. Captcha-Typ wechseln).

**Implementierung:** Registry + Tagged Services; Benutzer wählt Adapter via Konfiguration.

---

## Public API und @internal/@final

### Was ist Public API?

Alle `public` und `protected` Methoden, Eigenschaften und Konstanten gelten initial als Public API für Drittanbieter.

Die Shopware Public API muss in Minor-Releases kompatibel bleiben für:
- Service-Nutzung (Methoden aufrufen)
- Service-Decoration (erweitern)
- DTO-Nutzung (Daten lesen/übergeben)

### @final Annotation

Klasse ist Public API (konsumierbar), aber **nicht erweiterbar**.

**Erlaubte Änderungen an `@final`-Klassen:**
- Neue public Methoden/Properties/Konstanten hinzufügen
- Neue optionale Parameter zu public Methoden hinzufügen
- Protected/private Methoden ohne Einschränkung ändern
- Typen von public-Methoden-Parametern erweitern (widening)

**Verbotene Änderungen:**
- Public Methoden/Properties/Konstanten entfernen
- Public Methoden-Parameter entfernen
- Typen von public Methoden/Properties/Konstanten verengen (narrowing)

**Warum `final`?**
- DI-Container-Services: `final`, damit keine direkte Vererbung stattfindet — dekorierbare Services haben AbstractClass
- DTO-Klassen: `final` + Struct-Extensions für zusätzliche Daten
- Event-Subscriber: `final`

Hinweis: Da es sich um Doc-Annotations handelt, ist technisch Vererbung möglich — aber ohne Garantien.

### @internal Annotation

Klasse ist **Private API** — kein Einsatz in Plugins/Apps.

- Kann ohne Einschränkungen und ohne Deprecation geändert oder entfernt werden
- Einsatz: Interne Implementierungsdetails, Refactoring-Kandidaten, Klassen die nur existieren um "Master-Klassen" aufzuteilen
- `@internal` Interfaces: Wenn mehrere Implementierungen intern gebraucht werden, aber keine externe Interferenz gewünscht ist (z.B. DAL Field/FieldSerializer)

---

## Entscheidungsbaum: Welches Pattern?

```
Brauche ich externe Erweiterbarkeit?
├─ Ja, Listener-basiert (vor/nach einer Aktion) → Events / Hooks
├─ Ja, Service komplett ersetzbar/erweiterbar → Decoration Pattern (AbstractClass)
├─ Ja, neue Typen/Handler hinzufügbar → Factory / Registry + Tagged Services
├─ Ja, Objekte während Verarbeitung besuchen → Visitor Pattern
├─ Ja, Technologie komplett tauschbar → Adapter Pattern
└─ Nein, nur intern → @internal oder @final, kein AbstractClass nötig
```

---

## Architektur-Subsysteme

Shopware unterscheidet klar: **Core**, **Storefront**, **Administration**.

Extensions müssen diese Grenzen respektieren:
- Kein nicht-deterministisches Verhalten einführen
- Hintergrundjobs und CLI-Commands nicht brechen
- Keine Performance-Regressionen
- Upgrade-Kompatibilität sicherstellen

---

## Referenzen

- `guides/development/extensions/architecture/extendability.md`
- `guides/development/extensions/architecture/final-and-internal.md`
- `guides/development/extensions/architecture/internal.md`
- `guides/development/extensions/architecture/index.md`
- `resources/guidelines/code/core/extendability.md`
- `resources/guidelines/code/core/final-and-internal.md`
- `resources/guidelines/code/core/internal.md`
- `resources/guidelines/code/core/decorator-pattern.md`
- ADR: https://github.com/shopware/shopware/blob/trunk/adr/2020-11-25-decoration-pattern.md
