# Playwright Agent CLI — Video Recording

## Contents

- [Command overview](#command-overview)
- [video-start](#video-start)
- [video-chapter](#video-chapter)
- [video-stop](#video-stop)
- [Complete recording workflow](#complete-recording-workflow)
- [Automatic recording](#automatic-recording)
- [Use cases](#use-cases)

## Command overview

| Command | Description |
|--------|-------------|
| `video-start [filename]` | Start video recording |
| `video-chapter <title>` | Insert a chapter marker |
| `video-stop` | Stop the recording and save it |

---

## video-start

```bash
playwright-cli video-start
# Saved to: .playwright-cli/<timestamp>.webm

playwright-cli video-start demo.webm
# Custom file name

playwright-cli video-start recording.webm --size=800x600
# With a specific size
```

### video-start arguments and options

| Argument/Option | Type | Required | Default | Description |
|-----------------|-----|---------|---------|-------------|
| `[filename]` | string | No | Timestamp | File name for the video recording (`.webm`) |
| `--size=<WxH>` | string | No | Viewport size | Video resolution, e.g. `800x600`, `1280x720` |

---

## video-chapter

```bash
playwright-cli video-chapter "Login"
playwright-cli video-chapter "Checkout" --description="Entering payment details"
playwright-cli video-chapter "Confirmation" --description="Order confirmed" --duration=2000
```

### video-chapter arguments and options

| Argument/Option | Type | Required | Default | Description |
|-----------------|-----|---------|---------|-------------|
| `<title>` | string | Yes | — | Chapter label |
| `--description=<text>` | string | No | — | Additional description text |
| `--duration=<ms>` | number | No | — | Milliseconds the chapter card is displayed |

---

## video-stop

```bash
playwright-cli video-stop
```

No arguments. Stops the recording and saves the file.

---

## Complete recording workflow

```bash
playwright-cli video-start demo.webm

playwright-cli video-chapter "Home" --description="Landing page loaded"
playwright-cli goto https://demo.playwright.dev/todomvc/

playwright-cli video-chapter "Add todo"
playwright-cli type "Buy groceries"
playwright-cli press Enter

playwright-cli video-chapter "Complete"
playwright-cli check e21

playwright-cli video-stop
# Saved: .playwright-cli/demo.webm
```

---

## Automatic recording

Start automatically without manual commands:

### Via a configuration file

```json
{
  "saveVideo": {
    "width": 800,
    "height": 600
  }
}
```

### Via an environment variable

```bash
PLAYWRIGHT_MCP_SAVE_VIDEO=800x600 playwright-cli open https://example.com
```

---

## Use cases

| Scenario | Description |
|----------|-------------|
| Bug reproduction | Record faulty behavior for developers |
| Test documentation | Document a manual test run |
| Agent monitoring | Observe an automated agent run |
| Creating a demo video | Demonstrate product features |

---

Source: https://playwright.dev/agent-cli/commands/video-recording
