# Playwright — class: Coverage

> **Manifest:** 4 methods, 0 properties, 0 events.
> Captures JavaScript and CSS code coverage during page execution.
> **Only available in Chromium-based browsers.** Access: `page.coverage`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Complete example (Istanbul integration)](#complete-example-istanbul-integration)
- [Manifest](#manifest)

## Overview

`Coverage` collects information about which parts of JavaScript and
CSS code were actually executed during a session. The
collected data can be converted with tools such as `v8-to-istanbul` into
Istanbul/NYC-compatible coverage reports.

**Important:** Coverage is available exclusively in Chromium/Chrome.
In Firefox and WebKit these APIs are not supported.

---

## Methods

### coverage.startCSSCoverage(options?)

Starts CSS coverage capturing.

**Signature:**
```typescript
coverage.startCSSCoverage(options?: {
  resetOnNavigation?: boolean;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.resetOnNavigation` | `boolean` | no | `true` | Whether the coverage is reset on each navigation |

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.coverage.startCSSCoverage({ resetOnNavigation: false });
await page.goto('https://example.com');
// ... interactions ...
const coverage = await page.coverage.stopCSSCoverage();
```

---

### coverage.startJSCoverage(options?)

Starts JavaScript coverage capturing.

**Signature:**
```typescript
coverage.startJSCoverage(options?: {
  reportAnonymousScripts?: boolean;
  resetOnNavigation?: boolean;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.reportAnonymousScripts` | `boolean` | no | `false` | Capture anonymous scripts (via `eval` or `new Function`); they get the URL `__playwright_evaluation_script__` |
| `options.resetOnNavigation` | `boolean` | no | `true` | Whether the coverage is reset on each navigation |

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.coverage.startJSCoverage({ reportAnonymousScripts: true });
```

---

### coverage.stopCSSCoverage()

Stops CSS coverage capturing and returns the collected data.

**Signature:**
```typescript
coverage.stopCSSCoverage(): Promise<Array<{
  url: string;
  text?: string;
  ranges: Array<{
    start: number;
    end: number;
  }>;
}>>
```

**Parameters:** None

**Returns:** `Promise<Array<CSSCoverageEntry>>` with:

| Field | Type | Description |
|------|-----|--------------|
| `url` | `string` | URL of the stylesheet |
| `text` | `string` (optional) | Stylesheet content (if available) |
| `ranges` | `Array<{start, end}>` | Used ranges (sorted, non-overlapping) |
| `ranges[].start` | `number` | Inclusive text offset (characters) |
| `ranges[].end` | `number` | Exclusive text offset (characters) |

**Note:** Dynamically injected styles without a `sourceURL` are not
captured.

**Example:**
```javascript
const cssCoverage = await page.coverage.stopCSSCoverage();
for (const entry of cssCoverage) {
  const totalChars = entry.text?.length ?? 0;
  const usedChars = entry.ranges.reduce((acc, r) => acc + (r.end - r.start), 0);
  const pct = totalChars > 0 ? (usedChars / totalChars * 100).toFixed(1) : 'N/A';
  console.log(`${entry.url}: ${pct}% CSS used`);
}
```

---

### coverage.stopJSCoverage()

Stops JavaScript coverage capturing and returns the data in V8
format.

**Signature:**
```typescript
coverage.stopJSCoverage(): Promise<Array<{
  url: string;
  scriptId: string;
  source?: string;
  functions: Array<{
    functionName: string;
    isBlockCoverage: boolean;
    ranges: Array<{
      count: number;
      startOffset: number;
      endOffset: number;
    }>;
  }>;
}>>
```

**Parameters:** None

**Returns:** `Promise<Array<JSCoverageEntry>>` with:

| Field | Type | Description |
|------|-----|--------------|
| `url` | `string` | Script URL |
| `scriptId` | `string` | Internal script ID of the browser |
| `source` | `string` (optional) | Script source code (if available) |
| `functions` | `Array<...>` | V8 coverage data per function |
| `functions[].functionName` | `string` | Function name (empty for anonymous) |
| `functions[].isBlockCoverage` | `boolean` | Whether block coverage or line coverage |
| `functions[].ranges` | `Array<...>` | Coverage ranges |
| `functions[].ranges[].count` | `number` | Execution counter |
| `functions[].ranges[].startOffset` | `number` | Start offset in the source code |
| `functions[].ranges[].endOffset` | `number` | End offset in the source code |

**Note:** Anonymous scripts are excluded unless
`reportAnonymousScripts: true` was set.

---

## Complete example (Istanbul integration)

```javascript
const { chromium } = require('playwright');
const v8toIstanbul = require('v8-to-istanbul');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.coverage.startJSCoverage();
  await page.goto('https://chromium.org');
  // ... interactions ...
  const jsCoverage = await page.coverage.stopJSCoverage();

  for (const entry of jsCoverage) {
    const converter = v8toIstanbul('', 0, { source: entry.source });
    await converter.load();
    converter.applyCoverage(entry.functions);
    console.log(JSON.stringify(converter.toIstanbul()));
  }

  await browser.close();
})();
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods   | 4      |
| Properties | 0     |
| Events    | 0      |

**Summary:** The coverage API delivers V8-native coverage data suitable for modern
code-coverage reports. For CSS optimizations (removing unused CSS)
`stopCSSCoverage()` is particularly valuable. The data must be
converted externally (e.g. via `v8-to-istanbul`), since Playwright itself
generates no coverage reports.

---

*Source: https://playwright.dev/docs/api/class-coverage*
