# class-pageassertions — Playwright API Reference

`PageAssertions` is the assertion class for `Page` objects. All matchers retry automatically. Default timeout: `TestConfig.expect` (default 5000 ms).

Accessed via `expect(page).*`.

Matcher count: 6 matchers + property `not`

---

## Contents

- [not](#not)
- [toHaveScreenshot() — with name](#tohavescreenshot-with-name)
- [toHaveScreenshot() — automatic](#tohavescreenshot-automatic)
- [toHaveTitle()](#tohavetitle)
- [toHaveURL()](#tohaveurl)
- [toMatchAriaSnapshot() — inline](#tomatchariasnapshot-inline)
- [toMatchAriaSnapshot() — stored](#tomatchariasnapshot-stored)
- [Matcher overview (6 matchers)](#matcher-overview-6-matchers)

## not

```typescript
not: PageAssertions
```

Inverts the following assertion.

```typescript
await expect(page).not.toHaveURL('/error');
```

---

## toHaveScreenshot() — with name

```typescript
toHaveScreenshot(
  name: string | string[],
  options?: {
    animations?: 'disabled' | 'allow';
    caret?: 'hide' | 'initial';
    clip?: { x: number; y: number; width: number; height: number };
    fullPage?: boolean;
    mask?: Locator[];
    maskColor?: string;
    maxDiffPixelRatio?: number;
    maxDiffPixels?: number;
    omitBackground?: boolean;
    scale?: 'css' | 'device';
    stylePath?: string | string[];
    threshold?: number;
    timeout?: number;
  }
): Promise<void>
```

Compares a page screenshot against a stored snapshot. Waits for consecutive identical screenshots before comparing.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string \| string[]` | yes | — | Snapshot file name or path segments |
| `options.animations` | `'disabled' \| 'allow'` | no | `'disabled'` | How to handle CSS animations |
| `options.caret` | `'hide' \| 'initial'` | no | `'hide'` | Text cursor visibility |
| `options.clip` | `{ x; y; width; height }` | no | whole page | Region of the screenshot |
| `options.fullPage` | `boolean` | no | `false` | Capture the full scrollable page |
| `options.mask` | `Locator[]` | no | `[]` | Elements to mask |
| `options.maskColor` | `string` | no | `'#FF00FF'` | Color used for masking |
| `options.maxDiffPixelRatio` | `number` | no | from config | Maximum ratio of differing pixels (0-1) |
| `options.maxDiffPixels` | `number` | no | from config | Maximum number of differing pixels |
| `options.omitBackground` | `boolean` | no | `false` | Transparent background (PNG only) |
| `options.scale` | `'css' \| 'device'` | no | `'css'` | Pixel unit of measurement |
| `options.stylePath` | `string \| string[]` | no | — | Additional CSS files |
| `options.threshold` | `number` | no | `0.2` | Color difference threshold (YIQ, 0-1) |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page).toHaveScreenshot('startseite.png');
await expect(page).toHaveScreenshot('full.png', {
  fullPage: true,
  maxDiffPixelRatio: 0.02,
  mask: [page.locator('.live-clock')],
});
```

---

## toHaveScreenshot() — automatic

```typescript
toHaveScreenshot(options?: {
  animations?: 'disabled' | 'allow';
  caret?: 'hide' | 'initial';
  clip?: { x: number; y: number; width: number; height: number };
  fullPage?: boolean;
  mask?: Locator[];
  maskColor?: string;
  maxDiffPixelRatio?: number;
  maxDiffPixels?: number;
  omitBackground?: boolean;
  scale?: 'css' | 'device';
  stylePath?: string | string[];
  threshold?: number;
  timeout?: number;
}): Promise<void>
```

As above, but the snapshot name is generated automatically from the test name + a counter.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| all `options.*` | — | no | — | Identical to the named variant (without `name`) |

**Returns:** `Promise<void>`

```typescript
await expect(page).toHaveScreenshot({ fullPage: true });
```

---

## toHaveTitle()

```typescript
toHaveTitle(
  titleOrRegExp: string | RegExp,
  options?: { timeout?: number }
): Promise<void>
```

Checks the title of the current page.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `titleOrRegExp` | `string \| RegExp` | yes | — | Expected title (exact string or regex) |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page).toHaveTitle('My App - Dashboard');
await expect(page).toHaveTitle(/Dashboard/);
```

---

## toHaveURL()

```typescript
toHaveURL(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Checks the page's current URL.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `url` | `string \| RegExp \| URLPattern \| ((url: URL) => boolean)` | yes | — | Expected URL: exact string, regex, URLPattern or predicate function |
| `options.ignoreCase` | `boolean` | no | `false` | Ignore case (string only) |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page).toHaveURL('/dashboard');
await expect(page).toHaveURL(/\/user\/\d+/);
await expect(page).toHaveURL(url => url.searchParams.has('token'));
```

---

## toMatchAriaSnapshot() — inline

```typescript
toMatchAriaSnapshot(
  expected: string,
  options?: { timeout?: number }
): Promise<void>
```

Checks whether the page's `<body>` matches the given ARIA snapshot.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string` | yes | — | ARIA snapshot as a YAML string |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page).toMatchAriaSnapshot(`
  - heading "Welcome" [level=1]
  - link "Sign in"
`);
```

---

## toMatchAriaSnapshot() — stored

```typescript
toMatchAriaSnapshot(options?: {
  name?: string;
  timeout?: number;
}): Promise<void>
```

Compares against a stored `.aria.yml` file. If `name` is missing, the name is generated automatically.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.name` | `string` | no | auto | File name of the snapshot file |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page).toMatchAriaSnapshot({ name: 'homepage.aria.yml' });
```

---

## Matcher overview (6 matchers)

| Matcher | Checks |
|---|---|
| `toHaveScreenshot` (2x) | Visual page comparison against a stored baseline screenshot |
| `toHaveTitle` | `document.title` |
| `toHaveURL` | Current page URL |
| `toMatchAriaSnapshot` (2x) | ARIA tree of the `<body>` |

---

Source: https://playwright.dev/docs/api/class-pageassertions
