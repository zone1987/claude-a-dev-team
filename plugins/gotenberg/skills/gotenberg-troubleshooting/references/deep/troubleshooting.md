# Gotenberg — Troubleshooting (Vollreferenz)

## API-Probleme

### 400 Bad Request

**Ursachen:**
- Pflichtfelder fehlen
- Fehlerhaft formatiertes JSON in Form-Feldern
- Nicht unterstuetzte Dateiendungen
- Ungueltige Feldwerte

**Loesung:** `Gotenberg-Trace`-Header aus der Antwort mit den Logs abgleichen fuer Details zum fehlenden/unguelltigen Feld.

---

## Chromium-Probleme

### Leere / fehlende Inhalte

| Ursache | Loesung |
|---------|---------|
| JavaScript-Rendering noch nicht abgeschlossen | `waitDelay` oder `waitForExpression` verwenden |
| Hintergrundelemente fehlen | `printBackground=true` oder CSS `-webkit-print-color-adjust: exact` |
| Inhalt laedt nach dem Network-Idle-Event | `skipNetworkIdleEvent=false` setzen |

### Leere Charts / Google Maps (Versionen 8.29.0 - 8.31.0)

**Ursache:** chromedp 0.15.0 hat `requestAnimationFrame`, `ResizeObserver`, `IntersectionObserver` und CSS-Transitions/Animationen zwischen Seitenlade und PDF-Generierung gesperrt — verhinderte Rendering von Chart-Bibliotheken.

**Loesung:** Upgrade auf **v8.32.0+** (revertiert zu chromedp v0.14.2).

Betroffene Issues: #1531, #1534, #1535

### Sub-Ressourcen laden nicht mehr (nach v8.31.0)

**Ursache:** v8.31.0 blockierte private IP-Sub-Ressourcen standardmaessig, was CSS/Bilder/iframes auf internen Hostnames blockierte.

**Loesung:** v8.32.0 hat permissive Standards wiederhergestellt. Fuer strikten Modus: `CHROMIUM_DENY_PRIVATE_IPS=true` setzen.

### Localhost / fehlende Assets

| Problem | Loesung |
|---------|---------|
| Container findet `localhost` nicht | Echte Netzwerk-IP des Hosts verwenden oder `host.docker.internal` (Docker) |
| CSS/Schriften/Bilder fehlen | Dateien als zusaetzliche Files im Multipart-Request mitsenden ODER als Base64-Data-URIs einbetten ODER Assets oeffentlich zugaenglich machen |

### Grosse PDFs

