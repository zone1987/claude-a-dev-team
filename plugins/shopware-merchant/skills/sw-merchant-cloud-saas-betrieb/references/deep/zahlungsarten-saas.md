# Shopware SaaS — Zahlungsarten konfigurieren

**Quelle**: https://docs.shopware.com/de/shopware-6-de/saas/zahlungsarten

---

## Zugang

Nach Shop-Erstellung: Dashboard-Checkliste nutzen  
Alternativ: **Einstellungen > Shop > Zahlungsarten**

---

## Standardmäßig verfügbare Zahlungsarten

| Zahlungsart | Prozess |
|---|---|
| **Nachnahme** | Versand mit Nachnahme-Service; Zahlung bei Warenerhalt |
| **Vorkasse** | Bankverbindung bereitstellen; Kunde überweist vorab |
| **Rechnung** | Ware mit Rechnung versenden; Kundenausgleich erforderlich |

---

## PayPal

Die **PayPal-Erweiterung** bietet gängige PayPal-Zahlungsarten:
- PayPal Standard
- PayPal Express
- PayPal SEPA
- Später bezahlen (Pay Later)
- Kreditkarte via PayPal

**Aktivierung:**
1. Erweiterung aktivieren
2. PayPal-Account verknüpfen

**Verknüpfung:** Button „Connect PayPal Account" in den PayPal-Einstellungen anklicken → Zugangsdaten in Modal eingeben.

**Testmodus:** Verbindet Shop mit Sandbox-Account (Testbestellungen erscheinen NICHT im echten PayPal-Händlerkonto).

> „Nur für Evaluierungszwecke gedacht. Nicht in Produktionsumgebungen verwenden."

---

## Zahlungsart dem Verkaufskanal zuordnen

Zahlungsarten müssen dem Verkaufskanal zugewiesen werden:
1. Verkaufskanal öffnen
2. Reiter **Allgemein > Grundeinstellungen**
3. Verfügbare Zahlungsarten festlegen
4. Standard-Zahlungsart definieren

---

## Zahlungsart konfigurieren

| Feld | Beschreibung |
|---|---|
| **Name** | Admin & Storefront-Anzeige |
| **Position** | Sortierreihenfolge (kleinerer Wert = weiter oben) |
| **Beschreibung** | Kundenanleitungen / Erklärungstext |
| **Logo** | Individuelles Zahlungsart-Icon |
| **Aktiv** | Temporäre Deaktivierung möglich |
| **Zahlartwechsel nach Bestellabschluss erlauben** | Nachträgliche Änderung im Kundenaccount |
| **Verfügbarkeitsregel** | Bedingte Anzeige via Rule Builder |

---

## PayPal-Konfiguration (Detaileinstellungen)

**Pfad:** Einstellungen > Erweiterungen > PayPal

### Verkaufskanal-Einstellungen

| Einstellung | Beschreibung |
|---|---|
| Zahlungsabschluss | Wann Zahlung verarbeitet wird |
| Warenkorb-Übertragung | Artikel-Details oder nur Gesamt an PayPal senden |
| Markenname | Eigener Name auf PayPal-Zahlungsseite |
| Einstiegsseite | Registrierungsformular oder Login-Screen |
| Bestellnummer-Übertragung | Bestellnummer an PayPal senden |
| Bestellnummer Prefix/Suffix | Format der Bestellnummer anpassen |

### Express Checkout — Anzeige in Storefront

Express-Button anzeigen auf:
- Produktdetailseiten
- Warenkorb
- Off-Canvas-Warenkorb
- Login-Seite
- Listing-Seiten

**Button-Anpassung:**
- Farben: Gold, Blau, Silber, Schwarz
- Form: Rund oder rechteckig
- Sprache: Locale-Codes (z.B. `de_DE`, `en_GB`)
- „Pay Later"-Button ein-/ausblenden

---

## Storefront-Anzeige

Zahlungsarten werden im **modalen Fenster** während des Checkouts angezeigt.
Änderung vor und nach Bestellabschluss möglich.

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/saas/zahlungsarten | https://docs.shopware.com/de/shopware-6-de/saas/paypal*
