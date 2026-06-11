# Shopware 6 – Scene Editor (Beta): Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/commercial-features/scene-editor
> Insider Previews: https://docs.shopware.com/de/shopware-6-de/insider-previews
> Plan: Rise oder höher | Mindestversion: 6.6.8.1 | Status: Beta

---

## 1. Überblick

Der **Scene Editor** bietet die Möglichkeit, das volle Potenzial von 3D-Modellen
für die Erstellung von Produktbildern zu nutzen. Die Kernfunktionen:

- Verschiedenste **3D-Szenen** aufbauen
- Produkte in der Szene **platzieren und arrangieren**
- **Unbegrenzt Bilder** aus den Szenen generieren
- Exportierte Bilder sind perfekt auf die eigenen Produkte abgestimmt

**Pfad im Admin**: Inhalte > Scene Editor

---

## 2. Aktivierung (Insider Previews)

### Versionen 6.6.8.1 – 6.6.10.5

In diesen Versionen ist der Scene Editor ein **Insider Preview Feature** und muss
zunächst explizit aktiviert werden:

1. Im Admin das Modul **Insider Previews** aufrufen
2. Den **Scene Editor** in der Liste der verfügbaren Preview-Features finden
3. Feature **aktivieren**
4. Anschließend ist der Scene Editor unter **Inhalte > Scene Editor** erreichbar

### Ab Version 6.6.10.6

Der Scene Editor ist ohne Aktivierungsschritt direkt verfügbar.

---

## 3. Plan-Anforderungen

| Plan | Scene Editor verfügbar |
|---|---|
| Starter | Nein |
| Basics | Nein |
| Rise | Ja (ab 6.6.8.1) |
| Evolve | Ja |
| Beyond | Ja |

---

## 4. Beta-Status – Hinweise

> ⚠ **Dieses Feature befindet sich derzeit im Beta-Status.** Der Funktionsumfang ist
> in dieser Version noch eingeschränkt und kann in zukünftigen Updates weiter ausgebaut werden.
> Es kann sich in Verhalten und Umfang noch ändern.

Shopware freut sich über Feedback, um die Funktion gezielt weiterzuentwickeln.
Feedback kann über das verlinkte Feedback-Forum eingereicht werden.

---

## 5. Szenenübersicht

Die Startseite des Scene Editors listet alle angelegten Szenen.

### Bedienelemente

| Element | Nr. | Funktion |
|---|---|---|
| Listenansicht | (1) | Wechsel zwischen Kachel- und Listenansicht |
| Sortieren nach | (2) | Sortierung: Erstelldatum, Bearbeitungsdatum, Name |
| Kontextmenü | (3) | Löschen, Duplizieren, Bearbeiten |
| Neue Szene erstellen | (4) | Erstellungsdialog öffnen |

Direktes Öffnen: Klick auf einen Szenen-Eintrag öffnet die Bearbeitung sofort.

---

## 6. Neue Szene erstellen

1. **„Neue Szene erstellen"** anklicken
2. Szenenname vergeben (einziges Pflichtfeld)
3. Automatische Weiterleitung in die Bearbeitungsansicht

---

## 7. Bereich: 3D-Objekte

### 7.1 Hauptelemente

| Element | Nr. | Beschreibung |
|---|---|---|
| Objekt im Arbeitsbereich | (1) | Hauptfenster; frei drehbares Gitternetz; zeigt ausgewähltes 3D-Objekt |
| 3D-Objekt hinzufügen | (2) | Dropdown-Menü mit verschiedenen Objektarten |
| Gruppe hinzufügen | (3) | Mehrere Objekte zu einer Gruppe zusammenfassen |
| Ansichtsauswahl | (4) | Kamera-/Perspektivwechsel (z. B. "Freie Ansicht") |
| Verschieben-Werkzeug | (5) | Move-Tool aktivieren |
| Drehen-Werkzeug | (6) | Rotate-Tool aktivieren |
| Skalieren-Werkzeug | (7) | Scale-Tool aktivieren |
| Light Settings | (8) | Beleuchtung konfigurieren |
| Bild exportieren | (9) | Szene als Bilddatei exportieren |
| Szene speichern | (10) | Komplette Szene persistent speichern |

---

