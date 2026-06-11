# Shopware 6 – Kategorien: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/kataloge/kategorien  
> Gilt ab: Shopware 6.4.0.0+

---

## 1. Kategorieübersicht

Pfad: **Kataloge > Kategorien**

Die Kategorieverwaltung zeigt eine **Baumstruktur** (linke Seite) mit allen angelegten Kategorien.

### Baumstruktur-Funktionen

- **Drag & Drop**: Kategorien auf allen Ebenen verschiebbar
- Kategorien können als Unterkategorien unter andere gezogen werden
- Mehrere unabhängige Kategoriebäume möglich (z. B. für Footer, Service-Navigation)
- Rechtsklick / Drei-Punkte-Menü öffnet Kontextmenü

---

## 2. Kategorie anlegen

### Kontextmenü-Optionen

| Option | Ergebnis |
|---|---|
| Neue Kategorie davor | Neue Kategorie auf gleicher Ebene, vor der aktuellen |
| Neue Kategorie danach | Neue Kategorie auf gleicher Ebene, nach der aktuellen |
| Neue Subkategorie | Untergeordnete Kategorie unter der aktuellen |
| Bearbeiten | Öffnet die Bearbeitungsansicht |
| Löschen | Löscht Kategorie inkl. aller Unterkategorien |

### Schritt-für-Schritt

1. Kontextmenü der übergeordneten Kategorie öffnen
2. Gewünschte Anlage-Option wählen
3. Kategorienamen eingeben
4. Mit Häkchen bestätigen
5. Kategorie öffnen und **„Kategorie ist aktiv"** einschalten
6. Verkaufskanal zuweisen (falls Einstiegspunkt)

> **Wichtig**: Neu angelegte Kategorien sind initial **inaktiv**!

---

## 3. Kategorietypen

| Typ | Verwendung | Tabs verfügbar |
|---|---|---|
| Seite/Liste | Standard-Produktlisting, Shopseiten | Allgemein, Produkte, Layout, SEO |
| Strukturierungselement/Einstiegspunkt | Nur Navigationsgruppeierung, kein Inhalt | Allgemein |
| Link | Weiterleitung zu internen/externen Zielen | Allgemein |

---

## 4. Tab: Allgemein

### 4.1 Grundeinstellungen

| Feld | Beschreibung |
|---|---|
| Name (1) | Kategoriename; nachträglich änderbar; erscheint in Navigation |
| Kategorie ist aktiv (2) | Schalter; bestimmt ob Kategorie im Frontend erscheint |
| Tags (3) | Schlagworte für andere Programmbereiche (z. B. Rule Builder) |
| Kategorietyp (4) | Auswahl: Seite/Liste, Strukturierungselement, Link |

### 4.2 Benutzerdefinierter Link (nur bei Typ „Link")

| Feld | Beschreibung |
|---|---|
| Linktyp (1) | Extern (URL) oder Intern (Shopware-Entity) |
| Entität / Linkziel (2) | Bei extern: vollständige URL; bei intern: Entity-Auswahl |
| In neuem Tab öffnen (3) | Öffnet den Link in einem neuen Browser-Tab |

### 4.3 Einstiegspunkt (bei Seite/Liste und Strukturierungselement)

| Feld | Beschreibung |
|---|---|
| Einstiegspunkt (1) | Wo der Kategoriebaum im Shop verankert ist |
| | **Hauptnavigation**: Klassischer Produktaufbau oben |
| | **Footernavigation**: Unterer Seitenbereich (Impressum, Datenschutz) |
| | **Servicenavigation**: Oben rechts (z. B. Login, Kontakt) |
| Verkaufskanäle (2) | Mehrfachauswahl; welchen Kanälen dieser Baum zugeordnet ist |
| Startseite konfigurieren (3) | Kanal-spezifische Startseiten-Einstellungen |

### 4.4 Menü-Einstellungen

| Feld | Beschreibung |
|---|---|
| In der Navigation ausblenden (1) | Entfernt Kategorie aus der Navigationsleiste (Seite bleibt erreichbar) |
| Anzeigebild (2) | Bild das im Dropdown-Menü der Navigation angezeigt wird |
| Beschreibung (3) | Kundeninformation zur Kategorie (z. B. im Hover-Menü) |

---

## 5. Tab: Produkte

| Feld | Beschreibung |
|---|---|
| Typ (1) | Manuelle Auswahl oder Dynamische Produktgruppe |
| Produkte / Dynamische Produktgruppe (2) | Produkte manuell auswählen oder Produktgruppe verknüpfen |
| Produktliste (3) | Übersicht der aktuell zugewiesenen Produkte |

> **Hinweis**: Beim Wechsel zu dynamischer Zuordnung werden alle manuellen Zuweisungen in dieser Kategorie deaktiviert!

---

## 6. Tab: Layout

### 6.1 Layout zuweisen

- Erlebniswelt-Layout aus bestehenden Layouts auswählen
- **„Neues Layout erstellen"**: Öffnet direkt den Erlebniswelten-Editor
- Blöcke können direkt im Kategoriekontext angepasst werden (ohne Erlebniswelten zu wechseln)

