# Shopware Abonnements (Subscriptions) – Vollständige Dokumentation

## Überblick

Das Abonnements-Feature ermöglicht Händlern, wiederkehrende Bestellungen mit konfigurierbaren Intervallen anzubieten.

**Verfügbarkeit:** Beyond-Plan (auch: Rise laut einiger Quellen, primär Beyond)
**Mindestversion:** Shopware 6.5.4.0
**Voraussetzung:** Shopware Commercial Extension

---

## Kernkonzepte

### Plans (Abonnementpläne)

Pläne sind die Grundkonfigurationen für Abonnements. Jeder Plan definiert:

| Einstellung | Beschreibung |
|---|---|
| Name | Anzeigename des Plans im Storefront |
| Aktiv/Inaktiv | Sichtbarkeit für Kunden |
| Beschreibung | Erläuterung für Kunden |
| Verfügbarkeitsregeln | Rule Builder Integration für Bedingungen |
| Intervalle | Lieferrhythmus (täglich/wöchentlich/monatlich) |
| Mindestlaufzeit | Minimale Abo-Dauer vor Kündigung |
| Rabatt | Prozentualer Preisnachlass während der Abo-Dauer |

**Pfad im Admin:** Einstellungen → Abonnements → Pläne → Neuer Plan

#### Produkt-Zuweisung

Produkte können bidirektional mit Plänen verknüpft werden:
- Im Plan unter dem Tab „Produkte" Produkte hinzufügen
- Im Produkt selbst einen Plan zuweisen

### Intervalle

Flexible Zeitplanung für Lieferungen:

| Modus | Einstellung |
|---|---|
| Täglich | Intervall in Tagen |
| Wöchentlich | Wochentag auswählen |
| Monatlich | Datum im Monat |
| Erweitert | Kombination aus Wochentag, Datum und Monat |

Im Admin wird eine Vorschau der nächsten Bestelltermine angezeigt.

**Screenshot:** `../../assets/abonnements-intervalle.png`

---

## Storefront-Erlebnis

### Produktdetailseite

- Abonnement-Auswahl erscheint neben der „In den Warenkorb"-Option
- Mehrere Pläne werden als Radio-Button-Auswahl angezeigt
- Bei Auswahl eines Plans ändert sich der Button zu „Jetzt abonnieren"
- Separater Checkout-Prozess für Abonnements

**Screenshot:** `../../assets/abonnements-storefront.png`

### Mixed Cart (ab 6.7.4.0)

Kunden können Abonnements und Einmalkäufe im selben Warenkorb kombinieren:
- System trennt automatisch wiederkehrende und einmalige Lieferungen
- Rabatte und Versandkosten werden korrekt für beide Typen berechnet
- Kunden sehen klare Trennung im Checkout

---

## Zahlungsmethoden

Folgende Zahlungsmethoden werden unterstützt:

| Methode | Voraussetzung |
|---|---|
| Vorkasse | Standard |
| Rechnung | Standard |
| PayPal | PayPal mit aktiviertem Vaulting |
| Kreditkarte | PayPal Vaulting aktiviert |

**Wichtig:** Nicht alle Zahlungsanbieter unterstützen wiederkehrende Lastschriften. PayPal Vaulting muss separat aktiviert werden.

---

## Kundenverwaltung im Storefront

Kunden können ihre Abonnements eigenständig verwalten:

| Aktion | Beschreibung |
|---|---|
| Übersicht | Dashboard zeigt alle aktiven Abonnements |
| Pausieren | Einmalige Pause für einen Zyklus |
| Kündigen | Abonnement beenden |
| Status einsehen | Aktueller Status jedes Abonnements |

**Admin-Screenshot:** `../../assets/abonnements-pause-admin.png`

---

## Kündigungsverhalten

Das System unterscheidet zwei Szenarien:

### Mit Mindestlaufzeit
- Status: „Zur Kündigung vorgemerkt" (bis Laufzeit abläuft)
- Bestellungen laufen automatisch weiter bis zum Laufzeitende
- Kündigung wird erst nach Ablauf wirksam

### Ohne Mindestlaufzeit
- Status: „Zur Kündigung vorgemerkt" (sofort)
- Letzte Bestellung wird noch verarbeitet
- Dann endet das Abonnement

---

## Admin-Verwaltung

Händler können im Admin:
- Alle Kundabonnements einsehen und filtern
- Status manuell ändern
- Abonnements im Namen des Kunden pausieren/kündigen
- Protokoll aller Abonnement-Aktionen einsehen

**Pfad:** Bestellungen → Abonnements (oder Einstellungen → Abonnements)

---

## Integration mit anderen Features

### Rule Builder
- Verfügbarkeitsregeln für Pläne (z.B. nur für bestimmte Kundengruppen)
- Zahlungsmethoden-Einschränkungen per Regel

### Flow Builder
- Trigger: Abonnement erstellt / pausiert / gekündigt
- Aktionen: Erinnerungs-E-Mails, Verzögerungen vor Ablauf
- Beispiel: 3 Tage vor nächster Lieferung E-Mail senden

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/abonnements (Stand: 2026-06)*
