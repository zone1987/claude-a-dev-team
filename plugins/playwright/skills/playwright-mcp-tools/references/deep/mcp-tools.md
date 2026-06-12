# Playwright MCP: Vollstaendige Tool-Referenz

Alle Tools sind nach Capability-Gruppe organisiert. Core-Tools sind immer verfuegbar;
weitere Gruppen muessen explizit aktiviert werden (`--caps=...`).

---

## Core: Navigation

Capability: `core` (immer aktiv)

### `browser_navigate`

Navigiert zu einer URL im aktuellen Tab.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `url` | string | Ja | Vollstaendige URL mit Protokoll |

```
browser_navigate { url: "https://demo.playwright.dev/todomvc" }
```

Gibt Accessibility-Snapshot der geladenen Seite zurueck.

---

### `browser_navigate_back`

Geht in der Browser-Historie zurueck.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| — | — | — | Keine Parameter |

---

### `browser_navigate_forward`

Geht in der Browser-Historie vorwaerts.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| — | — | — | Keine Parameter |

---

### `browser_reload`

Laedt die aktuelle Seite neu.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| — | — | — | Keine Parameter |

---

### `browser_close`

Schliesst den aktuellen Tab und den Browser.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| — | — | — | Keine Parameter |

---

## Core: Snapshot

### `browser_snapshot`

Nimmt einen Accessibility-Snapshot der aktuellen Seite auf.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| — | — | — | Keine Parameter |

Gibt strukturierten ARIA-Baum mit ref-IDs zurueck. Meiste Tools geben nach Aktionen automatisch einen Snapshot zurueck.

---

## Core: Interaction

Capability: `core` (immer aktiv)

### `browser_click`

Klickt ein Element auf der Seite.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `ref` | string | Ja | Element-Referenz aus Snapshot (z.B. `e5`) |

```
browser_click { ref: "e10" }
```

---

### `browser_hover`

Hovert ueber ein Element (Tooltips, Dropdown-Hover-States).

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `ref` | string | Ja | Element-Referenz aus Snapshot |

---

### `browser_drag`

Drag-and-Drop zwischen zwei Elementen.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `startRef` | string | Ja | Zu ziehendes Element |
| `endRef` | string | Ja | Ziel-Element |

---

### `browser_select_option`

Waehlt eine oder mehrere Optionen in einem `<select>`-Dropdown.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `ref` | string | Ja | Das `<select>`-Element |
| `values` | string[] | Ja | Werte oder Labels der Optionen |

```
browser_select_option { ref: "e15", values: ["germany"] }
```

---

### `browser_resize`

Aendert die Groesse des Browser-Fensters.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `width` | number | Ja | Breite in Pixel |
| `height` | number | Ja | Hoehe in Pixel |

---

## Core: Forms

Capability: `core` (immer aktiv)

### `browser_type`

Text in editierbare Elemente eingeben (input, textarea, contenteditable).

| Parameter | Typ | Required | Default | Beschreibung |
|-----------|-----|----------|---------|--------------|
| `ref` | string | Ja | — | Element-Referenz |
| `text` | string | Ja | — | Einzugebender Text |
| `submit` | boolean | Nein | false | Enter nach dem Tippen druecken |
| `slowly` | boolean | Nein | false | Zeichen fuer Zeichen tippen (loest Key-Handler aus) |

```
browser_type { ref: "e5", text: "Buy groceries", submit: true }
browser_type { ref: "e8", text: "search query", slowly: true }
```

---

### `browser_fill_form`

Fuellt mehrere Formularfelder gleichzeitig (effizienter als einzelne type/click-Aufrufe).

Unterstuetzte Elemente: Textboxen, Checkboxen, Radio-Buttons, Comboboxen, Slider.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `fields` | array | Ja | Array von `{ ref, value }`-Objekten |

```
browser_fill_form {
  fields: [
    { ref: "e5", value: "Alice" },
    { ref: "e8", value: "alice@example.com" },
    { ref: "e12", value: true }
  ]
}
```

