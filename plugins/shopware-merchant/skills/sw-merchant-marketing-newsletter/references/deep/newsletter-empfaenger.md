# Newsletter Empfänger

**Pfad:** Admin > Marketing > Newsletter Empfänger
**Version:** ab Shopware 6.0.0

## Beschreibung

Die Seite "Newsletter Empfänger" zeigt eine Liste aller Kunden, die sich in ihrem Account für den Newsletter eingetragen haben. Händler können hier Empfänger verwalten, filtern und bearbeiten.

---

## Übersicht

Die Übersichtsseite enthält folgende Elemente:

| Element | Beschreibung |
|---------|--------------|
| **(1) Liste** | Alle Newsletter-Empfänger mit Status und Basisinfos |
| **(2) Kontextmenü** | Pro Eintrag: Bearbeiten oder Entfernen |
| **(3) Listeneinstellungen** | Spalten anpassen, Einträge pro Seite |
| **(4) Filter** | Filtern nach Status, Sprache, Verkaufskanal |

![Newsletter Empfänger Übersicht](../assets/Uebersicht.png)

---

## Status-Optionen

Jeder Empfänger hat einen der folgenden Status:

| Status | Beschreibung |
|--------|--------------|
| **Warten auf Aktivierung** | Double-Opt-In-E-Mail wurde versendet, aber noch nicht bestätigt |
| **Sofort Aktiv** | Eingetragen ohne Double-Opt-In-Prozess |
| **Aktiv** | Registrierung wurde per Double-Opt-In bestätigt |
| **Warten auf Löschung** | Empfänger hat sich vom Newsletter abgemeldet |

> **Hinweis:** Der Status "Warten auf Aktivierung" bedeutet, dass der Kunde die Bestätigungs-E-Mail noch nicht angeklickt hat. Erst nach Bestätigung wechselt der Status zu "Aktiv".

---

## Filter-Funktionalität

Über den Filter-Button können Empfänger gefiltert werden nach:

- **Status:** Aktiv, Warten auf Aktivierung, Sofort Aktiv, Warten auf Löschung
- **Sprache:** Sprachversion des Shops
- **Verkaufskanal:** Welcher Shop-Kanal der Empfänger zugeordnet ist

![Filter Newsletter](../assets/Filter.png)

---

## Empfänger bearbeiten

Über das Kontextmenü oder durch Klick auf einen Eintrag kann ein Empfänger bearbeitet werden.

### Bearbeitbare Felder

| Feld | Beschreibung |
|------|--------------|
| **E-Mail-Adresse** | E-Mail des Empfängers ändern |
| **Adresse** | Lieferadresse aktualisieren |
| **Sprache** | Newsletter-Sprache anpassen |
| **Tags** | Eigene Keywords zuweisen für spätere Suche und Filterung |

> **Tags:** Ermöglichen das Hinterlegen eigener Keywords, nach denen in der Übersicht gesucht werden kann. Nützlich für Segmentierung (z. B. "VIP", "Kunde2023").

![Empfänger bearbeiten](../assets/Editieren.png)

---

## Empfänger entfernen

Über das Kontextmenü kann ein Empfänger aus der Liste entfernt werden. Dies löscht den Eintrag aus der Newsletter-Empfängerliste, entfernt aber nicht den Kundendatensatz selbst.

---

## Zusammenhang mit Rule Builder

Der Newsletter-Status kann als Bedingung im Rule Builder genutzt werden:

**Bedingung:** `Kunde ist Newsletter-Empfänger`

Dies ermöglicht z. B. automatische Rabatte für aktive Newsletter-Empfänger. Siehe `sw-merchant-marketing-rule-builder` für Details.

---

## Typische Anwendungsfälle

1. **Double-Opt-In prüfen:** Filter nach Status "Warten auf Aktivierung" zeigt Empfänger, die die Bestätigungs-E-Mail noch nicht angeklickt haben.
2. **Abgemeldete Empfänger:** Filter nach Status "Warten auf Löschung" für DSGVO-konforme Bereinigung.
3. **Segmentierung:** Tags vergeben und nach Tags filtern für gezieltes E-Mail-Marketing.
4. **Verkaufskanal-spezifisch:** Filter nach Verkaufskanal für Multi-Shop-Betrieb.
