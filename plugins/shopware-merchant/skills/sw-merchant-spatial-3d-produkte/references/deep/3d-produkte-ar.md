# Shopware 6 – 3D-Produkt-Modelle & Augmented Reality: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/kataloge/produkte
> Quelle (Medien/AR): https://docs.shopware.com/de/shopware-6-de/Inhalte/medien
> Plan: Rise (oder höher)

---

## 1. Voraussetzungen

- **Shopware-Plan**: Rise oder höher
- **Dateiformat**: Ausschließlich `.glb` (GL Transmission Format Binary)
  - GLB ist ein Binärformat basierend auf dem weit verbreiteten **glTF-Standard**
  - Häufig genutztes Format im Austausch von 3D-Modellen zwischen Applikationen
- **3D-Rendering-Bibliothek**: ThreeJS (open-source, browserbasiert)

---

## 2. 3D-Modell an einem Produkt hochladen

### 2.1 Pfad

**Kataloge > Produkte** → Produkt öffnen oder neu anlegen → Tab **Allgemein** → Abschnitt **Medien**

### 2.2 Schritte

1. Im Abschnitt **Medien** die Schaltfläche zum Hinzufügen von Medien anklicken
2. `.glb`-Datei auswählen oder per Drag & Drop in die Mediagalerie ziehen
3. Das 3D-Modell erscheint in der Medien-Übersicht des Produkts

### 2.3 Wichtige Einschränkungen

| Einschränkung | Detail |
|---|---|
| Kein Cover-Bild | Ein 3D-Modell kann **nicht** als Produkt-Cover-Bild verwendet werden |
| Keine Erlebniswelten | 3D-Modelle aus dem Produkt-Tab können **nicht** direkt in Erlebniswelten genutzt werden |
| Keine automatische Optimierung | 3D-Dateien werden in Originalqualität und -größe gespeichert |
| Performance | Große, unoptimierte Dateien können die Ladezeit der Storefront erhöhen |

> ⚠ **Empfehlung**: Ausschließlich bereits optimierte 3D-Dateien hochladen, um Performance-Probleme zu vermeiden.

---

## 3. AR-Ansicht konfigurieren

### 3.1 Pfad

**Inhalte > Medien** → hochgeladene 3D-Datei anklicken → Bereich **Konfiguration**

### 3.2 AR aktivieren

1. Datei in der Medienbibliothek unter **Inhalte > Medien** suchen und anklicken
2. Im Detailbereich unter **Konfiguration** den Schalter **AR-Ansicht** aktivieren
3. **Produktgröße festlegen** (Pflicht):
   - Shopware normalisiert die Größe des 3D-Modells nicht automatisch
   - Die reale Abmessung des Produkts muss manuell eingegeben werden
   - Ohne korrekte Größenangabe erscheint das Produkt in AR in falschen Dimensionen

### 3.3 Warum Größenangabe wichtig ist

> "Die Größe des Produkts in AR muss vorher festgelegt werden, da die Größe des Produktes
> nicht in Shopware normalisiert ist."

Ein falsch dimensioniertes AR-Objekt (zu groß oder zu klein) kann das AR-Erlebnis
für Kunden unbrauchbar machen.

---

## 4. Storefront-Darstellung

### 4.1 3D-Viewer auf der Produktdetailseite

- Ein **3D-Symbol** erscheint **unten rechts** am Produktbild auf der Detailseite
- Klick auf das Symbol öffnet den integrierten 3D-Viewer (ThreeJS-basiert)
- Kunden können das Produkt:
  - frei drehen (Mausziehen / Touch-Geste)
  - zoomen (Mausrad / Pinch-Geste)
  - aus beliebigen Winkeln betrachten

### 4.2 AR-Erlebnis per QR-Code

1. Kunde klickt auf das 3D-Symbol auf der Produktdetailseite
2. Ein **QR-Code** wird erzeugt und angezeigt
3. Kunde scannt den QR-Code mit seinem Mobilgerät
4. Die AR-Ansicht startet im Browser des Mobilgeräts (kein App-Download erforderlich)
5. Das 3D-Modell erscheint in der realen Umgebung des Kunden in den festgelegten Dimensionen

---

## 5. Gerätekompatibilität

### 5.1 Unterstützte Systeme für AR

| Betriebssystem | Browser | Mindestversion | Zusätzliche Anforderung |
|---|---|---|---|
| iOS | Safari | iOS 12+ | — |
| Android | Chrome | Android 8.0+ | ARCore 1.9+ |

> ⚠ Ältere Browser-Versionen können Einschränkungen in der Performance erfahren.
> Nicht alle Geräte unterstützen ARCore – dies liegt in der Verantwortung des Geräteherstellers.

---

## 6. 3D-Viewer Block in Erlebniswelten

> Für die direkte Integration in Erlebniswelt-Layouts steht ein eigener **3D-Modell-Block** bereit.
> Dieser ist von den Produkt-Medien unabhängig.

### 6.1 Verfügbarkeit

- Ab dem kommerziellen Plan **Rise**
- Dateiformat: ausschließlich `.glb`

### 6.2 Block hinzufügen

1. **Inhalte > Erlebniswelten** → gewünschtes Layout öffnen
2. Blockbibliothek öffnen → Block **3D-Modell** per Drag & Drop in das Layout ziehen
3. In dem Block die `.glb`-Datei hochladen oder aus der Medienbibliothek auswählen
4. Darstellungsoptionen nach Bedarf anpassen

### 6.3 Interaktionsmöglichkeiten für Kunden

- Produkt aus verschiedenen Winkeln betrachten
- Zoomen und Drehen
- Verbesserte Wahrnehmung von Struktur, Oberfläche und Form

---

## 7. Technischer Hintergrund: GLB / glTF

- **glTF** (GL Transmission Format) ist ein offener Standard des Khronos Consortium
- **GLB** ist die Binärvariante von glTF (alles in einer Datei gebündelt)
- Vorteile: kleines Dateiformat, breite Kompatibilität, nativ in WebGL nutzbar
- Shopware verwendet **ThreeJS** als JavaScript-Bibliothek für das Rendern

---

## Quelle
https://docs.shopware.com/de/shopware-6-de/kataloge/produkte
https://docs.shopware.com/de/shopware-6-de/Inhalte/Erlebniswelten
https://docs.shopware.com/de/shopware-6-de/spatial-commerce
