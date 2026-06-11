# Shopware 6 – Themes: Vollständige Dokumentation

**Quelle:** https://docs.shopware.com/de/shopware-6-de/Inhalte/themes  
**Version:** ab 6.7.0.0 (ältere Versionen ab 6.0.0 verfügbar)

---

## Screenshots

| Datei | Inhalt |
|---|---|
| `../../assets/themes-uebersicht.png` | Themes-Übersicht |
| `../../assets/theme-farben.png` | Theme-Farben Konfiguration |
| `../../assets/status-ausgaben.png` | Status-Ausgaben Konfiguration |
| `../../assets/typografie.png` | Typografie-Einstellungen |
| `../../assets/e-commerce.png` | E-Commerce-Einstellungen |
| `../../assets/medien-logos.png` | Medien / Logos Konfiguration |
| `../../assets/verkaufskanal-zuordnen.png` | Theme einem Verkaufskanal zuordnen |

---

## Übersicht

Pfad: **Inhalte > Themes**

Die Themes-Übersicht zeigt alle im System installierten Themes. Jedes Theme
kann konfiguriert und Verkaufskanälen zugewiesen werden.

### Zuordnungsstatus-Anzeige

| Farbe des Punktes | Bedeutung |
|---|---|
| Grau | Theme ist keinem Verkaufskanal zugeordnet |
| Grün | Theme ist mindestens einem Verkaufskanal zugeordnet |

### Ansichtsoptionen
- Listenansicht
- Vorschauansicht (Kacheldarstellung mit Theme-Screenshot)
- Sortierung nach Name, Erstellungsdatum

---

## Kontextmenü (3-Punkte-Menü pro Theme)

| Aktion | Beschreibung |
|---|---|
| Vorschaubild ändern | Screenshot/Bild des Themes austauschen |
| Umbenennen | Anzeigenamen des Themes ändern |
| Duplikat erstellen | Kopie des Themes anlegen (zur Anpassung) |
| Löschen | Theme permanent entfernen |

**Hinweis**: Aktive/zugewiesene Themes können nicht gelöscht werden.

---

## Theme-Konfiguration

Klick auf ein Theme öffnet die Konfigurationsseite.

Die Konfiguration ist in folgende Bereiche unterteilt:

### 1. Theme-Farben

**Hintergrundfarben:**
- Haupt-Hintergrundfarbe (Body-Background)
- Rahmenfarben für Trennlinien und Boxen

**Primärfarbe:**
- Wird für Überschriften, Links und Akzente verwendet
- Beeinflusst das gesamte visuelle Erscheinungsbild

**Auswahl:** Farbpicker + Hex-Code-Eingabe möglich

---

### 2. Status-Ausgaben (Feedback-Farben)

Farben für System-Meldungen im Shop:

