# PayPal – Integration & Konfiguration

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/paypal

## Überblick

Die **PayPal-Extension** ist eine All-in-One-Zahlungslösung für Shopware 6 und unterstützt
neben klassischem PayPal auch Kreditkarte, Lastschrift und viele lokale Zahlungsmethoden.
Händler erhalten die **volle Zahlung sofort** – Kunden wählen ihren eigenen Zahlungszeitpunkt.

**Besonderheit**: PayPal ist in Shopware vorinstalliert (nur Aktivierung nötig).

---

## Installation & Aktivierung

### Variante 1: Während des Ersteinrichtungs-Assistenten
- Im Wizard PayPal-Schritt: API-Zugangsdaten eingeben

### Variante 2: Manuell
1. **Erweiterungen > Meine Erweiterungen** öffnen
2. PayPal-Eintrag finden → **Aktivieren**
3. Alternativ: Erweiterungen > Store → "PayPal" suchen → Hinzufügen

**Voraussetzung**: Im Shopware Account eingeloggt sein.

---

## Onboarding (Konto verknüpfen)

1. **Erweiterungen > Meine Erweiterungen > PayPal > Konfigurieren**
2. Abschnitt **Onboarding**
3. **Mit PayPal verbinden** klicken → Weiterleitung zu PayPal
4. PayPal-Händlerkonto einloggen → Berechtigungen erteilen
5. Automatische Credential-Generierung (keine manuelle API-Key-Eingabe nötig)

> **Sandbox vs. Live**: Für Tests zunächst Sandbox-Modus aktivieren.

---

## Unterstützte Zahlungsmethoden

| Methode | Beschreibung |
|---|---|
| PayPal (Wallet) | Zahlung aus dem PayPal-Konto |
| Kreditkarte | Mastercard, Visa, Amex (ohne PayPal-Konto) |
| Lastschrift (SEPA) | Direkte Bankabbuchung |
| PayPal Ratenzahlung | Kosten auf monatliche Raten aufteilen |
| PayPal Rechnungskauf | Kauf auf Rechnung (bis 14 Tage) |
| Pay Later | "Jetzt kaufen, später bezahlen" |
| Lokale Zahlarten | Abhängig von Ländereinstellung |

---

## Konfigurationsbereiche

### Onboarding
- PayPal-Händlerkonto verknüpfen
- Sandbox/Live-Modus wechseln
- API-Credentials (automatisch oder manuell)

### Shipping Tracking (ab Version 5.3.0)
- Carrier-Integration: Versandverfolgung direkt an PayPal übermitteln
- Reduziert Käuferschutz-Streitfälle

### Vaulting (ab Version 8.0.0)
- Wiederkehrende Zahlungen (Subscriptions)
- Kunden können Zahlungsmethoden speichern

### Invoice Purchase (Rechnungskauf)
- Kauf auf Rechnung mit automatischen Zahlungsanweisungen in der Bestellbestätigungs-E-Mail
- Buy Now Pay Later (BNPL)

### Smart Payment Buttons
- Anpassbare Checkout-Buttons (Farbe, Form, Größe)
- Alternative Zahlungsmethoden direkt im Button-Bereich anzeigen
- Platzierung: Produktseite, Warenkorb, Checkout

### Express Checkout
- PayPal-Button direkt auf der Produktdetailseite
- Kunden können sofort ohne Shopware-Konto kaufen

### Conflict Management
- PayPal-Streitfälle direkt im Shopware-Admin überwachen
- Transaktionsstatus und Eskalationen verfolgen

---

## Datenschutz & Datenweitergabe

Shopware übermittelt **ausschließlich aggregierte Tagesdaten** (Gesamttransaktionsvolumen) an Shopware:
- Keine personenbezogenen Daten
- Keine Bestellnummern
- Keine Einzeltransaktionen

---

## Storefront-Konfiguration

| Element | Konfigurierbar |
|---|---|
| Express Checkout Button | Position, Sichtbarkeit |
| Pay Later Banner | Platzierung auf Produktseiten, Warenkorb |
| Button-Styling | Farbe (Gold, Blau, Silber, Schwarz), Form (Rechteck, Pill) |
| Zahlungsanweisungen | E-Mail-Template für Rechnungskauf |

---

## Troubleshooting

| Problem | Lösung |
|---|---|
| Webhooks nicht aktiv | PayPal-Dashboard > Webhooks prüfen; oder Onboarding wiederholen |
| Update-Fehler | Cache leeren (`php bin/console cache:clear`), dann erneut aktualisieren |
| Sandbox-Zahlungen werden nicht verarbeitet | Sicherstellen, dass Sandbox-Modus aktiv und Sandbox-Credentials korrekt |
| Express Checkout erscheint nicht | Button-Konfiguration in den PayPal-Settings prüfen |
