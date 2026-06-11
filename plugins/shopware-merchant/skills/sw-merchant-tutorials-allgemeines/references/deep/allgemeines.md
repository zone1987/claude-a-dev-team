# Shopware 6 — Tutorials: Allgemeines (vollständige Referenz)

---

## 1. Berechnung des Warenkorbes

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/berechnung-des-warenkorbes  
**Ab Version:** 6.7.0.0

### Grundlagen

Zwei gesetzlich zulässige Steuerberechnungsverfahren:

**Horizontales Verfahren:** MwSt. wird pro Warenkorb-Position einzeln berechnet und summiert.

| Artikel | Netto | MwSt. (19%) | Brutto |
|---------|-------|-------------|--------|
| Produkt A | 1,99 € | 0,38 € | 2,37 € |
| Produkt B | 2,99 € | 0,57 € | 3,56 € |
| Produkt C | 3,99 € | 0,76 € | 4,75 € |
| **Gesamt** | **8,97 €** | **1,71 €** | **10,68 €** |

**Vertikales Verfahren:** MwSt.-Summe wird anhand des Bestellungs-Gesamtbetrags errechnet.

| Artikel | Netto |
|---------|-------|
| Produkt A–C | 8,97 € |
| MwSt. (19%) | 1,70 € |
| **Brutto** | **10,67 €** |

Differenz durch Rundung: 0,01 €

### Einstellungen

- **Verfahren:** Verkaufskanäle > Zahlung und Versand > Steuerberechnung
- **Preisrundung:** Einstellungen > Regional > Währungen
- **Steuerfreiheit:** Einstellungen > Regional > Länder

### Debugging

1. Warenkorb in Storefront nachstellen
2. Screenshot der `/checkout/finish`-Seite anfertigen
3. Summen mit Excel-Tabelle vergleichen
4. PDF-Rechnung prüfen
5. Erweiterungen als Störquelle prüfen

---

## 2. Hinweise zur APP_URL

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/hinweise-zur-app-url  
**Ab Version:** 6.0.0

### Grundprinzip

Die `APP_URL` ermöglicht externen Anwendungen (z. B. aus dem Shopware Store) den Zugriff auf den Shop. Sie wird in der `.env`-Datei (Root-Verzeichnis) gespeichert, ab 6.5.0.0 in `.env.local`.

```
APP_ENV="prod"
APP_URL="https://DEINE-DOMAIN"
DATABASE_URL="mysql://DEINE-DATENBANK"
```

### Sechs Kernempfehlungen

1. **Erreichbarkeit:** Die Domain muss extern aufrufbar sein (Browser-Test).
2. **Mehrere Domains:** Eine Domain als APP_URL wählen (Einstellungen > Verkaufskanäle > Domains).
3. **Domain/Shop verschoben:** Bei Umzug/Staging APP_URL anpassen; Lizenzdomain prüfen unter Einstellungen > System > Shopware Account.
4. **Umgebungsvariable:** Format `APP_URL=https://my-shop.com` — korrekte Schreibweise und Protokoll beachten.
5. **Domain-Änderung erkannt:** Drei Optionen im Admin-Modal:
   - **Migriere Apps:** Bei dauerhaftem Umzug — Apps bleiben, Shop-ID bleibt.
   - **Installiere Apps neu:** Beim Erstellen von Shop-Kopien (Staging) — neue Shop-ID.
   - **Deinstalliere Apps:** Kopien ohne Apps-Bedarf — neue Shop-ID, Apps gelöscht.
6. **Fehlermeldung unterdrücken:** `APP_URL_CHECK_DISABLED=1` in `.env` eintragen (Achtung: Apps können beeinträchtigt werden).

---

## 3. Flooding-Prävention (Rate Limiting)

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/flooding-praevention  
**Ab Version:** 6.4.6.0

### Standard-Limits

| Funktion | Versuche | Wartezeit (Eskalation) |
|----------|----------|------------------------|
| Login | 10 | 10 s → 30 s → 60 s |
| Kontaktformular | 3 | 30 s → 60 s → 90 s |
| Passwort-Wiederherstellung | 3 | 30 s → 60 s → 90 s |
| Reset nach: | — | 24 Stunden oder erfolgreiche Aktion |

### Konfiguration

Datei `config/packages/shopware.yaml` anlegen (neue Projekte haben nur `lock.yaml`):

```yaml
shopware:
    rate_limiter:
        login:
            enabled: false
        guest_login:
            enabled: true
        oauth:
            enabled: true
        reset_password:
            enabled: true
        user_recovery:
            enabled: true
        contact_form:
            enabled: true
```

