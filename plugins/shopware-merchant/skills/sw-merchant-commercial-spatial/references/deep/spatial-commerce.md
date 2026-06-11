# Shopware Spatial Commerce – Vollständige Dokumentation

## Überblick

Shopware Spatial Commerce umfasst alle 3D-Features zur dreidimensionalen Produktpräsentation im Online-Shop. Es ist im Rise-Plan und höher verfügbar.

**Verfügbarkeit:** Rise-Plan und höher
**Voraussetzung:** Shopware Commercial Extension

---

## Feature 1: 3D-Viewer Block für Erlebniswelten

### Beschreibung
3D-Modelle können hochgeladen und in den Shopping Experiences als interaktiver 3D-Viewer eingebunden werden.

### Anwendungsfälle
- Interaktive Produktpräsentation auf Landingpages
- 360°-Produktansicht ohne externe Tools
- AR-fähige Produktdarstellung (Augmented Reality im Storefront)

### Einrichtung
1. 3D-Modell-Datei hochladen (in der Medienübersicht)
2. Im Erlebniswelten-Editor: Block „3D-Viewer" hinzufügen
3. Hochgeladenes Modell dem Block zuweisen
4. Konfiguration: Hintergrundfarbe, Beleuchtung, Startposition

### Technische Details
- Unterstützte Dateiformate: glTF, GLB
- Funktioniert direkt im Browser (kein Plugin für Besucher nötig)
- AR-Unterstützung für kompatible Mobile-Browser

---

## Feature 2: Immersive Elements

### Beschreibung
Eine App (entwickelt in Partnerschaft mit Instorier) mit fünf verschiedenen 3D-Elementen für Erlebniswelten, um Produkte innovativ zu präsentieren.

**Mindestversion:** 16.05.2024
**Typ:** Shopware-Extension (im Lieferumfang des Plans enthalten)

### Enthaltene Elemente
Die Extension bietet 5 3D-Elemente für den Erlebniswelten-Editor:

1. Interaktive 3D-Produktdarstellung
2. Animierte Übergänge
3. Parallax-Scrolling-Effekte
4. Hotspot-Annotationen auf 3D-Modellen
5. 3D-Szenenintegration

### Ziel
- Online-Shop in ein unvergessliches Markenerlebnis verwandeln
- Kosteneffiziente Alternative zu externen Ressourcen
- Conversion Rate durch immersive Produktpräsentation steigern

### Weitere Informationen
https://www.shopware.com/de/erweiterungen/immersive-elements

---

## Feature 3: Scene Editor (Beta)

### Beschreibung
Der Scene Editor ermöglicht Händlern, 3D-Szenen zu erstellen, Produkte zu platzieren und unbegrenzt maßgeschneiderte Produktbilder zu generieren.

**Status:** Beta

### Kernfunktionen

#### 3D-Szenen erstellen
- Vorgefertigte oder eigene Szenen als Hintergrund
- Produkte in der Szene platzieren und ausrichten
- Beleuchtung und Kamera konfigurieren

#### Produkte platzieren
- Shopware-Produkte direkt aus dem Katalog in die Szene ziehen
- Position, Rotation, Skalierung anpassen
- Mehrere Produkte pro Szene möglich

#### Bilder generieren
- High-Quality-Renders aus der Szene exportieren
- Unbegrenzte Anzahl von Variationen
- Direkt in die Produktmedien übernehmen

### Anwendungsfälle
- Lifestyle-Produktbilder ohne Fotostudio
- Konsistente Produktbilder für gesamten Katalog
- Saisonale Variationen derselben Produkte

---

## 3D-Modelle verwalten

### Hochladen
**Pfad:** Inhalte → Medien → Neues Medium hochladen → 3D-Datei auswählen

### Unterstützte Formate
- glTF (empfohlen)
- GLB (Binary glTF)

### Optimierungsempfehlungen
- Dateigröße: Max. 50 MB (für Ladezeit im Browser)
- Polygonanzahl: Unter 500.000 für gute Performance
- Texturen: Komprimiert (KTX2 oder Basis Universal)

---

## Vergleich der Spatial-Features

| Feature | Plan | Status |
|---|---|---|
| 3D-Viewer Block | Rise+ | Produktiv |
| Immersive Elements | Rise+ | Produktiv (ab 16.05.2024) |
| Scene Editor | Rise+ | Beta |
| AR im Storefront | Rise+ | Produktiv |

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/spatial-commerce (Stand: 2026-06)*
