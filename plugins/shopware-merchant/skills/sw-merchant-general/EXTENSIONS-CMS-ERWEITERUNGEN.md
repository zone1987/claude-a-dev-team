# CMS-Erweiterungen – Quick View, Scroll-Navigation, Block-Visibility

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/cms-erweiterungen  
**Plan**: Shopware Evolve (oder höher)

## Überblick

Die **CMS-Erweiterungen** erweitern den integrierten Shopping Experiences (Erlebniswelten)
CMS-Editor um drei wesentliche Funktionen: Quick View, Scroll-Navigation und Block-Sichtbarkeit.

---

## Installation

1. **Shopware Evolve Plan** muss für die Shop-Domain registriert sein
2. Im Shopware Account Tab einloggen
3. **Erweiterungen > Meine Erweiterungen** → CMS Erweiterungen installieren + aktivieren

---

## Funktion 1: Quick View

**Was es ist**: Schnellansicht eines Produkts direkt aus der Kategorieliste,
ohne die Kategorie zu verlassen.

**Anwendbar auf**:
- Produkt-Boxen in Kategorie-Listen
- Produkt-Slider
- Cross-Selling-Elemente

**Aktivierung**:
1. Erlebniswelten-Editor öffnen (Content > Erlebniswelten)
2. Produktlisten-Element auswählen
3. In den Element-Einstellungen: "Quick View aktivieren" einschalten

**Storefront-Verhalten**: Kunden klicken auf ein Produkt → Modal-Fenster mit Produktdetails,
Varianten-Auswahl und "In den Warenkorb"-Button öffnet sich.

---

## Funktion 2: Scroll-Navigation

**Was es ist**: Navigationsanker innerhalb langer Erlebniswelten-Seiten.
Zeigt ein Navigationsmenü links (Desktop) oder unten rechts (Mobile).

**Anwendung**:
1. Erlebniswelt im Editor öffnen
2. Abschnitt/Block auswählen, der als Navigationspunkt erscheinen soll
3. Block-Einstellungen → "Navigationspunkt setzen" + Namen vergeben

**Storefront-Verhalten**:
- Desktop: Navigationsmenü erscheint links auf der Seite
- Mobile: Navigationssteuerelemente unten rechts

**Typischer Anwendungsfall**: Lange Marken- oder Kategorielanding-Pages mit mehreren Sektionen.

---

## Funktion 3: Block-Sichtbarkeit

**Was es ist**: Einzelne Blöcke in Erlebniswelten können über **Rule-Builder-Regeln**
ein- oder ausgeblendet werden.

**Beispiele für Regeln**:
- Block nur für eingeloggte Kunden sichtbar
- Block nur für bestimmte Kundengruppen
- Block nur in bestimmten Ländern anzeigen
- Zeitgesteuerte Sichtbarkeit (Anfang/Ende-Datum)

**Konfiguration**:
1. Erlebniswelt im Editor öffnen
2. Block auswählen → Block-Einstellungen öffnen
3. Unter "Sichtbarkeit" → Rule Builder-Regel auswählen
4. Regel aus bestehenden Regeln wählen oder neue erstellen (Einstellungen > Regeln)

---

## Funktion 4: Custom Forms (Benutzerdefinierte Formulare)

**Was es ist**: Alternative zu Standard-Kontaktformularen mit vollständig anpassbarem Layout.

**Feldtypen**:
| Typ | Beschreibung |
|---|---|
| Text | Einzeiliges Textfeld |
| E-Mail | E-Mail-Adresse mit Validierung |
| Zahl | Numerische Eingabe |
| Checkbox | Ja/Nein-Auswahl |
| Dropdown | Auswahl aus Liste (aus Entitäten oder festen Werten) |
| Textarea | Mehrzeiliges Textfeld |

**Konfiguration pro Feld**:
- Breite (Full Width, Half Width, etc.)
- Pflichtfeld (Required)
- Platzhaltertext
- Validierungsmeldung

**Einsatz**: Erlebniswelten-Editor → CMS-Block "Formular" hinzufügen → Custom Form-Element wählen.
