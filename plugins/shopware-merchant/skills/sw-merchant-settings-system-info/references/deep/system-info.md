# Shopware 6 – System-Info, Logs & Sonstige System-Einstellungen (vollständige Referenz)

Quellen:
- https://docs.shopware.com/de/shopware-6-de/einstellungen/logging
- https://docs.shopware.com/de/shopware-6-de/einstellungen/System/shopwareaccount
- https://docs.shopware.com/de/shopware-6-de/einstellungen/system/daten-teilen
- https://docs.shopware.com/de/shopware-6-de/einstellungen/Business-Events

---

## Ereignis-Logs

**Pfad:** Einstellungen > System > Ereignis-Logs  
**Nur für Self-Hosted**

Ab Version 6.5 wurden die Einträge minimalisiert. Für erweiterte Logging-Konfiguration (z.B. E-Mail-Logs): Developer-Dokumentation heranziehen.

### Bedienelemente
- `...`-Symbol: Spalten ausblenden
- 3-Striche-Symbol: Spalten einblenden, Kompaktmodus umschalten
- Zentrale Suchleiste: Log durchsuchen

### Spalten
| Spalte | Inhalt |
|---|---|
| Nachricht | Bereichsherkunft (z.B. Checkout, Mail) |
| Priorität | Wichtigkeitsstufe mit numerischem Wert |
| Inhalt | Meldungstext (anklickbar für Details) |

### Prioritätsstufen

| Stufe | Wert | Bedeutung |
|---|---|---|
| Debug | 100 | Funktions-Debugging |
| Info | 200 | Basis-Systeminformationen |
| Error | 300 | Zu überprüfende Fehlermeldung |
| Critical | 400 | Kritischer Fehler, sofortige Überprüfung erforderlich |

### Detailansicht
Modalfenster zeigt unterschiedliche Informationen je nach Eintragstyp.
- Mail-Logs: verschiedene Ansichtsmodi
- Debug-Einträge: nur im Quelltext-Format

---

## Shopware Account Verknüpfung

**Pfad:** Einstellungen > System > Shopware Account  
**Verfügbar ab:** 6.3.5.0  
**Nur für Self-Hosted**

Verbindet Shopware-Installation mit dem persönlichen Shopware Account für Zugriff auf erworbene Erweiterungen und Abonnements.

### Konfigurationsfelder

| Feld | Beschreibung |
|---|---|
| Lizenzierungshost | Host-Domain (muss exakt mit im Account registrierter Domain übereinstimmen inkl. `www.` falls nötig) |
| Verifikationsprüfsumme | Optional; erforderlich wenn Domain noch nicht verifiziert; beim Domain-Eintrag im Account angezeigt |

---

## Datenschutzeinstellungen (Daten teilen)

**Pfad:** Einstellungen > System > Datenschutzeinstellungen

Transparente und DSGVO-konforme Datenverwaltung für Analyse und Shopware-Verbesserungen.

### Zwei Datenkategorien

| Kategorie | Beschreibung |
|---|---|
| **Shop-Daten (anonym)** | Bestellungen, Diagnosen, allgemeine Shop-Informationen; vollständig anonymisiert |
| **Nutzungsdaten** | Persönliche Verhaltensdaten in der Administration (Klicks, Navigation, Funktionen) |

### Konfiguration
- **Shop-Daten:** Einstellungen > System > Datenschutzeinstellungen (Toggle)
- **Nutzungsdaten:** Eigenes Profil > Datenschutzeinstellungen (Toggle)

### Modal nach Login
Optionen:
- „Alles ablehnen" — kein Teilen
- „Alles akzeptieren" — beide Typen aktiviert
- „Auswahl speichern" — individuelle Konfiguration

### FAQ-Hinweis
Shop-Daten: Keine personenbezogenen Daten. Nutzungsdaten: Erfassung von Admin-Aktionen.

---

## Business-Events (Legacy)

**Pfad:** Einstellungen > Shop > Business-Events  
**Verfügbar ab:** 6.3.3.0  
**Hinweis:** Ab v6.4.8.0 durch den **Flow Builder** ersetzt.

### Tabellenkolumnen

| Spalte | Inhalt |
|---|---|
| Event | Technischer Name + verständliche Beschreibung |
| Titel | Individuell vergebener Name |
| Verkaufskanal | Zugeordnete Kanäle (leer = alle) |
| Regeln | Bedingungen aus dem Rule Builder |
| E-Mail-Template | Verwendete Vorlage |
| Aktiv | Status |

### Business-Event erstellen

| Feld | Beschreibung |
|---|---|
| Titel | Benutzerdefinierter Name |
| Aktiv | Aktivieren/Deaktivieren |
| Event | Zu automatisierendes Ereignis |
| E-Mail-Template | Versandvorlage |
| Verkaufskanal | Optional kanalspezifisch |
| Regeln | Rule-Builder-Bedingungen |

### E-Mail-Empfänger
Interne E-Mail-Adressen hinterlegen. Kunden erhalten Templates nur, wenn **keine** internen Empfänger konfiguriert sind.

---

## Suche (Einstellungen > Shop > Suche)

**Verfügbar ab:** 6.4.0.0

### Sonderzeichen in Produktnummern
Konfigurierbar in `config/packages/shopware.yaml`:
```yaml
shopware:
  search:
    product:
      search_ranking:
        special_chars: ['-', '_', '+', '.', '@', '/']
```

### Allgemein – Such-Verhalten
| Option | Beschreibung |
|---|---|
| UND-Modus | Nur Ergebnisse mit allen Suchbegriffen |
| ODER-Modus | Ergebnisse mit mindestens einem Begriff |
| Minimale Suchbegriffslänge | Standard: 2 Zeichen |
| Maximale Länge | 255 Zeichen |

### Durchsuchbare Inhalte (pro Feld konfigurierbar)
- Suchbar: Ein-/Ausschalten
- Ranking Punktzahl: Gewichtung
- Suchbegriffe trennen: Aufteilung nach Sonderzeichen

**Durchsuchbare Standard-Inhalte:**
Kategoriename, Kategorie-Zusatzfelder, Eigene Suchbegriffe, Produktbeschreibung, Produkt-EAN, Herstellername, Herstellernummer, Hersteller-Zusatzfelder, Produkt-Meta-Beschreibung, Produkt-Meta-Titel, Produktname, Eigenschaftsausprägung, Produktnummer, Eigenschaftsname, Produkt-Tag

### Such-Index
- „Such-Index neu erstellen"-Button
- Zeigt letzten Aktualisierungszeitpunkt
- Fortschrittsanzeige während Neuerstellung

### Advanced Search (ab Plan Evolve / Commercial)
Erfordert Elasticsearch oder OpenSearch.

| Option | Beschreibung |
|---|---|
| Advanced Search aktivieren | Pro Verkaufskanal |
| Trefferanzahl | Für Vorschausuche und Ergebnisseite |
| Echtzeit-Suche | Mit Testfunktion (ohne Frontend-Zugriff) |

### AI Copilot (ab Plan Rise)
- **Kontextbasierte Suche:** Natürlichsprachliche Eingabe, Verkaufskanalbeschreibung (max. 100 Zeichen), 3 Beispiel-Anweisungen pro Sprache
- **Bildbasierte Suche:** PNG/JPEG Upload oder Kamerafoto (bis zu 3 ähnliche Produkte)
