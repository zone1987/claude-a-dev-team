# Playwright Agent CLI — Network & Routing

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `network` | Netzwerk-Anfragen seit Seitenaufruf auflisten |
| `route <pattern> [optionen]` | Anfragen fuer URL-Muster mocken |
| `route-list` | Aktive Mock-Routen auflisten |
| `unroute [pattern]` | Mock-Route(n) entfernen |
| `network-state-set <state>` | Online/Offline-Zustand setzen |

---

## network

```bash
playwright-cli network
playwright-cli network --filter="api"
playwright-cli network --static
playwright-cli network --request-body
playwright-cli network --request-headers
playwright-cli network --clear
```

### network-Optionen

| Option | Typ | Standard | Beschreibung |
|--------|-----|---------|-------------|
| `--filter=<pattern>` | string | — | URL-Pattern als Filter (Teilstring-Match) |
| `--static` | flag | false | Statische Ressourcen einschliessen (Bilder, CSS, Fonts) |
| `--request-body` | flag | false | Request-Bodies einschliessen |
| `--request-headers` | flag | false | Request-Header einschliessen |
| `--clear` | flag | false | Log leeren |

---

## route

```bash
playwright-cli route "**/api/users" \
  --body='[{"name":"Alice"},{"name":"Bob"}]' \
  --content-type=application/json

playwright-cli route "**/api/data" --status=500
playwright-cli route "**/api/data" --status=503
playwright-cli route "**/*.jpg" --status=404
playwright-cli route "**/analytics/**" --status=204
playwright-cli route "**/*" --remove-header=cookie,authorization
```

### route-Argumente und Optionen

| Argument/Option | Typ | Pflicht | Standard | Beschreibung |
|-----------------|-----|---------|---------|-------------|
| `<pattern>` | string | Ja | — | Glob-Muster der abzufangenden URLs (z. B. `**/api/**`) |
| `--status=<code>` | number | Nein | 200 | HTTP-Status-Code der Mock-Antwort |
| `--body=<text>` | string | Nein | `""` | Antwort-Body (Text oder JSON-String) |
| `--content-type=<type>` | string | Nein | `text/plain` | Content-Type-Header der Antwort |
| `--header=<name:value>` | string | Nein | — | Zusaetzlicher Response-Header (wiederholbar) |
| `--remove-header=<names>` | string | Nein | — | Kommagetrennte Header-Namen, die aus dem Request entfernt werden |

### route-Anwendungsbeispiele

**API-Antwort mocken:**

```bash
playwright-cli route "**/api/users" \
  --body='[{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]' \
  --content-type=application/json
```

**Fehlerbehandlung testen:**

```bash
playwright-cli route "**/api/data" --status=500
playwright-cli route "**/api/timeout" --status=503
```

**Ressourcen blockieren:**

```bash
playwright-cli route "**/*.jpg" --status=404
playwright-cli route "**/analytics/**" --status=204
playwright-cli route "**/ads/**" --status=204
```

**Authentifizierungs-Header entfernen:**

```bash
playwright-cli route "**/*" --remove-header=cookie,authorization
```

**Komplexe Szenarien mit run-code:**

Fuer bedingte Antworten, Verzoegerungen oder Request-Body-Inspektion `run-code` verwenden.

---

## route-list

```bash
playwright-cli route-list
```

Listet alle aktiven Mock-Routen auf. Keine Argumente.

---

## unroute

```bash
playwright-cli unroute "**/api/users"   # Spezifische Route entfernen
playwright-cli unroute                  # Alle Routen entfernen
```

### unroute-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `[pattern]` | string | Nein | Glob-Muster der zu entfernenden Route; ohne Argument alle entfernen |

---

## network-state-set

```bash
playwright-cli network-state-set offline   # Offline gehen
playwright-cli reload                      # Seite zeigt Offline-State
playwright-cli network-state-set online    # Verbindung wiederherstellen
```

### network-state-set-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<state>` | string | Ja | `online` oder `offline` |

---

## Vollstaendiger Test-Workflow

```bash
# Seite laden und Netzwerk inspizieren
playwright-cli open https://app.example.com
playwright-cli network

# API mocken
playwright-cli route "**/api/products" \
  --body='[{"id":1,"name":"Widget","price":9.99}]' \
  --content-type=application/json

playwright-cli reload
playwright-cli snapshot

# Aktive Routen pruefen
playwright-cli route-list

# Fehlerbehandlung testen
playwright-cli route "**/api/products" --status=500
playwright-cli reload
playwright-cli screenshot --filename=error-state.png

# Alle Routen entfernen
playwright-cli unroute

# Offline-Verhalten testen
playwright-cli network-state-set offline
playwright-cli reload
playwright-cli screenshot --filename=offline.png
playwright-cli network-state-set online
```

---

Quelle: https://playwright.dev/agent-cli/commands/network-routing
