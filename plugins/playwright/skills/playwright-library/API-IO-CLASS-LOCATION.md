# Playwright — class: Location

> **Manifest:** 0 methods, 3 properties, 0 events.
> Represents a source code location (file, line, column) in Playwright Test.
> Used as a return type and parameter in various APIs.

---

## Contents

- [Overview](#overview)
- [Properties](#properties)
- [Usage as an interface](#usage-as-an-interface)
- [Complete example](#complete-example)
- [Manifest](#manifest)

## Overview

`Location` is a simple data interface without methods. It describes
where a test file, a test suite or a test case is defined in the source
code. It appears as a property on `TestCase`, `Suite`, `TestResult` as well as
a parameter in tracing APIs.

---

## Properties

### location.file

Path to the source file.

**Type:** `string`

**Added:** v1.10

**Example:**
```javascript
console.log(testCase.location.file);
// e.g. "/home/user/tests/login.spec.ts"
```

---

### location.line

Line number in the source file.

**Type:** `number`

**Added:** v1.10

**Note:** 1-based in most contexts, but in some APIs
(e.g. `ConsoleMessage.location()`) 0-based. Check the context.

**Example:**
```javascript
console.log(testCase.location.line); // e.g. 42
```

---

### location.column

Column number in the source file.

**Type:** `number`

**Added:** v1.10

**Note:** As with `line` — indexing depends on the calling context.

**Example:**
```javascript
console.log(testCase.location.column); // e.g. 5
```

---

## Usage as an interface

`Location` appears in the following APIs:

### As a property:
- `TestCase.location` — where the test is defined
- `Suite.location` — where the suite is defined

### As a return type:
- `ConsoleMessage.location()` — location of the `console.*()` call (0-based)
- `WebError.location()` — location of the unhandled error (0-based)
- `Debugger.pausedDetails()` — current pause location

### As a parameter:
- `tracing.group(name, { location })` — source location mapping for the trace group
- `debugger.runTo(location)` — target location for conditional pausing

---

## Complete example

```javascript
// In a reporter
class MyReporter {
  onTestBegin(test) {
    const loc = test.location;
    console.log(`Test "${test.title}" in ${loc.file}:${loc.line}:${loc.column}`);
  }
}

// In tracing
await context.tracing.group('My step', {
  location: {
    file: '/tests/login.spec.ts',
    line: 45,
    column: 3
  }
});
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 0      |
| Properties | 3 (file, line, column) |
| Events    | 0      |

**Conclusion:** `Location` is a pure data transfer object without logic.
It links runtime information with source code positions and is
central to reporter, tracing and debugger integrations. The indexing
(0- vs. 1-based) varies with the API context — always check the
respective API documentation.

---

*Source: https://playwright.dev/docs/api/class-location*