### 6.2 Anpassungshierarchie (Mehrsprachigkeit)

Prioritätsreihenfolge bei Sprachauswahl (höchste Priorität zuerst):

1. Sprachspezifische Anpassungen in dieser Kategorie
2. Eltern-Kind-Sprach-Fallback
3. System-Standardsprache
4. Layout-Einstellungen (niedrigste Priorität)

**Beispiele:**

- Nur Englisch-Anpassung vorhanden → alle Storefronts zeigen die Englisch-Version
- Österreichisch-Anpassung + Layout Englisch/Deutsch → Österreich bekommt eigene Anpassung
- Deutsch + Englisch vorhanden → Österreich erbt automatisch von Deutsch

### 6.3 Sichtbarkeit und Sortierung

| Funktion | Beschreibung |
|---|---|
| Sichtbarkeit anzeigen | Zeigt Viewport-Sichtbarkeit des Layout-Blocks |
| Block-Sichtbarkeit | Pro Block einstellbar (Desktop/Tablet/Mobil) |
| Produkt-Sortierung anzeigen | Frontend-Dropdown für Kunden zum Sortieren |
| Eigene Sortierung verwenden | Aktiviert erweiterte Sortieroptionen im Admin |
| Standard-Sortierung | Fallback wenn keine eigene Sortierung gewählt |
| Priorität | Reihenfolge bei mehreren Sortieroptionen |

---

## 7. Tab: SEO

| Feld | Beschreibung |
|---|---|
| SEO-Titel | Titel für Suchmaschinen (erscheint im Browser-Tab) |
| SEO-Beschreibung | Meta-Beschreibung für Suchmaschinen |
| Keywords | Zusätzliche Suchbegriffe |
| SEO URLs | Pro Verkaufskanal konfigurierbar; standardmäßig von SEO-Einstellungen abhängig |

---

## 8. Kategoriestruktur-Beispiele

### Beispiel 1: Shop mit Unterkategorien

```
Katalog #1 (Einstiegspunkt: Hauptnavigation)
├── Lebensmittel
│   ├── Getränke
│   └── Snacks
├── Bekleidung
│   ├── Herren
│   └── Damen
└── Freizeit & Elektro
```

Erstellung:
1. „Katalog #1" → Kontextmenü → „Neue Subkategorien"
2. Je Hauptkategorie: Kontextmenü → „Neue Subkategorie"

### Beispiel 2: Mehrere Shops (Subshop-Setup)

```
Katalog #1 (Verkaufskanal A)
├── Kategorie A1
└── Kategorie A2

Katalog #2 (Verkaufskanal B)
├── Kategorie B1
└── Kategorie B2
```

Erstellung:
1. „Katalog #1" → Kontextmenü → „Neue Kategorie danach" → „Katalog #2"
2. Je Katalog den passenden Verkaufskanal zuweisen

---

## 9. Landingpages

Landingpages sind **interne Seiten ohne Navigationseintrag**. Sie sind nur über eine direkte URL erreichbar.  
Adresse: `[Verkaufskanal-URL]/[Landingpage-SEO-URL]`

### Verwaltung

- Unterhalb der Kategorieübersicht (eigener Bereich)
- Reihenfolge der Landingpages ist irrelevant
- Kontextmenü: Entfernen, Duplizieren, Bearbeiten
- **„Landingpage hinzufügen"** Button

### Tab: Allgemein (Landingpages)

| Feld | Beschreibung |
|---|---|
| Name (1) | Interner Name und Seitentitel |
| Landingpage ist aktiv (2) | Steuert URL-Erreichbarkeit |
| Verkaufskanäle (3) | Zuordnung zu einem oder mehreren Kanälen |
| Tags (4) | Hilft bei der Admin-Suche |

### Tab: SEO (Landingpages)

| Feld | Beschreibung |
|---|---|
| SEO-Titel | Suchmaschinen-Titel |
| SEO-Beschreibung | Meta-Beschreibung |
| Keywords | Zusätzliche Suchbegriffe |
| SEO URL (**Pflichtfeld**) | Eindeutiger Seiten-Identifier; z. B. „aktion-sommer" → URL: `www.shop.de/aktion-sommer` |

Die SEO-URL wird automatisch aus dem Namen generiert, ist aber manuell anpassbar.

### Tab: Layout (Landingpages)

Identisch zu Kategorien-Layout:
- Erlebniswelt zuweisen
- Block-basierte Anpassung
- Mehrsprachige Anpassungen möglich

---

## 10. Tipps und Hinweise

- Kategorien können mehreren Verkaufskanälen als Einstiegspunkt dienen
- Eine Kategorie kann in mehreren Shops (verschiedene Verkaufskanäle) sichtbar sein
- Beim Löschen einer Elternkategorie werden **alle Unterkategorien** mitgelöscht
- Produkte bleiben nach dem Löschen einer Kategorie weiterhin im System, sind aber ggf. keiner Kategorie mehr zugeordnet
- Die Kategoriesortierung im Baum entspricht der Sortierung im Frontend

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/kataloge/kategorien*