---

### `browser_check`

Aktiviert eine Checkbox oder einen Radio-Button.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `ref` | string | Ja | Element-Referenz |

---

### `browser_uncheck`

Deaktiviert eine Checkbox.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `ref` | string | Ja | Element-Referenz |

---

## Core: Screenshots

Capability: `core` (immer aktiv)

### `browser_take_screenshot`

Nimmt einen Screenshot der aktuellen Seite, eines Elements oder der gesamten scrollbaren Seite.

| Parameter | Typ | Required | Default | Beschreibung |
|-----------|-----|----------|---------|--------------|
| `type` | string | Nein | `png` | Bildformat: `png` oder `jpeg` |
| `ref` | string | Nein | — | Element-Referenz fuer Element-Screenshot |
| `fullPage` | boolean | Nein | false | Gesamte scrollbare Seite aufnehmen |

```
# Viewport-Screenshot
browser_take_screenshot {}

# Element-Screenshot
browser_take_screenshot { ref: "e20" }

# Vollstaendige Seite
browser_take_screenshot { fullPage: true, type: "jpeg" }
```

---

## Core: Keyboard & Maus

Capability: `core` (immer aktiv, ohne Vision)

### `browser_press_key`

Drueckt eine Taste oder Tastenkombination.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `key` | string | Ja | Taste oder Kombination |

Haeufige Tasten: `Enter`, `Tab`, `Escape`, `Backspace`, `Delete`, `ArrowUp`, `ArrowDown`, `ArrowLeft`, `ArrowRight`, `Home`, `End`, `PageUp`, `PageDown`, `F5`

Kombinationen: `Control+a`, `Control+c`, `Control+v`, `Shift+Tab`, `Alt+F4`

```
browser_press_key { key: "Control+a" }
browser_press_key { key: "Enter" }
```

---

### Vision-Modus: Maus-Tools

Nur verfuegbar mit `--caps=vision`. Arbeiten mit Pixel-Koordinaten aus Screenshots.

#### `browser_mouse_move_xy`

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `x` | number | Ja | Horizontale Pixel-Position |
| `y` | number | Ja | Vertikale Pixel-Position |

#### `browser_mouse_click_xy`

| Parameter | Typ | Required | Default | Beschreibung |
|-----------|-----|----------|---------|--------------|
| `x` | number | Ja | — | Horizontale Koordinate |
| `y` | number | Ja | — | Vertikale Koordinate |
| `button` | string | Nein | `left` | `left`, `right`, `middle` |
| `clickCount` | number | Nein | 1 | Anzahl Klicks (2 fuer Doppelklick) |
| `delay` | number | Nein | 0 | Pause zwischen mousedown/mouseup (ms) |

#### `browser_mouse_drag_xy`

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `startX` | number | Ja | Start-X-Koordinate |
| `startY` | number | Ja | Start-Y-Koordinate |
| `endX` | number | Ja | Ziel-X-Koordinate |
| `endY` | number | Ja | Ziel-Y-Koordinate |

#### `browser_mouse_down` / `browser_mouse_up`

Maus-Button druecken / loslassen an der aktuellen Position. Keine Parameter.

#### `browser_mouse_wheel`

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `deltaX` | number | Ja | Horizontaler Scroll-Betrag (Pixel) |
| `deltaY` | number | Ja | Vertikaler Scroll-Betrag (positiv = nach unten) |

---

## Core: Tabs

Capability: `core` (immer aktiv)

### `browser_tabs`

Verwaltet Browser-Tabs (auflisten, erstellen, schliessen, wechseln).

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `action` | string | Ja | `list`, `new`, `close`, `select` |
| `url` | string | Nein | URL fuer `new`-Aktion |
| `index` | number | Nein | Tab-Index fuer `select` oder `close` |

