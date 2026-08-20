# Shopware 6 – Erlebniswelten (Shopping Experiences)

Pfad: **Inhalte > Erlebniswelten**

Shopwares visuelles Drag-and-Drop-CMS zur Gestaltung aller Seitentypen.
Keine Code-Kenntnisse erforderlich.

## Architektur

```
Layout (Seitentyp)
└── Sektion
    └── Block (aus Bibliothek)
        └── Element (Text, Bild, Video, ...)
```

## Layout erstellen – Schritt für Schritt

1. **Inhalte > Erlebniswelten > „Neues Layout anlegen"**
2. Seitentyp wählen (Shopseite / Landingpage / Kategorieseite / Produktseite / Bundle)
3. Sektions-Layout wählen (Sidebar oder volle Breite)
4. Layout benennen → Bestätigen
5. Im Editor: Blöcke per Drag-and-Drop aus rechter Sidebar einfügen
6. Elemente konfigurieren (Inhalt, Darstellung, Links)
7. Speichern → Layout zuweisen

## Block-Kategorien

Vollständige Referenz: `SHOPPING-EXPERIENCES-DETAIL.md`

## Layout zuweisen

| Seitentyp | Zuweisung |
|---|---|
| Shopseite | Einstellungen > Shops > Stammdaten |
| Kategorieseite | Kataloge > Kategorien > Tab Layout |
| Landingpage | Kataloge > Kategorien (als Landingpage) |
| Produktseite | Kataloge > Produkte > Tab Layout |