### 7.2 Verschieben-Werkzeug (Move-Tool) – Detail

**Farbkodierung der Achsen-Pfeile**:

| Farbe | Achse | Richtung |
|---|---|---|
| Blau | Z-Achse | Vorwärts / Rückwärts |
| Grün | Y-Achse | Aufwärts / Abwärts |
| Rot | X-Achse | Links / Rechts |

**Farbige Quadrate**: Bewegung entlang kombinierter Ebenen
**Mittleres Quadrat**: Freie Bewegung in alle Richtungen

---

### 7.3 Drehen-Werkzeug (Rotate-Tool) – Detail

**Farbkodierung der Rotationsringe**:

| Farbe | Rotation |
|---|---|
| Rot | Nach vorne/hinten kippen (Pitch) |
| Blau | Nach links/rechts kippen (Roll) |
| Grün | Um die eigene Achse drehen (Yaw) |
| Gelb (Außenring) | Drehung aus der Kameraperspektive |

---

### 7.4 Skalieren-Werkzeug (Scale-Tool) – Detail

| Modus | Beschreibung |
|---|---|
| **Gleichmäßig (Standard)** | Proportionen bleiben erhalten; alle Achsen skalieren gleichzeitig |
| **Achsenspezifisch** | Option deaktivieren für individuelle Achsenskalierung |

**Achsenspezifische Quadrate**:

| Farbe | Achse |
|---|---|
| Grün | Höhe |
| Rot | Breite |
| Blau | Tiefe |

---

### 7.5 Light Settings – Detail

| Parameter | Optionen |
|---|---|
| **Typ** | Szenenweites Licht **oder** objektspezifisches Licht |
| **Einstellungen** | Vordefinierte Presets **oder** benutzerdefinierte Anpassungen |
| **Lichtfarbe** | Farbcode eingeben (Beispiel: `#ffffff` = Weißlicht) |
| **Light Intensity** | Schieberegler 0–100 % |

> Die Ansicht der Lichtoptionen kann sich je nach ausgewähltem Objekt unterscheiden.

---

## 8. Bereich: Szene (globale Einstellungen)

| Einstellung | Nr. | Beschreibung |
|---|---|---|
| Szenenname | (1) | Name der Szene bearbeiten |
| Hintergrundfarbe | (2) | Hintergrundfarbe der Szene konfigurieren |
| Bodenfarbe | (3) | Bodenfarbe der Szene konfigurieren |

---

## 9. Bild exportieren – vollständiger Prozess

### Schritt-für-Schritt

1. Auf **„Bild exportieren"** (oben rechts) klicken
2. **Kamera (1)** auswählen: Welche der konfigurierten Kameras soll für den Export genutzt werden?
3. **Auflösung (2)** wählen: Vorlage oder benutzerdefiniert
4. **Breite (3)** in Pixeln eingeben
5. **Höhe (4)** in Pixeln eingeben
6. **„Bild speichern" (5)** anklicken
7. Das Bild wird automatisch im Medienordner **„Scene Editor Media"** gespeichert

### Verwendung der exportierten Bilder

Exportierte Bilder können direkt aus der Medienbibliothek:
- Als Produktbild zugewiesen werden
- In Erlebniswelten eingebaut werden
- Für Marketing-Materialien genutzt werden

---

## 10. Formen (Primitive)

Geometrische Grundformen als Bühnenelemente:

### Hinzufügen

1. **„3D-Objekt hinzufügen"** → Tab **„Primitive"** im Fenster "Medien auswählen"
2. Gewünschte Form auswählen und hinzufügen

### Konfigurierbar

- **Materialbeschaffenheit** (Oberfläche, Glanz, Reflexion)
- **Farbe** der Form

### Typische Verwendung

- Podest / Plattform für das Produkt
- Hintergrundwand
- Dekorative geometrische Elemente

---

## 11. Community Hub

Im **Community Hub** ist ein interaktiver Lernpfad zum Scene Editor verfügbar.
Dort können Funktionen direkt ausprobiert und Wissen spielerisch erweitert werden.

---

## Quelle
https://docs.shopware.com/de/shopware-6-de/commercial-features/scene-editor
https://docs.shopware.com/de/shopware-6-de/insider-previews
