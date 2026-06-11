# Shopware 6 – Hersteller: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/produkte/hersteller  
> Gilt ab: Shopware 6.0.0+

---

## 1. Herstellerübersicht

Pfad: **Kataloge > Hersteller**

Die Übersicht zeigt alle angelegten Hersteller mit den wichtigsten Informationen in einer Tabelle.

### Spalten und Funktionen

- Spalten sind per Klick auf den Spaltenkopf auf- und absteigend sortierbar
- Kontextmenü (**„..."**-Button) je Hersteller:

| Option | Beschreibung |
|---|---|
| Bearbeiten | Öffnet die Bearbeitungsmaske des Herstellers |
| Duplizieren | Erstellt eine Kopie mit allen bestehenden Daten |
| Löschen | Löscht den Hersteller (nur möglich wenn keinem Produkt zugewiesen) |

---

## 2. Hersteller anlegen

1. Klick auf **„Hersteller anlegen"**
2. Pflichtfeld: **Name** (einziges Pflichtfeld)
3. Optionale Felder:
   - **Website-Link**: URL der Herstellerwebsite
   - **Logo**: Bild-Upload (erscheint auf Produktdetailseite statt Name)
   - **Beschreibung**: Freitext-Beschreibung; unterstützt **Twig-Variablen** für Storefront-Darstellung
4. Speichern

---

## 3. Storefront-Darstellung

Herstellerinformationen erscheinen auf der **Produktdetailseite** in der **oberen rechten Ecke**.

| Situation | Darstellung |
|---|---|
| Nur Name vorhanden | Name wird als Text angezeigt |
| Logo hochgeladen | Logo wird anstelle des Namens angezeigt |
| Website-Link gesetzt | Name/Logo wird klickbar (Weiterleitung zur Herstellerwebsite) |
| Kein Hersteller zugewiesen | Kein Herstellerbereich auf der Detailseite |

---

## 4. Hersteller bearbeiten

Zugriff per Klick auf **„Bearbeiten"** im Kontextmenü oder per Direktklick auf den Namen.

Alle Felder aus der Anlage sind bearbeitbar:
- Name
- Website
- Logo (Bild ersetzen oder entfernen)
- Beschreibung

---

## 5. Herstellerseite erstellen (Workaround)

Shopware 6 hat keine native Herstellerseite. Der folgende Workaround erstellt eine dedizierte Seite:

### Schritt 1: Erlebniswelt-Landingpage erstellen

1. Inhalte > Erlebniswelten > **„Erlebniswelt hinzufügen"**
2. Typ: **Landingpage** wählen
3. Layout gestalten (Herstellerinfos, Produkte etc.)
4. Speichern und aktivieren

### Schritt 2: Landingpage in Kategorien anlegen

1. Kataloge > Kategorien
2. Unterhalb der Kategorieübersicht: **„Landingpage hinzufügen"**
3. Felder ausfüllen:
   - Name (z. B. „Shopware AG")
   - Landingpage ist aktiv: **Ja**
   - Verkaufskanal zuweisen
4. Tab **SEO** öffnen:
   - **SEO URL** (Pflicht): Pfad definieren, z. B. `shopwareag`
   - Die fertige URL lautet dann: `www.meinshop.de/shopwareag`
5. Tab **Layout** öffnen:
   - Die in Schritt 1 erstellte Erlebniswelt zuweisen
6. Speichern

### Schritt 3: SEO-URL beim Hersteller eintragen

1. Kataloge > Hersteller > Hersteller öffnen
2. Feld **„Hersteller-URL"** (oder vergleichbares Feld): SEO-URL mit führendem `/` eintragen
   - Beispiel: `/shopwareag`
3. Speichern

Ergebnis: Die Hersteller-Verlinkung auf der Produktdetailseite führt nun zur Landingpage statt zur externen Website.

---

## 6. Hersteller und Produkte

- Einem Produkt kann genau **ein Hersteller** zugewiesen werden
- Zuweisung erfolgt in der Produktmaske unter **Allgemein > Informationen > Hersteller**
- Neue Hersteller können direkt aus der Produktmaske angelegt werden (ohne in Kataloge > Hersteller zu wechseln)
- Ein Hersteller kann beliebig vielen Produkten zugewiesen sein

---

## 7. Hersteller löschen

- Löschen ist nur möglich wenn der Hersteller **keinem Produkt** mehr zugewiesen ist
- Zuerst alle Produktzuweisungen entfernen, dann löschen
- Alternativ: Duplizieren → nicht benötigt; Hersteller einfach keinem weiteren Produkt zuweisen

---

## 8. Tipps

- Das **Logo** sollte in einem Format mit transparentem Hintergrund hochgeladen werden (PNG, SVG), da es auf dem Produktbild-Hintergrund angezeigt wird
- Die **Beschreibung** kann Twig-Syntax enthalten und ist daher für dynamische Inhalte geeignet
- Für SEO-relevante Herstellerseiten ist der Landingpage-Workaround die empfohlene Methode
- Hersteller können auch für interne Sortierpurposen in der Produktübersicht genutzt werden

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/produkte/hersteller*
