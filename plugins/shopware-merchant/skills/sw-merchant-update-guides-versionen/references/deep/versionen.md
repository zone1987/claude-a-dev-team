# Shopware 6 — Versionsspezifische Update-Hinweise: Vollständige Referenz

## Update Guide: 6.4 → 6.5

**Quelle:** https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-64-zu-65

### Voraussetzungen (Pflicht)

| Komponente | Anforderung |
|---|---|
| Shopware-Ausgangsversion | 6.4.20.2 oder neuer (NICHT von 6.4.0–6.4.20.1!) |
| PHP | 8.1 oder höher |
| Node.js | 18 |
| Git | Installiert und konfiguriert |

> **WICHTIG:** Falls noch eine ältere 6.4-Version vorhanden ist, erst auf 6.4.20.2 updaten, dann erst auf 6.5.

### Erweiterungen: Alle deaktivieren (Pflicht)

Bei diesem Major-Update müssen ALLE Erweiterungen deaktiviert werden:

1. **Theme auf Standard setzen** — aktives eigenes Theme deaktivieren, Storefront-Standard aktivieren
2. **Theme-Extension unter Erweiterungen deaktivieren**
3. **Alle weiteren Erweiterungen deaktivieren**
4. Erst dann: Update auf 6.5 durchführen

Nach erfolgreichem Update:
- Erweiterungen im Store/Composer auf kompatible Versionen aktualisieren
- Erweiterungen wieder aktivieren

### Update durchführen

Update wie in der allgemeinen Anleitung beschrieben:
→ https://docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten#update-per-administration

### Neue Features in Shopware 6.5

- Vue 3 Unterstützung im Admin (Erweiterungen müssen angepasst werden)
- Node.js 18 als Mindestanforderung
- PHP 8.1 als Mindestanforderung
- Überarbeitetes Berechtigungssystem

---

## Update Guide: 6.5 → 6.6

**Quelle:** https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-65-zu-66

### Voraussetzungen (Pflicht)

| Komponente | Anforderung |
|---|---|
| Shopware-Ausgangsversion | 6.5.0.0 oder neuer |
| PHP | 8.2 |
| Node.js | 20 |
| MySQL | 8.0 oder höher |
| MariaDB | 10.11 oder höher |
| Git | Installiert und konfiguriert |

> **HINWEIS:** Falls noch Shopware 6.4 vorhanden ist, erst von 6.4 auf 6.5 updaten, dann auf 6.6.

### Erweiterungen: Alle deaktivieren (Pflicht)

Gleiche Vorgehensweise wie bei 6.4 → 6.5:

1. Theme auf Standard setzen
2. Theme-Extension deaktivieren
3. Alle weiteren Erweiterungen deaktivieren
4. Update durchführen
5. Nach Update: Extensions aktualisieren und reaktivieren

### Update durchführen

Update wie in der allgemeinen Anleitung beschrieben, per Administration.

### Neue Features in Shopware 6.6

Detailliert im Update Guide 6.6 dokumentiert (siehe nächster Abschnitt).

---

## Update Guide: Shopware 6.6 — Neuerungen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-shopware-66

**Gilt für:** Shopware 6.6.0.0 und neuer

### Systemanforderungen 6.6

| Komponente | Anforderung |
|---|---|
| PHP | 8.2+ |
| Node.js | 20 |
| Redis | 7.0 (optional) |
| MariaDB | 10.11+ |
| MySQL | 8.0+ |

### Technische Neuerungen

#### Vue 3 Vollunterstützung
- Vue 3 ist im Admin-Bereich vollständig aktiviert
- Extension-Inkompatibilitäten möglich → individuelle Extension-Updates erforderlich
- Erweiterungsentwickler müssen auf Vue 3 API umstellen

#### Webpack 5 mit SWC
- Webpack auf Version 5 aktualisiert
- Babel durch SWC ersetzt → **dreimal schnellere** Admin-Builds
- Plugin-Erweiterungen mit eigenen Webpack-Konfigurationen müssen auf Webpack 5 API migriert werden

#### Schnellere Storefront-Performance
- Verbesserte Seitengeschwindigkeit (SEO-Vorteil)
- Bis zu 6× schnellere Indizierung für mehrsprachige Shops
- Verbesserter Elasticsearch/OpenSearch-Mapping: mehrere Sprachen in einem Index

#### Automatischer Logout (verlängerbar)
- Login-Session kann via Checkbox auf bis zu 14 Tage verlängert werden
- Konfigurierbar: Einstellungen > Login-Einstellungen

