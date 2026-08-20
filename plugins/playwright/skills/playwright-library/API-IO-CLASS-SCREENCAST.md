# Playwright — class: Screencast

> **Manifest:** 7 methods, 0 properties, 0 events.
> Controls visual annotations and video frames for screencast recordings.
> Experimental feature. Access: `page.screencast`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Properties](#properties)
- [Events](#events)
- [Manifest](#manifest)

## Overview

`Screencast` offers an extended API for video recordings with visual
overlays: action annotations, chapter overlays and custom
HTML overlays. In addition, JPEG frames can be received live via a
callback.

**Note:** This API is experimental and may change in future
versions.

---

## Methods

### screencast.hideActions()

Removes all action annotations (action decorations) from the recording.

**Signature:**
```typescript
screencast.hideActions(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.screencast.hideActions();
```

---

### screencast.hideOverlays()

Hides all active overlays without removing them. Overlays can
be made visible again afterwards with `showOverlays()`.

**Signature:**
```typescript
screencast.hideOverlays(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.screencast.hideOverlays();
// Overlays are now invisible but still present
await page.screencast.showOverlays();
// Overlays are visible again
```

---

### screencast.showActions(options?)

Enables visual annotations on elements that are interacted with
(clicks, typing events etc.). Returns a `Disposable` — on dispose
action annotations are disabled again.

**Signature:**
```typescript
screencast.showActions(options?: {
  duration?: number;
  fontSize?: number;
  position?: 'top-left' | 'top' | 'top-right' | 'bottom-left' | 'bottom' | 'bottom-right';
}): Promise<Disposable>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.duration` | `number` | no | `500` | Display duration of the annotation in milliseconds |
| `options.fontSize` | `number` | no | `24` | Font size of the title in pixels |
| `options.position` | `string` | no | `'top-right'` | Position of the annotation relative to the element |

**Returns:** `Promise<Disposable>` — on `dispose()` action
annotations are stopped

**Example:**
```javascript
const disposable = await page.screencast.showActions({
  duration: 800,
  fontSize: 18,
  position: 'bottom'
});
// ... interactions are annotated visually ...
await disposable.dispose();
```

---

### screencast.showChapter(title, options?)

Shows a prominent chapter overlay in the centre of the page, with
an optional description and a blurred background.

**Signature:**
```typescript
screencast.showChapter(title: string, options?: {
  description?: string;
  duration?: number;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `title` | `string` | yes | — | Main title text, displayed prominently |
| `options.description` | `string` | no | — | Optional description text below the title |
| `options.duration` | `number` | no | `2000` | Automatic removal after N milliseconds |

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.screencast.showChapter('Step 3: Cart', {
  description: 'Add product to the cart',
  duration: 3000
});
await page.click('[data-testid="add-to-cart"]');
```

---

### screencast.showOverlay(html, options?)

Inserts a custom HTML overlay on top of the page.

**Signature:**
```typescript
screencast.showOverlay(html: string, options?: {
  duration?: number;
}): Promise<Disposable>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `html` | `string` | yes | — | HTML content of the overlay |
| `options.duration` | `number` | no | — | Automatic removal after N ms. Without it: remove manually via `dispose()` |

**Returns:** `Promise<Disposable>` — on `dispose()` or after `duration`
the overlay is removed

**Example:**
```javascript
const overlay = await page.screencast.showOverlay(
  '<div style="background:rgba(0,0,0,0.8);color:white;padding:10px">Test running...</div>'
);
await page.click('#submit');
await overlay.dispose();
```

---

### screencast.showOverlays()

Shows all overlays previously hidden with `hideOverlays()` again.

**Signature:**
```typescript
screencast.showOverlays(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.screencast.showOverlays();
```

---

### screencast.start(options?)

Starts the screencast recording. Can record a video file and/or
deliver frames via callback at the same time.

**Signature:**
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

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.onFrame` | `Function` | no | — | Callback for every JPEG-encoded frame. Receives `data` (Buffer), `viewportWidth` (number), `viewportHeight` (number) |
| `options.path` | `string` | no | — | File path for the video recording. If given, a video is saved. |
| `options.quality` | `number` | no | — | JPEG image quality between 0 and 100 |
| `options.size` | `Object` | no | — | Dimensions of the recorded frames |
| `options.size.width` | `number` | no | — | Width in pixels |
| `options.size.height` | `number` | no | — | Height in pixels |

**Returns:** `Promise<Disposable>` — on dispose the recording is stopped
(equivalent to `stop()`)

**Example:**
```javascript
// Record a video file
const recording = await page.screencast.start({ path: 'demo.webm', quality: 80 });
await page.goto('https://example.com');
await recording.dispose();

// Frame callback
await page.screencast.start({
  onFrame: ({ data, viewportWidth, viewportHeight }) => {
    // Process the JPEG buffer (e.g. send to a streaming service)
    console.log(`Frame ${viewportWidth}x${viewportHeight}: ${data.length} bytes`);
  },
  size: { width: 1280, height: 720 }
});
```

---

### screencast.stop()

Stops the screencast recording and saves the video (if `path` was given
in `start()`).

**Signature:**
```typescript
screencast.stop(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.screencast.stop();
```

---

## Properties

No public properties.

## Events

No own events.

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods   | 7      |
| Properties | 0     |
| Events    | 0      |

**Summary:** `start()` with `path` offers an alternative to the `recordVideo`
context option with fine-grained control. `showChapter()` and
`showOverlay()` are especially valuable for demo videos and tutorial
recordings. `showActions()` makes clicks and inputs visible to
viewers.

---

*Source: https://playwright.dev/docs/api/class-screencast*
