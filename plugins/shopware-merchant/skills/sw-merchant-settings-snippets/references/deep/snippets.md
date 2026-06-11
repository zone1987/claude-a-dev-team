# Shopware 6 – Textbausteine / Snippets (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/Textbausteine

---

## Überblick

**Pfad:** Einstellungen > Shop > Textbausteine  
Textbausteine dienen der Übersetzung und Anpassung von Texten in Storefront oder Dokumenten.

---

## Standard-Textbaustein-Sets

- `BASE de-DE` — Standardübersetzungen Deutsch
- `BASE en-GB` — Standardübersetzungen Englisch

> Die Basis-JSON-Dateien (`messages.de.base.json`, `storefront.de.json`) sollten **nicht manuell** angepasst werden, da sie zum Zurücksetzen benötigt werden.

---

## Verwaltungsfunktionen (Übersicht)

| Funktion | Beschreibung |
|---|---|
| Mehrfachänderung | Mehrere Sets gleichzeitig bearbeiten |
| Textbaustein-Set hinzufügen | Neues Set basierend auf Basisdateien erstellen |
| Kontextmenü | Sets bearbeiten, duplizieren oder löschen |
| Inline-Bearbeitung | Doppelklick aktiviert direkte Änderungen |

---

## Textbaustein bearbeiten

### Zugangswege
1. Direkt auf den Setnamen klicken
2. Sets per Checkbox auswählen → „Mehrfachänderung"
3. Kontextmenü verwenden

### Listenfunktionen
- Name-Spalte: Textbaustein-Schlüssel
- Separate Eingabefelder pro Set
- Aktualisieren-Button: Ansicht aktualisieren
- Filter-Optionen verfügbar

### Detailseite
Durch Klick auf Schlüssel oder „Bearbeiten" können Übersetzungen **setübergreifend** bearbeitet werden.

---

## Zurücksetzen-Dialog

- Auswahl via Checkboxen: Welche Sets sollen zurückgesetzt werden
- Anzeige aktueller und ursprünglicher Übersetzung
- „Für alle Textbaustein-Sets zurücksetzen": Globales Zurücksetzen

---

## Filter-Optionen

| Filter | Beschreibung |
|---|---|
| Nur leere Textbausteine | Einträge ohne Inhalt |
| Nur angepasste Textbausteine | Manuell bearbeitete Texte |
| Nur hinzugefügte Textbausteine | Von Admins erstellte Texte |
| Autor | Filtert nach Ersteller (Standard: „Shopware") |
| Bereich/Funktion | z.B. `_checkout_` |

---

## Neuen Textbaustein anlegen

**Globale Erstellung** — kein separates Anlegen pro Set nötig.

### Anforderungen
- Eindeutiger Name/Schlüssel (keine Leerzeichen oder Sonderzeichen)
- Beschreibender Name empfohlen (z.B. `checkout.headline`)
- Separate Eingabefelder pro verfügbarem Set

---

## Neues Textbaustein-Set anlegen

### Methode 1: Hinzufügen via Button
1. Inline-Bearbeitung mit aktiviertem Formular
2. Name eingeben
3. **Locale** festlegen (z.B. `en-GB`, `de-DE` oder zweistelliger ISO-639-1-Code)
4. **Basisdatei** auswählen (Fallback)
5. Speichern

> Locale folgt dem **BCP-47-Standard** und ist auf ISO-639-1-Sprachcodes beschränkt.

### Methode 2: Duplizieren
1. Kontextmenü eines bestehenden Sets
2. Kopie erhält Suffix `_Kopie`
3. Namenänderung via Doppelklick in der Übersicht (nicht auf der Detailseite)

---

## Tipps & Tricks

### Links in Textbausteine einbinden
```html
<a href="https://example.com">Angezeigter Text</a>
```

### Service-Hotline bearbeiten
- Textbaustein-Schlüssel: `footer.serviceHotline`
- Wird im Storefront-Footer angezeigt
- Erreichbar über Einstellungen > Shop > Textbausteine

### Zeilenumbrüche einfügen
```html
Nach dem Komma,<br> kommt ein Zeilenumbruch.
```
