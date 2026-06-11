# Shopware SaaS — Erweiterungen verwalten

**Quelle**: https://docs.shopware.com/de/shopware-6-de/saas/erweiterungen

> Diese Dokumentation gilt ausschließlich für Nutzer einer **Shopware 6 SaaS-Umgebung** (nicht für self-hosted).

---

## Store — Erweiterungen finden

Kostenlose und kostenpflichtige Erweiterungen durchstöbern und erwerben.

**Verfügbare Filter:**
- Sortierung
- Kategorien
- Bewertungen
- Bezahlmodell
- Zusatzoptionen (Support, Testversionen)

---

## Erweiterung hinzufügen

Prozess über Modal:
1. AGB akzeptieren (Pflicht)
2. Berechtigungen bestätigen (je nach Funktionsumfang der App)
3. Link „Berechtigungen anzeigen" für Details aufrufen (optional)
4. Erfolgsmeldung erscheint nach Abschluss

---

## Meine Erweiterungen verwalten

### Apps-Bereich
- Übersicht aller Apps mit Basisinformationen
- Schalter zum Ausblenden inaktiver Apps
- Sortieroptionen
- Aktiv-/Deaktiv-Schalter je App
- Kontextmenü:
  - **Berechtigungen** anzeigen
  - **Aktualisieren**
  - **Deinstallieren**
- Upload-Funktion für manuelle Installation (ZIP)

### Themes-Bereich
- Ähnliche Verwaltungsfunktionen wie Apps
- Zusätzliche Optionen: „Datenschutz & Datensicherheit", „Datenschutz-Erweiterungen"
- **Hinweis:** Aktive Themes müssen zusätzlich dem Verkaufskanal zugeordnet werden

---

## Erweiterung installieren

Button **„App installieren"** → Installation starten → danach ist „App öffnen" verfügbar.

---

## Kostenpflichtige Erweiterung kündigen und entfernen

Vollständige Entfernung erforderlich (Deaktivieren allein genügt nicht zur Kündigung).

**Vorgehen:**
1. „..."-Button bei der Erweiterung
2. **„Kündigen und entfernen"** wählen

> ⚠️ **Warnung:** Alle Einstellungen der Erweiterung gehen verloren!

---

## Inkompatible Apps

**Kennzeichnung:** Wird angezeigt wenn Apps mit der kommenden Shopware-Hauptversion nicht kompatibel sind.

**Automatisches Verhalten:** Apps werden bei Versionsaktualisierung automatisch deaktiviert, sofern sie bis dahin nicht aktualisiert wurden.

**Aktion:** App manuell aktualisieren und reaktivieren.

---

## SaaS-Updates und Erweiterungen

- Shopware aktualisiert den SaaS-Shop **automatisch**
- Inkompatible Erweiterungen können dabei **automatisch deaktiviert** werden
- Betreiber muss Erweiterungen **manuell aktualisieren und reaktivieren**
- Status-Informationen: `https://status.shopware.com/`

---

## Voraussetzungen für Erweiterungen

Auch für **kostenlose** Erweiterungen benötigt:

1. **Firmeninformationen** (Einstellungen > Account > Firma)
2. **Zahlungsart für Abrechnung** (Einstellungen > Account > Abrechnungen > Zahlungsart)

---

## Erweiterungen von macOS hochladen

> ⚠️ macOS erstellt beim Komprimieren automatisch einen Unterordner im ZIP-File.

Lösung: Erweiterung per Terminal komprimieren (ohne macOS-Metadaten):
```bash
cd /Pfad/zum/Plugin-Ordner
zip -r plugin-name.zip . -x "*.DS_Store" -x "__MACOSX/*"
```

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/saas/erweiterungen*