#### Lagerverwaltung (Lagerbestand)
- Lagerbestand wird nun beim Aufgeben der Bestellung abgezogen (nicht erst beim Abschluss)
- Einstellbar: Lagerbestandsberechnung kann deaktiviert werden

#### Medien-Pfad-Speicherung
- Dateipfade werden fest in der Datenbank gespeichert (vorher dynamisch berechnet)
- Behebt Performance-Probleme und "Datei nicht gefunden"-Fehler der Vorgängerversionen

#### Sprachabhängige Elasticsearch-Indizes
- OpenSearch/Elasticsearch-Indizes unterstützen nun sprachspezifische Konfigurationen
- Verbesserte Performance bei mehrsprachigen Shops

---

## Update Guide: Shopware 6.7 — Neuerungen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-shopware-67

**Gilt für:** Shopware 6.7.0.0 und neuer

### Systemanforderungen 6.7

| Komponente | Anforderung | Ausgeschlossene Versionen |
|---|---|---|
| PHP | 8.2, 8.3 oder 8.4 | — |
| Node.js | 20+ | — |
| MySQL | 8.0.17+ | 8.0.20, 8.0.21 (Bugs!) |
| MariaDB | 10.11+ | 10.11.5, 11.0.3 (Bugs!) |
| Redis | 7.0+ (optional) | — |
| OpenSearch | 1.0+ (optional) | — |
| Elasticsearch | 7.8+ (optional) | — |

### Technische Neuerungen

#### Webpack → Vite Migration
- Frontend-Toolchain vollständig auf Vite umgestellt
- **Konsequenz für Extension-Betreiber:** Erweiterungen mit Admin-Komponenten benötigen separate Plugin-Versionen für 6.6 und 6.7
- Storefront-Erweiterungen müssen auf Vite Build-System migriert werden

#### Vue 3 ohne Compat-Mode
- Vollständige Vue 3 Kompatibilität: Compatibility-Mode wurde beendet
- State Management: Vuex → Pinia
- **Konsequenz:** Extensions die noch Vue 2 APIs nutzen, sind inkompatibel

#### Cache-Architektur-Überarbeitung
Wesentliche Verbesserungen:
- **Delayed Cache Invalidation:** Cache wird verzögert geleert (verhindert Cache-Stampedes)
- **Store API Caching Layer entfernt:** Vereinfachte Architektur, bessere Performance
- **Erwartete Ergebnisse:** Weniger Speicherverbrauch, höhere Cache-Hit-Rate

#### Core Library Updates
| Library | Alte Version | Neue Version |
|---|---|---|
| PHPUnit | 10 | 11 |
| League OAuth2 Server | alt | aktuell |
| DomPDF | alt | aktuell |
| DBAL | 3.x | 4.0 |

> **Hinweis für Extension-Entwickler (Betreiber-Sicht):** Extensions, die diese Libraries direkt nutzen, müssen auf Kompatibilität geprüft werden. Im Shopware Store wird dies durch den Kompatibilitäts-Checker angezeigt.

---

## Upgrade-Pfad: Mehrere Versionen überspringen

### Direkt von 6.4 auf 6.7 möglich?
**Nein.** Shopware unterstützt keine Version-Sprünge. Jedes Major-Update muss einzeln durchgeführt werden:

```
6.4.x → 6.4.20.2 → 6.5.x → 6.6.x → 6.7.x
```

### Empfohlener Upgrade-Pfad

1. Auf neueste 6.4-Patch-Version updaten (6.4.20.2)
2. Alle Extensions deaktivieren
3. Update auf 6.5 (neueste Patch-Version)
4. Extensions auf 6.5-kompatible Versionen aktualisieren
5. Alle Extensions deaktivieren
6. Update auf 6.6 (neueste Patch-Version)
7. Extensions auf 6.6-kompatible Versionen aktualisieren
8. Alle Extensions deaktivieren
9. Update auf 6.7

---

## Kompatibilitäts-Matrix für gängige Anforderungen

| Shopware | PHP | Node.js | MariaDB | MySQL | Redis |
|---|---|---|---|---|---|
| 6.4.x | 7.4–8.1 | 14–16 | 10.3+ | 5.7.21+, 8.0+ | 6.0+ |
| 6.5.x | 8.1–8.2 | 18 | 10.11+ | 8.0+ | 7.0+ |
| 6.6.x | 8.2–8.3 | 20 | 10.11+ | 8.0.17+ | 7.0+ |
| 6.7.x | 8.2–8.4 | 20+ | 10.11+ | 8.0.17+ | 7.0+ |

---

*Quellen:*
*- https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-64-zu-65*
*- https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-65-zu-66*
*- https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-shopware-66*
*- https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-shopware-67*
