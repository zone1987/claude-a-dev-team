# OCTO / Ventrata API — Vollständiger Überblick

## Was ist Ventrata?

Ventrata ist eine Enterprise-Ticketing-Plattform für Hochvolumen-Attraktionen, Tour- und Aktivitätsanbieter. Das System verwaltet Online-, In-Person- und Drittanbieter-Verkaufskanäle sowie Ressourcenmanagement und Hardware-Integrationen.

**Bekannte Ventrata-Kunden:** Big Bus Tours, Sightseeing Pass, Tootbus, Historic Tours of America, Boston Duck Tours, Gray Line Operators, Empire State Building, Tower Bridge, und über 100 weitere Operatoren weltweit.

## Was ist OCTO?

OCTO (Open Connectivity for Tourism) ist eine **offene API-Spezifikation** für den In-Destination-Erlebnissektor der Reisebranche. Die Spezifikation definiert standardisierte Schemas, Endpunkte und Capabilities für die Verbindung von Plattformen, Resellern, OTAs und verwandten Technologien im Bereich Touren, Aktivitäten und Attraktionen.

**Offizielle OCTO-Ressourcen:**
- Spezifikation: https://docs.octo.travel/
- GitHub: https://github.com/octotravel
- Organisation: https://www.octo.travel/

## Integration Philosophy

- **Kostenlos:** Keine Gebühren für Reseller, die mit Ventrata-Clients über die OCTO API arbeiten
- **Standardisiert:** Ein Entwicklungsprojekt verbindet zu allen OCTO-kompatiblen Systemen
- **Reseller-seitig:** Viator, GetYourGuide, Expedia, Groupon, Klook, Tiqets verbinden sich direkt

## Basis-URL

```
https://api.ventrata.com/octo
```

## Das Capabilities-Konzept

Capabilities sind optionale API-Erweiterungen, die zusätzliche Felder und Funktionen in Responses hinzufügen. Sie werden per `Octo-Capabilities` Request-Header angefordert und im Response-Header zurückgespiegelt.

### Alle verfügbaren Capabilities

| Capability | Zweck |
|-----------|-------|
| `octo/pricing` | Preisfelder in Products/Availability/Bookings/Orders/Gifts |
| `octo/content` | Erweiterte Inhaltsfelder für Product/Option/Unit/Availability/Booking |
| `octo/offers` | Supplier-Angebote und angebotsbewusstes Pricing/Booking |
| `octo/extras` | Extra-Upsell-Inventar und Buchungs-Extra-Items |
| `octo/packages` | Package-Inhalte und Package-Buchungsflows |
| `octo/pickups` | Pickup/Dropoff-Felder für Product/Availability/Booking |
| `octo/questions` | Frage-Schemas und questionAnswers Write-Flows |
| `octo/waivers` | Haftungsausschluss-Vorlagen und Submission/Status-Felder |
| `octo/resources` | Availability-Ressourcen und Ressourcen-Zuordnungen |
| `octo/rentals` | rentalDurationId-Verhalten über Product/Availability/Booking |
| `octo/redemption` | Einlösung-Lookup, redeem/unredeem, no-show, credential flows |
| `octo/mappings` | Self-Service Mapping Write/Read-Flows |
| `octo/cart` | Order create/list/update/confirm/cancel flows |
| `octo/gifts` | Gift-Voucher create/list/update/confirm/cancel flows |
| `octo/checkin` | Check-in Lookup und Check-in-Felder für Bookings/Orders/Gifts |
| `octo/cardPayments` | Kartenzahlungs-Flows und Card-Payment-Lookup |
| `octo/memberships` | Membership-Lookup und Membership-Booking-Listing |
| `octo/adjustments` | Erweiterte Booking-Preiseingaben (Anpassungen) |
| `octo/webhooks` | Webhook create/update/list/delete und Trigger-Flows |
| `octo/waitlists` | Wartelisten-Create-Flow |
| `octo/identities` | Identity create/update/delete und identityId-Verknüpfung |
| `octo/campaigns` | Campaign-Listing-Endpunkt |
| `octo/notifications` | Notification-Subscription-CRUD |

