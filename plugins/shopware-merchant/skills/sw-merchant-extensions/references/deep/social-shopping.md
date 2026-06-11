# Social Shopping – Facebook, Instagram, Google Shopping, Pinterest

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/social-shopping  
**Plan**: Shopware Rise (oder höher)

## Überblick

Die **Social Shopping Extension** integriert Shopware 6 mit großen Social-Commerce-Plattformen.
Produkte werden als Feed exportiert und Conversions über Referral-Codes getrackt.

---

## Unterstützte Plattformen

| Plattform | Mechanismus | Feed-Format |
|---|---|---|
| **Facebook** | XML-Feed Export | RSS/Atom XML |
| **Instagram** | XML-Feed Export | RSS/Atom XML |
| **Google Shopping** | XML-Feed Export | Google Merchant XML |
| **Pinterest** | Metadaten (Rich Pins) | Kein Feed-Upload nötig |

---

## Installation

1. **Erweiterungen > Meine Erweiterungen**
2. Social Shopping installieren + aktivieren
3. Im Bereich **Verkaufskanäle** erscheinen neue Kanal-Typen

---

## Einrichtung pro Plattform

### Facebook & Instagram

**Schritte**:
1. **Verkaufskanäle** > Neuen Kanal hinzufügen → "Facebook" oder "Instagram" wählen
2. Kanal benennen
3. **Storefront und Domain** zuweisen
4. **Währung** wählen
5. **Produktgruppen** auswählen (welche Produkte exportiert werden)
6. **Generierungsintervall** setzen: Live oder geplant (täglich/stündlich)
7. Feed-URL aus Shopware kopieren
8. In Facebook Business Manager / Catalog Manager hinterlegen

### Google Shopping

**Schritte**:
1. Neuen Kanal → "Google Shopping" wählen
2. **Domain-Verifizierung** über Google Merchant Center durchführen
3. Google-Produktkategorie-IDs (numerisch) zuweisen
4. Feed-URL in Google Merchant Center hinterlegen

**Wichtig**: Google Produktkategorie-IDs müssen **numerisch** sein
(aus der Google-Taxonomy: https://www.google.com/basepages/producttype/taxonomy-with-ids.de-DE.txt)

### Pinterest

**Mechanismus**: Keine Feed-Upload nötig – Pinterest liest Metadaten direkt aus dem Storefront.

**Schritte**:
1. **Rich Pins Validierung** über Pinterest Entwicklertools:
   https://developers.pinterest.com/tools/url-debugger/
2. Shop-URL für Pinterest verifizieren
3. Shopware zieht Produktdaten automatisch aus dem Storefront-HTML

---

## Tracking & Statistiken

### Referral-Code in Templates
Für Conversion-Tracking muss jede Produktverknüpfung den Verkaufskanal-Parameter enthalten:

```
{{ socialShoppingSalesChannel.salesChannelId }}
```

Ohne diesen Parameter: Keine Attribution in den Bestelldetails.

### Tracking-Auswertung
- **Kunden-Übersicht**: Spalte "Einstiegspunkt" zeigt, von welchem Social-Kanal der Kunde kam
- **Bestellübersicht**: Spalte "Einstiegspunkt" für jede Bestellung

---

## Produktvalidierung

Vor dem Export prüft Shopware automatisch die Datenvollständigkeit:

| Pflichtfeld | Beschreibung |
|---|---|
| Produktname | Vorhanden und nicht leer |
| Beschreibung | Vorhanden |
| Hauptbild | Mindestens ein Bild |
| Preis | Gültiger Preis |
| GTIN/EAN | (Für Google Shopping empfohlen) |

Produkte mit fehlenden Daten werden aus dem Feed ausgeschlossen.

---

## Feed-Verwaltung

### Generierungsintervalle
| Option | Beschreibung |
|---|---|
| Live | Feed wird bei jedem Abruf neu generiert |
| Stündlich | Stündliche Vorab-Generierung (Cache) |
| Täglich | Einmal täglich |

### Wichtige Hinweise

- **Verkaufskanal löschen**: Immer **vor** dem Deaktivieren der Extension löschen!
  (Sonst verwaiste Kanal-Konfigurationen)
- Feed-URL ist öffentlich zugänglich (kein Auth nötig für Plattform-Import)

---

## Performance-Tipps

- Für große Kataloge: Geplante Generierung (nicht Live) verwenden
- Produktgruppen definieren, um nur relevante Produkte zu exportieren
- Feed-URL direkt in Platform-Dashboard hinterlegen (nicht manuell herunterladen/hochladen)
