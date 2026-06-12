# class-teststepinfo — Playwright TestStepInfo Reference

`TestStepInfo` is injected as the first argument of a `test.step()` body function. It
provides step-level control (skip, attach) analogous to what `TestInfo` provides at test level.

```ts
test('upload flow', async ({ page }) => {
  await test.step('Upload file', async (step) => {
    await page.setInputFiles('#upload', 'file.pdf');
    await step.attach('uploaded file', {
      path: 'file.pdf',
      contentType: 'application/pdf',
    });
  });
});
```

---

## Methods

### `attach(name, options?)`

Attach a file or buffer to the current step (rather than the top-level test).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | `string` | yes | Attachment label |
| `options.body` | `string \| Buffer` | no* | Inline content; mutually exclusive with `path` |
| `options.path` | `string` | no* | Filesystem path; mutually exclusive with `body` |
| `options.contentType` | `string` | no | MIME type; inferred or defaults to `text/plain` |

*One of `body` or `path` is required.

**Returns:** `Promise<void>`

```ts
await step.attach('api-response', {
  body: JSON.stringify(responseData),
  contentType: 'application/json',
});
```

---

### `skip()`
### `skip(condition, description?)`

Abort the current step and mark it as skipped.

| Signature | Parameters | Description |
|-----------|------------|-------------|
| `skip()` | — | Unconditionally skip and abort |
| `skip(condition)` | `condition: boolean` | Skip when condition is truthy |
| `skip(condition, description)` | `condition: boolean`, `description: string` | Skip with reason shown in report |

**Returns:** `void`

```ts
await test.step('Verify email notification', async (step) => {
  step.skip(!process.env.SMTP_HOST, 'SMTP not configured in this environment');
  // continues only when SMTP_HOST is set
  await expect(mailbox).toHaveMessage('Welcome');
});
```

---

## Properties

### `titlePath`

| Type | Description |
|------|-------------|
| `Array<string>` | Full title path starting with the test file name, through all parent steps, down to this step's title |

```ts
await test.step('Outer', async (outerStep) => {
  await test.step('Inner', async (innerStep) => {
    console.log(innerStep.titlePath);
    // e.g. ['tests/my.spec.ts', 'my test', 'Outer', 'Inner']
  });
});
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 2 (`attach`, `skip`) |
| Properties | 1 (`titlePath`) |

**Fazit:** `TestStepInfo` ist bewusst schlank. Es bietet nur das, was auf Step-Ebene sinnvoll
ist: Artefakte anhaengen (`attach`) und den Step abbrechen (`skip`). Das `titlePath`-Property
erlaubt die Positionsbestimmung innerhalb der Step-Hierarchie.

---

Source: https://playwright.dev/docs/api/class-teststepinfo
