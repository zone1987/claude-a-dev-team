# Session-Management

## Session-Keys

Das Plugin verwendet drei verschiedene Session-Keys:

### 1. Product Session: `octo-product-session-{shopwareProductId}`

**Gesetzt:** Bei jeder Verfügbarkeitsprüfung
**Methode:** `AvailbilityController::setUnitSessionItem()`
**Gelesen von:** CartController, AvailbilityController, octo-configurator.html.twig

```json
{
    "optionId": "api-option-uuid",
    "units": [
        {
            "id": "unit-uuid",
            "type": "ADULT",
            "quantity": 2,
            "price": { "retail": 2500, "net": 2100, "currency": "GBP", "currencyPrecision": 2 }
        },
        {
            "id": "unit-uuid",
            "type": "CHILD",
            "quantity": 1,
            "price": { "retail": 1500, "net": 1200, "currency": "GBP", "currencyPrecision": 2 }
        }
    ],
    "localDateStart": "2025-03-15T00:00:00.000Z"
}
```

**Zweck:** Speichert die aktuelle Konfiguration des Users (gewählte Option, Mengen pro Unit-Typ, Datum).

### 2. Unique Line-Item Session: `{uniqueLineItemId}`

**ID-Berechnung:**
```php
$unitString = implode('__', array_map(
    fn($u) => "{$u['id']}_q{$u['quantity']}",
    $units
));
$uniqueLineItemId = Uuid::fromStringToHex($productId . $unitString);
```

**Beispiel:** `018e1234abcd...` aus `"shopware-product-id" + "adult-uuid_q2__child-uuid_q1"`

**Gesetzt:** Bei jeder Verfügbarkeitsprüfung
**Methode:** `AvailbilityController::setOctoProductSessionItem()`
**Gelesen von:** CartController, OctoCartCollector

```json
{
    "units": [
        {
            "id": "unit-uuid",
            "type": "ADULT",
            "title": "Erwachsene",
            "quantity": 2,
            "price": { "retail": 28.59 },
            "restrictions": {
                "minAge": 16,
                "maxAge": null,
                "accompaniedBy": []
            }
        }
    ],
    "availability": {
        "id": "availability-uuid-from-api",
        "status": "AVAILABLE",
        "capacity": 50,
        "localDateTimeStart": "2025-03-15T09:00:00",
        "localDateTimeEnd": "2025-03-15T17:00:00"
    },
    "localTimeStart": "09:00"
}
```

**Zweck:** Speichert die API-Verfügbarkeitsantwort inklusive `availability.id` (wird für Reservierung benötigt!).

### 3. Generische Session Items (via SessionController)

**Routen:**
- `POST /octo-api/session/set` — `{ key: "time", value: "09:00" }`
- `POST /octo-api/session/get-item` — `{ key: "time" }`
- `POST /octo-api/session/remove-item` — `{ key: "time" }`

**Genutzt von:** TimeSelectPlugin speichert gewählte Uhrzeit.

---

## Unique Line-Item ID Berechnung

**KRITISCH:** Die gleiche Berechnung existiert in **drei** Klassen:

1. `AvailbilityController` — beim Schreiben der Session
2. `CartController` — beim Lesen der Session im Add-to-Cart
3. `OctoCartCollector` — beim Lesen der Session für Preisberechnung

```php
private function getUniqueLineItemId(string $referenceId, array $units): string
{
    $unitString = implode('__', array_map(
        fn ($unit) => $unit['id'] . '_q' . $unit['quantity'],
        $units
    ));
    return Uuid::fromStringToHex($referenceId . $unitString);
}
```

**Die Reihenfolge der Units MUSS identisch sein** beim Schreiben und Lesen!

---

## Session-Lebenszyklus

```
1. User öffnet Produktdetailseite
   → Keine Session-Daten vorhanden

2. User wählt Datum (DateSelectPlugin)
   → POST /octo-api/availability/check
   → AvailbilityController schreibt:
     a) octo-product-session-{productId}  (Units + OptionId + Datum)
     b) {uniqueLineItemId}                (Units + Availability + Time)
   → HTML-Response aktualisiert DOM

3. User ändert Menge (QuantitySelectPlugin)
   → Emittiert octo-quantity-changed → FfBuyBoxPlugin
   → Erneuter POST /octo-api/availability/check
   → Session wird überschrieben (neue uniqueLineItemId bei neuer Menge!)

4. User wählt Uhrzeit (TimeSelectPlugin)
   → POST /octo-api/session/set { key: "time", value: "09:00" }
   → Emittiert octo-time-changed

5. User klickt "In den Warenkorb"
   → POST /checkout/line-item/add
   → CartController liest:
     a) octo-product-session-{productId}  → optionId, units, datum
     b) {uniqueLineItemId}                → availability.id für Reservierung
   → Erstellt Booking-Reservierung
   → Line-Item mit reservationUuid im Payload

6. Cart wird berechnet
   → OctoCartCollector::process()
   → Liest {uniqueLineItemId} → units mit Preisen
   → Berechnet Gesamtpreis
```

---

## Twig-Zugriff auf Session

```twig
{# octo-configurator.html.twig #}
{% set sessionItem = app.request.session.get('octo-product-session-' ~ page.product.id)|json_decode %}

{% if sessionItem and sessionItem.units %}
    {% for unit in sessionItem.units %}
        {{ unit.type }}: {{ unit.quantity }}
    {% endfor %}
{% endif %}
```

---

## Session-Lebensdauer

- **PHP-Session-Timeout:** Typisch 30 Minuten Inaktivität
- **Reservierungs-Timeout:** API-konfigurierbar (5-60 Min, default 30)
- **Bei Session-Ablauf:** User verliert Konfiguration, muss neu wählen
- **Bei Reservierungs-Ablauf:** Reservierung muss ggf. erneuert werden

---

## SessionService

**Datei:** `src/Service/SessionService.php`

```php
public function setItem(SessionInterface $session, string $key, string $value): array
// Setzt Item, speichert Session, gibt alle Session-Items zurück

public function getItem(SessionInterface $session, string $key): mixed
// Gibt Item zurück oder wirft Exception wenn nicht gefunden/leer

public function removeItem(SessionInterface $session, string $key): mixed
// Entfernt Item und gibt es zurück
```
