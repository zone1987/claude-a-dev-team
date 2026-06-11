# Shopware 6 – Spatial Commerce: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/spatial-commerce
> Gilt ab: Shopware 6.6.8.1+ (Scene Editor), 6.7.9.0+ (Bundles)

---

## 1. Überblick Spatial Commerce

Shopware bündelt unter **Spatial Commerce** alle Funktionen zur dreidimensionalen und
immersiven Produktpräsentation. Ziel ist es, Kunden ein realistischeres Einkaufserlebnis
zu bieten, das über klassische 2D-Produktfotos hinausgeht.

### Enthaltene Funktionen

1. **3D-Produkt-Modelle** – 3D-Dateien (.glb) an Produkten hochladen und in der Storefront
   als 3D-Viewer sowie per Augmented Reality (AR) anzeigen lassen.
2. **3D-Viewer Block für Erlebniswelten** – Eigenständiger CMS-Block, der 3D-Modelle
   in beliebigen Layouts darstellt (Drag & Drop).
3. **Immersive Elements** – App in Kooperation mit Instorier (norwegische Experten für
   digitales Storytelling); bietet sechs spezialisierte 3D-Blöcke für Erlebniswelten.
4. **Scene Editor** – Werkzeug zur Erstellung von 3D-Szenen, Produktplatzierung und
   unlimitierten Bildexporten (Beta ab 6.6.8.1).

### Plan-Anforderungen

| Funktion | Mindestplan |
|---|---|
| 3D-Modelle an Produkten | Rise |
| 3D-Viewer Block | Rise |
| Immersive Elements | Rise (oder €49/Monat im Store) |
| Scene Editor | Rise (ab 6.6.8.1) |

---

## 2. 3D-Produkt-Modelle & Augmented Reality

Pfad: **Kataloge > Produkte** → Tab **Allgemein** → Abschnitt **Medien**

### 2.1 Dateiformat

- Nur `.glb` (GL Transmission Format Binary) wird unterstützt
- GLB ist ein Binärformat basierend auf dem weit verbreiteten glTF-Standard
- 3D-Dateien werden **nicht automatisch optimiert** – es sollten bereits optimierte
  Dateien hochgeladen werden, um Performance-Probleme zu vermeiden
- **Wichtige Einschränkung**: Ein 3D-Modell kann **nicht** als Cover-Bild eines
  Produkts oder direkt innerhalb von Erlebniswelten genutzt werden

### 2.2 3D-Modell hochladen

1. **Kataloge > Produkte** → Produkt öffnen
2. Tab **Allgemein** → Abschnitt **Medien**
3. 3D-Datei (.glb) hochladen (wie normale Medien)
4. Das Modell erscheint in der Mediengalerie des Produkts

### 2.3 AR-Ansicht konfigurieren

1. **Inhalte > Medien** → die hochgeladene 3D-Datei anklicken
2. Abschnitt **Konfiguration** → Schalter **AR-Ansicht** aktivieren
3. **Produktgröße festlegen**: Da Shopware die Größe nicht normalisiert, muss
   die reale Produktgröße manuell angegeben werden
   > ⚠ Ohne korrekte Größenangabe erscheint das Produkt in AR in falschen Dimensionen

### 2.4 Storefront-Darstellung

- 3D-Symbol erscheint **unten rechts** am Produktbild auf der Detailseite
- Klick auf das Symbol öffnet den 3D-Viewer (ThreeJS-basiert)
- **AR-Ansicht**: Klick erzeugt einen QR-Code → Kunde scannt mit Mobilgerät → AR-Ansicht startet
- AR läuft im Browser (kein App-Download nötig)

### 2.5 Gerätekompatibilität AR

| Betriebssystem | Browser | Mindestversion |
|---|---|---|
| iOS | Safari | iOS 12+ |
| Android | Chrome | Android 8.0+ mit ARCore 1.9+ |

Ältere Browser-Versionen können Einschränkungen in der Performance aufweisen.

### 2.6 ThreeJS-Bibliothek

Shopware verwendet die Open-Source-Bibliothek **ThreeJS** für das 3D-Rendering im Browser.

---

## 3. 3D-Viewer Block für Erlebniswelten

Pfad: **Inhalte > Erlebniswelten** → Layout bearbeiten → Block hinzufügen

### 3.1 Funktion

Der **3D-Modell-Block** ermöglicht die Integration von 3D-Modellen in beliebige
Erlebniswelt-Layouts. Kunden können das Produkt:

- aus verschiedenen Winkeln betrachten
- zoomen (Mausrad oder Pinch-Geste)
- drehen (Mausziehen oder Touch-Geste)

Dies verbessert das Produktverständnis bezüglich **Struktur, Oberfläche und Form**
gegenüber klassischen 2D-Fotos.

### 3.2 Verfügbarkeit

- Ab dem kommerziellen Plan **Rise** verfügbar
- Dateiformat: ausschließlich `.glb`

### 3.3 Block hinzufügen

1. Erlebniswelt-Layout öffnen
2. Block per **Drag & Drop** aus der Blockbibliothek ziehen
3. Im Block: `.glb`-Datei hochladen oder aus der Medienbibliothek auswählen
4. Darstellungseinstellungen konfigurieren

---

## 4. Immersive Elements App

Siehe Detail-Skill: `sw-merchant-spatial-immersive-elements`

Kurzübersicht der sechs Elemente:

| Element | Funktion | Preis |
|---|---|---|
| Cylinder Gallery | 360°-Bildslider mit Maussteuerung | Inklusive |
| Depth Gallery | Parallax-Effekt (Maus + Scrollen) | Inklusive |
| Exploded View | Interaktive Produktzerlegung in Einzelteile | €49/Monat Zusatz |
| 3D Model Journey | Animierte 360°-Produkttour mit Hotspots + Audio | Inklusive |
| Slide Behind Gallery | Horizontaler Inhaltswechsel (tiefer als Slider) | Inklusive |
| VR Cinema | 3D/VR-Erlebnis (webp-Videoformat) | Inklusive |

---

## 5. Scene Editor

Siehe Detail-Skill: `sw-merchant-spatial-scene-editor`

Kurzübersicht:
- Pfad: **Inhalte > Scene Editor**
- Status: **Beta** (Rise-Plan ab 6.6.8.1)
- Funktion: 3D-Szenen erstellen, Produkte platzieren, Bilder exportieren

---

## Quelle
https://docs.shopware.com/de/shopware-6-de/spatial-commerce
