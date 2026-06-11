# Shopware 6 – Abonnements (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/abonnements

---

## Überblick

**Pfad:** Einstellungen > Handel > Abonnements  
**Verfügbar ab:** 6.5.4.0  
**Plan:** Commercial — Shopware Beyond

Ermöglicht wiederkehrende Bestellungen mit konfigurierbaren Intervallen.

---

## Konfiguration: Drei Tabs

### Tab 1: Pläne

**Allgemeine Einstellungen:**
| Feld | Beschreibung |
|---|---|
| Name | Name des Abonnements |
| Aktiv | Aktivierungsschalter |
| Abweichender Storefront-Name | Optional anderen Namen für Kunden anzeigen |
| Beschreibung | Erklärungstext |
| Verfügbarkeitsregeln | Rule-Builder-Integration |

**Intervall-Konfiguration:**
| Feld | Beschreibung |
|---|---|
| Intervalle | Auswahl verfügbarer Intervalle |
| Mindestlaufzeit | Mindestabonnementszeit (z.B. 24 Monate) |
| Rabatt | Prozentrabatt während Abonnementdauer |

**Produkte-Zuordnung:** Produkte per Checkbox auswählen (Produktname + Produktnummer).

---

### Tab 2: Intervalle

**Grundeinstellungen pro Intervall:**
| Feld | Beschreibung |
|---|---|
| Name | Bezeichnung des Intervalls |
| Aktiv | Ein-/Ausschalten |
| Verfügbarkeitsregeln | Rule-Builder-Integration |
| Frequenz | z.B. wöchentlich, zweiwöchentlich |
| Zeitintervall | Tage, Wochen, Monate |
| Vorschau | Zukünftige Liefertermine |

**Erweiterte Einstellungen:**
- Reguläre Frequenz mit Detailoptionen
- Wochentag-Selektion
- Tage im Monat
- Monate im Jahr

---

### Tab 3: Einstellungen (ab v6.7.4.0)

| Option | Beschreibung |
|---|---|
| Gemischte Warenkörbe | Einmalprodukte und Abonnements in einer Bestellung kombinieren |

---

## Storefront-Darstellung

- Neben Warenkorb-Button erscheint Abonnement-Button
- Bei mehreren Plänen: Auswahl via Radiobutton
- Button wechselt zu „Jetzt abonnieren" bei Planauswahl

---

## Verwaltung

### Im Admin (Bestellungen > Abonnements)
- Abonnementdetails einsehen
- Status ändern: Aktiv, Pausiert, Gekündigt

### Im Kundenlogin
- Pausieren für einen Turnus
- Kündigen des Abonnements

**Status-Logik bei Kündigung vor Mindestlaufzeit:**
Admin zeigt „zur Kündigung vorgemerkt" — weitere Bestellungen werden weiterhin generiert bis Mindestlaufzeit erfüllt.

---

## Admin-Ansicht (gemischte Bestellungen)

- Alle Positionen sichtbar
- Abonnementartikel tragen Abonnement-Nummer
- Einmalprodukte ohne Nummer
- Rabatte automatisch zugeordnet

---

## Integration

| System | Unterstützung |
|---|---|
| Rule Builder | Zahlungsarten-Ausschluss, Verfügbarkeit |
| Flow Builder | Erinnerungsmails mit Delay-Funktion |
| Zahlungsarten | Vorkasse, Rechnung; mit PayPal Vaulting auch PayPal und Kreditkarte |
