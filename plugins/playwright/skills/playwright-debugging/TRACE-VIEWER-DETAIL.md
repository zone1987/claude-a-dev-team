# Playwright Trace Viewer & Debugging

## Contents

- [Recording traces](#recording-traces)
- [Opening the Trace Viewer](#opening-the-trace-viewer)
- [Trace Viewer: UI tabs and features](#trace-viewer-ui-tabs-and-features)
- [Playwright Inspector](#playwright-inspector)
- [VS Code Debugger](#vs-code-debugger)
- [PWDEBUG: browser console API](#pwdebug-browser-console-api)
- [Further debugging methods](#further-debugging-methods)
- [Source](#source)

## Recording traces

### Configuration in `playwright.config.ts`

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  retries: 1,
  use: {
    // Choose the trace mode:
    trace: 'on-first-retry',
  },
});
```

### Trace options

| Value | Behavior |
|------|-----------|
| `'off'` | No trace |
| `'on'` | Every test (performance-intensive) |
| `'retain-on-failure'` | Trace for every test, deletes the passing ones at the end |
| `'on-first-retry'` | Only on the first retry (recommended for CI) |
| `'on-all-retries'` | All retry attempts |

### Forcing a trace from the CLI (locally)

```bash
npx playwright test --trace on
npx playwright show-report
```

### Traces via the library API (without the test runner)

```typescript
const context = await browser.newContext();

// Start the trace
await context.tracing.start({
  screenshots: true,   // Screenshots in the timeline
  snapshots: true,     // DOM snapshots for every action
  sources: true,       // Source-code lines
});

const page = await context.newPage();
await page.goto('https://example.com');

// Stop the trace and save it
await context.tracing.stop({ path: 'trace.zip' });
```

### `tracing.start()` options

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `screenshots` | boolean | false | Record film-strip screenshots |
| `snapshots` | boolean | false | DOM snapshots before/after every action |
| `sources` | boolean | false | Include source-code lines |
| `title` | string | — | Optional title for the trace |

### HAR recording (from v1.60)

```typescript
await context.tracing.startHar({ path: 'network.har' });
// ... run the test ...
await context.tracing.stopHar({ path: 'network.har' });
```

---

## Opening the Trace Viewer

### From the CLI (locally)

```bash
# Local ZIP file
npx playwright show-trace path/to/trace.zip

# Remote URL
npx playwright show-trace https://example.com/trace.zip
```

### From the HTML report

```bash
npx playwright show-report
```
In the report: click the trace icon next to the test file name.

### From the web interface

URL: **https://trace.playwright.dev**

- No external data transfer (statically hosted)
- Upload by drag-and-drop or file picker
- Remote trace: `https://trace.playwright.dev/?trace=https://example.com/trace.zip`

---

## Trace Viewer: UI tabs and features

| Tab | Content |
|-----|--------|
| **Actions** | Action list with locators, timing, DOM snapshots (before/after) |
| **Screenshots** | Film strip with a magnified timeline |
| **Snapshots** | DOM state: before / action / after |
| **Source** | Highlighted line of code |
| **Call** | Action duration, locator, strict-mode information |
| **Log** | Detailed action sequence (scrolling, waiting, clicking) |
| **Errors** | Error messages with a timeline marker |
| **Console** | Browser and test logs with source attribution |
| **Network** | Requests filterable by type/status/method/duration |
| **Metadata** | Browser, viewport, test duration |
| **Attachments** | Visual-regression comparisons with a slider |

### Interactions in the viewer

- Double-click an action -> filter the time range
- Timeline slider to select action ranges
- Hover the film strip for a magnified preview
- "Show all" to reset filters

---

## Playwright Inspector

### Starting it

```bash
# Debug all tests
npx playwright test --debug

# A single test by file and line
npx playwright test example.spec.ts:10 --debug

# A specific browser
npx playwright test --project=chromium --debug

# Combined
npx playwright test example.spec.ts:10 --project=webkit --debug
```

### Inspector features

- **Playback controls**: step forward/back, play, pause
- **Current step**: highlighted in the inspector and in the browser
- **Pick Locator**: interactive element selection with real-time highlighting
- **Locator editor**: edit the locator live
- **Actionability log**: shows visibility, stability, whether a scroll is needed

### Breakpoints in code

```typescript
// The test halts at this point
await page.pause();
```

---

## VS Code Debugger

### Prerequisites

- Install the VS Code extension "Playwright Test for VS Code"

### Features

- Set breakpoints as red dots by clicking the line numbers
- Right-click a test line -> "Debug Test" launches the browser and stops at breakpoints
- **Live locator picking**: click locators in the VS Code panel -> browser highlight
- **Multi-browser debugging**: right-click the debug icon -> "Select Default Profile" -> Chromium/Firefox/WebKit/Mobile
- **Chrome DevTools**: keep working with "Show Browser" plus open DevTools

---

## PWDEBUG: browser console API

### Enabling it

```bash
# Exposes the `playwright` object in the browser console
PWDEBUG=console npx playwright test

# Opens the Playwright Inspector
PWDEBUG=1 npx playwright test
```

### The `playwright` object in the console

| Method | Description |
|---------|--------------|
| `playwright.$(selector)` | Query the first element with the Playwright engine |
| `playwright.$$(selector)` | Return all matches |
| `playwright.inspect(selector)` | Highlight the element in the Elements panel |
| `playwright.locator(selector)` | Create a locator with matching information |
| `playwright.selector(element)` | Generate a selector for a DOM element |

Prerequisite: insert `await page.pause();` before the test run.

---

## Further debugging methods

### Verbose logging

```bash
# Log all API calls
DEBUG=pw:api npx playwright test

# Browser-specific
DEBUG=pw:browser npx playwright test
```

### Headed mode + slowMo

```typescript
const browser = await chromium.launch({
  headless: false,
  slowMo: 100,  // Slow every action down by 100 ms
});
```

### Headed via config

```typescript
export default defineConfig({
  use: {
    headless: false,
    launchOptions: {
      slowMo: 100,
    },
  },
});
```

---

## Source

- https://playwright.dev/docs/trace-viewer
- https://playwright.dev/docs/trace-viewer-intro
- https://playwright.dev/docs/debug