```
# Alle Tabs auflisten
browser_tabs { action: "list" }

# Neuen Tab oeffnen
browser_tabs { action: "new", url: "https://example.com" }

# Zu Tab 1 wechseln
browser_tabs { action: "select", index: 1 }

# Aktuellen Tab schliessen
browser_tabs { action: "close" }

# Spezifischen Tab schliessen
browser_tabs { action: "close", index: 2 }
```

---

## Core: Dialoge

Capability: `core` (immer aktiv)

### `browser_handle_dialog`

Behandelt Browser-Dialoge (alert, confirm, prompt).

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `accept` | boolean | Ja | `true` = akzeptieren, `false` = abweisen |
| `promptText` | string | Nein | Text fuer Prompt-Dialoge |

```
# Alert bestaetigen
browser_handle_dialog { accept: true }

# Confirm abweisen
browser_handle_dialog { accept: false }

# Prompt mit Text bestaetigen
browser_handle_dialog { accept: true, promptText: "Mein Eingabewert" }
```

Dialog-Typen: `alert` (Nachricht), `confirm` (Ja/Nein), `prompt` (Texteingabe)
Hinweis: Dialog muss behandelt werden, bevor weitere Operationen moeglich sind.

---

## Core: Wartebedingungen

Capability: `core` (immer aktiv)

### `browser_wait_for`

Wartet auf eine Bedingung bevor fortgefahren wird.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `time` | number | Nein | Sekunden warten |
| `text` | string | Nein | Auf Erscheinen dieses Textes warten |
| `textGone` | string | Nein | Auf Verschwinden dieses Textes warten |

```
# 2 Sekunden warten
browser_wait_for { time: 2 }

# Auf Text warten
browser_wait_for { text: "Erfolgreich gespeichert" }

# Auf Verschwinden des Ladeindikators warten
browser_wait_for { textGone: "Laden..." }
```

Fuer komplexere Bedingungen: `browser_run_code { code: "await page.waitForSelector('.data-loaded')" }`

---

## Core: Console

Capability: `core` (immer aktiv)

### `browser_console_messages`

Greift auf Browser-Konsolen-Ausgaben zu.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `level` | string | Nein | Mindest-Level: `error`, `warning`, `info`, `debug` |

Jedes Level schliesst schwerwiegendere Level ein (`debug` = alle).

---

### `browser_console_clear`

Leert den Konsolen-Nachrichten-Puffer. Keine Parameter.

---

## Core: File Upload

Capability: `core` (immer aktiv)

### `browser_file_upload`

Behandelt Datei-Auswahldialoge.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `paths` | string[] | Ja | Absolute Dateipfade; leeres Array = abbrechen |

```
# Einzelne Datei
browser_file_upload { paths: ["/home/user/report.pdf"] }

# Mehrere Dateien
browser_file_upload {
  paths: [
    "/home/user/photo1.jpg",
    "/home/user/photo2.jpg"
  ]
}

# Abbrechen
browser_file_upload { paths: [] }
```

Sicherheit: Standardmaessig nur aus MCP-Workspace-Roots. `--allow-unrestricted-file-access` fuer beliebige Pfade.

---

## Code-Ausfuehrung

Capability: `core` (immer aktiv)

### `browser_run_code`

Fuehrt Playwright-Code-Schnipsel mit vollem API-Zugriff ueber ein `page`-Objekt aus.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `code` | string | Ja | Playwright-Code-String |

```
browser_run_code { code: "return await page.title()" }

browser_run_code {
  code: "await page.context().grantPermissions(['geolocation'])"
}

browser_run_code {
  code: "await page.evaluate(() => navigator.geolocation)"
}
```

Einsatz fuer: komplexe Multi-Step-Logik, Geolocation/Permissions, Custom-Wartebedingungen, iFrame-Interaktionen, Clipboard-Operationen.

---

### `browser_evaluate`

