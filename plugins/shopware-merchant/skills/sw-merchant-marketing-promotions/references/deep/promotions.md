# Rabatte & Aktionen

**Pfad:** Admin > Marketing > Rabatte & Aktionen
**Version:** ab Shopware 6.0.0 (aktuell 6.7.0.0)

## Beschreibung

Der Menüpunkt Rabatte & Aktionen bietet ein Modul, mit dem Rabattaktionen für Verkaufskanäle angelegt werden können. Aktionen können zeitlich begrenzt, mit Aktionscodes versehen und über den Rule Builder mit komplexen Bedingungen konfiguriert werden.

## Übersicht

Die Übersichtsseite zeigt alle vorhandenen Aktionen in einer Liste. Über das Kontextmenü können Aktionen bearbeitet oder gelöscht werden.

![Übersicht Rabatte & Aktionen](../assets/rabatt_overviewpng.png)

---

## Neue Rabattaktion anlegen

### 1. Allgemein

Reiter für grundlegende Einstellungen der Aktion.

#### Allgemeine Einstellungen

| Feld | Beschreibung |
|------|--------------|
| **Name** | Bezeichnung der Rabattaktion |
| **Priorität** | Reihenfolge bei mehreren gleichzeitigen Aktionen (höherer Wert = höhere Priorität) |
| **Gültig ab** | Startzeitpunkt (optional) |
| **Gültig bis** | Endzeitpunkt (optional) |
| **Gesamtnutzung** | Wie oft darf die Aktion insgesamt verwendet werden |
| **Nutzung je Kunde** | Wie oft darf ein einzelner Kunde die Aktion nutzen |
| **Aktiv** | Schalter zum Aktivieren/Deaktivieren der Aktion |

![Allgemeine Einstellungen](../assets/Promotions_AllgemeineEinstellungen_DE.png)

> **Hinweis:** Das Feld "Priorität" entscheidet bei mehreren gleichzeitig gültigen Aktionen, welche zuerst angewendet wird.

---

### 2. Aktionscodes

Drei Varianten für die Aktivierung einer Aktion:

#### Kein Aktionscode erforderlich
Die Aktion wird automatisch auf alle zutreffenden Warenkörbe angewendet. Kein Code notwendig.

#### Festgelegter Aktionscode
Ein einheitlicher Code, den mehrere Kunden verwenden können.

- Code wird vom Händler definiert (z. B. `SOMMER20`)
- Kann mehrfach eingelöst werden (begrenzt durch Gesamtnutzung/Nutzung je Kunde)

![Festgelegter Aktionscode](../assets/Allgemein_Aktionscodes_Festgelegter-Code.png)

#### Individuelle Aktionscodes
Einmalige Codes für einzelne Kunden.

- Codes werden manuell oder automatisch generiert
- Jeder Code kann nur einmal eingelöst werden
- Für Newsletter-Aktionen oder personalisierte Angebote geeignet

![Individuelle Aktionscodes](../assets/Allgemein_Aktionscodes_Individuelle-Codes.png)
![Code erzeugen](../assets/Allgemein_Aktionscodes_Individuellen-Code-erzeugen.png)

> **Hinweis:** Es ist nicht möglich, mehrere unterschiedliche individuelle Codes aus einer einzigen Promotion gleichzeitig anzuwenden.

---

### 3. Bedingungen

Definiert, für wen und unter welchen Umständen die Aktion gilt.

#### Voraussetzungen

Legt fest, ob Kunden bestimmte Voraussetzungen erfüllen müssen.

![Voraussetzungen](../assets/Marketing-Rabatte-Voraussetzungen.png)

#### Regelbasierte Bedingungen

Vier Regeltypen stehen zur Verfügung:

| Regeltyp | Beschreibung |
|----------|--------------|
| **Kunden-Regeln** | Zielgruppe eingrenzen (z. B. Kundengruppe, Newsletter-Status) |
| **Warenkorb-Regeln** | Warenkorb-Bedingungen setzen (z. B. Mindestbestellwert) |
| **Aktion auf Produkt-Sets** | Komplexe Produktkombinationen mit Set-Gruppen |
| **Bestellungsregeln** | Zahlungs- oder Versandartbeschränkungen |

