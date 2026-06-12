# Playwright — class: Mouse

> **Manifest:** 6 Methoden, 0 Properties, 0 Events.
> Vollstandige Maussteuerung in CSS-Pixel-Koordinaten relativ zur Viewport-Ecke oben-links.
> Zugriff: `page.mouse`.

---

## Uebersicht

`Mouse` emuliert alle Maus-Interaktionen des Browsers. Die Koordinaten beziehen
sich auf den Haupt-Frame-Viewport. Die Instanz ist ueber `page.mouse` erreichbar.

---

## Methoden

### mouse.click(x, y, options?)

Kombination aus `move()`, `down()` und `up()` — klickt an einer Koordinate.

**Signatur:**
```typescript
mouse.click(x: number, y: number, options?: {
  button?: 'left' | 'right' | 'middle';
  clickCount?: number;
  delay?: number;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `x` | `number` | ja | — | X-Koordinate in CSS-Pixeln |
| `y` | `number` | ja | — | Y-Koordinate in CSS-Pixeln |
| `options.button` | `'left' \| 'right' \| 'middle'` | nein | `'left'` | Welche Maustaste |
| `options.clickCount` | `number` | nein | `1` | Anzahl Klicks (fuer Einfach-/Doppelklick usw.) |
| `options.delay` | `number` | nein | `0` | Millisekunden zwischen mousedown und mouseup |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.mouse.click(100, 200);
await page.mouse.click(100, 200, { button: 'right' });
await page.mouse.click(100, 200, { clickCount: 2, delay: 50 });
```

---

### mouse.dblclick(x, y, options?)

Doppelklick: `move()`, `down()`, `up()`, `down()`, `up()`.

**Signatur:**
```typescript
mouse.dblclick(x: number, y: number, options?: {
  button?: 'left' | 'right' | 'middle';
  delay?: number;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `x` | `number` | ja | — | X-Koordinate in CSS-Pixeln |
| `y` | `number` | ja | — | Y-Koordinate in CSS-Pixeln |
| `options.button` | `'left' \| 'right' \| 'middle'` | nein | `'left'` | Welche Maustaste |
| `options.delay` | `number` | nein | `0` | Millisekunden zwischen den einzelnen Klicks |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.mouse.dblclick(150, 300);
```

---

### mouse.down(options?)

Sendet ein `mousedown`-Event an der aktuellen Mausposition.

**Signatur:**
```typescript
mouse.down(options?: {
  button?: 'left' | 'right' | 'middle';
  clickCount?: number;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.button` | `'left' \| 'right' \| 'middle'` | nein | `'left'` | Welche Maustaste gedrueckt wird |
| `options.clickCount` | `number` | nein | `1` | Click-Count im Event (relevant fuer Doppelklick-Sequenzen) |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.mouse.move(100, 100);
await page.mouse.down();
```

---

### mouse.move(x, y, options?)

Bewegt die Maus zu den angegebenen Koordinaten. Sendet `mousemove`-Events.

**Signatur:**
```typescript
mouse.move(x: number, y: number, options?: {
  steps?: number;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `x` | `number` | ja | — | Ziel-X-Koordinate in CSS-Pixeln |
| `y` | `number` | ja | — | Ziel-Y-Koordinate in CSS-Pixeln |
| `options.steps` | `number` | nein | `1` | Anzahl interpolierter Zwischenpositionen (erzeugt mehrere mousemove-Events) |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
// Direkte Bewegung
await page.mouse.move(200, 300);

// Sanfte Bewegung mit Zwischenpunkten (z.B. fuer Hover-Animationen)
await page.mouse.move(200, 300, { steps: 10 });
```

---

### mouse.up(options?)

Sendet ein `mouseup`-Event an der aktuellen Mausposition.

**Signatur:**
```typescript
mouse.up(options?: {
  button?: 'left' | 'right' | 'middle';
  clickCount?: number;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.button` | `'left' \| 'right' \| 'middle'` | nein | `'left'` | Welche Maustaste losgelassen wird |
| `options.clickCount` | `number` | nein | `1` | Click-Count im Event |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.mouse.up();
```

---

### mouse.wheel(deltaX, deltaY)

Simuliert ein Mausrad-Event (horizontales und vertikales Scrollen).

**Signatur:**
```typescript
mouse.wheel(deltaX: number, deltaY: number): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `deltaX` | `number` | ja | — | Horizontale Scroll-Delta in Pixeln (positiv = rechts) |
| `deltaY` | `number` | ja | — | Vertikale Scroll-Delta in Pixeln (positiv = unten) |

**Rueckgabe:** `Promise<void>`

**Hinweis:** Das `wheel`-Event kann Scrollen ausloesen, ohne darauf zu warten
dass das Scrollen abgeschlossen ist. Ggf. danach `page.waitForTimeout()` oder
einen sichtbaren Zustandswechsel abwarten.

**Beispiel:**
```javascript
// Nach unten scrollen
await page.mouse.wheel(0, 500);

// Horizontal scrollen
await page.mouse.wheel(200, 0);
```

---

## Vollstaendiges Beispiel: Drag-Rechteck zeichnen

```javascript
// Quadrat von (0,0) nach (100,100) zeichnen (Drag-Geste)
await page.mouse.move(0, 0);
await page.mouse.down();
await page.mouse.move(0, 100);
await page.mouse.move(100, 100);
await page.mouse.move(100, 0);
await page.mouse.move(0, 0);
await page.mouse.up();
```

---

## Properties

Keine offentlichen Properties.

## Events

Keine eigenen Events — Mouse-Interaktionen loesen Events auf den Seiten-
Elementen aus, nicht auf dem Mouse-Objekt selbst.

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 6      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** `click()` und `dblclick()` decken den Grossteil der Anwendungsfaelle ab.
`down()` / `move()` / `up()` benoetigt man fuer Drag-and-Drop oder komplexe
Mausgesten. `wheel()` ist die einzige Scroll-Methode auf der Maus-Ebene.

---

*Quelle: https://playwright.dev/docs/api/class-mouse*
