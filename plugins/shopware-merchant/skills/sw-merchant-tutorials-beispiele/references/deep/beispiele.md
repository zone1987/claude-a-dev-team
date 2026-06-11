# Shopware 6 — Anwendungsbeispiele (vollständige Referenz)

---

## 1. Dynamic Access — Beispielkonfiguration

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/dynamic-access-beispielkonfiguration  
**Ab Version:** 6.4.4.0 (Erweiterung Dynamic Access erforderlich)

### Szenario: Länderspezifische Kategorien

Ziel: Kunden sehen je nach Rechnungsland unterschiedliche Kategorien (DE sieht AT/CH-Produkte, nicht DE-Produkte usw.)

**Schritt 1 — Regeln erstellen (Einstellungen > Rule Builder):**
- Regel "Kunden aus Deutschland": Bedingung `Rechnungsland > Ist eine von > Deutschland`
- Regel "Kunden aus Österreich": analog
- Regel "Kunden aus der Schweiz": analog

**Schritt 2 — Kategorien erstellen (Kataloge > Kategorien):**
- "Spezialitäten aus Deutschland"
- "Spezialitäten aus Österreich"
- "Spezialitäten aus der Schweiz"

**Schritt 3 — Dynamic Access in Kategorien zuweisen:**
- Kategorie DE: Regeln AT + CH zuweisen (= wird nur für AT/CH-Kunden sichtbar)
- Kategorien AT/CH: jeweils entsprechende Regel

**Schritt 4 — Produkte:** Für jeden Artikel ebenfalls Dynamic Access-Regeln setzen (Kataloge > Produkte > Allgemein > Dynamic Access), damit sie nicht über die Suche auffindbar sind.

### Szenario: VIP-Kategorie

Regel: `Anzahl Bestellungen >= 100` → Kategorie nur für Vielkäufer sichtbar.

---

## 2. Rabatte und Aktionen — Anwendungsbeispiele

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/rabatte-und-aktionen-anwendungsbeispiele

### Beispiel 1: Versandkostenfrei
- Aktionscode: keiner
- Rabatt: Versandkosten | Prozentual | 100 %

### Beispiel 2: 25 % Rabatt auf alle Artikel
- Aktionscode: `2022_25`
- Rabatt: Warenkorb | Prozentual | 25 %

### Beispiel 3: Festpreis für bestimmte Artikel
- Voraussetzung: Regel "Sales Oberteile" (Rule Builder)
- Aktionscode: `ALLfor10`
- Rabatt: Warenkorb | Nur ausgewählte Produkte: aktiv | Produktregel: Sales Oberteile | Fester Stückpreis | 10 €

### Beispiel 4: Mehrfach-Rabatte (ein Code)
- Mehrere Rabatte kombinieren: z. B. Versandkosten 100 % + Warenkorb 25 %

### Beispiel 5: VIP-Kunden (automatisch)
- Voraussetzung: Regel `Anzahl Bestellungen >= 100`
- Kein Aktionscode — automatische Anwendung
- Rabatt: Warenkorb | Prozentual | 5 %

### Beispiel 6: Packages (Kauf 3 zum Sonderpreis)
- Aktionscode: `AKTION`
- Bedingungen: Produkt-Set | Anzahl: 3 | Preis aufsteigend | Produktregel: Sales Oberteile
- Rabatt: Set-Gruppe-1 | Fester Stückpreis | 10 €

### Beispiel 7: Bundles (Hose + T-Shirt)
- Voraussetzung: Regeln "Sales Hosen" + "Sales T-Shirts"
- 2 Set-Gruppen konfigurieren
- Rabatt: Gesamtes-Set | Festpreis | 20 €

### Beispiel 8: Kauf 3, Zahl 2
- Aktionscode: `kauf3`
- Produkt-Set: 3 Stück, aufsteigende Sortierung, Regel: Sales T-Shirt
- Rabatt: 1. Produkt aufsteigend | Prozentual | 100 % (günstigstes gratis)

### Beispiel 9: Rabatt für Newsletter-Empfänger
- Bedingung: Kunden-Regel mit `Newsletter-Opt-in`
- Rabatt: Warenkorb | Prozentual | 10 % | Maximalwert: 150 €

### Beispiel 10: Rabatt für Kundengruppe
- Bedingung: Kunden-Regel `Standard Kundengruppe`
- Priorität: 1 | Verkaufskanal auswählen

### Beispiel 11: Versandkostenfrei ab Warenkorbwert
- Regel: `Warenkorbwert >= 50`
- Staffelung möglich: ab 25 € → 50 %, ab 100 € → 100 %
- Wichtig: Höherwertige Rabatte in "Nicht kombinieren mit" ausschließen

### Beispiel 12: Rabatt auf Kategorie-Produkte
- Regel: `Position in Kategorie | Mind. eine | Ist eine von | [Kategorie]`

### Beispiel 13: Rabatt für Hersteller-Produkte
- Regel: `Position mit Hersteller | Mind. eine | Ist eine von | [Hersteller]`

### Beispiel 14: Gratisartikel
- Gratisartikel mit Tag "gratis" kennzeichnen
- Dynamische Produktgruppe "Gratisartikel": Tag = gratis
- Rabatt: Warenkorb | Nur ausgewählte Produkte: aktiv | Fester Stückpreis | 0 €

