# Playwright: extensions, videos and release channels

## Contents

- [Custom Selector Engines (Extensibility)](#custom-selector-engines-extensibility)
- [Video recording](#video-recording)
- [Release channels](#release-channels)
- [Current release highlights](#current-release-highlights)
- [Sources](#sources)

## Custom Selector Engines (Extensibility)

### `selectors.register()`

Registers a custom selector engine before page initialization.

```typescript
// tests/fixtures.ts
import { test as base, selectors } from '@playwright/test';

export const test = base.extend({
  // Worker-scoped fixture for selector registration
  selectorsRegistered: [async ({}, use) => {
    // Register the selector engine
    await selectors.register('tag', () => ({
      query(root, selector) {
        return root.querySelector(selector);
      },
      queryAll(root, selector) {
        return Array.from(root.querySelectorAll(selector));
      },
    }));
    await use(true);
  }, { scope: 'worker', auto: true }],
});
```

### Signature

```typescript
await playwright.selectors.register(
  engineName: string,
  createEngineFunction: () => SelectorEngine,
  options?: { contentScript?: boolean }
);
```

### Parameters

| Parameter | Type | Description |
|-----------|-----|--------------|
| `engineName` | `string` | Prefix for selectors (e.g. `'tag'` -> `tag=button`) |
| `createEngineFunction` | `() => SelectorEngine` | Function that returns the engine instance |
| `options.contentScript` | `boolean` | `true`: isolated from the frame JavaScript (safer, like the built-ins) |

### SelectorEngine interface

```typescript
interface SelectorEngine {
  // Return the first matching element in the root subtree
  query(root: Element, selector: string): Element | null;

  // Return all matching elements in the root subtree
  queryAll(root: Element, selector: string): Element[];
}
```

### Usage

```typescript
// Use the registered selector
await page.locator('tag=button').click();

// Combined with built-in locators
await page.locator('tag=article').getByText('Playwright').click();
await page.locator('tag=input').filter({ hasText: 'Name' }).fill('Alice');

// Assertions
await expect(page.locator('tag=li')).toHaveCount(3);
```

### Notes

- Registration must happen before page initialization
- `contentScript: true` recommended for production-like behavior
- Engines run in the frame's JavaScript context by default

---

## Video recording

### Configuration in `playwright.config.ts`

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    video: 'on-first-retry',
  },
});
```

### Video options

| Value | Behavior |
|------|-----------|
| `'off'` | No video recording |
| `'on'` | Every test |
| `'retain-on-failure'` | Record, but delete successes |
| `'on-first-retry'` | Only on the first retry |

### Advanced video configuration

```typescript
export default defineConfig({
  use: {
    video: {
      mode: 'on',
      size: { width: 1280, height: 720 },
      // Overlay action annotations (from v1.59)
      show: {
        actions: {
          duration: 500,        // Display duration in ms (default: 500)
          position: 'top-right', // Position on the video
          fontSize: 14,          // Font size
        },
        test: {
          level: 'step',        // Verbosity: 'step', 'test', 'suite'
          position: 'top-left',
          fontSize: 12,
        },
      },
    },
  },
});
```

### Retrieving the video path

```typescript
test('example', async ({ page }) => {
  await page.goto('https://example.com');
  // ... test actions
});

// After the test completes (context/page must be closed):
const path = await page.video().path();
console.log('Video saved at:', path);
```

Important: only call `page.video().path()` after closing the page or context.

### Notes

- Videos are saved in the `test-results/` directory
- Default scaling: max 800x800 with the viewport at the top left
- Format: WebM
- `page.screencast` API (v1.59): streaming, chapter titles, action annotations

---

## Release channels

### NPM dist tags

| Tag | Content |
|-----|--------|
| `latest` | Stable releases |
| `next` | Daily canary releases from the `main` branch |
| `beta` | Beta releases (approx. one week before stable) |

### Installation per channel

```bash
# Stable (default)
npm install -D @playwright/test

# Canary (daily)
npm install -D @playwright/test@next

# Beta
npm install -D @playwright/test@beta
```

### Canary characteristics

- Are published daily (on code commits to `main`)
- Pass all automated tests including HTML report, Trace Viewer, Inspector
- Enables feedback to the maintainers before the stable release
- Docs at `/docs/next/...` (press Shift 5x on playwright.dev)

---

## Current release highlights

### v1.60
- HAR recording as a first-class API: `tracing.startHar()` / `tracing.stopHar()`
- `locator.drop()` for drag-and-drop with files or clipboard data
- `expect(page).toMatchAriaSnapshot()` directly on pages
- `test.abort()` for failing from fixtures or route handlers
- Browser lifecycle events: `browser.on('context')`
- Breaking changes: `Locator.ariaRef()`, `videosPath`/`videoSize`, logger configuration removed

### v1.59
- `page.screencast` API: video with action annotations, chapter titles and frame streaming
- `browser.bind()`: launched browsers accept connections from multiple clients
- `page.ariaSnapshot()`, `locator.normalize()`, `page.pickLocator()`
- `browserContext.setStorageState()`: reset storage without a new context
- `await using` syntax for automatic resource cleanup
- Breaking: macOS 14 removed for WebKit; `@playwright/experimental-ct-svelte` removed

### v1.58
- HTML reporter timeline tab for merged reports
- UI mode: system theme follows the OS settings
- Trace Viewer network panel with JSON formatting
- `browserType.connectOverCDP()` with an `isLocal` option

### v1.57
- Playwright now uses Chrome for Testing (instead of Chromium)
- `testConfig.webServer.wait`: regex pattern for log matching
- `page.accessibility` removed after three years of deprecation

### v1.56
- Playwright Test Agents: planner, generator and healer agents for LLM-guided tests
- `page.consoleMessages()`, `page.pageErrors()`, `page.requests()`

---

## Sources

- https://playwright.dev/docs/extensibility
- https://playwright.dev/docs/videos
- https://playwright.dev/docs/canary-releases
- https://playwright.dev/docs/release-notes