Wertet JavaScript direkt auf der Seite oder einem Element aus.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `expression` | string | Ja | Auszufuehrender JavaScript-Code |
| `ref` | string | Nein | Element-Referenz fuer Element-Scope |

```
browser_evaluate { expression: "document.title" }
browser_evaluate { expression: "getAttribute('href')", ref: "e20" }
browser_evaluate { expression: "window.innerWidth + 'x' + window.innerHeight" }
```

---

## Network

Capability: `network` (mit `--caps=network`)

### `browser_network_requests`

Listet seit dem Seitenlade erfasste Netzwerk-Requests.

| Parameter | Typ | Required | Default | Beschreibung |
|-----------|-----|----------|---------|--------------|
| `filter` | string | Nein | — | RegExp-Muster zum Filtern nach URL |
| `includeStatic` | boolean | Nein | false | Bilder, CSS, Fonts einschliessen |
| `includeBody` | boolean | Nein | false | Request-Body einschliessen |
| `includeHeaders` | boolean | Nein | false | Request-Headers einschliessen |

---

### `browser_route`

Intercepts eine URL und gibt eine benutzerdefinierte Antwort zurueck.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `pattern` | string | Ja | URL-Muster mit Glob-Unterstuetzung |
| `status` | number | Nein | HTTP-Status-Code |
| `body` | string | Nein | Response-Body |
| `contentType` | string | Nein | Content-Type-Header |
| `headers` | object | Nein | Zusaetzliche Response-Header |
| `removeHeaders` | string[] | Nein | Zu entfernende Request-Header |

```
browser_route {
  pattern: "**/api/users",
  status: 200,
  body: '{"users":[{"id":1,"name":"Test"}]}',
  contentType: "application/json"
}
```

---

### `browser_route_list`

Zeigt aktive Route-Muster, Status-Codes und Content-Types. Keine Parameter.

---

### `browser_unroute`

Entfernt aktive Routen.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `pattern` | string | Nein | Spezifisches Muster; weglassen = alle entfernen |

---

### `browser_network_state_set`

Simuliert Online/Offline-Zustand.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `state` | string | Ja | `"online"` oder `"offline"` |

---

## Storage

Capability: `storage` (mit `--caps=storage`)

### `browser_storage_state`

Speichert den kompletten Browser-State (Cookies + localStorage) als JSON. Keine Parameter.

---

### `browser_set_storage_state`

Stellt einen gespeicherten Browser-State wieder her.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `path` | string | Ja | Pfad zur State-JSON-Datei |

---

### Cookie-Tools

#### `browser_cookie_list`

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `domain` | string | Nein | Nach Domain filtern |
| `path` | string | Nein | Nach Pfad filtern |

Gibt: Name, Value, Domain, HttpOnly, Secure, Expires zurueck.

#### `browser_cookie_get`

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `name` | string | Ja | Cookie-Name |

#### `browser_cookie_set`

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `name` | string | Ja | Cookie-Name |
| `value` | string | Ja | Cookie-Wert |
| `domain` | string | Nein | Domain |
| `path` | string | Nein | Pfad |
| `expires` | number | Nein | Unix-Timestamp |
| `httpOnly` | boolean | Nein | HttpOnly-Flag |
| `secure` | boolean | Nein | Secure-Flag |
| `sameSite` | string | Nein | `Strict`, `Lax`, oder `None` |

#### `browser_cookie_delete`

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `name` | string | Ja | Cookie-Name |

#### `browser_cookie_clear`

Loescht alle Cookies. Keine Parameter.

---

### localStorage-Tools

#### `browser_localstorage_list`
Listet alle localStorage-Eintraege. Keine Parameter.

#### `browser_localstorage_get`
| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `key` | string | Ja | Schlussel |

#### `browser_localstorage_set`
| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `key` | string | Ja | Schlussel |
| `value` | string | Ja | Wert |

#### `browser_localstorage_delete`
| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `key` | string | Ja | Schlussel |

#### `browser_localstorage_clear`
Loescht alle localStorage-Eintraege. Keine Parameter.

