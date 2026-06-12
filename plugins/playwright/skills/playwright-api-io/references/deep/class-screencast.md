# Playwright — class: Screencast

> **Manifest:** 7 Methoden, 0 Properties, 0 Events.
> Steuert visuelle Annotierungen und Video-Frames fuer Screencast-Aufnahmen.
> Experimentelles Feature. Zugriff: `page.screencast`.

---

## Uebersicht

`Screencast` bietet eine erweiterte API fuer Video-Aufnahmen mit visuellen
Ueberlagerungen: Aktions-Annotierungen, Kapitel-Overlays und benutzerdefinierte
HTML-Overlays. Ausserdem koennen JPEG-Frames live per Callback empfangen
werden.

**Hinweis:** Diese API ist experimentell und kann sich in zukunftigen
Versionen aendern.

---

## Methoden

### screencast.hideActions()

Entfernt alle Aktions-Annotierungen (Action-Decorations) von der Aufnahme.

**Signatur:**
```typescript
screencast.hideActions(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.screencast.hideActions();
```

---

### screencast.hideOverlays()

Versteckt alle aktiven Overlays, ohne sie zu entfernen. Overlays koennen
danach mit `showOverlays()` wieder sichtbar gemacht werden.

**Signatur:**
```typescript
screencast.hideOverlays(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.screencast.hideOverlays();
// Overlays sind jetzt unsichtbar aber noch vorhanden
await page.screencast.showOverlays();
// Overlays sind wieder sichtbar
```

---

### screencast.showActions(options?)

Aktiviert visuelle Annotierungen auf Elementen, mit denen interagiert wird
(Klicks, Tipp-Events usw.). Gibt ein `Disposable` zurueck — beim Dispose
werden Aktions-Annotierungen wieder deaktiviert.

**Signatur:**
```typescript
screencast.showActions(options?: {
  duration?: number;
  fontSize?: number;
  position?: 'top-left' | 'top' | 'top-right' | 'bottom-left' | 'bottom' | 'bottom-right';
}): Promise<Disposable>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.duration` | `number` | nein | `500` | Anzeigedauer der Annotation in Millisekunden |
| `options.fontSize` | `number` | nein | `24` | Schriftgroesse des Titels in Pixeln |
| `options.position` | `string` | nein | `'top-right'` | Position der Annotation relativ zum Element |

**Rueckgabe:** `Promise<Disposable>` — bei `dispose()` werden Aktions-
Annotierungen gestoppt

**Beispiel:**
```javascript
const disposable = await page.screencast.showActions({
  duration: 800,
  fontSize: 18,
  position: 'bottom'
});
// ... Interaktionen werden visuell annotiert ...
await disposable.dispose();
```

---

### screencast.showChapter(title, options?)

Zeigt ein prominentes Kapitel-Overlay in der Mitte der Seite an, mit
optionaler Beschreibung und unscharfem Hintergrund.

**Signatur:**
```typescript
screencast.showChapter(title: string, options?: {
  description?: string;
  duration?: number;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `title` | `string` | ja | — | Haupttitel-Text, prominent angezeigt |
| `options.description` | `string` | nein | — | Optionaler Beschreibungstext unterhalb des Titels |
| `options.duration` | `number` | nein | `2000` | Automatische Entfernung nach N Millisekunden |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.screencast.showChapter('Schritt 3: Warenkorb', {
  description: 'Produkt zum Warenkorb hinzufuegen',
  duration: 3000
});
await page.click('[data-testid="add-to-cart"]');
```

---

### screencast.showOverlay(html, options?)

Fuegt ein benutzerdefiniertes HTML-Overlay ueber der Seite ein.

**Signatur:**
```typescript
screencast.showOverlay(html: string, options?: {
  duration?: number;
}): Promise<Disposable>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `html` | `string` | ja | — | HTML-Inhalt des Overlays |
| `options.duration` | `number` | nein | — | Automatische Entfernung nach N ms. Ohne Angabe: manuell via `dispose()` entfernen |

**Rueckgabe:** `Promise<Disposable>` — bei `dispose()` oder nach `duration`
wird das Overlay entfernt

**Beispiel:**
```javascript
const overlay = await page.screencast.showOverlay(
  '<div style="background:rgba(0,0,0,0.8);color:white;padding:10px">Test lauft...</div>'
);
await page.click('#submit');
await overlay.dispose();
```

---

### screencast.showOverlays()

Zeigt alle zuvor mit `hideOverlays()` versteckten Overlays wieder an.

**Signatur:**
```typescript
screencast.showOverlays(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.screencast.showOverlays();
```

---

### screencast.start(options?)

Startet die Screencast-Aufnahme. Kann gleichzeitig eine Video-Datei
aufzeichnen und/oder Frames per Callback liefern.

**Signatur:**
```typescript
screencast.start(options?: {
  onFrame?: (frame: {
    data: Buffer;
    viewportWidth: number;
    viewportHeight: number;
  }) => void;
  path?: string;
  quality?: number;
  size?: {
    width: number;
    height: number;
  };
}): Promise<Disposable>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.onFrame` | `Function` | nein | — | Callback fuer jeden JPEG-kodierten Frame. Erhaelt `data` (Buffer), `viewportWidth` (number), `viewportHeight` (number) |
| `options.path` | `string` | nein | — | Dateipfad fuer Video-Aufzeichnung. Wenn angegeben, wird ein Video gespeichert. |
| `options.quality` | `number` | nein | — | JPEG-Bildqualitaet zwischen 0 und 100 |
| `options.size` | `Object` | nein | — | Abmessungen der aufgezeichneten Frames |
| `options.size.width` | `number` | nein | — | Breite in Pixeln |
| `options.size.height` | `number` | nein | — | Hoehe in Pixeln |

**Rueckgabe:** `Promise<Disposable>` — beim Dispose wird die Aufnahme gestoppt
(entspricht `stop()`)

**Beispiel:**
```javascript
// Video-Datei aufnehmen
const recording = await page.screencast.start({ path: 'demo.webm', quality: 80 });
await page.goto('https://example.com');
await recording.dispose();

// Frame-Callback
await page.screencast.start({
  onFrame: ({ data, viewportWidth, viewportHeight }) => {
    // JPEG-Buffer verarbeiten (z.B. an Streaming-Service senden)
    console.log(`Frame ${viewportWidth}x${viewportHeight}: ${data.length} bytes`);
  },
  size: { width: 1280, height: 720 }
});
```

---

### screencast.stop()

Stoppt die Screencast-Aufnahme und speichert das Video (falls `path` in
`start()` angegeben wurde).

**Signatur:**
```typescript
screencast.stop(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.screencast.stop();
```

---

## Properties

Keine offentlichen Properties.

## Events

Keine eigenen Events.

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 7      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** `start()` mit `path` bietet eine Alternative zur `recordVideo`-
Context-Option mit feingranularer Kontrolle. `showChapter()` und
`showOverlay()` sind besonders wertvoll fuer Demo-Videos und Tutorial-
Aufzeichnungen. `showActions()` macht Klicks und Eingaben fuer Zuschauer
sichtbar.

---

*Quelle: https://playwright.dev/docs/api/class-screencast*
