# Playwright Agent CLI — Storage & Authentication

## Befehlsuebersicht

| Gruppe | Befehl | Beschreibung |
|--------|--------|-------------|
| State | `state-save [filename]` | Kompletten Browser-State speichern (Cookies + localStorage) |
| State | `state-load <filename>` | State aus Datei wiederherstellen |
| Cookies | `cookie-list` | Alle Cookies auflisten |
| Cookies | `cookie-get <name>` | Bestimmtes Cookie abrufen |
| Cookies | `cookie-set <name> <value>` | Cookie erstellen/aendern |
| Cookies | `cookie-delete <name>` | Cookie loeschen |
| Cookies | `cookie-clear` | Alle Cookies loeschen |
| localStorage | `localstorage-list` | Alle Schluessel-Wert-Paare auflisten |
| localStorage | `localstorage-get <key>` | Wert nach Schluessel abrufen |
| localStorage | `localstorage-set <key> <value>` | Wert setzen |
| localStorage | `localstorage-delete <key>` | Schluessel loeschen |
| localStorage | `localstorage-clear` | Gesamten Storage leeren |
| sessionStorage | `sessionstorage-list` | Alle Schluessel-Wert-Paare auflisten |
| sessionStorage | `sessionstorage-get <key>` | Wert nach Schluessel abrufen |
| sessionStorage | `sessionstorage-set <key> <value>` | Wert setzen |
| sessionStorage | `sessionstorage-delete <key>` | Schluessel loeschen |
| sessionStorage | `sessionstorage-clear` | Gesamten Storage leeren |

---

## state-save / state-load

Speichert und stellt den vollstaendigen Browser-State (Cookies + localStorage) in einer Datei
wieder her.

```bash
playwright-cli state-save                         # automatisch benannte Datei
playwright-cli state-save auth.json               # benutzerdefinierter Dateiname
playwright-cli state-load auth.json               # wiederherstellen
```

### state-save-Argumente

| Argument | Typ | Pflicht | Standard | Beschreibung |
|----------|-----|---------|---------|-------------|
| `[filename]` | string | Nein | Auto-generiert | Zieldatei (JSON) |

### state-load-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<filename>` | string | Ja | Quelldatei (JSON) |

### Authentifizierungs-Persistenz (Beispiel)

```bash
playwright-cli open https://app.example.com/login
playwright-cli fill e3 "user@example.com"
playwright-cli fill e5 "password123"
playwright-cli click e7
playwright-cli state-save auth.json

# Spaeter: State laden und direkt zur geschuetzten Seite navigieren
playwright-cli state-load auth.json
playwright-cli goto https://app.example.com/dashboard
```

---

## Cookies

### cookie-list

```bash
playwright-cli cookie-list
playwright-cli cookie-list --domain=.github.com
playwright-cli cookie-list --path=/app
```

#### cookie-list-Optionen

| Option | Typ | Beschreibung |
|--------|-----|-------------|
| `--domain=<domain>` | string | Filter nach Domain |
| `--path=<path>` | string | Filter nach Pfad |

### cookie-get

```bash
playwright-cli cookie-get session_id
playwright-cli cookie-get auth_token
```

#### cookie-get-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<name>` | string | Ja | Name des abzurufenden Cookies |

### cookie-set

```bash
playwright-cli cookie-set theme light
playwright-cli cookie-set session abc123 --domain=.example.com --secure --http-only
playwright-cli cookie-set prefs "{\"lang\":\"de\"}" --domain=.example.com
playwright-cli cookie-set consent true --expires=1735689600 --same-site=Strict
```

#### cookie-set-Argumente und Optionen

| Argument/Option | Typ | Pflicht | Standard | Beschreibung |
|-----------------|-----|---------|---------|-------------|
| `<name>` | string | Ja | — | Cookie-Name |
| `<value>` | string | Ja | — | Cookie-Wert |
| `--domain=<domain>` | string | Nein | Aktuelle Domain | Cookie-Domain |
| `--path=<path>` | string | Nein | `/` | Cookie-Pfad |
| `--expires=<timestamp>` | number | Nein | Session | Unix-Timestamp fuer Ablauf |
| `--http-only` | flag | Nein | false | HTTP-Only-Flag (kein JavaScript-Zugriff) |
| `--secure` | flag | Nein | false | Secure-Flag (nur HTTPS) |
| `--same-site=<value>` | string | Nein | — | `Strict`, `Lax` oder `None` |

### cookie-delete

```bash
playwright-cli cookie-delete session_id
playwright-cli cookie-delete auth_token
```

### cookie-clear

```bash
playwright-cli cookie-clear
```

---

## localStorage

### localstorage-list

```bash
playwright-cli localstorage-list
```

### localstorage-get

```bash
playwright-cli localstorage-get user_preferences
playwright-cli localstorage-get theme
```

### localstorage-set

```bash
playwright-cli localstorage-set onboarding_done "false"
playwright-cli localstorage-set theme "dark"
playwright-cli localstorage-set user_prefs '{"lang":"de","currency":"EUR"}'
playwright-cli reload      # Seite neu laden um Aenderung zu aktivieren
```

### localstorage-delete

```bash
playwright-cli localstorage-delete user_preferences
```

### localstorage-clear

```bash
playwright-cli localstorage-clear
```

---

## sessionStorage

Hinweis: Daten werden beim Schliessen des Tabs geloescht.

```bash
playwright-cli sessionstorage-list
playwright-cli sessionstorage-get wizard_step
playwright-cli sessionstorage-set wizard_step "3"
playwright-cli sessionstorage-delete temp_data
playwright-cli sessionstorage-clear
```

Alle Befehle haben identische Argumente wie ihre localStorage-Aequivalente.

---

Quelle: https://playwright.dev/agent-cli/commands/storage
