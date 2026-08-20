# Shopware DAL — Vollständige Konzept-Doku

Quelle: `concepts/framework/data-abstraction-layer.md`

---

## Datenbankzugriff

Shopware verwendet **kein ORM** (kein Doctrine), sondern eine eigene Data Abstraction Layer (DAL).
Konzepte wie Criteria sind Doctrine ähnlich, aber für Shopware-spezifische Anforderungen implementiert.

Referenz-ERD: https://developer.shopware.com/assets/shopware6-erd.pdf (für 6.6.5.0)

---

## CRUD-Operationen

`EntityRepository` ist der einzige empfohlene Weg, mit der DAL zu interagieren.

### Bereitstellen via Dependency Injection

```php
// Konstruktor-Injection
public function __construct(EntityRepository $productRepository)
{
    $this->productRepository = $productRepository;
}
```

```php
// Explizite DI-Konfiguration (services.php)
$services->set(DalExampleService::class)
    ->args([service('product.repository')]);
```

Mit Service-Autowiring und korrektem Typ + Argumentname wird das Repository automatisch injiziert.

---

## Übersetzungen (DAL-Ebene)

Bei Lese-/Suchoperationen werden drei Sprachebenen durchsucht:

1. **Aktuelle Sprache** — die dem Nutzer angezeigte Sprache
2. **Parent-Sprache** — optionale übergeordnete Sprache für Dialekte (z.B. `de-DE` als Parent von `de-AT`)
3. **Systemsprache** — Installations-Sprache; jede Entität hat hier mindestens eine Übersetzung (finaler Fallback)

Übersetzungen werden in separaten Tabellen gespeichert: `<entity-tabelle>_translation` (Suffix `_translation`).

---

## Versioning

- Ermöglicht mehrere Versionen einer Entität
- Alle assoziierten Daten werden dupliziert für neue Version
- Mehrere Entities/Änderungen können einer Version zugeordnet werden
- Einsatz: Previews, Publishing, Kampagnen (Änderungen vorbereiten ohne live zu gehen)

**Einschränkung**: Kein "Entwurf zuerst, dann live" — es muss immer eine Live-Version existieren,
bevor eine neue Version abgeleitet werden kann.

**Datenbankstruktur**: Versionierbare Entities haben Compound-FK: `id` + `version_id`.
Fremdschlüssel auf versionierte Records: `product_id` + `product_version_id`.

---

## Context (`core/Framework/Context.php`)

- Einmal pro Request instanziiert
- Definiert wichtige Shop-Konfiguration
- Beeinflusst CRUD-Verhalten der DAL (z.B. Währung wechseln → alle Operationen nutzen neue Währung)
- Enthält: Sprache, Währung, Preisregeln, Berechtigungen

---

## Inheritance (Vererbung)

Implementiert für das Produkt-/Variantensystem:

- **Parent-Child-Vererbung** — Varianten erben Records, Properties und Associations vom Parent-Produkt
- Beispiel: Variante ohne eigene Kategorien/Bilder → erbt vom Parent-Produkt
- Gilt für Felder und Associations

---

## Indexing (Entity Indexer Pattern)

Design-Prinzip: "Je mehr Zeit ins Indizieren investiert wird, desto schneller ist das Lesen."

- Produkte werden selten geschrieben, aber sehr häufig gelesen
- Beim Schreiben: entsprechender **Product Indexer** wird getriggert
- Indexer pre-selektiert Aggregationen und schreibt sie optimiert für spätere Lesevorgänge
- Ergebnis: Lesevorgänge sind minimal aufwändig (denormalisierte, indexierte Daten)