![Regelbasierte Bedingungen](../assets/Bedingungen_Regelbasierte-Bedingungen.png)
![Produkt-Sets](../assets/Bedingungen_Regelbasierte-Bedingungen_Produkt-Sets.png)

##### Set-Gruppen-Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Modus** | Anzahl, Bruttopreis oder Nettopreis |
| **Wert** | Anzahl/Betrag zum Erfüllen der Bedingung |
| **Sortierung** | Auf- oder absteigend nach Kaufpreis |
| **Produktregeln** | Rule-Builder-Bedingungen für Produktauswahl |

#### Erweiterte Auswahl

Über die erweiterte Auswahl können weitere Regeln für Produkte innerhalb der Aktion definiert werden.

![Erweiterte Auswahl](../assets/Rabatte_ErweiterteAuswahl_DE.png)
![Erweiterte Auswahl Regeln](../assets/Rabatte_ErweiterteAuswahl-Regeln_DE.png)

---

### 4. Rabatte

Konfiguration des eigentlichen Rabatts.

#### "Anwenden auf" Kategorien

| Option | Beschreibung |
|--------|--------------|
| Gesamter Warenkorb | Rabatt auf den gesamten Warenkorbwert |
| Versandkosten | Rabatt nur auf die Versandkosten |
| Gesamtes Produktset | Rabatt auf ein definiertes Produktset |
| Spezifische Set-Gruppen | Rabatt nur auf ausgewählte Set-Gruppen |

#### Rabattarten

| Typ | Beschreibung |
|-----|--------------|
| **Absolut** | Festbetrag (z. B. 10 € Rabatt) |
| **Prozentual** | Prozentualer Abzug (mit optionaler Obergrenze in €) |
| **Festpreis / Stückpreis** | Produkt wird auf einen festgelegten Preis gesetzt |

![Rabatt Konfiguration](../assets/Rabatte_Rabatt.png)

---

## Storefront-Anwendung

### Gutschein-Code eingeben

Kunden können Aktionscodes im Warenkorb oder im Off-Canvas-Warenkorb eingeben:

1. Feld "Gutschein-Code eingeben" aufrufen
2. Code eingeben
3. Bestätigung anklicken

Rabatte werden nach Eingabe in der Artikelübersicht angezeigt.

![Off-Canvas-Warenkorb](../assets/OffCanvas-Warenkorb.png)
![Warenkorb](../assets/Warenkorb.png)
![Off-Canvas-Warenkorb mit Rabatt](../assets/OffCanvas-Warenkorb-Rabatt.png)
![Warenkorb mit Rabatt](../assets/Warenkorb-Rabatt.png)

### Darstellung eingelöster Gutscheincodes

**Individueller Code:**
- Sichtbar in Marketing > Rabatte & Aktionen
- Filter in der Bestellübersicht nach "Aktionscode" möglich

**Festgelegter Code:**
- Kann mehrfach verwendet werden
- Filterbar in der Bestellübersicht nach Code

![Individueller Code Übersicht](../assets/1_Individuell_code_DE.png)
![Übersicht eingelöste Codes](../assets/2_Uebersicht_DE.png)

---

## 15 Praktische Anwendungsbeispiele

### Beispiel 1: Versandkostenfrei

**Ziel:** Alle Kunden erhalten kostenlosen Versand ohne Code.

| Einstellung | Wert |
|-------------|------|
| Aktionscode | Kein Code erforderlich |
| Anwenden auf | Versandkosten |
| Rabattart | Prozentual: 100% |

### Beispiel 2: 25% Rabatt auf alle Artikel

| Einstellung | Wert |
|-------------|------|
| Aktionscode | Festgelegt: `2022_25` |
| Anwenden auf | Gesamter Warenkorb |
| Rabattart | Prozentual: 25% |

### Beispiel 3: Festpreis für bestimmte Artikel

