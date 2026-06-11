# Shopware 6 – Zahlungsarten (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/Zahlungsarten

---

## Überblick

**Pfad:** Einstellungen > Handel > Zahlungsarten

Listet alle gespeicherten Zahlungsmethoden mit Name, Aktivstatus und Beschreibung.

### Standard-Zahlungsarten (vorinstalliert)
- Nachnahme (Cash on Delivery)
- Rechnung (Invoice)
- Vorkasse (Prepayment)
- Lastschrift (Direct Debit)

> **Hinweis:** Die Verfügbarkeit im Shop hängt von der Zuweisung in den Verkaufskanal-Einstellungen ab.

---

## Zahlungsart erstellen

Schaltfläche „Zahlungsart anlegen"

| Feld | Nr. | Beschreibung |
|---|---|---|
| Name | 1 | Anzeigename der Zahlungsart |
| Technischer Name | 2 | Eindeutiger Bezeichner (Änderung kann bestehende Zahlungsarten deaktivieren!) |
| Position | 3 | Anzeigereihenfolge in der Storefront |
| Beschreibung | 4 | Kurze Erklärung der Zahlungsmethode |
| Logo | 5 | Eigenes Logo hochladen |
| Aktiv | 6 | Zahlungsart aktivieren/deaktivieren |
| Zahlungsartwechsel nach Abschluss | 7 | Kunden dürfen nach Bestellung die Zahlungsart im Account wechseln |

> **Wichtig:** Der technische Name darf nach dem Erstellen nicht mehr geändert werden, wenn die Zahlungsart bereits verwendet wird.

---

## Verfügbarkeitsregel

Bestimmt mithilfe des Rule Builders, unter welchen Bedingungen die Zahlungsart angezeigt wird.

- Neue Regeln können direkt erstellt werden
- Bestehende Regeln können ausgewählt werden
- Typische Bedingungen: Lieferland, Warenkorbwert, Kundengruppe

---

## Zahlungsart im Verkaufskanal zuweisen

Nach dem Anlegen muss die Zahlungsart dem Verkaufskanal zugewiesen werden:
1. Verkaufskanäle > [Kanal auswählen] > Grundeinstellungen > Zahlungsarten
2. Zahlungsart hinzufügen
3. Optional: Standard-Zahlungsart festlegen