| Ursache | Loesung |
|---------|---------|
| Webfonts | Eigene Schriften konfigurieren (Fonts-Konfiguration, Issue #521) |
| Duplizierte Bilder | Bekannter Chromium-Bug (#1077) — aktuell kein Fix |

### Start-Fehler

- Startup-Timeout in Chromium-Modul-Konfiguration erhoehen
- macOS Docker Desktop: "Use Virtualization Framework" deaktivieren (Issue #792)

### Liveness-Probe-Fehler unter Last (vor v8.33.0)

**Problem:** Einzelne langsame Health-Probe unter hoher Last loeste "unhealthy"-Status aus, ließ Kubernetes gesunde Pods neu starten.

**Behoben in v8.33.0:**
- Toleriert eine transiente Fehler-Probe
- Cacht kurz erfolgreiche Probe-Ergebnisse
- Verhindert Probe-Spam beim Ueberlasten von Prozessen
- Tote Prozesse werden beim naechsten Check erkannt

Issue: #1561

### Print Error -32000

**Ursachen:**
1. Sehr grosse Dokumente konvertieren (bekannter Chromium-Bug)
2. Ungewoehnlich grosse Header/Footer

**Loesungen:**
- Container-Speicher erhoehen
- Header/Footer-Groesse reduzieren
- Dokumentgroe-e pruefen (Issue #788)

### Abgeschnittene Screenshots

**Problem:** Screenshots wiederholen sich oder erscheinen abgeschnitten.

**Loesung:** `skipNetworkIdleEvent=false` setzen (Issue #1065).

### Timeouts (503)

**Diagnose:**
1. Ist die Gotenberg-Instanz ueberlastet?
2. Reagieren Zielseiten-Ressourcen langsam?
3. Ist die Zielseite erreichbar?

**Loesungen:**
- Horizontal skalieren (mehr Gotenberg-Instanzen)
- API-Timeout in API-Modul-Konfiguration erhoehen
- Maximale Queue-Groesse definieren (schnelleres Abbrechen)

---

## LibreOffice-Probleme

### Layout & Schrift-Verschiebungen

**Ursache:** Fehlende System-Schriften zwingen zu Ersatzschriften — verschiebt Seitenumbrueche und Layout.

**Loesungen:**
- Erforderliche Schriften per eigenem Dockerfile installieren
- Fonts-Konfiguration konsultieren

**Aenderung ab v8.30.0:** Schrift-Stack von 30+ auf 8 Pakete reduziert. Microsoft Core Fonts (Arial, Times New Roman, Calibri) verwenden jetzt Metrik-kompatible Ersatzschriften.

**Nach Upgrade:** `ttf-mscorefonts-installer` oder spezifische Skript-Schriften installieren.

### Verlinkte Bilder fehlen (nach v8.34.0)

**Aenderung:** Inhalte von nicht-vertrauenswuerdigen Quellen werden blockiert; hochgeladene Dokumente gelten als nicht vertrauenswuerdig.

**Verhalten:** Konvertierung gibt `200 OK` zurueck, aber Bilder/verlinkter Inhalt fehlt.

**Workaround:** Inhalte direkt in Dokumente einbetten statt verlinken.

**Hinweis:** Kein Opt-out moeglich — blockiert Sicherheitsschwachstellen (local-file-read und SSRF).

### Server-Fehler (500)

**Ursache:** Dokumentkonvertierung ist ressourcenintensiv.

**Loesung:** Speicher- und CPU-Zuweisung erhoehen (Issue #465).

### UUID in CSV-Seitenheadern (vor v8.34.0)

**Problem:** Zufaellige UUID erschien als zentrierter Header bei CSV-Konvertierungen.

**Ursache:** LibreOffice benannte Calc-Tabelle nach dem Eingabedateinamen; Gotenberg speicherte Dateien mit UUID-basierten Namen, was den Standard-Seiten-Header ausloeste.

**Behoben in v8.34.0:** Auto-generierter Header fuer CSV-Eingaben unterdrueckt.

**Hinweis:** XLSX/ODS mit eigenen Seitenstilen sind nicht betroffen (Issue #1568).

### Start-Fehler

**Loesungen:**
1. Startup-Timeout erhoehen (LibreOffice-Modul-Konfiguration)
2. Debian-Nutzer: aktuelle Distribution sicherstellen
3. Synology/Paperless-ngx: spezifischen Konfigurationskommentar konsultieren (Issue #763)

Issue: #794

### Erster Request Timeout, folgende Requests schlagen fehl (vor v8.32.0)

**Problem:** Supervisor cachete anfaenglichen Start-Fehler, gab identischen Fehler an alle folgenden Requests zurueck wenn `LIBREOFFICE_START_TIMEOUT` kuuerzer als soffice-Kaltstart-Dauer.

**Behoben in v8.32.0:** Fehlgeschlagene Starts setzen den Zustand zurueck; naechster Request startet von vorne.

**Temporaere Loesung (aeltere Versionen):** `LIBREOFFICE_START_TIMEOUT` (Standard: 20s) auf mehr als soffice-Kaltstart-Zeit erhoehen (Issue #1538).

### PDF/A-1a-Unterstuetzung

**Seit LibreOffice 7.6:** PDF/A-1a wird nicht mehr unterstuetzt. Frueheres Verhalten: generierte PDF/A-1b-Dateien (manchmal von Validatoren falsch identifiziert).

---

## Webhook-Probleme

### HTTPS-Webhooks schlagen fehl (Chromium-Variante vor v8.34.0)

**Problem:** `gotenberg/gotenberg:8-chromium` Image enthielt kein `ca-certificates` — TLS-Verifizierungsfehler bei HTTPS-Webhook-Endpunkten.

**Hinweis:** Konvertierungen selbst sind nicht betroffen (Chromium buendelt eigene Zertifikate).

**Behoben in v8.34.0:** ca-certificates jetzt enthalten.

**Fuer aeltere Versionen:** `ca-certificates` per eigenem Dockerfile installieren.

**Andere Varianten:** Full- und LibreOffice-Varianten waren nie betroffen.

---

## Allgemeine Debugging-Strategie

1. **Trace-ID verwenden:** `Gotenberg-Trace`-Header in Logs suchen fuer detaillierte Fehlermeldungen
2. **Debug-Route aktivieren:** `API_ENABLE_DEBUG_ROUTE=true` → `GET /debug` fuer Konfigurationsinfo
3. **Version pruefen:** `GET /version` — viele Fehler sind in neueren Versionen behoben
4. **Health-Check:** `GET /health` fuer Modulstatus
5. **Ressourcen pruefen:** Viele Timeouts und Fehler sind Speicher-/CPU-Probleme

---

## Versions-Upgrade-Checkliste

| Von → Nach | Was zu pruefen |
|-----------|---------------|
| < 8.30.0 → 8.30.0+ | Schriftart-Pakete pruefen (ttf-mscorefonts, Skript-Schriften) |
| < 8.32.0 → 8.32.0+ | LibreOffice-Start-Timeout pruefen |
| < 8.33.0 → 8.33.0+ | Kubernetes-Liveness-Probe-Konfiguration pruefen |
| < 8.34.0 → 8.34.0+ | Verlinkte Bilder in LibreOffice-Dokumenten → einbetten; Webhook-TLS-Konfiguration pruefen |

---

Quelle: https://gotenberg.dev/docs/troubleshooting
