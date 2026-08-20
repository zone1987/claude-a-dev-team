# Klarna Payments – Integration & Konfiguration

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/klarna

## Überblick

**Klarna Payments** für Shopware 6 bietet ein einfaches Einkaufserlebnis:
- Händler erhalten die **volle Zahlung sofort**
- Kunden wählen ihren eigenen Zahlungszeitpunkt (Ratenzahlung, Rechnung, Sofort)

---

## Zahlungsoptionen

| Option | Beschreibung |
|---|---|
| **Rechnung (Invoice)** | Kauf jetzt, Zahlung innerhalb von 14 Tagen – kostenlos für Kunden |
| **Ratenzahlung (Installments)** | Kosten auf monatliche Zahlungen aufteilen |
| **Sofortzahlung (Direct)** | Banküberweisung, Lastschrift, Kreditkarte |

---

## Installation

### Variante 1: Ersteinrichtungs-Assistent
- Im Wizard-Schritt "Erweiterungen" nach Klarna suchen und installieren

### Variante 2: Shopware Store
1. https://store.shopware.com → "Klarna" suchen
2. Lizenz erwerben
3. Im Admin: **Erweiterungen > Meine Erweiterungen** → Installieren + Aktivieren

### Variante 3: Direkt im Admin
1. **Erweiterungen > Store** im Admin
2. "Klarna" suchen → Hinzufügen/Kaufen
3. Aktivierung über Toggle in Meine Erweiterungen

**Voraussetzung**: Im Shopware Account eingeloggt sein (für Lizenzverifizierung).

---

## Konfiguration

Für die vollständige Einrichtung verweist die Shopware-Dokumentation auf die offizielle
Klarna-Dokumentation: https://klarna-shopware.426-upgrade.com/de/index.html

### Grundlegende Schritte
1. Klarna-Händlerkonto erstellen: https://portal.klarna.com
2. API-Credentials (API Key + Secret) in der Klarna-Konfiguration im Shopware Admin eintragen
3. Zahlungsmethoden aktivieren (Rechnung, Ratenzahlung, Sofort)
4. Zahlungsmethoden den Verkaufskanälen zuordnen (Einstellungen > Zahlungen)
5. Regeln für Verfügbarkeit konfigurieren (z. B. nur für bestimmte Länder)

---

## Regionale Verfügbarkeit

Klarna Payments ist in folgenden Ländern verfügbar (Stand 2024):
- Deutschland, Österreich, Schweiz
- Schweden, Norwegen, Finnland, Dänemark
- Niederlande, Belgien
- Vereinigtes Königreich
- USA, Kanada, Australien
- und weitere Länder

---

## Hinweise für die Nutzung

- Klarna prüft die Bonität der Kunden automatisch im Hintergrund
- Nicht verfügbare Zahlmethoden werden im Checkout automatisch ausgeblendet
- Streitfälle und Rückerstattungen über das Klarna-Portal verwalten
