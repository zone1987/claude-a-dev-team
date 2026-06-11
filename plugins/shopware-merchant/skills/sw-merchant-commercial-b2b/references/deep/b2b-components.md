# Shopware B2B Components – Vollständige Dokumentation

## Überblick

Die B2B Components sind ein Set von Funktionalitäten für den B2B-Handel in Shopware 6. Sie aktivieren essentielle B2B-Workflows über die Shopware Commercial Extension.

**Verfügbarkeit:** Evolve-Plan und höher
**Aktivierung:** Einzeln pro Kunde oder über Kundengruppen-Registrierungsformulare

### B2B für einzelne Kunden aktivieren
Pfad: Kunden → Übersicht → Kunde auswählen → B2B-Bereich → Aktivieren

### B2B für Kundengruppen aktivieren
Pfad: Einstellungen → Kunden → Kundengruppen → Registrierungsformular mit B2B-Option

---

## Feature 1: Angebots-Management (Quote Management)

**Verfügbar ab:** Evolve-Plan

### Workflow
1. Kunden befüllen den Warenkorb und fordern ein Angebot an
2. Händler sieht die Anfrage unter: Bestellungen → Angebote
3. Händler überprüft und antwortet mit:
   - Individuellen Preisen oder Rabatten
   - Optionalem Ablaufdatum
4. Kunden erhalten das Angebot und können es annehmen/ablehnen

### Für Sales Agent
Außendienstmitarbeiter können über die Sales Agent App Angebote erstellen:
- Allgemeine Infos: Kundenwahl, Verkaufskanal
- Positionen: Produkte hinzufügen mit Standard- und Sonderpreisen
- Rabatte: Absolut oder prozentual
- Dokumente: Auto-PDF oder Upload
- Sendungseinstellungen: Ablaufdatum, persönliche Nachricht

---

## Feature 2: Mitarbeiterverwaltung (Employee Management)

**Verfügbar ab:** Shopware 6.5.6.0 (Evolve+)

### Funktionsumfang
- Unternehmen registrieren Mitarbeiter im B2B-Bereich
- Rollen zuweisen mit spezifischen Berechtigungen:
  - Mitarbeiterverwaltung
  - Rollenverwaltung
  - Bestellungen

### Mitarbeiter-Rollen
Administratoren legen Rollen fest und bestimmen, welche Aktionen Mitarbeiter ausführen dürfen.

**Pfad im Admin:** Kunden → B2B → Mitarbeiter

---

## Feature 3: Bestellgenehmigungen (Order Approvals)

**Verfügbar ab:** Shopware 6.5.8.0 (Evolve+)

### Funktionsweise
1. Händler erstellt Genehmigungsregeln je Rolle
2. Regel definiert: Wer muss Bestellungen genehmigen? Unter welchen Bedingungen?
   - Beispiel: Bestellwert über 1.000 € benötigt Manager-Genehmigung
   - Beispiel: Bestimmte Versandmethoden benötigen Freigabe
3. Bestellung wird bei Genehmigungspflicht pausiert
4. Genehmigender Mitarbeiter erhält Benachrichtigung und kann freigeben/ablehnen

---

## Feature 4: Organisationseinheiten (Organizational Units)

**Verfügbar ab:** Evolve+

### Anwendungsfälle
- Multi-Standort-Unternehmen (z.B. Filialen)
- Bildungseinrichtungen mit Abteilungen
- Konzerne mit Tochtergesellschaften

### Funktionen je Einheit
- Eigene Bestellhistorie
- Separate Lieferadressen
- Eigene Benutzer und Rollen
- Unabhängige Budget-Verwaltung

---

## Feature 5: Erweiterte Produktkataloge

**Verfügbar ab:** Evolve+

Händler können die Sichtbarkeit von Produktkategorien je Organisationseinheit einschränken:
- Im Storefront: Produkte nur für bestimmte Einheiten sichtbar
- Im Admin: Kategorien für bestimmte Einheiten freigeben/sperren

---

## Feature 6: Budgets

**Verfügbar ab:** Shopware 6.7.4.0 (Evolve+)

### Konfiguration
- Ausgabelimits für Organisationseinheiten festlegen
- Automatische Erneuerungsoptionen (täglich/monatlich/jährlich)
- Benachrichtigungen bei Schwellenwert-Annäherung

### Verhalten
- Mitarbeiter können nicht über ihr Budget hinaus bestellen
- Genehmiger können Budget-Überschreitungen manuell freigeben

---

## Feature 7: B2B Kundenspezifische Preise

**Verfügbar ab:** Shopware 6.7.8.0 (Evolve+)

Prozentuale, fixe oder gestaffelte Rabatte basierend auf:
- Zugewiesene Regeln für Organisationseinheiten
- Kunden-Tags

**Wichtig:** Dies ist die B2B-interne Variante. Die vollständige kundenspezifische Preisgestaltung per API ist ein Beyond-Feature (→ `sw-merchant-commercial-custom-pricing`).

---

## Feature 8: Schnell-Bestellungen (Quick Orders)

**Verfügbar ab:** Evolve+

Beschleunigter Bestellprozess für wiederkehrende B2B-Käufer:

**Methode 1: Produktnummer-Suche**
- Kunden geben Produktnummern direkt ein
- System ergänzt Produktname und Preis automatisch

**Methode 2: CSV-Upload**
```
product_number,quantity
SW-100,5
SW-200,10
SW-300,2
```

Beide Methoden leiten direkt in den Warenkorb weiter.

---

## Feature 9: Einkaufslisten (Shopping Lists)

**Verfügbar ab:** Evolve+

### Kunden-Einkaufslisten
- Kunden erstellen persönliche Listen für häufige Käufe
- Listen können gespeichert, benannt und verwaltet werden
- Direkt in Warenkorb übernehmbar

### Vorkonfigurierte Listen (Händler)
- Händler erstellen Listen für spezifische Anwendungsfälle
- Zur Verfügung stellen für Kundengruppen oder Einzelkunden
- Beispiel: „Standard-Bürobedarf" für Firmenkunden

---

## Feature 10: Sales Agent (Außendienst)

Separater Skill: `sw-merchant-commercial-sales-agent`

Die Sales Agent App ermöglicht Außendienstmitarbeitern:
- Kundendaten einsehen und verwalten
- Bestellungen direkt für Kunden erstellen
- Angebote erstellen und versenden

---

## Aktivierungsübersicht

| Feature | Plan | Mindestversion |
|---|---|---|
| Angebots-Management | Evolve+ | 6.5.x |
| Mitarbeiterverwaltung | Evolve+ | 6.5.6.0 |
| Bestellgenehmigungen | Evolve+ | 6.5.8.0 |
| Organisationseinheiten | Evolve+ | 6.5.x |
| Erweiterte Produktkataloge | Evolve+ | 6.5.x |
| Budgets | Evolve+ | 6.7.4.0 |
| B2B Kundenpreise | Evolve+ | 6.7.8.0 |
| Schnell-Bestellungen | Evolve+ | 6.5.x |
| Einkaufslisten | Evolve+ | 6.5.x |
| Sales Agent | Evolve+ | 6.5.0.0 |

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/commercial-features/b2b-components (Stand: 2026-06)*
