# Playwright — class: Touchscreen

> **Manifest:** 1 Methode, 0 Properties, 0 Events.
> Simuliert Touch-Gesten. Nur verfuegbar, wenn der BrowserContext mit `hasTouch: true` erstellt wurde.
> Zugriff: `page.touchscreen`.

---

## Uebersicht

`Touchscreen` erlaubt das Senden von Touch-Events an den Browser. Die Klasse
ist auf einen einzelnen Tap-Befehl beschraenkt; komplexere Gesten (Pinch,
Swipe, Multi-Touch) muessen manuell ueber `page.dispatchEvent()` implementiert
werden.

**Voraussetzung:** Der BrowserContext muss mit `hasTouch: true` erzeugt werden:

```javascript
const context = await browser.newContext({ hasTouch: true });
const page = await context.newPage();
```

---

## Methoden

### touchscreen.tap(x, y)

Sendet ein `touchstart`- gefolgt von einem `touchend`-Event an der
angegebenen Position.

**Signatur:**
```typescript
touchscreen.tap(x: number, y: number): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `x` | `number` | ja | — | X-Koordinate in CSS-Pixeln, relativ zum Haupt-Frame-Viewport |
| `y` | `number` | ja | — | Y-Koordinate in CSS-Pixeln, relativ zum Haupt-Frame-Viewport |

**Rueckgabe:** `Promise<void>`

**Hinweise:**
- Wirft einen Fehler, wenn `hasTouch` im BrowserContext nicht aktiviert wurde.
- Loest `touchstart` + `touchend` aus; kein `touchmove`.
- Koordinaten beziehen sich auf den Haupt-Frame — bei iframes ggf. Offset
  berechnen.

**Beispiel:**
```javascript
const context = await browser.newContext({ hasTouch: true });
const page = await context.newPage();
await page.goto('https://example.com');
await page.touchscreen.tap(150, 200);
```

---

## Manuelle Multi-Touch-Gesten

Da `Touchscreen` nur `tap()` anbietet, werden komplexere Gesten ueber
`page.dispatchEvent()` implementiert:

```javascript
// Swipe nach links (touchstart -> touchmove -> touchend)
const element = await page.$('#swipeable');
const box = await element.boundingBox();

await page.dispatchEvent('#swipeable', 'touchstart', {
  touches: [{ clientX: box.x + box.width / 2, clientY: box.y + box.height / 2 }]
});
await page.dispatchEvent('#swipeable', 'touchmove', {
  touches: [{ clientX: box.x, clientY: box.y + box.height / 2 }]
});
await page.dispatchEvent('#swipeable', 'touchend', { touches: [] });
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
| Methoden  | 1      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** Die Klasse ist bewusst minimal gehalten. Fuer einfache Touch-Tests
genuegt `tap()`. Fuer reale Mobile-Emulation empfiehlt sich die Kombination mit
`page.emulate({ device: playwright.devices['iPhone 14'] })` und
`hasTouch: true` im Context. Komplexe Gesten erfordern manuelles
`dispatchEvent`.

---

*Quelle: https://playwright.dev/docs/api/class-touchscreen*
