# class-suite — Playwright Suite Reference

`Suite` is the tree node in the Reporter API that groups tests. The root `Suite` passed to
`reporter.onBegin()` contains the entire test hierarchy.

Hierarchy levels: **root** → **project** → **file** → **describe** → (TestCase)

```ts
import { Reporter, Suite } from '@playwright/test/reporter';

class MyReporter implements Reporter {
  onBegin(config, rootSuite: Suite) {
    for (const projectSuite of rootSuite.suites) {
      console.log('Project:', projectSuite.title);
    }
  }
}
```

---

## Methods

### `allTests()`

Returns a flat list of all `TestCase` instances in this suite and all its descendants.

**Returns:** `Array<TestCase>`

```ts
const all = rootSuite.allTests();
console.log(`Total tests: ${all.length}`);
```

---

### `entries()`

Returns direct children in declaration order — both `TestCase` and `Suite` instances.
Use `entry.type` to discriminate (`"test"` or `"root" | "project" | "file" | "describe"`).

**Returns:** `Array<TestCase \| Suite>`

Added in: v1.44

```ts
for (const entry of fileSuite.entries()) {
  if (entry.type === 'test') {
    console.log('Test:', entry.title);
  } else {
    console.log('Describe:', entry.title);
  }
}
```

---

### `project()`

Returns the `FullProject` configuration this suite belongs to.

**Returns:** `FullProject \| undefined`

- `undefined` for the root suite.
- The same `FullProject` for all suites inside a project.

```ts
const proj = fileSuite.project();
if (proj) console.log(proj.name);
```

---

### `titlePath()`

Returns the list of titles from the root suite down to this suite.

**Returns:** `Array<string>`

```ts
console.log(describeSuite.titlePath().join(' > '));
// e.g. '' > 'chromium' > 'tests/auth.spec.ts' > 'Login'
```

---

## Properties

### `location`

| Type | Description |
|------|-------------|
| `Location \| undefined` | Source code position of the suite declaration; `undefined` for root and project suites |

`Location` shape: `{ file: string, line: number, column: number }`

---

### `parent`

| Type | Description |
|------|-------------|
| `Suite \| undefined` | Parent suite in the hierarchy; `undefined` for the root suite |

---

### `suites`

| Type | Description |
|------|-------------|
| `Array<Suite>` | Direct child suites (not test cases) |

---

### `tests`

| Type | Description |
|------|-------------|
| `Array<TestCase>` | Test cases directly in this suite (excludes tests nested inside child suites) |

---

### `title`

| Type | Description |
|------|-------------|
| `string` | Suite title; empty string for the root suite; project name for project suites; file path for file suites; `describe` title for describe suites |

---

### `type`

| Type | Description |
|------|-------------|
| `"root" \| "project" \| "file" \| "describe"` | Suite level in the hierarchy; useful for routing logic in reporters |

---

## Traversal Patterns

### Recursive depth-first traversal

```ts
function traverse(suite: Suite, depth = 0): void {
  const indent = '  '.repeat(depth);
  console.log(`${indent}[${suite.type}] ${suite.title}`);
  for (const test of suite.tests) {
    console.log(`${indent}  - ${test.title}`);
  }
  for (const child of suite.suites) {
    traverse(child, depth + 1);
  }
}
traverse(rootSuite);
```

### Collect all tests for a given project

```ts
const chromiumProject = rootSuite.suites.find(s => s.title === 'chromium');
const tests = chromiumProject?.allTests() ?? [];
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 4 (`allTests`, `entries`, `project`, `titlePath`) |
| Properties | 6 (`location`, `parent`, `suites`, `tests`, `title`, `type`) |

**Fazit:** `Suite` bildet die vollstaendige Baumstruktur aller Tests ab. `allTests()` liefert
eine flache Liste fuer einfache Iteration; `entries()` und `suites` erlauben strukturtreue
Traversal. Das `type`-Property ist der zuverlaessige Diskriminator fuer die vier Hierarchieebenen.

---

Source: https://playwright.dev/docs/api/class-suite
