# Sprachpaket – Mehrsprachigkeit für Admin & Storefront

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/sprachpaket  
**Verfügbar**: Kostenlos im Shopware Store  
**Wichtig**: Ab Shopware 6.8 nicht mehr unterstützt!

## Überblick

Das **Sprachpaket** ermöglicht den Betrieb von Shopware 6 in bis zu 29 Sprachen –
sowohl für die Administration als auch für den Storefront.

---

## WICHTIG: Deprecation ab Version 6.8

> **Das Sprachpaket wird ab Shopware 6.8 nicht mehr unterstützt.**
> Ab Shopware 6.7.3.0 steht ein **natives Sprach-Management-System** zur Verfügung.
> → Migration auf das native System für neue Installationen empfohlen.

---

## Unterstützte Sprachen (29)

| Sprache | Sprache | Sprache |
|---|---|---|
| Bosnisch | Bulgarisch | Chinesisch (vereinfacht) |
| Chinesisch (traditionell) | Dänisch | Englisch (USA) |
| Finnisch | Französisch | Griechisch |
| Hebräisch | Hindi | Indonesisch |
| Italienisch | Japanisch | Koreanisch |
| Kroatisch | Niederländisch | Norwegisch |
| Persisch | Polnisch | Portugiesisch |
| Russisch | Schwedisch | Serbisch |
| Slowakisch | Spanisch | Tschechisch |
| Türkisch | Ukrainisch | Ungarisch |
| Vietnamesisch | | |

(Englisch und Deutsch sind in Shopware standardmäßig enthalten)

---

## Installation

### Variante 1: Ersteinrichtungs-Assistent
- Im Wizard-Schritt "Erweiterungen" Sprachpaket suchen und installieren

### Variante 2: Shopware Store
1. https://store.shopware.com → "Sprachpaket Shopware 6" suchen
2. Kostenlose Lizenz aktivieren
3. Im Admin: **Erweiterungen > Meine Erweiterungen** → Installieren + Aktivieren

---

## Konfiguration

### Für die Administration (Admin-Interface)
Nach Installation und Aktivierung:
1. **Profil** (unten links) → Sprache auswählen
2. Seite neu laden → Admin in neuer Sprache

### Für den Storefront
Storefront-Sprachen müssen explizit aktiviert werden:
1. **Verkaufskanäle** → Storefront öffnen
2. Abschnitt "Sprachen" → gewünschte Sprache hinzufügen
3. Als Standard-Sprache setzen oder als zusätzliche Sprache

---

## Übersetzungsworkflow

Nachdem eine Sprache zum Verkaufskanal hinzugefügt wurde:

1. **Produkte** übersetzen: Katalog > Produkte > [Produkt] → Sprache oben rechts wechseln
2. **Kategorien** übersetzen: Katalog > Kategorien → Sprache wechseln
3. **E-Mail-Templates** übersetzen: Einstellungen > E-Mail-Templates → Sprache wechseln
4. **Erlebniswelten** übersetzen: Content > Erlebniswelten → Sprache wechseln

### Vererbungsmodell
- Felder ohne Übersetzung erben von der **Standard-/Fallback-Sprache**
- Vererbung wird durch grünes Schloss-Symbol angezeigt
- Schloss öffnen = Feld kann überschrieben werden

---

## Migration auf natives Sprachsystem (ab 6.7.3.0)

Ab Shopware 6.7.3.0 ist das Sprachpaket nicht mehr notwendig:
- Sprachen direkt in den Shop-Einstellungen verwalten
- Kein separater Extension-Download nötig
- **Einstellungen > Sprachen** im Admin

Für bestehende Installationen mit Sprachpaket:
1. Native Sprachen im Admin konfigurieren
2. Sprachpaket deaktivieren (nach Überprüfung, dass alle Übersetzungen vorhanden)
3. Sprachpaket deinstallieren
