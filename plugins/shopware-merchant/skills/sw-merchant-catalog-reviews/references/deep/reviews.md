# Shopware 6 – Produktbewertungen: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/kataloge/bewertungen  
> Gilt ab: Shopware 6.0.0+

---

## 1. Überblick

Produktbewertungen ermöglichen Kunden, Rezensionen zu gekauften oder angesehenen Produkten zu hinterlassen. In der Administration können Betreiber Bewertungen moderieren, freigeben, kommentieren und mit KI-Unterstützung zusammenfassen oder übersetzen.

Verwaltung unter: **Kataloge > Bewertungen**

---

## 2. Bewertungsübersicht

### Spalten der Übersicht

| Spalte | Beschreibung |
|---|---|
| Titel | Titel der Bewertung (vom Kunden vergeben) |
| Sterne | Anzahl der vergebenen Sterne (1–5) |
| Produkt | Das bewertete Produkt |
| Kunde | Name des bewertenden Kunden |
| Status / Sichtbarkeit | Ob die Bewertung im Frontend sichtbar ist |

### Ansichten

- **Übersicht**: Listenansicht mit den oben genannten Spalten
- **Details**: Vollständiger Bewertungstext mit allen Verwaltungsoptionen

---

## 3. Bewertung moderieren

### 3.1 Bewertung freigeben (sichtbar schalten)

1. Bewertung in der Übersicht öffnen (Klick auf Bewertung oder Bearbeiten im Kontextmenü)
2. Tab **„Eigenschaften"** öffnen
3. **„Sichtbar"** aktivieren
4. **Sprache** der Bewertung festlegen (wichtig für Sprachfilterung im Frontend)
5. Speichern

> **Wichtig**: Bewertungen sind nach dem Einreichen durch den Kunden standardmäßig **nicht sichtbar** und müssen manuell freigegeben werden!

### 3.2 Bewertung kommentieren

Betreiber können eine Antwort auf Bewertungen hinterlassen:
1. Bewertung öffnen
2. Kommentarfeld ausfüllen
3. Speichern

Der Kommentar erscheint **unterhalb der Bewertung** im Frontend-Bereich.

### 3.3 Bewertung ablehnen / unsichtbar schalten

- „Sichtbar" deaktivieren → Bewertung verschwindet aus dem Frontend
- Bewertung bleibt im System erhalten (nicht gelöscht)

---

## 4. Bewertungen deaktivieren (global)

Um das Bewertungssystem für einen Verkaufskanal komplett zu deaktivieren:

1. Einstellungen > Handel > **Produkte**
2. Bereich **„Bewertungen"**
3. Toggle **„Bewertungen anzeigen"** auf **Aus** stellen
4. Verkaufskanal auswählen (kanalspezifische Einstellung)
5. Speichern

---

## 5. Frontend-Darstellung für Kunden

Auf der Produktdetailseite sehen Kunden:

| Element | Beschreibung |
|---|---|
| Gesamtbewertung | Durchschnittliche Sternebewertung groß dargestellt |
| Bewertungsverteilung | Prozentuale und absolute Anzahl je Sternanzahl |
| Filterung | Kunden können nach Sternanzahl filtern (z. B. nur 5-Sterne) |
| „Bewertung schreiben" Button | Öffnet das Bewertungsformular |
| Andere Sprachbewertungen | Option zum Anzeigen von Bewertungen in anderen Sprachen |

### Bewertungsformular (Kundensicht)

- Titelfeld
- Sternebewertung (1–5)
- Bewertungstext: **Mindestlänge 40 Zeichen**
- Absenden-Button → Bewertung wartet auf Freigabe durch den Betreiber

---

## 6. AI-Features

### 6.1 KI-Übersetzung (ab Shopware Rise)

- Aktivierung: Einstellungen > [Shopname] > Auswahl des Verkaufskanals
- Übersetzt Bewertungen automatisch in die Sprache des Shops/Kanals
- Kunden sehen Bewertungen in ihrer eigenen Sprache

### 6.2 AI-Zusammenfassung (ab Shopware Rise)

Der **AI Copilot** generiert automatisch eine Kurzzusammenfassung aus allen Bewertungen eines Produkts:

- **Formulierungsstil wählbar**: Neutral oder positiv
- **Bearbeitbar**: Die generierte Zusammenfassung kann manuell angepasst werden
- **Im Frontend anzeigen**: Zusammenfassung erscheint prominent auf der Produktdetailseite

Aktivierung in der Bewertungs-Verwaltung des jeweiligen Produkts.

---

## 7. Bewertungen im Produktkontext

Bewertungen können auch direkt aus der Produktmaske aufgerufen werden:

1. Kataloge > Produkte > Produkt öffnen
2. Tab **„Bewertungen"**
3. Übersicht aller Bewertungen für dieses Produkt
4. Direkte Freigabe oder Verlinkung zur Bewertungs-Detailseite

---

## 8. Tipps und Best Practices

- Bewertungsbenachrichtigungen einrichten: Neue Bewertungen per E-Mail an den Betreiber senden (über Trigger/Flows konfigurierbar)
- **Antworten auf negative Bewertungen** sind öffentlich sichtbar und zeigen Kunden, dass der Betreiber aktiv ist
- **Sprache korrekt setzen** bei der Freigabe – falsche Sprachzuordnung kann dazu führen, dass Bewertungen im falschen Sprachkontext erscheinen
- Regelmäßige Moderation empfohlen (tägliches oder wöchentliches Review der neuen Bewertungen)
- Für **Trustpilot-Integration** oder externe Bewertungstools: Shopware bietet Plugins für alle gängigen Plattformen

---

## 9. Datenschutzhinweise

- Kundendaten in Bewertungen unterliegen der DSGVO
- Auf Anfrage von Kunden müssen Bewertungen gelöscht werden können
- Die Löschung erfolgt direkt in der Bewertungsverwaltung über das Kontextmenü

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/kataloge/bewertungen*