### sessionStorage-Tools

Identische Schnittstelle wie localStorage, aber Session-begrenzt:
- `browser_sessionstorage_list`
- `browser_sessionstorage_get` (`key`)
- `browser_sessionstorage_set` (`key`, `value`)
- `browser_sessionstorage_delete` (`key`)
- `browser_sessionstorage_clear`

---

## Testing

Capability: `testing` (mit `--caps=testing`)

### `browser_verify_element_visible`

Verifiziert Sichtbarkeit eines Elements ueber ARIA-Rolle.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `role` | string | Ja | ARIA-Rolle (z.B. `button`, `heading`, `textbox`) |
| `name` | string | Ja | Zugaenglicher Name des Elements |

```
browser_verify_element_visible { role: "button", name: "Speichern" }
```

---

### `browser_verify_text_visible`

Prueft ob ein Text auf der Seite sichtbar ist.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `text` | string | Ja | Zu pruefender Text |

---

### `browser_verify_list_visible`

Validiert eine Liste mit erwarteten Eintraegen.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `label` | string | Ja | Listenbeschriftung / Zugaenglicher Name |
| `items` | string[] | Ja | Erwartete Listenelemente |

---

### `browser_verify_value`

Prueft ob der Wert eines Elements dem erwarteten Wert entspricht.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `ref` | string | Ja | Element-Referenz |
| `value` | string | Ja | Erwarteter Wert |

---

### `browser_generate_locator`

Generiert einen Playwright-Locator fuer ein Element (fuer Test-Code-Generierung).

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `ref` | string | Ja | Element-Referenz aus Snapshot |

```
browser_generate_locator { ref: "e5" }
// Gibt zurueck: page.getByRole('textbox', { name: 'New todo' })
```

---

## Devtools: Tracing

Capability: `devtools` (mit `--caps=devtools`)

### `browser_start_tracing`

Startet die Aufzeichnung eines Execution-Trace. Keine Parameter.

Aufgenommen wird: DOM-Snapshots, Screenshots, Netzwerk-Requests, Konsolen-Nachrichten, Timing.

---

### `browser_stop_tracing`

Stoppt die Aufzeichnung und speichert als `.zip`-Datei. Keine Parameter.

```bash
# Trace anzeigen
npx playwright show-trace /output/trace-2024-03-15.zip
```

Automatische Aufzeichnung: `--save-session`-Flag.

---

## Devtools: Video

Capability: `devtools` (mit `--caps=devtools`)

### `browser_start_video`

Startet die Video-Aufzeichnung der Browser-Session.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `filename` | string | Nein | Benutzerdefinierter Dateiname |
| `width` | number | Nein | Video-Breite in Pixel |
| `height` | number | Nein | Video-Hoehe in Pixel |

---

### `browser_stop_video`

Stoppt die Aufzeichnung und speichert als WebM-Datei. Keine Parameter.

---

### `browser_video_chapter`

Fuegt Chapter-Markierungen in die Aufzeichnung ein.

| Parameter | Typ | Required | Beschreibung |
|-----------|-----|----------|--------------|
| `title` | string | Ja | Chapter-Titel |
| `description` | string | Nein | Chapter-Beschreibung |
| `duration` | number | Nein | Anzeigedauer in Millisekunden |

---

## PDF

Capability: `pdf` (mit `--caps=pdf`)

### `browser_pdf_save`

Exportiert die aktuelle Seite als PDF-Datei. Keine Parameter.

Datei wird im Output-Verzeichnis gespeichert. Anwendungsfaelle: Belege, Archive, Berichte, Dokumentation.

---

## Vollstaendige Tool-Uebersicht

