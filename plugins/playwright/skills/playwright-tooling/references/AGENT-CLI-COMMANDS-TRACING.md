# Playwright Agent CLI — Tracing

## Contents

- [Command overview](#command-overview)
- [tracing-start](#tracing-start)
- [tracing-stop](#tracing-stop)
- [Viewing a trace](#viewing-a-trace)
- [Basic workflow](#basic-workflow)
- [Debugging workflow](#debugging-workflow)
- [Automatic session recording](#automatic-session-recording)
- [When to use tracing](#when-to-use-tracing)

## Command overview

| Command | Description |
|--------|-------------|
| `tracing-start` | Start trace recording |
| `tracing-stop` | Stop trace recording and save it |

---

## tracing-start

```bash
playwright-cli tracing-start
```

No arguments. Starts recording all actions, DOM snapshots, network requests
and timing information.

---

## tracing-stop

```bash
playwright-cli tracing-stop
# Trace saved to .playwright-cli/trace.zip
```

No arguments. Stops the recording and saves it as a ZIP file.

---

## Viewing a trace

```bash
npx playwright show-trace .playwright-cli/trace.zip
```

The Trace Viewer shows:

| Information | Description |
|-------------|-------------|
| Action timeline | Chronological list of all executed actions |
| DOM snapshots | Page state before and after each action |
| Screenshots | Visual reference for every step |
| Network requests | All HTTP requests and responses |
| Console messages | Browser console output |
| Timing information | Duration of each action |

---

## Basic workflow

```bash
playwright-cli tracing-start
playwright-cli goto https://example.com
playwright-cli click e5
playwright-cli fill e3 "test"
playwright-cli tracing-stop
# Trace saved to .playwright-cli/trace.zip

npx playwright show-trace .playwright-cli/trace.zip
```

---

## Debugging workflow

```bash
playwright-cli tracing-start
playwright-cli goto https://store.example.com/checkout
playwright-cli fill e10 "4111111111111111"
playwright-cli click e15
playwright-cli snapshot
playwright-cli console error
playwright-cli tracing-stop
# Provide the trace for team analysis
```

---

## Automatic session recording

Trace sessions automatically without manual commands:

```bash
playwright-cli --save-session
```

Automatically records traces for every session without manual intervention.

---

## When to use tracing

- Debugging non-reproducible errors
- Capturing the execution context for team analysis
- Diagnosing timing problems
- Documenting network requests on failures
- Analyzing CI failures in Playwright tests

---

Source: https://playwright.dev/agent-cli/commands/tracing
