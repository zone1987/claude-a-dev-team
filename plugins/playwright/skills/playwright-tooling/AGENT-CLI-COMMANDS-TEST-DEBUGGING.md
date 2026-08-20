# Playwright Agent CLI — Test Debugging

## Contents

- [Command overview](#command-overview)
- [Starting a test in debug mode](#starting-a-test-in-debug-mode)
- [attach (test debugging mode)](#attach-test-debugging-mode)
- [Exploring the page state](#exploring-the-page-state)
- [Execution control](#execution-control)
- [Complete debugging workflow](#complete-debugging-workflow)
- [Investigating a flaky test](#investigating-a-flaky-test)

## Command overview

| Command | Description |
|--------|-------------|
| `pause-at <file>:<line>` | Set a breakpoint at a specific line |
| `resume` | Resume test execution |
| `step-over` | Advance to the next action |
| `attach <session-name>` | Connect to a paused test |

---

## Starting a test in debug mode

```bash
npx playwright test --debug=cli
# Output: Session name: pw-debug-session-abc123
```

Starts the test paused and prints the session name the CLI can connect with.

---

## attach (test debugging mode)

```bash
playwright-cli attach pw-debug-session-abc123
```

### attach arguments (test mode)

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<session-name>` | string | Yes | Session name from the `--debug=cli` output |

---

## Exploring the page state

Once connected, all normal commands are available:

| Command | Purpose |
|--------|-------|
| `playwright-cli snapshot` | View the current page state |
| `playwright-cli console error` | Check for errors |
| `playwright-cli eval "() => document.title"` | Execute JavaScript |
| `playwright-cli screenshot --filename=debug-state.png` | Take a screenshot |
| `playwright-cli network` | Inspect network requests |

---

## Execution control

| Command | Type | Description |
|--------|-----|-------------|
| `resume` | — | Resume test execution |
| `step-over` | — | Advance to the next action |
| `pause-at <file>:<line>` | string | Breakpoint at a specific test file line |

### pause-at arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<file>:<line>` | string | Yes | File path and line number (e.g. `test.ts:42`) |

---

## Complete debugging workflow

### 1. Start the test with the debug flag

```bash
npx playwright test --debug=cli tests/checkout.spec.ts
# Output: Connect with: playwright-cli attach pw-debug-abc123
```

### 2. Connect the CLI in a separate terminal

```bash
playwright-cli attach pw-debug-abc123
```

### 3. Inspect the page state

```bash
playwright-cli snapshot
playwright-cli console error
playwright-cli network
```

### 4. Start tracing for analysis

```bash
playwright-cli tracing-start
```

### 5. Step through the execution

```bash
playwright-cli step-over              # Next action
playwright-cli step-over              # Next action
playwright-cli snapshot               # Check the state after the actions
playwright-cli console                # Check messages
```

### 6. Navigate to the failure point

```bash
playwright-cli pause-at test.ts:42   # Set a breakpoint
playwright-cli resume                 # Run up to it
playwright-cli snapshot               # Page state at the failure
playwright-cli screenshot --filename=failure-point.png
```

### 7. Save the trace

```bash
playwright-cli tracing-stop
npx playwright show-trace .playwright-cli/trace.zip
```

---

## Investigating a flaky test

```bash
# Run the test repeatedly with the debug flag
npx playwright test --debug=cli --repeat-each=3 tests/flaky.spec.ts

playwright-cli attach <session>
playwright-cli tracing-start
playwright-cli step-over
playwright-cli step-over
playwright-cli console
playwright-cli network
playwright-cli tracing-stop
```

---

Source: https://playwright.dev/agent-cli/commands/test-debugging
