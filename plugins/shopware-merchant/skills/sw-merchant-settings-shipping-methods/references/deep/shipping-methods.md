# Shopware 6 – Versandarten (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/versand

---

## Überblick

**Pfad:** Einstellungen > Handel > Versand

Tabelle mit Name, Beschreibung, Aktivstatus und Position.

---

## Versandart erstellen – Basisinformationen

| Feld | Beschreibung |
|---|---|
| Name | Intern und extern verwendeter Name |
| Technischer Name | Eindeutiger Bezeichner für Admin und Erweiterungen |
| Position | Anzeigereihenfolge im Checkout (1 = erste Stelle) |
| Aktiv | Aktivierungsstatus |
| Beschreibung | Erklärung (sichtbar in Übersicht und Frontend) |
| Logo | Benutzerdefiniertes Logo (Mediathek oder Upload) |
| Lieferzeit | Anzeigezeit bei Versandartauswahl (erfordert Aktivierung unter Warenkorb-Einstellungen) |
| Tracking-URL | Verfolgungslink mit Platzhalter `%s` für automatische Tracking-Nummer-Einfügung |
| Tags | Schlagwörter für bessere Auffindbarkeit |

---

## Verfügbarkeitsregel

Definiert anhand des Rule Builders, wann diese Versandart verfügbar ist.
- Neue Regeln können direkt erstellt werden
- Typische Bedingungen: Lieferland, Warenkorbwert, Gewicht

---

## Steuerberechnung

| Option | Beschreibung |
|---|---|
| **Automatisch** | Proportionale Berechnung basierend auf Warenkorb-Steuersätzen |
| **Höchste** | Berechnung mit dem höchsten Steuersatz im Warenkorb |
| **Festgelegt** | Manuell gewählter Steuersatz |

---

## Preismatrix

### Nach Eigenschaften
Versandpreise abhängig von:
| Eigenschaft | Einheit |
|---|---|
| Anzahl Positionen | Alle Positionen im Warenkorb |
| Warenkorbwert | Gesamtsumme aller Positionen |
| Gewicht | Standard: Kilogramm |
| Volumen | Breite × Höhe × Länge (in Kubikmillimetern) |

**Aufbau der Matrix:**
- Bis zu einem bestimmten Wert → Preis X
- Über einem bestimmten Wert → Preis Y
- Beliebig viele Staffeln möglich

### Nach Rule Builder
Alternativ: Benutzerdefinierte Regeln aus dem Rule Builder verwenden (z.B. nach Lieferland differenzieren).

---

## Verkaufskanal-Zuordnung

Versandarten müssen den Verkaufskanälen zugewiesen werden:
1. Verkaufskanäle > [Kanal auswählen] > Grundeinstellungen > Versandarten
2. Versandart hinzufügen
3. Optional: Standard-Versandart festlegen
