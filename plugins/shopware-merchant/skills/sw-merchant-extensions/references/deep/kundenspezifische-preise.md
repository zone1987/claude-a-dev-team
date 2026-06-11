# Kundenspezifische Preise – Individuelle Preisgestaltung

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/kundenspezifische-preise  
**Plan**: Shopware Beyond (exklusiv)  
**Voraussetzung**: Shopware Commercial Extension aktiv

## Überblick

**Kundenspezifische Preise** ermöglicht individuell kalkulierte Preise für einzelne Kunden –
optimiert für große B2B-Shops mit ERP-Integration.

Besonderheit: "Du kannst sowohl Listenpreise als auch Staffelpreise oder währungsabhängige
Preise individuell auf den Kunden zuschneiden"

---

## WICHTIG: API-Only-Ansatz

> **Es gibt KEINE UI im Admin für kundenspezifische Preise!**
> Die Funktion arbeitet **ausschließlich über API-Calls**.
> Dies ist designbedingt – für die Bulk-Synchronisation aus ERP-Systemen optimiert.

---

## Technische Grundlagen

### Datenbankstruktur
Kundenspezifische Preise werden in einer eigenen Tabelle gespeichert:
- Kunden-ID (customer_id)
- Produkt-ID / Varianten-ID (product_id)
- Preis-Definition (JSON mit Brutto/Netto, Staffeln, Währungen)

### Keine Vererbung
> Im Gegensatz zu Produktvarianten: Keine Preisinheritanz bei kundenspezifischen Preisen.
> Für jede Variante muss der Preis **direkt mit der Varianten-ID** gesetzt werden.
> (Nicht über die Eltern-Produkt-ID)

---

## API-Endpunkte

### Preise setzen (POST/PATCH)
```
POST /api/customer-price
PATCH /api/customer-price/{id}
```

### Bulk-Synchronisierung
```
POST /api/_action/sync
```
Mit Body für Massenzuweisung von Preisen (für ERP-Integration empfohlen)

### Preise abrufen
```
GET /api/customer-price?filter[customer.id]=<customer-id>
```

---

## Preisdefinition (JSON-Schema)

```json
{
  "customerId": "uuid-des-kunden",
  "productId": "uuid-der-variante",
  "price": [
    {
      "currencyId": "b7d2554b0ce847cd82f3ac9bd1c0dfca",
      "gross": 19.99,
      "net": 16.80,
      "linked": true
    }
  ],
  "quantityStart": 1,
  "quantityEnd": 9
}
```

### Staffelpreise (Quantity Ranges)
Mehrere Preisregeln pro Kunde/Produkt für unterschiedliche Mengen:

| quantityStart | quantityEnd | Preis |
|---|---|---|
| 1 | 9 | 19,99 € |
| 10 | 49 | 17,99 € |
| 50 | null | 15,99 € |

---

## Storefront-Verhalten

| Zustand | Anzeige |
|---|---|
| Kunde eingeloggt | Kundenspezifischer Preis wird sofort angezeigt |
| Kunde ausgeloggt | Standard-Listenpreis wird angezeigt |
| Staffelpreis | Abhängig von gewählter Menge (Änderung im Preisbereich) |

---

## Integration mit ERP-Systemen

Typischer Workflow:
1. ERP (z. B. SAP, Microsoft Dynamics) hält individuelle Preise
2. Bei Änderungen: ERP ruft Shopware Sync-API auf
3. Shopware speichert neue Preise in Datenbank
4. Beim nächsten Login des Kunden: neue Preise sofort sichtbar

### Performance-Hinweis
- System ist für große Datenvolumen ausgelegt ("Speed-orientierte API")
- Bulk-Sync via `_action/sync` statt Einzelaufrufen verwenden

---

## Zugriff auf API-Dokumentation

Vollständige API-Dokumentation: https://shopware.stoplight.io
(Kategorie: Customer Price / Kundenpreise)