### Capability-Objekt-Felder

```typescript
type Capability = {
  id: CapabilityId;          // z.B. "octo/pricing"
  revision: number;          // Versionsnummer
  required: boolean;         // ob Pflicht
  dependencies: CapabilityId[]; // automatisch eingeschlossene Capabilities
  docs: string | null;       // Dokumentations-URL
};
```

### GET /capabilities

Gibt alle vom Supplier unterstützten Capabilities zurück (kein `Octo-Capabilities`-Header nötig).

```
GET https://api.ventrata.com/octo/capabilities/
Authorization: Bearer {api_key}
```

## 4-stufiger Integrationsprozess

### Schritt 1: Dokumentation lesen und planen
- OCTO API und Ventrata-Implementierung kennenlernen
- Endpunkte auswählen (Mindest-Pflicht: Products, Availability, Booking)
- Ventrata empfiehlt die `octo/pricing`-Capability aufgrund verbreiteter dynamischer Preisgestaltung

### Schritt 2: Entwickeln
- Die meisten Reseller schließen die Entwicklung in 2–10 Tagen ab
- EdinExplore (fiktiver Test-Supplier) für Self-Testing nutzen
- Bietet typische Produktkonfigurationen, Buchungen und API-Logs

### Schritt 3: Testen
- Self-Testing mit EdinExplore-Account
- Integration Review bei connectivity@ventrata.com einreichen
- Benötigte Informationen: Firmenname, Logo, Favicon, Lieferantenbeschreibung, Website-Link
- Prüfzeit: 1–2 Werktage
- Können Testbuchungen, Voucher-Muster, Capability-Bestätigungen verlangen

### Schritt 4: Live gehen
- Integration wird zur Ventrata-Partnerliste hinzugefügt
- Im Helpdesk für Supplier-Zugang dokumentiert
- Ventrata-Kunden kontaktieren, um Produkte zu verbinden und Verkauf zu beginnen

## Glossar der OCTO-Begriffe

| Begriff | Definition |
|---------|-----------|
| **Reseller** | Der Distributor, der sich via API mit einem Supplier verbindet, um Produkte weiterzuverkaufen |
| **Supplier** | Der Operator, der Produkte anbietet und Ventrata nutzt |
| **Product** | Eine Attraktion, Aktivität oder Tour, die von einem Supplier angeboten wird |
| **Option** | Eine Produktvariante. Jedes Produkt hat mindestens eine Option |
| **Unit** | Ein Ticket-Typ, z.B. Erwachsener, Kind oder Senior |
| **Unit Item** | Ein Zeileneintrag für eine spezifische Unit innerhalb einer Buchung |
| **Booking** | Eine Reservierung für eine spezifische Produktoption mit einem oder mehreren Unit Items |
| **Voucher** | Ein einzelnes Einlassdokument (Barcode, QR-Code, PDF, etc.) für die gesamte Buchung |
| **Ticket** | Ein Einlassdokument (Barcode, QR-Code, PDF, etc.) für jedes Unit Item |

## Test-Credentials

Test-Credentials werden individuell nach Registrierung auf der Ventrata-Plattform generiert und auf dem Account-Setup-Bildschirm angezeigt. Es gibt **keine öffentlich dokumentierten Test-API-Keys** — jeder Reseller erhält eigene Zugangsdaten.

**Test-Modus:** Header `Octo-Env: test` verwenden
- Verbraucht keine Verfügbarkeit
- Barcodes funktionieren nicht
- Keine Rechnungsstellung

**EdinExplore Test-Account:** Fiktiver Supplier für Self-Testing. Registrierung unter der offiziellen Ventrata-Signup-Seite.

---

**Quellen:**
- https://docs.ventrata.com (Overview)
- https://docs.ventrata.com/getting-started/steps-to-integrate
- https://docs.ventrata.com/getting-started/glossary-of-terms
- https://docs.ventrata.com/getting-started/getting-started
- https://docs.ventrata.com/getting-started/test-credentials
- https://docs.ventrata.com/getting-started/request-capabilities
