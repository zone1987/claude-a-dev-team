# Aktionscodes – Rabatte & Aktionen

**Pfad:** Admin > Marketing > Rabatte & Aktionen > [Aktion] > Reiter "Allgemein"
**Version:** ab Shopware 6.0.0

## Übersicht der Code-Typen

In jeder Rabattaktion kann unter dem Reiter **Allgemein > Aktionscodes** festgelegt werden, wie Kunden die Aktion aktivieren:

| Typ | Beschreibung | Anwendungsfall |
|-----|--------------|----------------|
| **Kein Aktionscode erforderlich** | Aktion wird automatisch angewendet | Automatische Rabatte (z. B. VIP, Versandkostenfrei) |
| **Festgelegter Aktionscode** | Ein einheitlicher Code für alle Kunden | Allgemeine Rabattaktionen (z. B. Newsletterversand) |
| **Individuelle Aktionscodes** | Einmalige Codes pro Kunde | Personalisierte Angebote, Gewinnspiele |

---

## Kein Aktionscode erforderlich

Die Aktion wird automatisch auf alle Warenkörbe angewendet, die die definierten Bedingungen erfüllen. Der Kunde muss keinen Code eingeben.

**Typische Einsatzszenarien:**
- Versandkostenfrei ab einem Mindestbestellwert
- Kundengruppen-Rabatte
- VIP-Kunden-Rabatte

---

## Festgelegter Aktionscode

Ein Code, den mehrere Kunden verwenden können.

### Konfiguration

1. Option "Festgelegter Aktionscode" wählen
2. Code im Textfeld eingeben (z. B. `SOMMER20`)
3. Speichern

![Festgelegter Aktionscode](../assets/Allgemein_Aktionscodes_Festgelegter-Code.png)

### Nutzungsregeln

- Der Code kann mehrfach eingelöst werden
- Gesamtnutzung und Nutzung je Kunde begrenzen die Verwendungshäufigkeit
- Code ist case-sensitive (Groß-/Kleinschreibung beachten)

### Nachverfolgung

Eingelöste festgelegte Codes sind in der Bestellübersicht filterbar:

1. Bestellungen > Übersicht aufrufen
2. Filter setzen: "Aktionscode" = [Code]
3. Alle Bestellungen mit diesem Code werden angezeigt

---

## Individuelle Aktionscodes

Einmalige Codes für einzelne Kunden. Jeder Code kann nur einmal eingelöst werden.

### Codes erzeugen

1. Option "Individuelle Aktionscodes" wählen
2. Schaltfläche "Codes erzeugen" klicken
3. Anzahl gewünschter Codes eingeben
4. Optional: Präfix/Suffix für Codes definieren
5. Generieren bestätigen

![Individuelle Aktionscodes](../assets/Allgemein_Aktionscodes_Individuelle-Codes.png)
![Codes erzeugen Dialog](../assets/Allgemein_Aktionscodes_Individuellen-Code-erzeugen.png)

### Regeln für individuelle Codes

> **Wichtig:** Es ist nicht möglich, mehrere unterschiedliche individuelle Codes aus einer einzigen Promotion gleichzeitig anzuwenden.

- Jeder generierte Code ist einmalig
- Nach Einlösung ist der Code deaktiviert
- Neue Codes können jederzeit nachgeneriert werden

### Nachverfolgung individueller Codes

**In der Aktionsdetailansicht:**
- Marketing > Rabatte & Aktionen aufrufen
- Gewünschte Aktion öffnen
- Reiter "Aktionscodes" zeigt alle Codes mit Status (eingelöst / nicht eingelöst)

**In der Bestellübersicht:**
- Bestellungen > Übersicht aufrufen
- Filter: "Aktionscode" = [gewünschter Code]
- Zugehörige Bestellung wird angezeigt

![Individueller Code Übersicht](../assets/1_Individuell_code_DE.png)
![Bestellübersicht Codes](../assets/2_Uebersicht_DE.png)

---

## Codes in der Storefront einlösen

Kunden geben Codes im Warenkorb ein:

1. Warenkorb oder Off-Canvas-Warenkorb öffnen
2. Feld "Gutschein-Code eingeben" finden
3. Code eingeben
4. Bestätigung-Button klicken
5. Rabatt wird in der Artikelliste angezeigt

---

## Häufige Fragen

### Kann ich einen Code für mehrere Aktionen nutzen?

Nein. Jeder Code ist einer Aktion zugeordnet. Es können jedoch mehrere Aktionen gleichzeitig aktiv sein und verschiedene Codes angewendet werden.

### Was passiert wenn ein Code abgelaufen ist?

Ist die Aktion nicht mehr aktiv (Gültigkeitszeitraum abgelaufen oder deaktiviert), wird der Code als ungültig abgelehnt.

### Kann ich individuelle Codes exportieren?

Codes können aus der Aktionsdetailansicht exportiert werden, um sie z. B. per Newsletter zu versenden.
