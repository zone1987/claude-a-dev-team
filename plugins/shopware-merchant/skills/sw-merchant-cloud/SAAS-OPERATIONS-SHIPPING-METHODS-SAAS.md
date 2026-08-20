# Shopware SaaS — Versandarten einrichten

**Quelle**: https://docs.shopware.com/de/shopware-6-de/saas/versand

---

## Übersicht

**Pfad:** Einstellungen > Shop > Versand

Integration erfolgt durch **manuelle Zuweisung** im Bestellmodul — keine vordefinierten Carrier-Integrationen.

**Übersicht zeigt:**
- Name, Beschreibung und Aktivstatus aller Versandarten
- Listeneinstellungen (2): Spaltensichtbarkeit anpassen
- Kontextmenü (3): Bearbeiten, Duplizieren, Löschen
- Button „Versandart anlegen" (4): Neue Versandart erstellen
- Sprachauswahl (5): Anzeige nach Sprache filtern

---

## Versandart anlegen — Basisdaten

| Feld | Beschreibung | Hinweis |
|---|---|---|
| **Name** | Intern + extern (Checkout) | — |
| **Technischer Name** | Eindeutiger Identifier | Änderungen beeinflussen Integrationen |
| **Position** | Sortierung im Checkout | Kleinerer Wert = weiter oben |
| **Aktiv** | Versandart aktivieren/deaktivieren | — |
| **Beschreibung** | Detailtext in Übersicht und Storefront | — |
| **Logo** | Versandart-Icon | Datei, URL oder Medienbibliothek |
| **Lieferzeit** | Angabe während Methodenauswahl | — |
| **Tracking-URL** | Carrier-Tracking mit `%s` als Platzhalter | — |
| **Tags** | Stichwörter für Suchbarkeit | — |

---

## Verfügbarkeitsregel

Bestimmt **wann** dieser Versandweg verfügbar ist.
Konfiguration über den **Rule Builder** (bedingte Logik).

---

## Preismatrix

Flexible Preisstruktur mit mehreren Regeln und Matrizen:

| Element | Funktion |
|---|---|
| **Einschränkung (1)** | Bedingte Rule-Builder-Logik |
| **Preisregel hinzufügen (2)** | Weitere Preisregeln ergänzen |
| **Kontextmenü (3)** | Matrix entfernen oder duplizieren |
| **Eigenschaftsbasiert (4)** | Preis nach Shop-Eigenschaften |
| **Regelbasiert (5)** | Preis nach Rule-Builder-Bedingungen |
| **Matrix hinzufügen (6)** | Mehrere Matrizen konfigurieren |

### Eigenschaftsbasierte Preismatrix

Verfügbare Eigenschaften:
- Anzahl der Positionen
- Warenkorbwert
- Gewicht
- Volumen

**Beispiel:**
> Warenkorbwert von 0 bis 45 € = Preis: **4,99 €** Versandkosten

### Regelbasierte Preismatrix

Custom Rule-Builder-Bedingungen.

**Beispiel:**
> Lieferland ist Deutschland = Preis: **5,99 €**

---

## Verkaufskanal-Zuweisung

Versandarten müssen dem Verkaufskanal zugewiesen werden:
1. Verkaufskanal-Einstellungen öffnen
2. Alle verfügbaren Versandarten auswählen
3. Standard-Versandart festlegen

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/saas/versand*