Nach Änderungen: `php bin/console cache:clear`

---

## 4. Message Queue und Scheduled Tasks

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/message-queue-und-scheduled-tasks

### Überblick

Shopware verarbeitet viele Aufgaben asynchron über eine Message Queue. Beispiele:
- E-Mail-Versand
- Produktindexierung
- Sitemap-Generierung

### Wichtige Scheduled Tasks

| Task | Intervall | Funktion |
|------|-----------|----------|
| `log_entry.cleanup` | täglich | Log-Tabelle leeren |
| `shopware.invalidate_cache` | 20 Sek. | Cache-Invalidierung |
| `app_update` | täglich | Erweiterungs-Updates prüfen |
| `shopware.sitemap_generate` | täglich | Sitemap erstellen |
| `cart.cleanup` | täglich | Alte Warenkörbe löschen |

### Worker-Optionen

**Admin Worker** (Standard): Nutzt den Browser. Nicht für Produktionssysteme empfohlen.

**CLI Worker** (empfohlen für Produktion):

**Schritt 1** — Admin Worker deaktivieren (`config/packages/z-shopware.yaml`):

```yaml
shopware:
    admin_worker:
        enable_admin_worker: false
```

**Schritt 2** — CLI-Befehle als Cronjob/Service einrichten (jede ~60 Sekunden):

```bash
# Message Queue
bin/console messenger:consume async low_priority --time-limit=60

# Scheduled Tasks
bin/console scheduled-task:run --time-limit=60
```

Alternativ mit `--memory-limit=512M`.

---

## 5. Merkzettel (Wunschliste) verwenden

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/merkzettel-verwenden  
**Ab Version:** 6.4.0.0

### Aktivierung

Aktivierung in den Warenkorb-Einstellungen (Einstellungen > Shop > Warenkorb).

Nicht eingeloggte Besucher müssen Cookies für "Komfortfunktionen" akzeptieren.

### Bedienung

- **Aus Produktlisting:** Herz-Icon rechts unten auf dem Produktbild
- **Aus Produktdetailseite:** Herz-Button rechts unterhalb von "In den Warenkorb"
- **Zugriff:** Herz-Icon im Header neben dem Account-Menü
- **Entfernen:** X-Button auf dem Produktbild im Merkzettel

---

## 6. Performance-Tipps

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/performance-tipps  
**Ab Version:** 6.5.4.0

### Allgemeine Tipps

| Thema | Standard | Optimal |
|-------|----------|---------|
| PHP | — | FPM |
| Bytecode-Cache | APC | ZendOpcache + APCu (+25 %) |
| Datenbank | ≥ MySQL 8 / MariaDB ≥ 10.3.22 | ≥ MySQL 8 |
| Webserver | Apache 2.4 | NGINX |
| Debug/Profiling | — | Deaktiviert in Produktion |

**Tipp:** Immer auf die neueste Shopware-Version aktualisieren — jedes Release enthält Performance-Verbesserungen.

### Performance messen

1. Alle Drittanbieter-Erweiterungen deaktivieren
2. Standard-Theme zuweisen
3. Cache leeren und aufwärmen
4. Messung durchführen

**Apache Benchmark:**
```bash
ab -n 10 -c 1 http://www.domain.tld:80/{startseite,kategorie,listing}
```

### MySQL optimieren

```bash
wget http://mysqltuner.pl/ -O mysqltuner.pl
chmod +x mysqltuner.pl
./mysqltuner.pl
```

### Erweiterte Maßnahmen

- **Elasticsearch/OpenSearch:** Für Produktsuche bei großen Katalogen
- **Session Handling via Redis:** Reduziert Datenbankload
- **Flysystem:** Externe Datenspeicherung für Redundanz und Performance

---

## 7. Onboarding — Dein Shop in einer Stunde

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/allgemeines/Onboarding  
**Ab Version:** 6.0.0

### Schnell-Übersicht

| Schritt | Admin-Pfad |
|---------|-----------|
| Installation | Installationsanleitung |
| Ersteinrichtungs-Assistent | Startet automatisch nach Login |
| Kategorien anlegen | Kataloge > Kategorien |
| Produkte anlegen | Kataloge > Produkte |
| Hersteller | Kataloge > Hersteller |
| Eigenschaften (Varianten) | Einstellungen > Katalog > Eigenschaften |
| Themes | Inhalte > Themes |
| Erlebniswelten | Inhalte > Erlebniswelten |
| Versand | Einstellungen > Shop > Versand |
| Zahlungsarten | Einstellungen > Shop > Zahlungsarten |
| Import/Export | Einstellungen > Import/Export |
| Benutzer & Rechte | Einstellungen > System > Benutzer & Rechte |