### Beispiel 15: Rabatt auf Zielartikel
- Regel: `Position | Mind. eine | Ist eine von | [Produkt]`
- Rabatt: Warenkorb | Nur ausgewählte Produkte | Prozentual

---

## 3. Rule Builder — Beispielregeln

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/rule-builder-beispielregeln  
**Ab Version:** 6.5.0.0

### Versand-Regeln

| Anwendungsfall | Bedingung | Verwendung |
|----------------|-----------|------------|
| Speditionsversand | Position mit Tag = "Spedition" | Versandart-Verfügbarkeitsregel |
| Nachnahme | Verwendete Zahlungsart = Nachnahme | Versandart-Verfügbarkeitsregel |
| PLZ-Versand | Lieferadresse: PLZ = [PLZ] | Versandart-Verfügbarkeitsregel |
| Versandkosten-Ausschluss | Position mit spez. Custom Field | Versandart deaktivieren |

### Zahlungsarten-Regeln

| Anwendungsfall | Bedingung |
|----------------|-----------|
| Kundengruppe | Kundengruppe = [Gruppe] |
| Mindestbestellwert | Warenkorbwert >= [Betrag] |

### Rabatt-Regeln

| Anwendungsfall | Bedingung |
|----------------|-----------|
| Versandkostenfrei ab 50 € | Gesamtsumme >= 50 |
| VIP-Rabatt | Anzahl Bestellungen >= 100 |

---

## 4. Flow Builder — Beispielflows

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/flow-builder-beispielflows  
**Ab Version:** 6.4.6.0

### Kunden: Neue Kunden mit Tag versehen

- **Trigger:** Checkout / Customer / Register
- Bedingung: Kundenland prüfen (USA, AT, CH)
- Aktion: Entsprechendes Tag zuweisen

### Kunden: Artikel nur einmal bestellbar

1. Regel: "Position im Warenkorb ist eine von [Artikel]"
2. Flow "Order placed" erweitern
3. Bedingung mit Regel + Aktion: Tag zuweisen
4. Mit Dynamic Access: Artikel für getaggte Kunden ausblenden

### Dokumente: Rechnung automatisch versenden

- **Trigger:** Checkout / Order / Placed
- Aktionen:
  1. Dokument erzeugen (Typ: Invoice)
  2. E-Mail verschicken (Anhang: erzeugtes Dokument)

### Benachrichtigungen: Lager bei bezahlter Bestellung

- **Trigger:** State Enter / Order Transaction / State / Paid
- Aktionen:
  1. Dokumente erzeugen (Invoice, Lieferschein)
  2. E-Mail an eigenen Empfänger (Lager)

### Benachrichtigungen: Slack-Webhook

Erfordert Extension "Flow Builder Professional" (Webhook-Aktion).

**Shopware Flow-Konfiguration:**
- Trigger: Checkout / Order / Placed
- Aktion: URL aufrufen (POST)
- Body-Typ: Raw

```json
{
  "orderURL": "http://doku1.test.shopware.in/admin#/sw/order/detail/{{ order.id }}",
  "orderPositions": "{% for lineItem in order.LineItems %}{{ lineItem.payload.productNumber }} - {{ lineItem.label }}{% endfor %}",
  "orderNumber": "{{ order.orderNumber }}",
  "orderCustomerAdress": "{% set billingAddress = order.addresses.get(order.billingAddressId) %}{{ billingAddress.company }} {{ billingAddress.firstName }} {{ billingAddress.lastName }} {{ billingAddress.street }} {{ billingAddress.zipcode }} {{ billingAddress.city }} {{ billingAddress.country.translated.name }}"
}
```

---

## 5. Tags — Anwendungsbeispiele

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/tags-anwendungsbeispiele  
**Ab Version:** 6.0.0

Tags können vergeben werden an: Produkte, Kategorien, Medien, Kunden, Bestellungen, Versandarten, Newsletter-Empfänger, Landingpages.

| Beispiel | Anwendung |
|----------|-----------|
| Google Shopping Export | Tag "Google Shopping" → Dynamische Produktgruppe filtern |
| Sperrgut-Versand | Tag "Sperrgut" → Versandart-Regel: "Position mit Tag" |
| Kundenspezifische Rabatte | Kunden taggen → Rule Builder → Rabattaktion |
| Dynamische Produktgruppen | Tag "Sale" → Gruppe → Kategorie |
| Flow Builder Integration | Bedingung nach Tag → Personalisierte Aktionen |

---

## 6. Advanced Search — Beispiele

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/beispiele/advanced-search-beispiele  
**Ab Version:** 6.4.1.0 (Elasticsearch/OpenSearch + Advanced Search Erweiterung erforderlich)

### Konfiguration (Einstellungen > Erweiterungen > Shopware Erweiterte Suche)

| Funktion | Beschreibung |
|----------|-------------|
| Produktsuche | Felder auf "Durchsucht" stellen (z. B. Produktnummer, Name) |
| Teiltreffer | Findet Begriffe auch in der Wortmitte |
| Zusammengesetzte Wörter | Erkennt Treffer über mehrere Wörter |
| Herstellersuche | Herstellerliste in Suche anzeigen |
| Boosting | Bevorzugte Produkte priorisieren (Stream-basiert) |
| Aktionen | Suchbegriff → Weiterleitung zu Produkt/URL |
| Synonyme | Alternative Suchbegriffe konfigurieren |

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/beispiele — Stand: 2026-06*
