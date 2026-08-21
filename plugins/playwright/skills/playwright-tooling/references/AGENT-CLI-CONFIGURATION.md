# Playwright Agent CLI — Configuration

## Contents

- [Headed / headless mode](#headed-headless-mode)
- [Browser selection](#browser-selection)
- [Profile modes](#profile-modes)
- [Configuration file](#configuration-file)
- [Complete config schema](#complete-config-schema)
- [Example configurations](#example-configurations)
- [Browser extension](#browser-extension)
- [open command — all parameters](#open-command-all-parameters)
- [Environment variables](#environment-variables)

## Headed / headless mode

The default is headless. To show the browser window:

```bash
playwright-cli open https://playwright.dev --headed
```

## Browser selection

```bash
playwright-cli open --browser=chrome     # Google Chrome (default)
playwright-cli open --browser=firefox    # Mozilla Firefox
playwright-cli open --browser=webkit     # WebKit (Safari engine)
playwright-cli open --browser=msedge     # Microsoft Edge
```

## Profile modes

### In-memory (default)
Cookies and storage persist between commands and are deleted on close:

```bash
playwright-cli open https://example.com
```

### Persistent (on disk)
The profile is stored and survives restarts:

```bash
playwright-cli open https://example.com --persistent
```

Default storage locations:
- macOS: `~/Library/Caches/ms-playwright/mcp-{channel}-profile`
- Linux: `~/.cache/ms-playwright/mcp-{channel}-profile`
- Windows: `%LOCALAPPDATA%\ms-playwright\mcp-{channel}-profile`

### Custom profile directory

```bash
playwright-cli open https://example.com --profile=./my-profile
```

### Isolated (explicitly in-memory via config)

```json
{"browser": {"isolated": true}}
```

## Configuration file

```bash
playwright-cli --config path/to/config.json open example.com
```

Loaded automatically when present: `.playwright/cli.config.json`

Show the current config:

```bash
playwright-cli config-print
```

## Complete config schema

```json
{
  "browser": {
    "browserName": "chromium | firefox | webkit",
    "isolated": false,
    "userDataDir": "./profil",
    "launchOptions": {
      "channel": "chrome | msedge | ...",
      "headless": true,
      "executablePath": "/pfad/zum/browser",
      "args": ["--no-sandbox"],
      "proxy": {
        "server": "http://proxy:8080",
        "bypass": "localhost,*.intern",
        "username": "user",
        "password": "pass"
      }
    },
    "contextOptions": {
      "viewport": { "width": 1280, "height": 720 },
      "locale": "de-DE",
      "userAgent": "...",
      "storageState": "./auth.json",
      "permissions": ["geolocation"],
      "serviceWorkers": "allow | block"
    },
    "cdpEndpoint": "http://localhost:9222",
    "cdpHeaders": { "Authorization": "Bearer token" },
    "cdpTimeout": 30000,
    "remoteEndpoint": "ws://localhost:3000",
    "initPage": ["./setup-page.ts"],
    "initScript": ["./setup.js"]
  },
  "extension": false,
  "saveVideo": { "width": 800, "height": 600 },
  "saveSession": false,
  "sharedBrowserContext": false,
  "snapshot": { "mode": "full | none" },
  "imageResponses": "allow | omit",
  "outputDir": "./test-output",
  "outputMode": "file | stdout",
  "console": { "level": "error | warning | info | debug" },
  "network": {
    "allowedOrigins": ["https://api.example.com"],
    "blockedOrigins": ["https://analytics.com"]
  },
  "secrets": { "API_KEY": "secret" },
  "testIdAttribute": "data-testid",
  "timeouts": {
    "action": 5000,
    "navigation": 30000,
    "expect": 5000
  },
  "allowUnrestrictedFileAccess": false,
  "codegen": "typescript | none"
}
```

## Example configurations

### Local development

```json
{"browser": {"launchOptions": {"headless": false}}}
```

### CI environment

```json
{
  "browser": {
    "launchOptions": {"headless": true},
    "contextOptions": {"viewport": {"width": 1280, "height": 720}}
  },
  "outputDir": "./test-output"
}
```

### Behind a proxy

```json
{
  "browser": {
    "launchOptions": {
      "proxy": {
        "server": "http://proxy.corp.example.com:8080",
        "bypass": "localhost,*.internal.com"
      }
    }
  }
}
```

### Device emulation (mobile)

```json
{
  "browser": {
    "contextOptions": {
      "viewport": {"width": 375, "height": 812},
      "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)..."
    }
  }
}
```

### Init scripts

```json
{
  "browser": {
    "initScript": ["./setup.js"],
    "initPage": ["./setup-page.ts"]
  }
}
```

## Browser extension

Connect to existing browser tabs without launching a new browser:

```bash
playwright-cli attach --extension
```

## open command — all parameters

```bash
playwright-cli open [url]                  # Open the browser
playwright-cli open --headed               # Show the browser window
playwright-cli open --browser=firefox      # Specific browser
playwright-cli open --persistent           # Store the profile on disk
playwright-cli open --profile=<pfad>       # Custom profile
playwright-cli open --config=file.json     # Config file
playwright-cli attach --extension          # Connect via extension
playwright-cli attach --cdp <url>          # Connect via CDP
playwright-cli attach --endpoint <url>     # Connect to a Playwright server
```

## Environment variables

| Variable | Description |
|----------|-------------|
| `PLAYWRIGHT_CLI_SESSION` | Default session name |
| `PLAYWRIGHT_MCP_BROWSER` | Browser selection (`chrome`, `firefox`, `webkit`, `msedge`) |
| `PLAYWRIGHT_MCP_HEADLESS` | Headless mode |
| `PLAYWRIGHT_MCP_CAPS` | Enable capabilities (comma-separated) |
| `PLAYWRIGHT_MCP_CONFIG` | Path to the config file |
| `PLAYWRIGHT_MCP_ISOLATED` | In-memory profile |
| `PLAYWRIGHT_MCP_EXTENSION` | Connect via browser extension |
| `PLAYWRIGHT_MCP_USER_DATA_DIR` | Profile directory |
| `PLAYWRIGHT_MCP_STORAGE_STATE` | Storage state file |
| `PLAYWRIGHT_MCP_DEVICE` | Device to emulate |
| `PLAYWRIGHT_MCP_EXECUTABLE_PATH` | Custom browser path |
| `PLAYWRIGHT_MCP_VIEWPORT_SIZE` | Viewport size (e.g. `1280x720`) |
| `PLAYWRIGHT_MCP_PROXY_SERVER` | Proxy server URL |
| `PLAYWRIGHT_MCP_PROXY_BYPASS` | Domains that bypass the proxy |
| `PLAYWRIGHT_MCP_USER_AGENT` | Custom user agent |
| `PLAYWRIGHT_MCP_IGNORE_HTTPS_ERRORS` | Ignore HTTPS errors |
| `PLAYWRIGHT_MCP_TIMEOUT_ACTION` | Action timeout (ms) |
| `PLAYWRIGHT_MCP_TIMEOUT_NAVIGATION` | Navigation timeout (ms) |
| `PLAYWRIGHT_MCP_CONSOLE_LEVEL` | Console message level |
| `PLAYWRIGHT_MCP_TEST_ID_ATTRIBUTE` | Test ID attribute |
| `PLAYWRIGHT_MCP_CDP_ENDPOINT` | CDP endpoint |
| `PLAYWRIGHT_MCP_OUTPUT_DIR` | Output directory |
| `PLAYWRIGHT_MCP_CODEGEN` | Code generation language |
| `PLAYWRIGHT_MCP_INIT_PAGE` | Page init TypeScript |
| `PLAYWRIGHT_MCP_INIT_SCRIPT` | Page init JavaScript |
| `PLAYWRIGHT_MCP_BLOCKED_ORIGINS` | Block origins |
| `PLAYWRIGHT_MCP_ALLOWED_ORIGINS` | Allow origins |
| `PLAYWRIGHT_MCP_GRANT_PERMISSIONS` | Browser permissions |
| `PLAYWRIGHT_MCP_BLOCK_SERVICE_WORKERS` | Block service workers |
| `PLAYWRIGHT_MCP_NO_SANDBOX` | Disable the sandbox |
| `PLAYWRIGHT_MCP_SAVE_SESSION` | Save session data |
| `PLAYWRIGHT_MCP_SAVE_VIDEO` | Record video automatically (e.g. `800x600`) |
| `PLAYWRIGHT_MCP_SECRETS_FILE` | Secrets file (dotenv format) |

---

Source: https://playwright.dev/agent-cli/configuration
