# Playwright Agent CLI — Sessions & Dashboard

## Uebersicht

Die CLI haelt das Browser-Profil standardmaessig im Arbeitsspeicher — Cookies und Storage-State
bleiben zwischen CLI-Aufrufen innerhalb einer Session erhalten, gehen aber beim Schliessen des
Browsers verloren.

---

## Benannte Sessions

Mehrere isolierte Browser-Instanzen koennen gleichzeitig laufen, jede mit:
- eigenem Browser-Prozess
- eigenen Cookies
- eigenem localStorage
- eigener Navigations-History
- eigenem Console-Log

```bash
playwright-cli open https://playwright.dev
playwright-cli -s=example open https://example.com --persistent
playwright-cli list
```

### Session-Flag

| Flag | Beschreibung |
|------|-------------|
| `-s=<name>` | Benannte Session fuer diesen Befehl verwenden |

---

## Standard-Session per Umgebungsvariable

Session-Namen fuer alle CLI-Befehle innerhalb eines Agent-Prozesses vorbelegen:

```bash
PLAYWRIGHT_CLI_SESSION=todo-app claude .
```

---

## Profil-Persistenz

### In-Memory (Standard)

Profil-Daten bleiben nur waehrend der aktiven Session erhalten und gehen beim Schliessen verloren.

```bash
playwright-cli open https://example.com
```

### Persistent (auf Disk)

Profil wird gespeichert und ueberlebt Browser-Neustarts.

```bash
playwright-cli open https://example.com --persistent
```

Standard-Speicherorte:

| Plattform | Pfad |
|-----------|------|
| macOS | `~/Library/Caches/ms-playwright/mcp-{channel}-profile` |
| Linux | `~/.cache/ms-playwright/mcp-{channel}-profile` |
| Windows | `%LOCALAPPDATA%\ms-playwright\mcp-{channel}-profile` |

### Benutzerdefiniertes Verzeichnis

```bash
playwright-cli open https://example.com --profile=./my-profile
```

---

## Session-Management-Befehle

| Befehl | Beschreibung |
|--------|-------------|
| `playwright-cli list` | Alle Sessions auflisten |
| `playwright-cli -s=<name> close` | Spezifische Session schliessen |
| `playwright-cli close-all` | Alle Browser schliessen |
| `playwright-cli kill-all` | Nicht reagierende Browser zwangsbeenden |
| `playwright-cli -s=<name> delete-data` | Profil-Daten loeschen |

---

## Dashboard

```bash
playwright-cli show
```

Zeigt ein Session-Grid mit:
- Live-Screencast aller Sessions
- Session-Details mit Remote-Input-Moeglichkeiten
- Monitoring, Uebernahme bei Fehlern, Session-Management

---

## State-Management

```bash
playwright-cli state-save auth-state.json   # Authentifizierten State speichern
playwright-cli state-load auth-state.json   # State in neuer Session wiederherstellen
```

---

## Isolierter Test-Workflow (Beispiel)

Separate Admin- und Nutzer-Sessions mit persistenter Authentifizierung und gleichzeitigem
Monitoring beider Sessions via Dashboard:

```bash
# Admin-Session einrichten
playwright-cli -s=admin open https://app.example.com/login --persistent
playwright-cli -s=admin fill e3 "admin@example.com"
playwright-cli -s=admin fill e5 "admin-password"
playwright-cli -s=admin click e7
playwright-cli -s=admin state-save admin-auth.json

# Nutzer-Session einrichten
playwright-cli -s=user open https://app.example.com/login --persistent
playwright-cli -s=user fill e3 "user@example.com"
playwright-cli -s=user fill e5 "user-password"
playwright-cli -s=user click e7

# Beide Sessions gleichzeitig ueberwachen
playwright-cli show

# Session-Liste pruefen
playwright-cli list
```

---

Quelle: https://playwright.dev/agent-cli/sessions