| Einstellung | Wert |
|-------------|------|
| Aktionscode | `ALLfor10` |
| Produktregel | Rule Builder: gewünschte Produkte |
| Rabattart | Festpreis: 10 € |

### Beispiel 4: Mehrfach-Rabatte kombinieren

Kombiniere in einer Aktion mehrere Rabatte, z. B.:
- 100% Versandkostenrabatt
- 25% Warenkorbrabatt

### Beispiel 5: VIP-Kunden-Rabatt

| Einstellung | Wert |
|-------------|------|
| Kunden-Regel | Mindestens 100 abgeschlossene Bestellungen |
| Aktionscode | Kein Code erforderlich |
| Rabattart | Prozentual: 5% |

### Beispiel 6: Pakete / Packages

Kaufe 3 bestimmte Artikel und erhalte jeden für 10 € statt 20 €:
- Produktgruppe: 3 Artikel (Set-Gruppe)
- Festpreis je Artikel: 10 €

### Beispiel 7: Bundles

Kombiniere zwei Produktgruppen (z. B. Hose + T-Shirt) mit festem Paketpreis:
- Set-Gruppe 1: Hose
- Set-Gruppe 2: T-Shirt
- Festpreis für das Bundle

### Beispiel 8: Kaufe 3, zahle 2

**Ziel:** Beim Kauf von 3 T-Shirts ist das günstigste gratis.

| Einstellung | Wert |
|-------------|------|
| Aktionscode | `kauf3` |
| Set-Gruppe | Modus: Anzahl, Wert: 3, Sortierung: aufsteigend nach Preis |
| Anwenden auf | 1. Produkt der Set-Gruppe |
| Rabattart | Prozentual: 100% |

![Kaufe 3 zahle 2 Konfiguration](../assets/Beispiel_Kaufe3Zahle2.PNG)

### Beispiel 9: Newsletter-Empfänger-Rabatt

| Einstellung | Wert |
|-------------|------|
| Kunden-Regel | Kunde ist Newsletter-Empfänger |
| Rabattart | Prozentual: 10%, max. 150 € |

### Beispiel 10: Kundengruppen-Rabatt

| Einstellung | Wert |
|-------------|------|
| Kunden-Regel | Bestimmte Kundengruppe |
| Aktionscode | Kein Code erforderlich |
| Rabattart | Prozentual: X% |

### Beispiel 11: Versandkostenfrei ab Warenkorbwert

| Einstellung | Wert |
|-------------|------|
| Warenkorb-Regel | Summe aller Positionen ≥ 50 € |
| Anwenden auf | Versandkosten |
| Rabattart | Prozentual: 100% |

> **Tipp:** Staffelung möglich: 50% ab 25 €, 100% ab 100 € (separate Aktionen anlegen).

### Beispiel 12: Kategorie-spezifische Rabatte

Rule Builder Bedingung:
```
Position in Kategorie | Mind. eine | ist eine von | [gewählte Kategorie]
```

### Beispiel 13: Hersteller-spezifische Rabatte

Rule Builder Bedingung:
```
Position mit Hersteller | Mind. eine | ist eine von | [Hersteller]
```

### Beispiel 14: Gratisartikel

1. Artikel mit Tag "gratis" kennzeichnen
2. Dynamische Produktgruppe für "gratis"-Tag erstellen
3. Cross-Selling-Funktion zur Artikelanzeige nutzen
4. Rabatt: 100% auf Artikel der Produktgruppe

### Beispiel 15: Einzelprodukt-Rabatte

Rule Builder: Einzelnes Produkt auswählen, dann prozentualen Rabatt auf Warenkorb mit Produktregel konfigurieren.

---

## Weitere Hinweise

- **Priorität:** Beim Einsatz mehrerer Aktionen gleichzeitig entscheidet die Priorität über die Reihenfolge der Anwendung.
- **Verkaufskanäle:** Aktionen können auf bestimmte Verkaufskanäle beschränkt werden.
- **Rule Builder:** Für komplexe Bedingungen den Rule Builder unter Einstellungen > Automatisierung > Rule Builder nutzen. Siehe `sw-merchant-marketing-rule-builder`.