| Tool | Capability | Parameter |
|------|-----------|-----------|
| `browser_navigate` | core | url |
| `browser_navigate_back` | core | — |
| `browser_navigate_forward` | core | — |
| `browser_reload` | core | — |
| `browser_close` | core | — |
| `browser_snapshot` | core | — |
| `browser_click` | core | ref |
| `browser_hover` | core | ref |
| `browser_drag` | core | startRef, endRef |
| `browser_select_option` | core | ref, values[] |
| `browser_resize` | core | width, height |
| `browser_type` | core | ref, text, [submit, slowly] |
| `browser_fill_form` | core | fields[] |
| `browser_check` | core | ref |
| `browser_uncheck` | core | ref |
| `browser_take_screenshot` | core | [type, ref, fullPage] |
| `browser_press_key` | core | key |
| `browser_tabs` | core | action, [url, index] |
| `browser_handle_dialog` | core | accept, [promptText] |
| `browser_wait_for` | core | [time, text, textGone] |
| `browser_console_messages` | core | [level] |
| `browser_console_clear` | core | — |
| `browser_file_upload` | core | paths[] |
| `browser_run_code` | core | code |
| `browser_evaluate` | core | expression, [ref] |
| `browser_mouse_move_xy` | vision | x, y |
| `browser_mouse_click_xy` | vision | x, y, [button, clickCount, delay] |
| `browser_mouse_drag_xy` | vision | startX, startY, endX, endY |
| `browser_mouse_down` | vision | — |
| `browser_mouse_up` | vision | — |
| `browser_mouse_wheel` | vision | deltaX, deltaY |
| `browser_network_requests` | core | [filter, includeStatic, includeBody, includeHeaders] |
| `browser_route` | network | pattern, [status, body, contentType, headers, removeHeaders] |
| `browser_route_list` | network | — |
| `browser_unroute` | network | [pattern] |
| `browser_network_state_set` | network | state |
| `browser_storage_state` | storage | — |
| `browser_set_storage_state` | storage | path |
| `browser_cookie_list` | storage | [domain, path] |
| `browser_cookie_get` | storage | name |
| `browser_cookie_set` | storage | name, value, [domain, path, expires, httpOnly, secure, sameSite] |
| `browser_cookie_delete` | storage | name |
| `browser_cookie_clear` | storage | — |
| `browser_localstorage_list` | storage | — |
| `browser_localstorage_get` | storage | key |
| `browser_localstorage_set` | storage | key, value |
| `browser_localstorage_delete` | storage | key |
| `browser_localstorage_clear` | storage | — |
| `browser_sessionstorage_*` | storage | (wie localStorage) |
| `browser_verify_element_visible` | testing | role, name |
| `browser_verify_text_visible` | testing | text |
| `browser_verify_list_visible` | testing | label, items[] |
| `browser_verify_value` | testing | ref, value |
| `browser_generate_locator` | testing | ref |
| `browser_start_tracing` | devtools | — |
| `browser_stop_tracing` | devtools | — |
| `browser_start_video` | devtools | [filename, width, height] |
| `browser_stop_video` | devtools | — |
| `browser_video_chapter` | devtools | title, [description, duration] |
| `browser_pdf_save` | pdf | — |

---

## Quellen

- https://playwright.dev/mcp/tools/navigation
- https://playwright.dev/mcp/tools/interaction
- https://playwright.dev/mcp/tools/forms
- https://playwright.dev/mcp/tools/screenshots
- https://playwright.dev/mcp/tools/keyboard-mouse
- https://playwright.dev/mcp/tools/tabs
- https://playwright.dev/mcp/tools/dialogs
- https://playwright.dev/mcp/tools/waiting
- https://playwright.dev/mcp/tools/console
- https://playwright.dev/mcp/tools/file-upload
- https://playwright.dev/mcp/tools/code-execution
- https://playwright.dev/mcp/tools/network-mocking
- https://playwright.dev/mcp/tools/storage
- https://playwright.dev/mcp/tools/assertions
- https://playwright.dev/mcp/tools/tracing
- https://playwright.dev/mcp/tools/video
- https://playwright.dev/mcp/tools/pdf
