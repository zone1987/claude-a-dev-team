# Shopware 6 — Tutorials: Bestellungen (vollständige Referenz)

---

## 1. Bestellung im Admin anlegen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/bestellungen/bestellung-im-admin-anlegen  
**Ab Version:** 6.5.0.0

### Schritt-für-Schritt

**Schritt 1 — Kunden auswählen:**
- Bestellungen > Bestellübersicht > "Bestellung anlegen"
- Kunden aus der Liste wählen oder direkt im Formular anlegen

**Schritt 2 — Produkte hinzufügen:**
- Bereich "Produkte" > "Produkt hinzufügen"
- Preis wird automatisch ermittelt (anpassbar)
- Standard-Steuersatz wird automatisch zugewiesen

**Schritt 3 — Leere Positionen (für nicht-katalogisierte Produkte):**
- Dropdown neben "Produkt hinzufügen" > "Leere Position hinzufügen"
- Name, Bruttopreis, Steuersatz, Menge eingeben

**Schritt 4 — Gutschriften:**
- Dropdown > "Gutschrift hinzufügen"
- Steuersatz wird automatisch berechnet; Bezeichnung und Betrag eingeben

**Schritt 5 — Optionen konfigurieren:**
- Automatische Rabattaktionen aktivieren/deaktivieren
- Bestellsprache festlegen
- Rabatt-Code eingeben
- Zahlungsart wählen
- Rechnungs- und Lieferadresse definieren
- Versandart und -kosten festlegen
- Währung auswählen

**Schritt 6 — Speichern:**
- "Bestellung speichern" → Bestätigungsmail wird automatisch versendet
- Alle Zahlungs-, Versand- und Bestellinfos im Details-Bereich einsehbar

### Tipps
- Versandkosten: Doppelklick auf Eintrag zum manuellen Anpassen
- Position löschen: Checkbox aktivieren + Löschoption
- PayPal-Zahlung: Kunden können nachträglich über ihr Konto bezahlen

---

## 2. Bestellungen exportieren

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/bestellungen-exportieren  
**Ab Version:** 6.4.7.0

### Schritt 1: Neues Profil erstellen

Einstellungen > Import/Export > Profile > Neues Profil anlegen.

**Pflichtfelder (ohne diese schlägt der Export fehl):**
- `id`
- `salesChannelId`
- `orderDateTime`
- `stateId`

Weitere Felder über Dropdown in der Spalte "Datenbank-Eintrag" hinzufügen. Der Wert in "Name" wird zum Spaltennamen im Export.

### Schritt 2: Export starten

Profil "Bestellungen" auswählen, Export starten.

### Schritt 3: Datei herunterladen

Exportierte CSV herunterladen. Empfehlung: OpenOffice (keine ungewollte Formatierung).

---

## 3. Bestellungen mit PayPal

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/bestellungen-mit-paypal  
**Ab Version:** 6.3.0.0

### Grundprinzip

Zahlung und Bestellung sind **getrennte Entitäten**. Die Bestellung entsteht bei "Zahlungspflichtig bestellen" — unabhängig davon, ob die Zahlung abgeschlossen wird.

### Zahlungsstatus-Erklärungen

| Status | Ursache |
|--------|---------|
| Abgebrochen | Kunde klickt "Zurück zum Shop" im PayPal-Fenster |
| Fehlgeschlagen | Zahlung wurde durch Kunden nicht abgeschlossen |
| Unbestätigt | Bestellung ausgelöst, PayPal erhielt keine Transaktion (Browser-Absturz) |

### Kundenoptionen bei fehlgeschlagener Bestellung

Kunden können im eigenen Konto:
- Zahlungsart wechseln (leitet zu Checkout) → Bestellstatus: "In Bearbeitung"
- Bestellung wiederholen (neue Bestellung wird erstellt)

### Feldbezeichnungen: Shopware vs. PayPal

| Shopware | PayPal | Bedeutung |
|----------|--------|-----------|
| `zahlungs_id` | `order_id` | Eindeutige Bestell-ID |
| `tracking_id` | `capture_id` / `transaction_id` / `resource_id` | Zahlungs-Tracking |
| `händler_id` | `merchant_id` / `payer_id` | Händler-Identifikation |

Einsehbar unter: Bestellungen > Übersicht > Bestellung > PayPal

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/bestellungen — Stand: 2026-06*
