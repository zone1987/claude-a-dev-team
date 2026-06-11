# B2B-Suite – Administration & Kundenaccount

**Quellen**:  
- https://docs.shopware.com/de/shopware-6-de/erweiterungen/b2b-suite-administration  
- https://docs.shopware.com/de/shopware-6-de/erweiterungen/b2b-suite-kundenaccount  
**Plan**: Shopware Evolve (oder höher)

## WICHTIGER HINWEIS: Deprecation

> **Die B2B-Suite wird nicht mehr weiterentwickelt!**
> Alle neuen Features werden über die **B2B-Components** realisiert.
> Support-Ende: **nach Shopware 6.8**
> Migrationsfrist: **bis 24. Mai 2025** (auf B2B-Components umstellen)

Für neue Projekte: **B2B-Components** verwenden (Teil von Shopware Commercial ab Evolve Plan).

---

## Überblick (B2B-Suite Legacy)

Die B2B-Suite bietet Unternehmen erweiterte Organisationsstrukturen für ihre Shopware-6-Instanz:
- Mehrstufige Unternehmenshierarchien
- Rollenbasierte Berechtigungen
- Budgets und Genehmigungsworkflows

---

## Rollen in der B2B-Suite

| Rolle | Beschreibung |
|---|---|
| **Debitor** | Zentrales Unternehmenskonto (primäres B2B-Konto) |
| **Field Service Representative** | Außendienstmitarbeiter; kann auf Kundenkonten zugreifen |
| **Kontakt** | Mitarbeiterkonto innerhalb des Debitors |

---

## Administration (Admin-Perspektive)

### Konfigurationsort
- B2B-Konfiguration ist **nicht als separater Menüpunkt** vorhanden
- Integration direkt in die **Kundenverwaltung**: Kunden > [Kundename] > B2B

### Angebotsverwaltung (Offers)

Workflow für kundenindividuelle Preise:

1. Kunde stellt Preisanfrage über Storefront-Kundenkonto
2. Admin sieht Anfrage in der **Angebotsverwaltung**
3. Admin kann:
   - **Annehmen**: Angebot zu gewünschtem Preis bestätigen
   - **Ablehnen**: Anfrage zurückweisen
   - **Gegenangebot**: Eigenen Preis vorschlagen

**Status-Farbcodes**:
- Grau: Noch nicht bearbeitet (wartet auf Review)
- Rot: Abgelehnt
- Blau: Angenommen / aktiv

---

## Kundenaccount-Funktionen (Storefront-Perspektive)

### Dashboard-Bereiche

| Bereich | Funktion |
|---|---|
| **Dashboard** | Übersicht aller B2B-Funktionen |
| **Unternehmen** | Rollen, Kontakte, Adressen, Budgets, Quoten verwalten |
| **Statistiken** | Filterbare Bestellanalysen |
| **Bestellungen** | Bestellhistorie, ausstehende Genehmigungen |
| **Bestelllisten** | Wiederverwendbare Produktlisten für regelmäßige Bestellungen |
| **Schnellbestellung** | Massenprodukt-Eingabe (Artikelnummer + Menge) |
| **Angebote** | Angebotsanfragen stellen und verwalten |
| **Bestellnummern** | Interne Produktnummerierung |

### Rollen & Berechtigungen (Kundensicht)
Debitoren können Unterkonten (Kontakte) mit spezifischen Rechten anlegen:
- Bestellen erlaubt
- Bestelllimit (Budget)
- Zugriff auf bestimmte Bereiche

### Budgets & Quoten
- Ausgabelimits pro Zeitraum (z. B. 1.000 € / Monat)
- Bei Überschreitung: Bestellung geht in Genehmigungsworkflow
- Genehmigung durch Vorgesetzten/Administrator

---

## Migration zu B2B-Components

### Warum migrieren?
- B2B-Suite: Keine neuen Features, End of Support nach 6.8
- B2B-Components: Aktiv entwickelt, Teil von Shopware Commercial

### Verfügbare B2B-Components (ab Evolve Plan)
- Quick Order (Schnellbestellung)
- Freigabeprozesse (Bestellgenehmigungen)
- Angebote (Quotes)
- Employee Management
- Order Lists

### Migrationsleitfaden
→ https://docs.shopware.com/de/shopware-6-de/features/b2b-components
