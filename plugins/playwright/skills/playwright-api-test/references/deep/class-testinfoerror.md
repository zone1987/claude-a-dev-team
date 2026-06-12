# class-testinfoerror — Playwright TestInfoError Reference

`TestInfoError` describes a single error that occurred during test execution. It is the type
of `testInfo.error` and each element in `testInfo.errors`.

It differs from `TestError` (used in the Reporter API) in that it is scoped to the running
test's `TestInfo` rather than post-run reporting.

---

## Properties

### `cause`

| Type | Added | Description |
|------|-------|-------------|
| `TestInfoError \| undefined` | v1.49 | The underlying cause of this error, if the thrown Error had a `.cause` property that was itself an Error instance. `undefined` when no cause exists or cause is not an Error. |

```ts
// caught in afterEach
if (testInfo.error?.cause) {
  console.log('Root cause:', testInfo.error.cause.message);
}
```

---

### `errorContext`

| Type | Added | Description |
|------|-------|-------------|
| `string \| undefined` | v1.60 | Additional context about the error — for example the ARIA snapshot of the element at the time an `expect()` matcher failed. |

---

### `message`

| Type | Added | Description |
|------|-------|-------------|
| `string \| undefined` | v1.10 | Error message. Set when an `Error` (or subclass) was thrown. `undefined` when a non-Error value was thrown (see `value`). |

```ts
if (testInfo.error?.message?.includes('ENOENT')) {
  console.warn('Missing file during test');
}
```

---

### `stack`

| Type | Added | Description |
|------|-------|-------------|
| `string \| undefined` | v1.10 | Full stack trace. Set when an `Error` (or subclass) was thrown. |

---

### `value`

| Type | Added | Description |
|------|-------|-------------|
| `string \| undefined` | v1.10 | The stringified thrown value when something other than an `Error` was thrown (e.g. a plain string or number). |

```ts
// throw 'something went wrong'; → testInfo.error.value === 'something went wrong'
```

---

## Usage Examples

```ts
test.afterEach(async ({}, testInfo) => {
  if (testInfo.status !== testInfo.expectedStatus) {
    const err = testInfo.error;
    if (err) {
      console.log('Error message:', err.message);
      console.log('Stack:', err.stack);
      if (err.errorContext) console.log('Context:', err.errorContext);
    }
  }
});
```

---

## Manifest

| Category | Count |
|----------|-------|
| Properties | 5 (`cause`, `errorContext`, `message`, `stack`, `value`) |
| Methods | 0 |

**Fazit:** `TestInfoError` ist ein einfaches Daten-Objekt mit fuenf optionalen Properties.
`message` und `stack` decken den Standardfall (Error-Instanz) ab; `value` behandelt primitive
Throws; `errorContext` (v1.60) liefert zusaetzlichen UI-Kontext bei Assertion-Fehlern.

---

Source: https://playwright.dev/docs/api/class-testinfoerror
