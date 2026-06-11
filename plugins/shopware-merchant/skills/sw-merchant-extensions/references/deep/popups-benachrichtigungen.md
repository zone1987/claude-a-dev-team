# Anpassbare Popups & Benachrichtigungen

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/anpassbare-popups-und-benachrichtigungen  
**Verfügbar**: Kostenlos im Shopware Store  
**Mindestversion**: Shopware 6.4.0.0

## Überblick

Die Extension **Anpassbare Popups & Benachrichtigungen** ermöglicht verschiedene
Popup- und Banner-Typen für den Storefront – zur Kundenkommunikation bei Shop-Besuch.

---

## Installation

1. **Erweiterungen > Store** → "Custom Popups & Notifications" suchen
2. Kostenlos herunterladen
3. **Erweiterungen > Meine Erweiterungen** → Installieren + Aktivieren

---

## Konfigurationspfad

**Erweiterungen > Meine Erweiterungen > Anpassbare Popups & Benachrichtigungen > Konfigurieren**

Oder direkt: **Einstellungen > Erweiterungen > Anpassbare Popups & Benachrichtigungen**

Konfiguration ist **pro Verkaufskanal** möglich (verschiedene Popups für verschiedene Shops).

---

## Popup-Typen

### 1. Consent Popup (Einwilligungs-Popup)
**Beschreibung**: Popup erscheint direkt beim Shop-Besuch und muss **aktiv bestätigt** werden.

**Anwendungsfälle**:
- Altersprüfung ("Sind Sie 18 Jahre oder älter?")
- Allgemeine Einwilligung/Hinweis für bestimmte Shops (z. B. Apotheken, Alkohol-Shops)

**Konfigurierbar**:
- Titel
- Beschreibungstext
- Button-Text (Bestätigen / Ablehnen)
- Weiterleitung bei Ablehnung

---

### 2. Banner
**Beschreibung**: Konfigurierbare Leiste am **oberen Seitenrand**.

**Konfigurierbare Optionen**:
| Eigenschaft | Optionen |
|---|---|
| Hintergrundfarbe | Frei wählbar (Color Picker) |
| Textfarbe | Frei wählbar |
| Text | Freitext |
| Scrolling-Animation | Text läuft durch (Marquee-Effekt) |
| Schließbar | Ja/Nein (X-Button für Kunden) |
| Permanent | Immer sichtbar, auch nach Scroll |

**Typische Anwendungsfälle**:
- "Kostenloser Versand ab 50 €"
- "SALE: 20% auf alles" (befristet)
- "Neue Kollektion jetzt verfügbar"

---

### 3. Info Popup
**Beschreibung**: Popup beim Shop-Einstieg mit allgemeinen Informationen oder Aktionsankündigungen.

**Konfigurierbar**:
- Titel
- Beschreibungstext
- Bild hochladen (Banner-Bild für visuellen Eindruck)

**Typische Anwendungsfälle**:
- Saisonale Ankündigungen ("Winter Sale beginnt!")
- Shop-News ("Neue Funktionen verfügbar")
- Wartungsankündigungen

---

### 4. Newsletter-Registrierungs-Popup
**Beschreibung**: Popup direkt beim Shop-Besuch zur **Newsletter-Anmeldung**.

**Konfigurierbar**:
- Titel und Beschreibung
- Optionale Felder: Vorname, Nachname (an/aus)
- Pflichtfelder für Anmeldung

**Integration**: Verknüpft mit Shopware Newsletter-System
→ Abonnenten erscheinen in **Marketing > Newsletter-Empfänger**

---

## Multi-Kanal-Konfiguration

Ein Popup kann für **mehrere Verkaufskanäle** oder nur für **spezifische Kanäle** aktiviert werden.
Jeder Kanal kann unterschiedliche Popup-Einstellungen haben.

---

## DSGVO-Hinweise

- Consent Popup: Geeignet für Pflichteinwilligungen
- Newsletter Popup: Double-Opt-In muss in Shopware-Einstellungen konfiguriert sein
  → **Einstellungen > E-Mail-Templates > Newsletter-Bestätigung**
