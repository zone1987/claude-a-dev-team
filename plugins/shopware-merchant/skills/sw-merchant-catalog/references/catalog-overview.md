# Shopware 6 – Kataloge: Überblick und Zusammenhänge

> Quelle: https://docs.shopware.com/de/shopware-6-de/kataloge

---

## 1. Was ist der Katalog-Bereich?

Der Bereich **Kataloge** in der Shopware 6 Administration ist das Herzstück der Produktverwaltung. Hier werden alle produktbezogenen Stammdaten angelegt und gepflegt.

**Admin-Pfad:** Hauptmenü > Kataloge

---

## 2. Enthaltene Bereiche

| Bereich | Admin-Pfad | Funktion |
|---|---|---|
| **Produkte** | Kataloge > Produkte | Produktanlage, -bearbeitung, Varianten, Preise |
| **Kategorien** | Kataloge > Kategorien | Navigationsstruktur, Produktzuweisung |
| **Hersteller** | Kataloge > Hersteller | Hersteller verwalten, Produkten zuweisen |
| **Eigenschaften** | Kataloge > Eigenschaften | Filterattribute und Variantenbasis |
| **Dynamische Produktgruppen** | Kataloge > Dynamische Produktgruppen | Regelbasierte Produktgruppen |
| **Bewertungen** | Kataloge > Bewertungen | Kundenbewertungen moderieren |
| **Medien** | Inhalte > Medien | Zentrale Dateiverwaltung (technisch nicht unter Kataloge, aber inhaltlich verknüpft) |

---

## 3. Abhängigkeitsdiagramm

```
┌─────────────────────────────────────────────┐
│                  MEDIEN                      │
│  (Bilder, Videos, Dokumente, 3D-Modelle)    │
└──────────────┬──────────────────────────────┘
               │ verwendet in
    ┌──────────┼──────────────┬──────────────┐
    ▼          ▼              ▼              ▼
PRODUKTE   KATEGORIEN    HERSTELLER    ERLEBNISWELTEN

    ▲          ▲
    │ zugewiesen
    │
EIGENSCHAFTEN ──────────────────────→ VARIANTEN
    │                                  (aus Produkten)
    └──────────────────────────────────

DYNAMISCHE PRODUKTGRUPPEN
    │
    ├──→ Kategorien (befüllen)
    ├──→ Produkte (Cross-Selling)
    └──→ Erlebniswelten (Slider)

BEWERTUNGEN ──→ Produkte (verknüpft)
```

---

## 4. Typischer Workflow: Neues Produkt einrichten

### Vorbereitungsschritte (einmalig)

1. **Eigenschaften anlegen** (Kataloge > Eigenschaften)
   - Eigenschaftsgruppen mit Ausprägungen definieren
   - z. B. Größe (XS, S, M, L, XL), Farbe (Rot, Blau, Grün)

2. **Hersteller anlegen** (Kataloge > Hersteller)
   - Name, Logo, Website-URL

3. **Kategoriestruktur aufbauen** (Kataloge > Kategorien)
   - Navigationsbaum definieren
   - Verkaufskanäle zuweisen

4. **Medien vorbereiten** (Inhalte > Medien)
   - Produktbilder hochladen
   - Ordnerstruktur anlegen

### Produktanlage

5. **Produkt anlegen** (Kataloge > Produkte)
   - Pflichtfelder: Titel, Produktnummer, Steuersatz, Preise, Lagerbestand
   - Hersteller zuweisen
   - Kategorien zuweisen
   - Bilder aus Medienverwaltung hinzufügen
   - Eigenschaften zuweisen (für Filter)
   - Varianten generieren (falls gewünscht)
   - SEO-Einstellungen vornehmen
   - Cross-Selling konfigurieren (optional)

---

## 5. Wichtige Grundregeln

### Löschen und Auswirkungen

| Aktion | Auswirkung |
|---|---|
| Eigenschaft löschen | Wird von ALLEN Produkten entfernt |
| Hersteller löschen | Nur möglich wenn kein Produkt zugewiesen |
| Kategorie löschen | Alle Unterkategorien werden mitgelöscht |
| Produkt löschen | Bleibt in bestehenden Bestellungen sichtbar (→ lieber inaktiv schalten) |
| Medium löschen | Fehlende Bilder im Shop wenn noch verwendet |

### Aktivierung

- Neue Kategorien sind initial **inaktiv**
- Neue Produkte sind initial **aktiv** (wenn kein Verkaufskanal zugewiesen → nicht sichtbar)
- Bewertungen sind nach Einreichung **nicht sichtbar** (müssen freigegeben werden)

---

## 6. Verkaufskanal-Verknüpfung

Der Katalog-Bereich ist eng mit Verkaufskanälen verknüpft:

- Produkte müssen einem Verkaufskanal zugewiesen werden um sichtbar zu sein
- Kategorien werden als Einstiegspunkt für einen Verkaufskanal festgelegt
- SEO-URLs können pro Verkaufskanal unterschiedlich konfiguriert werden
- Preise können je Währung/Kanal variieren

---

## 7. Weiterführende Dokumentation

| Thema | Skill |
|---|---|
| Produkte vollständig verstehen | `sw-merchant-catalog-products` |
| Kategorien und Navigation | `sw-merchant-catalog-categories` |
| Hersteller verwalten | `sw-merchant-catalog-manufacturers` |
| Eigenschaften und Filter | `sw-merchant-catalog-properties` |
| Dynamische Produktgruppen | `sw-merchant-catalog-product-streams` |
| Bewertungen moderieren | `sw-merchant-catalog-reviews` |
| Medienverwaltung | `sw-merchant-catalog-media` |

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/kataloge*