### Deploymentmodelle

| Modell | Merkmal |
|--------|---------|
| Self-hosted | Volle Kontrolle, Code-Zugriff, IT-Kenntnisse nötig |
| Cloud SaaS | Shopware hostet, automatische Updates, kein Code-Zugriff |
| Cloud PaaS | Shopware hostet Infrastruktur, Nutzer macht Updates, Code-Zugriff |

---

## 8. Produktdarstellung in Kategorien

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/produktdarstellung-in-kategorien  
**Ab Version:** 6.4.0.0

- Einstellung für "In den Warenkorb"-Button in Listings: Einstellungen > Shop > Produkte
- Produktbox-Layout in Erlebniswelten (Kategorieseite) > Produktlisting-Block
- Erweiterte Preise: "Ab X €"-Anzeige, kein direkter Warenkorb-Button
- Streichpreis: Durchgestrichen + Rabatt-Badge
- Varianteninformationen: Sichtbar in Produktbox

---

## 9. Shopware Konsolenbefehle (CLI)

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shopware-cli

Shopware stellt Funktionen über die Kommandozeile bereit. Zugriff via SSH (macOS/Linux: Terminal, Windows: PuTTY).

Vollständige Befehlsreferenz: https://developer.shopware.com/docs/resources/references/core-reference/commands-reference.html

---

## 10. Umsatzsteuer-ID der Shopkunden

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/umsatzsteuer-id-der-shopkunden  
**Ab Version:** 6.3.5.0

- Nur bei gewerblichen Kunden sichtbar/editierbar
- Im Admin: Kundenprofil > Allgemein > USt-ID (im Bearbeitungsmodus)
- Kunden können selbst bearbeiten: Mein Konto > Profil
- Seit 6.3.5.0: USt-ID automatisch auf Rechnungen

---

## 11. PayPal Plus zu PayPal Checkout migrieren

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/allgemeines/paypal-checkout  
**Ab Version:** PayPal Extension 4.0.0

### Einrichtungsschritte

1. Einstellungen > Erweiterungen > PayPal öffnen
2. PayPal-Assistant über "PayPal-Sandbox-Konto verbinden" starten
3. Mit Sandbox-Zugangsdaten anmelden und bestätigen
4. "Sandboxdaten verwenden" aktivieren (für Tests)
5. "Start onboarding" klicken
6. Nach Bestätigung: PayPal Plus deaktivieren
7. Gewünschte Zahlungsarten aktivieren (Regler auf "Aktiv")
8. In Verkaufskanälen unter Zahlungsarten zuweisen

---

## 12. Sicherheitsmaßnahmen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/sicherheitsmassnahmen  
**Ab Version:** 6.5.0.0

| Maßnahme | Beschreibung |
|----------|-------------|
| Rate Limiter | Schutz gegen Brute-Force-Angriffe (Login, Passwort-Reset) |
| IP-Whitelisting | Verkaufskanal temporär deaktivieren / Wartungsmodus |
| HTML Sanitizer | XSS-Prävention (ab 6.5) — entfernt unsicheres HTML |
| SQL Injection | Prepared Statements via Doctrine DBAL/ORM |
| API-Feldschutz | Selektive Sichtbarkeit von Feldern über Flag-System |
| SameSite Cookies | Konfigurierbar via Symfony FrameworkBundle (`framework.yaml`) |
| DSGVO | Datenschutz-Compliance integriert |
| Security Plugin | Sicherheits-Updates ohne Plattform-Upgrade |
| Captcha | Mehrere Captcha-Optionen für Registrierung/Storefront |

---

## 13. Bugs über GitHub melden

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/GithubIssues

- **Platform:** https://github.com/shopware/shopware/issues
- Kein Account zum Lesen nötig; kostenloser Account für Erstellen/Kommentieren
- Vor dem Melden: Suche mit `is:issue is:open [Suchbegriff]`
- **Bug-Report muss enthalten:** Titel, Shopware-Version, betroffener Bereich, Ist-Verhalten, Soll-Verhalten, Reproduktionsschritte
- **Feature Wünsche:** Nur auf https://feedback.shopware.com/ — nicht via GitHub Issues

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/allgemeines — Stand: 2026-06*