| Status | Beschreibung |
|---|---|
| Erfolg (Success) | Grüne Meldungen (z.B. „Produkt zum Warenkorb hinzugefügt") |
| Info | Blaue Hinweismeldungen |
| Warnung (Warning) | Gelbe Warnmeldungen |
| Fehler (Danger) | Rote Fehlermeldungen |

---

### 3. Typografie

**Schriftarten:**
- Schriftart für Fließtext (Body Font)
- Schriftart für Überschriften (Headline Font)
- Schriftgröße (Base Font Size)

**Textfarben:**
- Allgemeine Textfarbe
- Überschriften-Textfarbe
- Link-Farbe (Standard und Hover-Zustand)

---

### 4. E-Commerce

**Kaufen-Button:**
- Hintergrundfarbe des Buttons
- Textfarbe des Buttons
- Hover-Farbe (Farbe beim Überfahren mit der Maus)

**Preisdarstellung:**
- Farbe des Originalpreises
- Farbe des Streichpreises (Reduktionspreis)
- Hervorhebungsfarbe für Sonderpreise

---

### 5. Medien (Logos & Icons)

#### Logo-Konfiguration

Logos sind responsiv konfigurierbar – separate Logos für verschiedene Breakpoints:

| Breakpoint | Bildschirmbreite | Logo-Slot |
|---|---|---|
| Desktop | > 991 px | Desktop-Logo |
| Tablet | 767–991 px | Tablet-Logo (optional) |
| Mobil | < 767 px | Mobil-Logo (optional) |

**Empfehlung**: Mindestens Desktop-Logo hinterlegen; andere Größen optional.

#### Favicon
- Format: ICO, PNG oder SVG
- Optimale Größe: 32×32 px oder 16×16 px
- Erscheint im Browser-Tab

#### Social-Share-Icon (OG-Image)
- Bild das erscheint wenn Shop-Link in Social Media geteilt wird
- Format: JPG oder PNG
- Empfohlene Größe: 1200×630 px

---

## Theme duplizieren

**Verwendungsfall**: Theme anpassen, ohne das Original zu verändern.

**Voraussetzung**: Das zu duplizierende Theme darf **keine externe Vererbung** besitzen
(also kein Theme eines Drittanbieter-Eltern-Themes nutzen, das nicht im System ist).

**Schritte:**
1. Kontextmenü des Themes öffnen (3-Punkte-Symbol)
2. „Duplikat erstellen" auswählen
3. Namen für das Duplikat eingeben
4. Bestätigen → Duplikat öffnet sich automatisch in der Konfiguration

**Vererbung im Duplikat:**
- Alle Einstellungen werden vom Original übernommen
- Jede Einstellung kann im Duplikat individuell deaktiviert/überschrieben werden
- Deaktivierte Einstellungen erben weiterhin vom Original (falls Eltern-Theme)

---

## Theme einem Verkaufskanal zuweisen

### Methode 1: Über Themes-Bereich
Inhalte > Themes > Theme öffnen > Bereich „Verkaufskanäle" > Kanal auswählen

### Methode 2: Über Verkaufskanal-Einstellungen (bevorzugt)

1. Einstellungen (oder Verkaufskanäle) > [Verkaufskanal öffnen]
2. Tab **„Themes"** auswählen
3. Gewünschtes Theme aus Liste wählen
4. **„Speichern"** → Theme wird auf Storefront aktiviert

**Hinweis**: Nach Zuweisung kann die Aktivierung einige Sekunden dauern (Theme wird kompiliert).

---

## Theme-Vererbung

Shopware nutzt ein Vererbungssystem für Themes:

- **Eltern-Theme**: Basis-Theme (meist Shopware Standard-Theme oder gekauftes Theme)
- **Kind-Theme**: Eigenes Theme, das vom Eltern-Theme erbt

Beim Duplizieren wird ein Kind-Theme erstellt, das alle Werte des Eltern-Themes
übernimmt. Einzelne Werte können überschrieben werden; der Rest bleibt vererbt.

**Vorteile:**
- Updates des Eltern-Themes werden automatisch übernommen (außer überschriebene Werte)
- Klare Trennung zwischen Standard und Anpassung

---

## Template-Änderungen (für Entwickler)

Über die Admin-Oberfläche können nur Konfigurationswerte geändert werden.
Für Template-Anpassungen (HTML/Twig/CSS/JS) ist Entwickler-Zugriff nötig.

Dokumentation: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/aenderungen-am-template-vornehmen

---

## Häufige Anwendungsfälle

### Shop-Logo austauschen
1. Inhalte > Themes > Theme anklicken
2. Abschnitt „Medien" → Desktop-Logo-Slot
3. Bild aus Medienbibliothek wählen oder hochladen
4. Optional: Tablet- und Mobil-Logo setzen
5. Speichern

### Primärfarbe ändern
1. Inhalte > Themes > Theme anklicken
2. Abschnitt „Theme-Farben" → Primärfarbe
3. Farbpicker oder Hex-Code (z.B. `#E84E1B`)
4. Speichern → Änderung ist sofort im Storefront sichtbar

### Kaufen-Button anpassen
1. Inhalte > Themes > Theme anklicken
2. Abschnitt „E-Commerce" → Kaufen-Button
3. Hintergrundfarbe und Textfarbe setzen
4. Speichern

### Theme für neuen Verkaufskanal aktivieren
1. Neues Theme ggf. installieren (Erweiterungen > Meine Erweiterungen)
2. Einstellungen > Verkaufskanäle > [Kanal] > Tab „Themes"
3. Theme auswählen → Speichern

---

## Best Practices

- **Duplikat erstellen** bevor Anpassungen: Schutz vor versehentlichen Änderungen
- **Konsistente Farbpalette**: Maximal 3–4 Hauptfarben verwenden
- **Logos vorbereiten**: Alle drei Größen (Desktop/Tablet/Mobil) vorbereiten
- **Kontrastverhältnis**: WCAG-Richtlinien beachten (mind. 4.5:1 für Text)
- **Favicon nicht vergessen**: Professioneller Eindruck im Browser-Tab
- **OG-Image**: Für Social-Media-Sharing wichtig

---

## Verwandte Dokumentation

- Erlebniswelten: `sw-merchant-content-shopping-experiences`
- Medien: `sw-merchant-content-media`
- Template-Anpassungen (Entwickler): https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/aenderungen-am-template-vornehmen
- Verkaufskanäle: `sw-merchant-sales-channels`
